"""Audit updated A/B/C with the pinned XLM-R tokenizer, without editing data.
Defaults resolve relative to this script. Requires transformers 4.57.6 and
tokenizers 0.22.2. Run with --output-dir NEW_FOLDER to reproduce.
"""
import argparse
import csv
import hashlib
import importlib.metadata
import json
import math
import os
import platform
import statistics
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
LIMITS = (128, 256, 512)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def percentile(values, p):
    return sorted(values)[max(0, math.ceil(len(values) * p) - 1)]


def summarize(condition, label, values):
    result = dict(condition=condition, label=label, rows=len(values),
                  min_tokens=min(values), mean_tokens=round(statistics.mean(values), 4),
                  median_tokens=statistics.median(values), p90_tokens=percentile(values, .90),
                  p95_tokens=percentile(values, .95), p99_tokens=percentile(values, .99),
                  max_tokens=max(values))
    for limit in LIMITS:
        count = sum(n > limit for n in values)
        result[f'over_{limit}_rows'] = count
        result[f'over_{limit}_percent'] = round(100 * count / len(values), 4)
        result[f'over_{limit}_excess_tokens'] = sum(max(0, n-limit) for n in values)
    return result


def write_csv(path, rows):
    with path.open('w', encoding='utf-8', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]), lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data-dir', type=Path, default=HERE/'quality_candidates_v2')
    parser.add_argument('--revision-file', type=Path, default=HERE/'environment_records/fyp-voter1-model-revision.json')
    parser.add_argument('--output-dir', type=Path, default=HERE/'token_length_audit_v1')
    parser.add_argument('--cache-dir', type=Path, default=None)
    parser.add_argument('--local-files-only', action='store_true')
    args = parser.parse_args()
    require(not args.output_dir.exists(), 'Choose a new output folder; existing results are never overwritten.')
    for package, expected in [('transformers', '4.57.6'), ('tokenizers', '0.22.2')]:
        require(importlib.metadata.version(package) == expected, f'Expected {package}=={expected}')
    if args.local_files_only:
        os.environ['HF_HUB_OFFLINE'] = '1'
        os.environ['TRANSFORMERS_OFFLINE'] = '1'
    from transformers import AutoTokenizer
    record = json.loads(args.revision_file.read_text(encoding='utf-8-sig'))
    require(record['model_id'] == 'FacebookAI/xlm-roberta-base', 'Unexpected model ID')
    require(record['revision'] == 'e73636d4f797dec63c3081bb6ed5c7b0bb3f2089', 'Unexpected revision')
    manifest_path = args.data_dir/'preparation_manifest.json'
    manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
    source_hashes = {str(manifest_path.name): sha(manifest_path)}
    datasets = {}
    for condition in 'ABC':
        path = args.data_dir/f'condition_{condition.lower()}_training.csv'
        source_hashes[path.name] = sha(path)
        require(source_hashes[path.name] == manifest['outputs_sha256'][path.name], 'Dataset hash mismatch: '+condition)
        with path.open(encoding='utf-8-sig', newline='') as stream:
            rows = list(csv.DictReader(stream))
        require(len(rows) == manifest['rows'][condition], 'Dataset count mismatch')
        datasets[condition] = rows
    tokenizer = AutoTokenizer.from_pretrained(record['model_id'], revision=record['revision'],
                use_fast=True, trust_remote_code=False, cache_dir=args.cache_dir,
                local_files_only=args.local_files_only)
    require(tokenizer.is_fast and type(tokenizer).__name__ == record['tokenizer_class'], 'Wrong tokenizer implementation')
    require(len(tokenizer('Makanan ni memang best, I love it!', truncation=False)['input_ids']) == 11,
            'University sample token count mismatch')
    special = tokenizer.num_special_tokens_to_add(pair=False)
    require(special == 2, 'Unexpected special token count')
    detail, summary, shared_counts = [], [], {}
    for condition, rows in datasets.items():
        condition_detail = []
        for start in range(0, len(rows), 256):
            batch = rows[start:start+256]
            texts = [r['comment/tweet'] if condition == 'B' else r['text'] for r in batch]
            encoded = tokenizer(texts, add_special_tokens=True, truncation=False, padding=False,
                                return_attention_mask=False, return_token_type_ids=False,
                                return_length=True, verbose=False)
            for row, text, ids, length in zip(batch, texts, encoded['input_ids'], encoded['length']):
                label = row['majority_sent'].strip() if condition == 'B' else row['label']
                post_id = row['id'] if condition == 'B' else row['post_id'] if condition == 'A' else row['record_id']
                require(length == len(ids) and length >= special, 'Invalid token length')
                key = sha_text = hashlib.sha256(text.encode('utf-8')).hexdigest()
                require(shared_counts.get(key, length) == length, 'Shared text token counts disagree')
                shared_counts[key] = length
                item = dict(condition=condition, post_id=post_id, label=label, text_sha256=sha_text,
                            content_tokens=length-special, total_tokens=length)
                condition_detail.append(item)
        require(Counter(r['label'] for r in condition_detail) == manifest['class_counts'][condition], 'Class count mismatch')
        detail.extend(condition_detail)
        for label in ['all', 'negative', 'neutral', 'positive']:
            values = [r['total_tokens'] for r in condition_detail if label == 'all' or r['label'] == label]
            summary.append(summarize(condition, label, values))
    require(all(sha(args.data_dir/name) == value for name, value in source_hashes.items()), 'Inputs changed during audit')
    args.output_dir.mkdir(parents=True)
    write_csv(args.output_dir/'token_lengths_by_post.csv', detail)
    write_csv(args.output_dir/'token_length_summary.csv', summary)
    lines = ['# XLM-R token-length audit', '', 'Updated A/B/C only. No text modified, padded or truncated.',
             'Counts include two special tokens. A post exactly at a limit is not counted as truncated.',
             'Percentiles use nearest rank; median uses the standard midpoint for even-sized samples.',
             'Limits are scenarios, not selected training settings. Counts are separate per candidate; C overlaps A/B.', '',
             '| Dataset / label | Posts | Median | P95 | Max | >128 | >256 | >512 |',
             '|---|---:|---:|---:|---:|---:|---:|---:|']
    for row in summary:
        cells = [f"{row[f'over_{n}_rows']} ({row[f'over_{n}_percent']:.2f}%)" for n in LIMITS]
        lines.append(f"| {row['condition']} / {row['label']} | {row['rows']} | {row['median_tokens']} | {row['p95_tokens']} | {row['max_tokens']} | " + ' | '.join(cells)+' |')
    lines += ['', '## Verification and limits', '',
              '- Input SHA-256 hashes, row counts and sentiment counts match the quality-adjusted manifest.',
              '- University sample reproduces 11 tokens. Shared text has consistent lengths across candidates.',
              '- Python runtime and installed package versions are recorded; this audit needs no GPU or model weights.',
              '- Final maximum length requires the methodology and GPU training trial; data length alone does not select it.',
              '- Keep the protected evaluation sets separate. This report does not evaluate model performance.',
              '', '## Reproduce', '',
              'Run measure_token_lengths.py with the same data/revision files and pinned tokenizer packages.',
              'Use --output-dir with a new folder. --local-files-only permits reuse of cached tokenizer files.', '']
    (args.output_dir/'Token_Length_Report.md').write_text('\n'.join(lines), encoding='utf-8')
    tokenizer.save_pretrained(args.output_dir/'tokenizer_snapshot')
    outputs = {p.relative_to(args.output_dir).as_posix(): sha(p) for p in sorted(args.output_dir.rglob('*')) if p.is_file()}
    audit = dict(model=record, source_sha256=source_hashes, revision_file_sha256=sha(args.revision_file),
                 script_sha256=sha(Path(__file__)), python=platform.python_version(),
                 packages={d.metadata['Name']: d.version for d in importlib.metadata.distributions()},
                 add_special_tokens=True, special_tokens_per_post=special, truncation=False, padding=False,
                 percentile_method='nearest_rank', limits=list(LIMITS), summary=summary,
                 checks='input hashes/counts/classes, sample parity, shared-text lengths: PASS',
                 outputs_sha256=outputs)
    (args.output_dir/'audit_manifest.json').write_text(json.dumps(audit, indent=2, sort_keys=True)+'\n', encoding='utf-8')
    print(json.dumps([r for r in summary if r['label']=='all'], indent=2))


if __name__ == '__main__':
    main()
