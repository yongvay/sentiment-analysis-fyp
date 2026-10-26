# Stage 1.2 author audit

Source: `RQ1/Training Datasets/Sentiment MC Dataset/annotated_bicodemix_publicsa_v2.csv`.
The source is unchanged. No partitions have been assigned.
Reproduce with `python analyze_authors.py` from the parent stage folder.
Full counts, rules and source SHA-256 are in `author_summary.json`; per-author counts are in `author_counts.csv`.

## Pool reconciliation

- Full dataset: 10,000 posts, 7,880 distinct nonmissing author identifiers.
- Code-mixed (`lang_id=cm`): 2,320 posts.
- Code-mixed with blank sentiment: 39 posts.
- Code-mixed with positive, negative or neutral sentiment: 2,281 posts, matching the tracker.
- Labelled code-mixed class counts: negative 988, positive 653, neutral 640.
- This is a provisional label-based pool. No source records were removed.

## Authors in the 2,281-post pool

| Posts per author | Authors | Posts |
|---|---:|---:|
| 1 | 1,756 | 1,756 |
| 2 | 132 | 264 |
| 3-5 | 54 | 191 |
| 6-11 | 9 | 70 |
| Total | 1,951 | 2,281 |

Mean: 1.169 posts per author. Median: 1. Maximum: 11.
There are 195 authors with multiple posts, accounting for 525 posts.
Author grouping trims outer whitespace and preserves case. Counts refer to supplied identifiers, not verified real-world individuals or linked cross-platform accounts.

## Interpretation and remaining checks

Author-disjoint splitting appears practical: author groups are small and many singleton authors provide flexibility for adjusting sizes and sentiment proportions. Exact simultaneous partition sizes and class targets have not yet been tested by an assignment algorithm.

Proposed next step: construct a provisional four-way author-grouped allocation targeting 800/600/120/761 posts, with approximately proportional sentiment distributions. Validate author and post-ID separation before accepting any split.

There are no missing authors, missing IDs, duplicate IDs or empty texts in the labelled code-mixed pool. One exact trimmed-text duplicate contributes one excess row and requires review before freezing membership. Do not automatically delete it or allow equivalent text to leak between training and evaluation.

415 authors in this pool also contribute 811 labelled monolingual posts. If Stage 1.3 adds monolingual training data, exclude posts belonging to protected held-out authors according to the agreed partition policy.

The source README defines `my` as Malay, `en` as English and `cm` as code-mixed. It describes three expert sentiment annotators and one expert language annotator. It does not explain the reason for blank majority sentiment values; do not infer that they necessarily mean ties.
