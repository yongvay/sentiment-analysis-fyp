"""University-PC feasibility trial. No evaluation data or trained checkpoints saved.
Run with the existing fyp-voter1-env Python. Each case uses a fresh child process.
"""
import argparse
import csv
import hashlib
import importlib.metadata
import json
import math
import platform
import subprocess
import sys
import time
import traceback
from pathlib import Path

HERE = Path(__file__).resolve().parent
MODEL = 'FacebookAI/xlm-roberta-base'
REVISION = 'e73636d4f797dec63c3081bb6ed5c7b0bb3f2089'
LABELS = {'negative': 0, 'neutral': 1, 'positive': 2}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save(path, data):
    path.write_text(json.dumps(data, indent=2, sort_keys=True)+'\n', encoding='utf-8')


def verified_rows():
    lock = json.loads((HERE/'input_record.json').read_text(encoding='utf-8'))
    path = HERE/'condition_b_training.csv'
    if digest(path) != lock['sha256']:
        raise ValueError('Training input checksum mismatch')
    with path.open(encoding='utf-8-sig', newline='') as stream:
        rows = list(csv.DictReader(stream))
    if len(rows) != 799 or any(r['majority_sent'] not in LABELS for r in rows):
        raise ValueError('Unexpected training records')
    return rows


def trial(batch_size, checkpointing):
    import torch
    from transformers import AutoModelForSequenceClassification, AutoTokenizer, set_seed
    if not torch.cuda.is_available():
        raise RuntimeError('CUDA GPU unavailable in this environment')
    set_seed(42)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    rows = verified_rows()
    tokenizer = AutoTokenizer.from_pretrained(MODEL, revision=REVISION, use_fast=True, trust_remote_code=False)
    # Choose longest training examples deterministically; pad to the full proposed limit.
    lengths = tokenizer([r['comment/tweet'] for r in rows], truncation=False,
                        padding=False, return_length=True, verbose=False)['length']
    if max(lengths) > 128:
        raise ValueError('Unexpected training text longer than audited limit')
    ordered = sorted(zip(rows, lengths), key=lambda item: (-item[1], int(item[0]['id'])))
    selected = [r for r, _ in ordered[:48]]
    encoded = tokenizer([r['comment/tweet'] for r in selected], truncation=False,
                        padding='max_length', max_length=128, return_tensors='pt')
    labels = torch.tensor([LABELS[r['majority_sent']] for r in selected])
    initial_free, total = torch.cuda.mem_get_info()
    torch.cuda.reset_peak_memory_stats()
    load_start = time.perf_counter()
    model = AutoModelForSequenceClassification.from_pretrained(
        MODEL, revision=REVISION, num_labels=3, id2label={v:k for k,v in LABELS.items()},
        label2id=LABELS, attn_implementation='eager', trust_remote_code=False,
        use_safetensors=True)
    if checkpointing:
        model.gradient_checkpointing_enable(gradient_checkpointing_kwargs={'use_reentrant': False})
    model.to('cuda')
    model.train()
    torch.cuda.synchronize()
    load_seconds = time.perf_counter()-load_start
    optimizer = torch.optim.AdamW(model.parameters(), lr=2e-5, weight_decay=.01, foreach=False)
    scaler = torch.amp.GradScaler('cuda')
    accumulation = 16 // batch_size
    events = []
    successful = 0
    # Three successful updates: one warm-up and two measured. Retry AMP scale backoffs.
    for attempt in range(12):
        optimizer.zero_grad(set_to_none=True)
        torch.cuda.synchronize()
        start = time.perf_counter()
        losses = []
        for micro in range(accumulation):
            offset = (successful*16 + micro*batch_size) % len(selected)
            batch = {k:v[offset:offset+batch_size].to('cuda') for k,v in encoded.items()}
            target = labels[offset:offset+batch_size].to('cuda')
            with torch.autocast(device_type='cuda', dtype=torch.float16):
                result = model(**batch, labels=target)
                loss = result.loss
            if not torch.isfinite(loss).item():
                raise FloatingPointError('Non-finite training loss')
            losses.append(loss.detach().float().item())
            scaler.scale(loss/accumulation).backward()
        scaler.unscale_(optimizer)
        grad_norm = torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        before = scaler.get_scale()
        scaler.step(optimizer)
        scaler.update()
        after = scaler.get_scale()
        torch.cuda.synchronize()
        skipped = after < before
        finite_grad = bool(torch.isfinite(grad_norm).item())
        if not skipped and not finite_grad:
            raise FloatingPointError('Non-finite gradients without AMP skip')
        events.append(dict(attempt=attempt+1, successful_update=successful+1 if not skipped else None,
                           skipped=skipped, seconds=time.perf_counter()-start,
                           mean_loss=sum(losses)/len(losses), gradient_norm=float(grad_norm) if finite_grad else None,
                           scale_before=before, scale_after=after))
        if not skipped:
            successful += 1
        if successful == 3:
            break
    if successful != 3:
        raise FloatingPointError('Could not complete three finite optimizer updates within 12 attempts')
    measured = [event['seconds'] for event in events if not event['skipped']][1:]
    return dict(status='PASS', micro_batch=batch_size, gradient_accumulation=accumulation,
                effective_batch=16, max_length=128, precision='fp16 AMP; FP32 parameters',
                attention='eager', gradient_checkpointing=checkpointing,
                optimizer='AdamW foreach=False', learning_rate=2e-5, weight_decay=.01,
                seed=42, successful_updates=successful, events=events,
                skipped_updates=sum(e['skipped'] for e in events),
                measured_update_seconds=sum(measured)/len(measured),
                measured_examples_per_second=32/sum(measured), load_seconds=load_seconds,
                peak_allocated_mib=torch.cuda.max_memory_allocated()/2**20,
                peak_reserved_mib=torch.cuda.max_memory_reserved()/2**20,
                gpu_total_mib=total/2**20, initial_free_mib=initial_free/2**20,
                gpu_name=torch.cuda.get_device_name(), sample_ids=[r['id'] for r in selected],
                limitation='Short training-only stress trial, not evaluation, checkpoint reload or long-run stability proof.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--worker', type=int, choices=[1,2,4,8])
    parser.add_argument('--checkpointing', action='store_true')
    parser.add_argument('--result', type=Path)
    parser.add_argument('--output-dir', type=Path, default=HERE/'results')
    args = parser.parse_args()
    if args.worker:
        try:
            result = trial(args.worker, args.checkpointing)
        except Exception as exc:
            import torch
            result = dict(status='OOM' if isinstance(exc, torch.cuda.OutOfMemoryError) else 'ERROR',
                          micro_batch=args.worker, gradient_checkpointing=args.checkpointing,
                          error=str(exc), traceback=traceback.format_exc())
        save(args.result, result)
        print(json.dumps(result, indent=2))
        return
    import torch
    for package, expected in [('torch','2.6.0+cu124'), ('transformers','4.57.6'),
                              ('tokenizers','0.22.2'), ('accelerate','1.6.0')]:
        if importlib.metadata.version(package) != expected:
            raise ValueError(f'Expected {package}=={expected}; do not silently change the trial environment')
    if not torch.cuda.is_available():
        raise RuntimeError('This must run on the university PC in its GPU-enabled environment.')
    verified_rows()
    args.output_dir.mkdir(parents=True, exist_ok=False)
    save(args.output_dir/'environment.json', dict(python=sys.version, platform=platform.platform(),
        gpu=torch.cuda.get_device_name(), gpu_total_mib=torch.cuda.get_device_properties(0).total_memory/2**20,
        cuda=torch.version.cuda, model=MODEL, revision=REVISION,
        script_sha256=digest(Path(__file__)), input_sha256=digest(HERE/'condition_b_training.csv'),
        packages={d.metadata['Name']:d.version for d in importlib.metadata.distributions()}))
    smi = subprocess.run(['nvidia-smi'], capture_output=True, text=True)
    (args.output_dir/'nvidia-smi.txt').write_text(smi.stdout+smi.stderr, encoding='utf-8')
    results = []
    # Separate processes release all GPU allocations after each test, including OOM.
    for checkpointing in [False, True]:
        if checkpointing and any(r['status']=='PASS' for r in results):
            break
        for batch in [1,2,4,8]:
            name = f'batch_{batch}_checkpointing_{checkpointing}'
            target = (args.output_dir/(name+'.json')).resolve()
            cmd = [sys.executable, str(Path(__file__).resolve()), '--worker', str(batch), '--result', str(target)]
            if checkpointing:
                cmd.append('--checkpointing')
            print(f'Testing batch {batch}, gradient checkpointing={checkpointing} ...', flush=True)
            with (args.output_dir/(name+'.log')).open('w', encoding='utf-8') as log:
                process = subprocess.run(cmd, stdout=log, stderr=subprocess.STDOUT)
            result = json.loads(target.read_text()) if target.exists() else dict(status='ERROR', error=f'Worker exit {process.returncode}; see log')
            results.append(result)
            save(args.output_dir/'trial_summary.json', dict(results=results, settings_status='provisional; review before final training'))
            print(result['status'], flush=True)
            if result['status']=='ERROR':
                print('Stopped: send the results folder for diagnosis.', flush=True)
                return
            if result['status']=='OOM':
                break
    print('Finished. Send trial_summary.json and environment.json for review. No trained checkpoint was saved.')


if __name__ == '__main__':
    main()
