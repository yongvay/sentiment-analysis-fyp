# Stage 1.5 quality policy applied — final freeze pending

Use the A/B/C CSVs in this package for the next Stage 1.5 checks. Earlier v1 packages remain historical evidence.

## Decisions
- Retain short and expressive text; use the identical MESoc scanner on both training inputs.
- Retain MESoc mesoc_016651 after assistant review: readable neutral promotion, not confirmed unusable. No labels changed.
- Remove redundant exact expert training copy 39303; retain 37432 (lowest numeric ID). Both had the same author, text and negative label.
- The original 800-post expert training partition remains immutable. The derived B input contains 799 posts. No post moves into another partition.
- Preserve previous MESoc near-duplicate exclusions; these historical rules differ from exact-copy deduplication and are not claimed to be identical.
- Regenerate C using the existing seed-42 SHA-256 neutral ranking and expert precedence. Only B:39303 is removed; all other C records and values are unchanged.

## Results
Class counts: {"A": {"negative": 1022, "neutral": 13144, "positive": 2802}, "B": {"negative": 345, "neutral": 225, "positive": 229}, "C": {"negative": 1367, "neutral": 3031, "positive": 3031}}.
Screening counts: {"MESocSentiment": {"flag_counts": {"possible_promotion": 1, "repeated_character_run": 29, "short_text": 1370}, "flagged": 1400, "scanned": 16968}, "expert": {"flag_counts": {"repeated_character_run": 36, "short_text": 10}, "flagged": 45, "scanned": 800}}.
Exact-text, protected expert ID/author and MESoc reserved-text checks pass. MESoc author separation cannot be verified.

## Reproduce
Run `python apply_quality_policy.py --output-dir <new-directory>` from the parent stage folder. Inputs and imported processors must match input_lock.json. Existing output folders are refused. This uses only Python's standard library. Output manifests contain all input, script and output SHA-256 hashes.

## Status and superseded decisions
This decision record supersedes the earlier requirement to review all short/repeated-character flags and the decision to retain both expert duplicate copies in training. It does not rewrite historical preparation evidence or partition membership.
The Excel tracker still describes the historical v1 candidates; consult this package for current quality-adjusted inputs.
Final tokenizer-length/truncation checks, hardware trial, shared training configuration and final freeze are still pending. This package is not declared frozen for training.
