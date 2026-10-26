# Voter 1 university GPU trial

This is a feasibility measurement, not the nine A/B/C comparison runs. It does not select a model or save a trained checkpoint. It contains the quality-adjusted expert training input (799 posts); no protected development, calibration or test data.

## Run on the university PC

1. Extract the ZIP. Open the extracted `fyp-voter1-gpu-trial` folder containing `run_gpu_trial.py`.
2. Open PowerShell in that folder (File Explorer address bar: type `powershell`, then Enter).
3. Run:

```powershell
& "$env:USERPROFILE\fyp-voter1-env\Scripts\python.exe" .\run_gpu_trial.py
```

Use the already configured Python 3.11 environment. The script checks the pinned package versions. Internet is required for the first download of the pinned XLM-R tokenizer and approximately 1.12 GB model.safetensors file. Dataset text is processed locally, not uploaded.

Progress and download warnings are captured in the `results` folder's `.log` files. The console prints each case and its result. A warning about newly initialized classifier weights is expected: the base model does not already have the three-class sentiment head. The script trains that temporary head and the full backbone for the feasibility check.

Return `results/trial_summary.json` and `results/environment.json`. If a case reports ERROR, also return its `.log` file. An OOM means the case ran out of GPU memory; it is recorded and the process releases its allocations. Do not reinstall packages just because a batch size does not fit.

Existing result folders are never overwritten. To repeat:

```powershell
& "$env:USERPROFILE\fyp-voter1-env\Scripts\python.exe" .\run_gpu_trial.py --output-dir results_repeat
```

## What is measured

- XLM-R-base revision e73636d4f797dec63c3081bb6ed5c7b0bb3f2089.
- Three sentiment labels; FP32 model parameters with FP16 automatic mixed precision and gradient scaling.
- Maximum length 128, fixed padding to 128 for a conservative sequence-shape trial.
- Longest 48 eligible expert training texts, ties broken by numeric ID. Seed 42; no relabelling or evaluation.
- Micro-batches 1/2/4/8, effective batch 16 via accumulation. Stop larger batches after OOM. If no normal case passes, retry with gradient checkpointing.
- AdamW, learning rate 2e-5, weight decay .01, foreach=False, gradient clipping 1.0, eager attention. These are provisional trial settings, not a final experimental configuration.
- Three successful optimizer updates per case, first update excluded from throughput timing. AMP overflow/backoff events are recorded, not counted as successful updates. At most 12 attempts per case.
- Peak PyTorch allocated/reserved GPU memory, initial free memory, loading time, measured throughput, finite loss/gradient checks, exact inputs and runtime versions.
- Each case starts from pretrained weights in a fresh process, releasing GPU allocations at process exit.

## Limits and next steps

This short trial cannot establish long-run stability or final performance. PyTorch peak memory does not include every Windows/driver allocation. Shared system memory is not extra dedicated VRAM. Leave practical memory headroom when selecting settings. The measured timing uses a small long-text sample and includes stability diagnostics, so it is not a production runtime estimate.

Checkpoint save/reload, full training/evaluation implementation, prespecified checkpoint/tie selection rules, final shared settings and final data freeze remain separate tasks. This trial must not be reported as model selection or as a completed training run.
