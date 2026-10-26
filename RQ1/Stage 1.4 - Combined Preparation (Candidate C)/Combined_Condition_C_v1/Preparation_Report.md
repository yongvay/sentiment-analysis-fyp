# Stage 1.4: Candidate C preparation

Candidate C contains 7,430 rows: 1,368 negative, 3,031 neutral and 3,031 positive.
All 800 expert training rows are preserved. 2,806 MESoc neutral rows were selected from 13,144 eligible MESoc neutral rows.

## Agreed rules

Combine the fixed Candidate A and B inputs. For exact text matches after outer whitespace trimming, exclude the A row and preserve B, including the expert label if labels conflict. Record every pair. Preserve previous within-source decisions, including B's two distinct IDs with repeated text. No source file or text is edited. Namespaced IDs distinguish A and B IDs.

After cross-source deduplication, keep all positive/negative rows and all expert rows. Set total neutral count equal to the larger positive/negative class. Sample only MESoc neutral rows without replacement. Fail if the target is infeasible.

Seed: 42. Selection uses ascending SHA-256 of UTF-8 text `candidate-c-neutral-v1\n{seed}\n{record_id}`, breaking ties by ID. Take the first required number. This is deterministic pseudorandom ranking, not Python random.sample. It avoids dependence on input ordering or changes to random-library sampling algorithms. Every score and selection is recorded. Output is sorted by namespaced ID; shuffle during model training with the training-run seed.

## Audit and reproducibility

Input bytes are locked by SHA-256; changed inputs cause failure. The manifest records input and output checksums and the script checksum. Outputs use UTF-8, LF newlines and deterministic ordering, with no timestamps or machine-specific paths. Existing output directories are refused. Only Python 3.9+ standard-library modules are needed. No installation, downloads or API access is required.

Run `python prepare_candidate_c.py` from this script's folder for the first build. To reproduce, run `python prepare_candidate_c.py --output-dir Combined_Condition_C_v1_reproduced`. Defaults resolve inputs relative to the script, independent of working directory. Use `--rq1-root` for a relocated copy of RQ1. Keep seed 42 to reproduce v1; a different `--seed` produces a different sample.

The neutral log records all eligible A neutral rows. The inclusion log accounts for every A/B row and the reason it was retained or excluded. Original data remain recoverable in A/B. Empty duplicate logs still include headers.

## Validation and remaining work

Exact cross-source pairs: 0. Heuristic near-duplicate pairs: 0. Near-duplicate flags are retained for Stage 1.5 review, not automatically removed. The scan uses NFKC/casefold/whitespace equivalence, plus pairs with the same first 12 normalized characters, at least 30 characters and SequenceMatcher ratio >= 0.95 (autojunk disabled). It is not exhaustive.

Candidate C has no exact trimmed-text match with the protected expert development, calibration or secondary test sets. Expert IDs and author identifiers are also separated. MESoc has no author identifiers, so cross-source author separation cannot be established. Previously retained repeated B text remains intentionally present.

Stage 1.4 preparation is complete. Final A/B/C freeze, full overlap/quality review and tokenizer length checks remain in Stage 1.5. The A-versus-C comparison changes both source composition and class proportions, so results cannot isolate the effect of adding expert data alone.
