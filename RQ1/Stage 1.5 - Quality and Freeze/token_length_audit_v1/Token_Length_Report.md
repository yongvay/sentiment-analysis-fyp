# XLM-R token-length audit

Updated A/B/C only. No text modified, padded or truncated.
Counts include two special tokens. A post exactly at a limit is not counted as truncated.
Percentiles use nearest rank; median uses the standard midpoint for even-sized samples.
Limits are scenarios, not selected training settings. Counts are separate per candidate; C overlaps A/B.

| Dataset / label | Posts | Median | P95 | Max | >128 | >256 | >512 |
|---|---:|---:|---:|---:|---:|---:|---:|
| A / all | 16968 | 13.0 | 32 | 68 | 0 (0.00%) | 0 (0.00%) | 0 (0.00%) |
| A / negative | 1022 | 19.0 | 39 | 56 | 0 (0.00%) | 0 (0.00%) | 0 (0.00%) |
| A / neutral | 13144 | 13.0 | 31 | 68 | 0 (0.00%) | 0 (0.00%) | 0 (0.00%) |
| A / positive | 2802 | 16.0 | 35 | 57 | 0 (0.00%) | 0 (0.00%) | 0 (0.00%) |
| B / all | 799 | 32 | 79 | 114 | 0 (0.00%) | 0 (0.00%) | 0 (0.00%) |
| B / negative | 345 | 35 | 78 | 114 | 0 (0.00%) | 0 (0.00%) | 0 (0.00%) |
| B / neutral | 225 | 27 | 82 | 111 | 0 (0.00%) | 0 (0.00%) | 0 (0.00%) |
| B / positive | 229 | 32 | 78 | 102 | 0 (0.00%) | 0 (0.00%) | 0 (0.00%) |
| C / all | 7429 | 16 | 41 | 114 | 0 (0.00%) | 0 (0.00%) | 0 (0.00%) |
| C / negative | 1367 | 22 | 56 | 114 | 0 (0.00%) | 0 (0.00%) | 0 (0.00%) |
| C / neutral | 3031 | 13 | 36 | 111 | 0 (0.00%) | 0 (0.00%) | 0 (0.00%) |
| C / positive | 3031 | 17 | 38 | 102 | 0 (0.00%) | 0 (0.00%) | 0 (0.00%) |

## Verification and limits

- Input SHA-256 hashes, row counts and sentiment counts match the quality-adjusted manifest.
- University sample reproduces 11 tokens. Shared text has consistent lengths across candidates.
- Python runtime and installed package versions are recorded; this audit needs no GPU or model weights.
- Final maximum length requires the methodology and GPU training trial; data length alone does not select it.
- Keep the protected evaluation sets separate. This report does not evaluate model performance.

## Reproduce

Run measure_token_lengths.py with the same data/revision files and pinned tokenizer packages.
Use --output-dir with a new folder. --local-files-only permits reuse of cached tokenizer files.
