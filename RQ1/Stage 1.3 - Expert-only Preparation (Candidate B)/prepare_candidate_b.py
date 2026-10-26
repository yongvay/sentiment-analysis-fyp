"""Package fixed Stage 1.2 training membership without modifying source data."""
import argparse
import csv
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_csv(path):
    with path.open(encoding='utf-8-sig', newline='') as stream:
        reader = csv.DictReader(stream)
        return reader.fieldnames, list(reader)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-dir', type=Path, default=Path(__file__).resolve().parent.parent / 'Stage 1.2 - Prepare and partition the expert corpus' / 'expert_partitions_v1')
    parser.add_argument('--output-dir', type=Path, default=Path(__file__).resolve().parent / 'Expert_Condition_B_v1')
    args = parser.parse_args()
    src, out = args.source_dir.resolve(), args.output_dir.resolve()
    require(not out.exists(), 'Output directory already exists; reproduce into a new directory.')
    manifest = json.loads((src / 'partition_manifest.json').read_text(encoding='utf-8'))
    inputs = ['expert_training.csv', 'expert_development.csv', 'expert_calibration.csv', 'expert_secondary_test.csv', 'partition_membership.csv']
    for name in inputs:
        require(sha(src / name) == manifest['outputs_sha256'][name], f'Source hash mismatch: {name}')
    fields, rows = read_csv(src / 'expert_training.csv')
    require(fields == ['id', 'comment/tweet', 'username', 'majority_sent', 'lang_id'], 'Unexpected schema')
    require(len(rows) == 800, 'Expected 800 training posts')
    require(all(all(r[k].strip() for k in fields) for r in rows), 'Missing required value')
    require(all(r['lang_id'].strip() == 'cm' for r in rows), 'Non-code-mixed record')
    counts = dict(Counter(r['majority_sent'].strip() for r in rows))
    require(counts == {'negative': 346, 'neutral': 225, 'positive': 229}, 'Unexpected class counts')
    ids = {r['id'].strip() for r in rows}
    authors = {r['username'].strip() for r in rows}
    texts = {r['comment/tweet'].strip() for r in rows}
    require(len(ids) == 800 and len(authors) == 684, 'ID uniqueness or author count failure')
    _, membership = read_csv(src / 'partition_membership.csv')
    require(len({r['id'] for r in membership}) == len(membership) == 2281, 'Invalid membership records')
    expected = {r['id']: r['author_key'] for r in membership if r['partition'] == 'training'}
    require(expected == {r['id']: r['username'].strip() for r in rows}, 'Training membership mismatch')
    overlaps = {}
    for part in ['development', 'calibration', 'secondary_test']:
        _, protected = read_csv(src / f'expert_{part}.csv')
        overlaps[part] = {
            'post_id': len(ids & {r['id'].strip() for r in protected}),
            'author': len(authors & {r['username'].strip() for r in protected}),
            'trimmed_text': len(texts & {r['comment/tweet'].strip() for r in protected}),
        }
        require(not any(overlaps[part].values()), f'Protected overlap: {part}')
    repeated = defaultdict(list)
    for row in rows:
        repeated[row['comment/tweet'].strip()].append(row['id'])
    duplicate_groups = [group for group in repeated.values() if len(group) > 1]
    checks = {'source_hashes_match_stage12': True, 'fixed_training_membership_matches': True,
              'all_required_values_present': True, 'all_code_mixed': True,
              'unique_post_ids': True, 'protected_partition_overlaps': overlaps,
              'retained_duplicate_text_id_groups': duplicate_groups}
    out.mkdir(parents=True)
    target = out / 'condition_b_training.csv'
    target.write_bytes((src / 'expert_training.csv').read_bytes())
    require(target.read_bytes() == (src / 'expert_training.csv').read_bytes(), 'Output differs from source')
    checks['output_byte_identical_to_training_source'] = True
    (out / 'validation_report.json').write_text(json.dumps(checks, indent=2) + '\n', encoding='utf-8')
    report = '''# Stage 1.3: Candidate B preparation

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
'''
    (out / 'Preparation_Report.md').write_text(report, encoding='utf-8')
    result = {'stage': '1.3', 'version': 1, 'condition': 'B', 'status': 'prepared; final freeze pending Stage 1.5',
              'source_directory': str(src), 'source_partition_seed': manifest['seed'],
              'source_files_sha256': {name: sha(src / name) for name in inputs + ['partition_manifest.json']},
              'script_sha256': sha(Path(__file__)), 'columns': fields, 'posts': len(rows), 'authors': len(authors),
              'sentiments': counts, 'rules': 'All and only fixed expert training rows; cm only; preserve original bytes and membership; exclude protected partitions; no balancing or cleaning.',
              'checks': checks, 'outputs_sha256': {p.name: sha(p) for p in sorted(out.iterdir())}}
    (out / 'preparation_manifest.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'output': str(out), 'posts': len(rows), 'authors': len(authors), 'sentiments': counts, 'checks': checks}, indent=2))


if __name__ == '__main__':
    main()
