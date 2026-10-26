"""Build Candidate C v1 reproducibly with Python 3.9+ standard library only."""
import argparse
import csv
import hashlib
import io
import json
import unicodedata
from collections import Counter, defaultdict
from difflib import SequenceMatcher
from pathlib import Path

LABELS = {'negative': 0, 'neutral': 1, 'positive': 2}
A_REL = 'Stage 1.1 - MESoc Preparation (Candidate A)/MESocSentiment_Condition_A_v1/condition_a_training.csv'
B_REL = 'Stage 1.3 - Expert-only Preparation (Candidate B)/Expert_Condition_B_v1/condition_b_training.csv'
PART_REL = 'Stage 1.2 - Prepare and partition the expert corpus/expert_partitions_v1'
LOCKED = {
    A_REL: 'b87ee0f801bd8deab4afe5d4714ca8cf3bd0c45d0c107c7caa98dd46a0192d76',
    B_REL: '264a891dfdf27df2745bc66dd4c32f8838f9b008364207fdec534c09d2376f0b',
    PART_REL + '/partition_manifest.json': '9da57b8324a0772a051611c0a74131914baafb3d1f12ef6c8dc8ac62e8c9e7f0',
}
FIELDS = ['record_id', 'dataset_source', 'source_post_id', 'source_row',
          'raw_text', 'text', 'label', 'label_id', 'label_source', 'username', 'lang_id']


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def read_csv(data):
    return list(csv.DictReader(io.StringIO(data.decode('utf-8-sig'), newline='')))


def json_bytes(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + '\n').encode('utf-8')


def csv_bytes(fields, rows):
    stream = io.StringIO(newline='')
    writer = csv.DictWriter(stream, fieldnames=fields, lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode('utf-8')


def convert(rows, source):
    converted = []
    for r in rows:
        is_a = source == 'A'
        post_id = r['post_id'] if is_a else r['id']
        label = r['label'] if is_a else r['majority_sent'].strip()
        text = r['text'] if is_a else r['comment/tweet']
        require(label in LABELS and text.strip() and post_id.strip(), 'Invalid ID, label or text')
        if is_a:
            require(r['label_id'] == str(LABELS[label]), 'A label mapping mismatch')
        else:
            require(r['lang_id'].strip() == 'cm', 'Non-code-mixed B example')
        converted.append(dict(zip(FIELDS, [
            source + ':' + post_id, 'MESocSentiment' if is_a else 'expert', post_id,
            r['source_row'] if is_a else '', r['raw_text'] if is_a else text,
            text, label, LABELS[label], r['label_source'] if is_a else 'expert_majority',
            '' if is_a else r['username'], '' if is_a else r['lang_id'],
        ])))
    require(len({r['record_id'] for r in converted}) == len(converted), 'Duplicate source IDs')
    return converted


def combine(a, b):
    """Expert rows win exact trimmed-text matches; preserve B internal membership."""
    by_text = defaultdict(list)
    for r in b:
        by_text[r['text'].strip()].append(r)
    eligible, log = [], []
    for r in a:
        matches = by_text.get(r['text'].strip(), [])
        if matches:
            for expert in sorted(matches, key=lambda x: x['record_id']):
                log.append({'excluded_a_id': r['record_id'], 'retained_b_id': expert['record_id'],
                            'a_label': r['label'], 'b_label': expert['label'],
                            'label_conflict': str(r['label'] != expert['label']).lower(),
                            'rule': 'exact_trimmed_text_keep_expert', 'text': r['text']})
        else:
            eligible.append(r)
    return eligible + b, log


def sample_neutral(rows, seed):
    """Seeded SHA-256 ranking is independent of input order and RNG versions."""
    counts = Counter(r['label'] for r in rows)
    target = max(counts['positive'], counts['negative'])
    b_neutral = sum(r['dataset_source'] == 'expert' and r['label'] == 'neutral' for r in rows)
    pool = [r for r in rows if r['dataset_source'] == 'MESocSentiment' and r['label'] == 'neutral']
    take = target - b_neutral
    require(0 <= take <= len(pool), 'Neutral target infeasible while retaining all expert rows')
    def score(r):
        return digest(('candidate-c-neutral-v1\n' + str(seed) + '\n' + r['record_id']).encode('utf-8'))
    ranked = sorted(pool, key=lambda r: (score(r), r['record_id']))
    pool_ids = {r['record_id'] for r in pool}
    selected = {r['record_id'] for r in ranked[:take]}
    result = sorted([r for r in rows if r['record_id'] not in pool_ids or r['record_id'] in selected],
                    key=lambda r: r['record_id'])
    log = [{'record_id': r['record_id'], 'seed': seed, 'sha256_score': score(r), 'rank': i,
            'selected': str(i <= take).lower()} for i, r in enumerate(ranked, 1)]
    return result, log, target


def normalized(text):
    return ' '.join(unicodedata.normalize('NFKC', text).casefold().split())


def near_review(a, b):
    """Flag only: normalized equality, or same first 12 chars and similarity >= .95."""
    exact, prefixes = defaultdict(list), defaultdict(list)
    for r in b:
        t = normalized(r['text'])
        exact[t].append(r)
        if len(t) >= 30:
            prefixes[t[:12]].append((t, r))
    log = []
    for r in a:
        t = normalized(r['text'])
        candidates = {x['record_id']: (t, x, 'normalized_equal') for x in exact[t]}
        if len(t) >= 30:
            for u, x in prefixes[t[:12]]:
                candidates.setdefault(x['record_id'], (u, x, 'prefix12_similarity'))
        for _, (u, x, kind) in sorted(candidates.items()):
            if r['text'].strip() == x['text'].strip():
                continue
            ratio = SequenceMatcher(None, t, u, autojunk=False).ratio()
            if ratio >= .95:
                log.append({'a_id': r['record_id'], 'b_id': x['record_id'], 'match_rule': kind,
                            'similarity': format(ratio, '.6f'), 'a_label': r['label'],
                            'b_label': x['label'], 'a_text': r['text'], 'b_text': x['text'],
                            'action': 'flag_only_review_in_stage_1.5'})
    return log


def build(root, out, seed=42):
    require(not out.exists(), 'Output directory exists. Choose a new --output-dir.')
    inputs = {name: (root / name).read_bytes() for name in LOCKED}
    for name, expected in LOCKED.items():
        require(digest(inputs[name]) == expected, 'Input checksum mismatch: ' + name)
    pm = json.loads(inputs[PART_REL + '/partition_manifest.json'])
    for name in ['expert_training.csv', 'expert_development.csv', 'expert_calibration.csv',
                 'expert_secondary_test.csv', 'partition_membership.csv']:
        key = PART_REL + '/' + name
        inputs[key] = (root / key).read_bytes()
        require(digest(inputs[key]) == pm['outputs_sha256'][name], 'Partition checksum mismatch: ' + name)
    require(inputs[B_REL] == inputs[PART_REL + '/expert_training.csv'], 'B differs from fixed training input')
    a, b = convert(read_csv(inputs[A_REL]), 'A'), convert(read_csv(inputs[B_REL]), 'B')
    eligible, duplicate_log = combine(a, b)
    final, sampling_log, target = sample_neutral(eligible, seed)
    near_log = near_review(a, b)
    final_ids = {r['record_id'] for r in final}
    duplicate_ids = {r['excluded_a_id'] for r in duplicate_log}
    inclusion = [{'record_id': r['record_id'], 'label': r['label'],
                  'included': str(r['record_id'] in final_ids).lower(),
                  'reason': ('retained_expert' if r['dataset_source'] == 'expert' else
                             'cross_source_exact_duplicate' if r['record_id'] in duplicate_ids else
                             'neutral_selected' if r['record_id'] in final_ids and r['label'] == 'neutral' else
                             'neutral_not_selected' if r['label'] == 'neutral' else 'retained_non_neutral')}
                 for r in sorted(a + b, key=lambda r: r['record_id'])]
    protected = {}
    for part in ['development', 'calibration', 'secondary_test']:
        held = read_csv(inputs[PART_REL + '/expert_' + part + '.csv'])
        protected[part] = {
            'trimmed_text_overlap': len({r['text'].strip() for r in final} & {r['comment/tweet'].strip() for r in held}),
            'expert_id_overlap': len({r['source_post_id'] for r in b} & {r['id'] for r in held}),
            'expert_author_overlap': len({r['username'].strip() for r in b} & {r['username'].strip() for r in held}),
        }
        require(not any(protected[part].values()), 'Protected overlap: ' + part)
    counts = dict(Counter(r['label'] for r in final))
    require(counts['neutral'] == target, 'Neutral target mismatch')
    require({r['record_id'] for r in b} <= final_ids, 'Expert row lost')
    require(all(r in final for r in eligible if r['label'] != 'neutral'), 'Non-neutral row lost')
    repeated = defaultdict(list)
    for r in final:
        repeated[r['text'].strip()].append(r['record_id'])
    validation = {'all_checks_passed': True, 'all_800_expert_rows_retained': len(b) == 800,
                  'input_hashes_verified': True, 'unique_namespaced_ids': len(final_ids) == len(final),
                  'neutral_target_met': True, 'protected_overlaps': protected,
                  'retained_internal_duplicate_groups': [ids for ids in repeated.values() if len(ids) > 1],
                  'cross_source_exact_pairs': len(duplicate_log), 'near_duplicate_flags': len(near_log),
                  'limitations': ['MESoc author identity is unavailable; cross-source author disjointness cannot be verified.',
                                 'Near-duplicate scan is heuristic, not exhaustive.',
                                 'Quality review, full overlap checks, token lengths and final freeze remain in Stage 1.5.']}
    files = {
        'condition_c_training.csv': csv_bytes(FIELDS, final),
        'cross_source_duplicate_log.csv': csv_bytes(['excluded_a_id', 'retained_b_id', 'a_label', 'b_label', 'label_conflict', 'rule', 'text'], duplicate_log),
        'near_duplicate_review.csv': csv_bytes(['a_id', 'b_id', 'match_rule', 'similarity', 'a_label', 'b_label', 'a_text', 'b_text', 'action'], near_log),
        'neutral_sampling_log.csv': csv_bytes(['record_id', 'seed', 'sha256_score', 'rank', 'selected'], sampling_log),
        'row_inclusion_log.csv': csv_bytes(['record_id', 'label', 'included', 'reason'], inclusion),
        'validation_report.json': json_bytes(validation),
    }
    report = f'''# Stage 1.4: Candidate C preparation

Candidate C contains {len(final):,} rows: {counts['negative']:,} negative, {counts['neutral']:,} neutral and {counts['positive']:,} positive.
All {len(b)} expert training rows are preserved. {sum(x['selected'] == 'true' for x in sampling_log):,} MESoc neutral rows were selected from {len(sampling_log):,} eligible MESoc neutral rows.

## Agreed rules

Combine the fixed Candidate A and B inputs. For exact text matches after outer whitespace trimming, exclude the A row and preserve B, including the expert label if labels conflict. Record every pair. Preserve previous within-source decisions, including B's two distinct IDs with repeated text. No source file or text is edited. Namespaced IDs distinguish A and B IDs.

After cross-source deduplication, keep all positive/negative rows and all expert rows. Set total neutral count equal to the larger positive/negative class. Sample only MESoc neutral rows without replacement. Fail if the target is infeasible.

Seed: {seed}. Selection uses ascending SHA-256 of UTF-8 text `candidate-c-neutral-v1\\n{{seed}}\\n{{record_id}}`, breaking ties by ID. Take the first required number. This is deterministic pseudorandom ranking, not Python random.sample. It avoids dependence on input ordering or changes to random-library sampling algorithms. Every score and selection is recorded. Output is sorted by namespaced ID; shuffle during model training with the training-run seed.

## Audit and reproducibility

Input bytes are locked by SHA-256; changed inputs cause failure. The manifest records input and output checksums and the script checksum. Outputs use UTF-8, LF newlines and deterministic ordering, with no timestamps or machine-specific paths. Existing output directories are refused. Only Python 3.9+ standard-library modules are needed. No installation, downloads or API access is required.

Run `python prepare_candidate_c.py` from this script's folder for the first build. To reproduce, run `python prepare_candidate_c.py --output-dir Combined_Condition_C_v1_reproduced`. Defaults resolve inputs relative to the script, independent of working directory. Use `--rq1-root` for a relocated copy of RQ1. Keep seed 42 to reproduce v1; a different `--seed` produces a different sample.

The neutral log records all eligible A neutral rows. The inclusion log accounts for every A/B row and the reason it was retained or excluded. Original data remain recoverable in A/B. Empty duplicate logs still include headers.

## Validation and remaining work

Exact cross-source pairs: {len(duplicate_log)}. Heuristic near-duplicate pairs: {len(near_log)}. Near-duplicate flags are retained for Stage 1.5 review, not automatically removed. The scan uses NFKC/casefold/whitespace equivalence, plus pairs with the same first 12 normalized characters, at least 30 characters and SequenceMatcher ratio >= 0.95 (autojunk disabled). It is not exhaustive.

Candidate C has no exact trimmed-text match with the protected expert development, calibration or secondary test sets. Expert IDs and author identifiers are also separated. MESoc has no author identifiers, so cross-source author separation cannot be established. Previously retained repeated B text remains intentionally present.

Stage 1.4 preparation is complete. Final A/B/C freeze, full overlap/quality review and tokenizer length checks remain in Stage 1.5. The A-versus-C comparison changes both source composition and class proportions, so results cannot isolate the effect of adding expert data alone.
'''
    files['Preparation_Report.md'] = report.encode('utf-8')
    manifest = {'stage': '1.4', 'version': 1, 'condition': 'C', 'seed': seed,
                'status': 'prepared; final freeze pending Stage 1.5', 'python_requirement': 'Python 3.9+; standard library',
                'input_sha256': {name: digest(data) for name, data in inputs.items()},
                'script_sha256': digest(Path(__file__).read_bytes()), 'label_mapping': LABELS,
                'input_counts': {'A': dict(Counter(r['label'] for r in a)), 'B': dict(Counter(r['label'] for r in b))},
                'after_deduplication': dict(Counter(r['label'] for r in eligible)),
                'final_counts': counts, 'final_rows': len(final), 'neutral_target': target,
                'sampling_algorithm': 'seeded_sha256_ranking_v1',
                'source_counts': dict(Counter(r['dataset_source'] for r in final)),
                'outputs_sha256': {name: digest(data) for name, data in files.items()}}
    files['preparation_manifest.json'] = json_bytes(manifest)
    # Detect concurrent input modification before writing anything.
    require(all((root / name).read_bytes() == data for name, data in inputs.items()), 'Inputs changed during preparation')
    out.mkdir(parents=True, exist_ok=False)
    for name, data in files.items():
        (out / name).write_bytes(data)
    require(all((out / name).read_bytes() == data for name, data in files.items()), 'Saved output verification failed')
    return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--rq1-root', type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument('--output-dir', type=Path, default=Path(__file__).resolve().parent / 'Combined_Condition_C_v1')
    parser.add_argument('--seed', type=int, default=42)
    args = parser.parse_args()
    manifest = build(args.rq1_root.resolve(), args.output_dir.resolve(), args.seed)
    print(json.dumps({'output': str(args.output_dir.resolve()), 'rows': manifest['final_rows'],
                      'classes': manifest['final_counts'], 'seed': args.seed}, indent=2))


if __name__ == '__main__':
    main()
