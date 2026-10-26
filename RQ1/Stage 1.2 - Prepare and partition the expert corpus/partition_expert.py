"""Reproducible code-mixed-only, four-way author-disjoint partitioning.

Run: python partition_expert.py [--source PATH] [--output-dir PATH] [--seed 42]
No source files are modified. Existing output directories are refused.
"""
import argparse
import csv
import hashlib
import json
import random
from collections import Counter, defaultdict
from pathlib import Path

LABELS = ['negative', 'neutral', 'positive']
SIZES = {'training': 800, 'development': 600, 'calibration': 120, 'secondary_test': 761}
FIELDS = ['id', 'comment/tweet', 'username', 'majority_sent', 'lang_id']


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_csv(path, fields, rows):
    with path.open('w', encoding='utf-8-sig', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(rows)


def main():
    base = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, default=base.parent / 'Training Datasets/Sentiment MC Dataset/annotated_bicodemix_publicsa_v2.csv')
    parser.add_argument('--output-dir', type=Path, default=base / 'expert_partitions_v1')
    parser.add_argument('--seed', type=int, default=42)
    args = parser.parse_args()
    if args.output_dir.exists():
        raise FileExistsError('Output directory already exists; use a new version directory to preserve membership.')
    with args.source.open(encoding='utf-8-sig', newline='') as stream:
        reader = csv.DictReader(stream)
        if not set(FIELDS) <= set(reader.fieldnames or []):
            raise ValueError('Missing required columns')
        source = list(reader)
    eligible, excluded = [], []
    for number, row in enumerate(source, 2):
        if None in row or any(row[k] is None for k in FIELDS):
            raise ValueError(f'Malformed CSV record {number}')
        reason = ('not_code_mixed' if row['lang_id'].strip() != 'cm' else
                  'missing_or_invalid_sentiment' if row['majority_sent'].strip() not in LABELS else '')
        if reason:
            excluded.append({'source_record': number, 'id': row['id'], 'reason': reason})
        else:
            eligible.append(row)
    assert len(eligible) == sum(SIZES.values()), 'Eligible count differs from planned 2,281'
    assert len({r['id'].strip() for r in eligible}) == len(eligible), 'Duplicate IDs'
    groups = defaultdict(list)
    for row in eligible:
        assert row['id'].strip() and row['comment/tweet'].strip(), 'Missing ID/text'
        key = row['username'].strip()
        assert key.lower() not in {'', '---', 'nan', 'none', 'null', 'n/a'}, 'Missing author'
        groups[key].append(row)
    total = Counter(r['majority_sent'].strip() for r in eligible)
    # Round proportional class quotas while satisfying every row and column total.
    n = len(eligible)
    quota = {p: {c: SIZES[p] * total[c] // n for c in LABELS} for p in SIZES}
    cells = sorted(((SIZES[p] * total[c] % n, p, c) for p in SIZES for c in LABELS), reverse=True)
    while sum(sum(v.values()) for v in quota.values()) < n:
        progressed = False
        for _, p, c in cells:
            if sum(quota[p].values()) < SIZES[p] and sum(quota[q][c] for q in SIZES) < total[c]:
                quota[p][c] += 1
                progressed = True
        assert progressed, 'Unable to round quotas'
    rng = random.Random(args.seed)
    grouped = sorted(groups.items())
    rng.shuffle(grouped)
    grouped.sort(key=lambda item: -len(item[1]))
    remaining = {p: dict(q) for p, q in quota.items()}
    assignments = {}
    # Large groups first; singleton groups can then fill individual class deficits.
    for key, rows in grouped:
        vector = Counter(r['majority_sent'].strip() for r in rows)
        choices = [p for p in SIZES if all(remaining[p][c] >= vector[c] for c in LABELS)]
        if not choices:
            raise ValueError('No exact allocation found for this seed; nothing written')
        weights = [sum(remaining[p].values()) for p in choices]
        p = rng.choices(choices, weights=weights, k=1)[0]
        assignments[key] = p
        for c in LABELS:
            remaining[p][c] -= vector[c]
    assert all(v == 0 for q in remaining.values() for v in q.values())
    partitions = {p: [] for p in SIZES}
    for row in eligible:
        partitions[assignments[row['username'].strip()]].append(row)
    texts = defaultdict(list)
    for row in eligible:
        texts[row['comment/tweet'].strip()].append(row)
    duplicate_rows = []
    for text, rows in texts.items():
        if len(rows) > 1:
            destinations = {assignments[r['username'].strip()] for r in rows}
            assert len(destinations) == 1, 'Duplicate text crosses partitions'
            for row in rows:
                duplicate_rows.append({'id': row['id'], 'author_key': row['username'].strip(),
                                       'partition': next(iter(destinations)), 'text_sha256': hashlib.sha256(text.encode()).hexdigest(),
                                       'policy': 'Retained as distinct source IDs; same author and partition'})
    stats = {}
    for p, rows in partitions.items():
        labels = Counter(r['majority_sent'].strip() for r in rows)
        assert len(rows) == SIZES[p] and dict(labels) == quota[p]
        stats[p] = {'posts': len(rows), 'authors': len({r['username'].strip() for r in rows}), 'sentiments': dict(labels)}
    # All validation occurs before writing any outputs.
    args.output_dir.mkdir(parents=True)
    for p, rows in partitions.items():
        rng.shuffle(rows)
        write_csv(args.output_dir / f'expert_{p}.csv', FIELDS, rows)
    write_csv(args.output_dir / 'partition_membership.csv', ['id', 'author_key', 'partition'],
              [{'id': r['id'], 'author_key': r['username'].strip(), 'partition': assignments[r['username'].strip()]} for r in eligible])
    write_csv(args.output_dir / 'excluded_records.csv', ['source_record', 'id', 'reason'], excluded)
    write_csv(args.output_dir / 'duplicate_text_review.csv', ['id', 'author_key', 'partition', 'text_sha256', 'policy'], duplicate_rows)
    manifest = {'version': 1, 'seed': args.seed, 'source': str(args.source.resolve()), 'source_sha256': sha(args.source),
                'script_sha256': sha(Path(__file__)), 'source_posts': len(source), 'eligible_posts': n,
                'excluded_by_reason': dict(Counter(r['reason'] for r in excluded)),
                'eligibility': 'lang_id.strip() == cm; majority_sent.strip() in negative/neutral/positive. No monolingual rows permitted in Stage 1.3.',
                'author_policy': 'Outer whitespace trimmed, case preserved; all eligible posts per author assigned to exactly one of four partitions.',
                'text_policy': 'Original source values preserved; trimmed text checked for cross-partition duplicates. Repeated source IDs prohibited; distinct IDs with identical text retained together.',
                'algorithm': 'Proportional integer quotas with fixed margins; seeded shuffle, descending author-group size, random capacity-weighted feasible allocation; seeded row shuffle.',
                'membership_policy': 'Use saved membership as authority. Do not repartition for model seeds; changes require a new version and recorded rationale.',
                'partitions': stats, 'class_quotas': quota,
                'checks': {'exact_sizes': True, 'exact_class_quotas': True, 'author_overlap': 0, 'post_id_overlap': 0, 'trimmed_text_overlap': 0, 'all_eligible_rows_assigned_once': True},
                'outputs_sha256': {p.name: sha(p) for p in sorted(args.output_dir.glob('*.csv'))}}
    (args.output_dir / 'partition_manifest.json').write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    lines = ['# Stage 1.2 partition report', '', 'Only labelled code-mixed posts are included. Monolingual data is excluded from Stage 1.3 training by user decision.', '',
             '| Partition | Posts | Authors | Negative | Neutral | Positive |', '|---|---:|---:|---:|---:|---:|']
    for p, s in stats.items():
        lines.append(f"| {p} | {s['posts']} | {s['authors']} | {s['sentiments']['negative']} | {s['sentiments']['neutral']} | {s['sentiments']['positive']} |")
    lines += ['', 'All four partitions are pairwise author-disjoint, ID-disjoint and exact-trimmed-text-disjoint. All 2,281 eligible records appear exactly once. Exact target sizes and proportional integer class quotas were met.', '',
              'Excluded from these partitions: 7,680 non-code-mixed records and 39 code-mixed records without a valid sentiment label. The source file remains unchanged.', '',
              'The two identical-text records (IDs 39303 and 37432) are retained together under their shared author. This preserves the planned 2,281 records; record the repeated content as a limitation. No near-duplicate or semantic similarity audit has been performed.', '',
              'Seed: 42 by default (see manifest for actual value). Author identities are supplied identifiers, not verified real-world identities. Separation applies within this expert corpus; cross-dataset overlap checks remain for Stage 1.5.', '',
              'Use expert_training.csv as the permitted code-mixed input for Candidate B in Stage 1.3. Development, annotator calibration and secondary test rows are protected from training. Stage 1.3 packaging is a separate step.', '',
              'Preserve partition_membership.csv and partition_manifest.json. Use these same memberships across model runs. The script refuses to overwrite an existing output directory. Reproduce into a new directory using the same source and seed.']
    (args.output_dir / 'Partition_Report.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(json.dumps({'partitions': stats, 'checks': manifest['checks'], 'output_dir': str(args.output_dir)}, indent=2))


if __name__ == '__main__':
    main()
