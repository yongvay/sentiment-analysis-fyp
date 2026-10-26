# Stage 1.2 partition report

Only labelled code-mixed posts are included. Monolingual data is excluded from Stage 1.3 training by user decision.

| Partition | Posts | Authors | Negative | Neutral | Positive |
|---|---:|---:|---:|---:|---:|
| training | 800 | 684 | 346 | 225 | 229 |
| development | 600 | 514 | 260 | 168 | 172 |
| calibration | 120 | 105 | 52 | 34 | 34 |
| secondary_test | 761 | 648 | 330 | 213 | 218 |

All four partitions are pairwise author-disjoint, ID-disjoint and exact-trimmed-text-disjoint. All 2,281 eligible records appear exactly once. Exact target sizes and proportional integer class quotas were met.

Excluded from these partitions: 7,680 non-code-mixed records and 39 code-mixed records without a valid sentiment label. The source file remains unchanged.

The two identical-text records (IDs 39303 and 37432) are retained together under their shared author. This preserves the planned 2,281 records; record the repeated content as a limitation. No near-duplicate or semantic similarity audit has been performed.

Seed: 42 by default (see manifest for actual value). Author identities are supplied identifiers, not verified real-world identities. Separation applies within this expert corpus; cross-dataset overlap checks remain for Stage 1.5.

Use expert_training.csv as the permitted code-mixed input for Candidate B in Stage 1.3. Development, annotator calibration and secondary test rows are protected from training. Stage 1.3 packaging is a separate step.

Preserve partition_membership.csv and partition_manifest.json. Use these same memberships across model runs. The script refuses to overwrite an existing output directory. Reproduce into a new directory using the same source and seed.
