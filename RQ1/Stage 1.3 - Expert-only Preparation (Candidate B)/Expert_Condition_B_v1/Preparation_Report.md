# Stage 1.3: Candidate B preparation

Candidate B contains the fixed 800 expert-labelled code-mixed training posts from Stage 1.2: 684 authors; 346 negative, 225 neutral and 229 positive labels.

## Inclusion rules

- Include every record in expert_training.csv, using the saved v1 membership as authority.
- Require lang_id.strip() == "cm" and a valid negative, neutral or positive label.
- Exclude monolingual records and all development, calibration and secondary-test records.
- Preserve all five source columns, original values, row order and CSV bytes. No resampling, text cleaning, relabelling, balancing or new partitioning is applied.
- Retain the existing repeated-text records, including IDs 39303 and 37432. Distinct post IDs remain distinct records.

## Verification

Source hashes match the Stage 1.2 manifest. All 800 IDs are unique and match saved training membership and authors. Required values are populated. Candidate B has zero post-ID, author or exact-trimmed-text overlap with each protected partition. The output CSV is byte-identical to expert_training.csv. Detailed results are in validation_report.json; hashes and provenance are in preparation_manifest.json.

## Reproduction

Run the parent folder's prepare_candidate_b.py with Python 3. It uses only the standard library. Defaults locate the neighbouring Stage 1.2 package. Use --source-dir to supply another copy of that same verified package and --output-dir to specify a new destination. Existing output directories are refused. No random seed is needed because the existing seed-42 membership and row order are preserved.

## Scope and remaining work

Stage 1.3 packaging is complete. Candidate B is not yet the final frozen training input. Cross-dataset overlap, near-duplicate/quality decisions, tokenizer lengths and final A/B/C freeze remain in Stage 1.5. Training occurs in Stage 2. Author separation uses the supplied identifiers, not verified real-world identity. Repeated text is retained as a known limitation.
