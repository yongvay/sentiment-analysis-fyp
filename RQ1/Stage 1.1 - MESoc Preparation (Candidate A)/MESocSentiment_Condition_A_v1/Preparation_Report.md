# MESocSentiment Condition A preparation report

Status: **Candidate dataset. Not frozen for training.**

## Result

- Original corpus: 19,714 records.
- Reserved supplied test file: 2,000 records, retaining both manual and automatic labels.
- Candidate training pool: 16,968 records.
- Excluded corpus records: 2,746.
- Source rows whose surrounding whitespace was trimmed: 0.
- Original duplicate pairs handled by exclusion policy: 582.
- Unique candidate rows excluded by that policy: 746.
- Suspicious rows flagged across the original corpus: 1,410.
- Remaining candidate rows with suspicious-text flags: 1,400.

| Candidate label | Count |
|---|---:|
| positive | 2,802 |
| neutral | 13,144 |
| negative | 1,022 |

## Processing decisions

Original CSVs were not changed. IDs use original data-row positions (header excluded) and are tied to source SHA-256 hashes in the manifest. Raw text is preserved. The training text only has leading/trailing whitespace removed. Sentiment labels are mapped to negative=0, neutral=1, positive=2. Labels remain automatic; they have not been corrected by a person.

All texts matching the supplied test file after trimming are reserved. This follows the preparation decision discussed for this project; it does not replace the expert development/test design. Invalid and empty records are excluded. All members of a conflicting-label exact-text group are quarantined; same-label exact duplicates retain the first source row. Each exclusion is recorded with its reason.

No class balancing, model tokenisation, length filtering, spam filtering, label correction, or random 80/20 split was performed. The supplied Train Set.csv is inventoried but not used as training input.

By the user's decision, every candidate post participating in an originally flagged near-duplicate pair is excluded, including both endpoints of candidate-candidate pairs. Reserved test records are preserved. This conservative policy does not establish semantic equivalence and may discard distinct posts. The original screen is applied once, without iterative rescreening after removal. Excluded rows remain recoverable in mesoc_exclusions.csv; each pair records its policy decision.

Suspicious-text scanning checks all original corpus records, including excluded records, for empty text, invalid labels, possible encoding damage, control/invisible characters, HTML, URL/mention-only content, short or non-alphanumeric text, repeated characters and possible promotion. It only flags these conditions; it does not remove or modify additional rows. Emoji, negation, capitalisation and Manglish spelling are preserved. Exact rules and thresholds are recorded in suspicious_text_summary.json. A row can have multiple flags, so flag counts do not sum to unique flagged rows. Character counts and whitespace-unit counts are not model-token lengths.

## Verification

row reconciliation, unique IDs/text, no prepared exact audit overlap, valid labels, originals unchanged: PASS

## Files and use

- condition_a_training.csv: input candidate pool; train on text and label_id only after remaining checks.
- mesoc_reserved_test.csv: supplied test examples with manual and automatic labels; keep out of training.
- mesoc_exclusions.csv: corpus rows omitted and reasons.
- mesoc_duplicate_review.csv: original flagged pairs and applied exclusion-policy decisions.
- mesoc_suspicious_text.csv: flagged source rows, reasons and current candidate/excluded disposition.
- suspicious_text_summary.json: scan counts, thresholds, rules and flag-only policy.
- preparation_manifest.json: counts, source hashes, rules, label mapping and processor version hash.

## Required before final training freeze

1. Assess suspicious-text flags and document any further handling decisions. Flags alone are not evidence that a post is invalid. Original near-duplicate pairs have been handled by the recorded automatic exclusion policy.
2. Compare with the expert development, calibration and test records once their partitions exist, and exclude confirmed evaluation overlap.
3. Record the absence of author identifiers in MESocSentiment; author separation cannot be verified for this source.
4. Decide and record shared RQ1 training settings, measure token lengths and truncation, then freeze a new final training manifest.

The similarity screen is a heuristic, not an exhaustive semantic or fuzzy duplicate audit. It checks case/Unicode/whitespace equivalence and adjacent lexicographically sorted texts sharing a 12-character prefix with at least 30 characters and sequence similarity >=0.95. Other paraphrases may remain. No expert dataset was changed or partitioned in this preparation step.

## Reproduction

Run the accompanying prepare_mesoc.py with --root pointing to the RQ1 folder (the folder containing Training Datasets) and --output pointing to a new directory that does not already exist. It uses only Python's standard library and refuses to overwrite an existing output directory.

From the FYP project folder, run:

```powershell
python "RQ1/Stage 1.1 - MESoc Preparation (Candidate A)/MESocSentiment_Condition_A_v1/prepare_mesoc.py" --root "RQ1" --output "RQ1/Stage 1.1 - MESoc Preparation (Candidate A)/MESocSentiment_Condition_A_reproduced"
```

The example creates a separate reproduction folder only when run. Choose another unused output name for subsequent runs. The script writes condition_a_training.csv and mesoc_reserved_test.csv, matching this package's filenames. Despite its filename, condition_a_training.csv remains a candidate pool until the checks above are complete. Inspect the manifest and checks before using regenerated outputs.
