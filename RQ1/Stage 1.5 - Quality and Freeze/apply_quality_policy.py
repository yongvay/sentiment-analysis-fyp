"""Apply the approved training-only quality policy; preserve all earlier packages.
Run with Python 3.9+: python apply_quality_policy.py --output-dir quality_candidates_v2
Inputs and reusable processors are pinned in input_lock.json. No external packages.
"""
import argparse
import csv
import hashlib
import importlib.util
import io
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
A = 'Stage 1.1 - MESoc Preparation (Candidate A)/MESocSentiment_Condition_A_v1/condition_a_training.csv'
B = 'Stage 1.3 - Expert-only Preparation (Candidate B)/Expert_Condition_B_v1/condition_b_training.csv'
C = 'Stage 1.4 - Combined Preparation (Candidate C)/Combined_Condition_C_v1/condition_c_training.csv'
PART = 'Stage 1.2 - Prepare and partition the expert corpus/expert_partitions_v1/'
SCAN = 'Stage 1.1 - MESoc Preparation (Candidate A)/prepare_mesoc.py'
COMBINE = 'Stage 1.4 - Combined Preparation (Candidate C)/prepare_candidate_c.py'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def require(ok, message):
    if not ok:
        raise ValueError(message)


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def read(data):
    return list(csv.DictReader(io.StringIO(data.decode('utf-8-sig'), newline='')))


def build(out):
    require(not out.exists(), 'Choose a new output directory; existing outputs are never overwritten.')
    lock = json.loads((HERE / 'input_lock.json').read_text(encoding='utf-8'))
    inputs = {name: (ROOT / name).read_bytes() for name in lock}
    require(all(sha(inputs[name]) == expected for name, expected in lock.items()), 'Pinned input changed.')
    scan, combine = load('quality_scan', ROOT / SCAN), load('quality_combine', ROOT / COMBINE)
    a, b = read(inputs[A]), read(inputs[B])
    require(len(a) == 16968 and len(b) == 800, 'Unexpected baseline counts.')
    audit = []
    for source, rows in [('MESocSentiment', a), ('expert', b)]:
        for row in rows:
            text = row['text'] if source == 'MESocSentiment' else row['comment/tweet'].strip()
            label = row['label'] if source == 'MESocSentiment' else row['majority_sent'].strip()
            post_id = row['post_id'] if source == 'MESocSentiment' else row['id']
            flags = scan.suspicious_flags(text, label)
            if not flags:
                continue
            decision = 'retain_short_or_expressive_text'
            reason = 'Length and repetition alone do not establish invalid sentiment data.'
            unusual = set(flags) - {'short_text', 'repeated_character_run'}
            if unusual:
                require(source == 'MESocSentiment' and post_id == 'mesoc_016651'
                        and unusual == {'possible_promotion'}, 'New flag needs an explicit quality decision.')
                require(text == 'malaysia airlines promo code voucher code discount code malaysiaoffer url'
                        and label == 'neutral', 'Reviewed promotion content changed.')
                decision = 'retain_reviewed_promotion'
                reason = ('Readable promotional content with a plausible neutral label; no established '
                          'advertising exclusion rule. Heuristic flag does not establish unusability. '
                          'Assistant-reviewed; not expert label validation.')
            audit.append(dict(dataset_source=source, post_id=post_id, text=text, label=label,
                              flags=';'.join(flags), decision=decision, reason=reason))
    groups = defaultdict(list)
    for row in b:
        groups[row['comment/tweet'].strip()].append(row)
    duplicate_log, excluded = [], set()
    for text, rows in groups.items():
        if len(rows) < 2:
            continue
        require(len({r['majority_sent'] for r in rows}) == 1, 'Conflicting expert labels need review.')
        ordered = sorted(rows, key=lambda r: int(r['id']))
        for removed in ordered[1:]:
            excluded.add(removed['id'])
            duplicate_log.append(dict(removed, retained_id=ordered[0]['id'],
                                      reason='exact_trimmed_text_duplicate_keep_lowest_numeric_id'))
    require(excluded == {'39303'}, 'Unexpected expert duplicate set.')
    b2 = [r for r in b if r['id'] not in excluded]
    ca, cb = combine.convert(a, 'A'), combine.convert(b2, 'B')
    eligible, cross = combine.combine(ca, cb)
    final, sampling, target = combine.sample_neutral(eligible, 42)
    near = combine.near_review(ca, cb)
    old = {r['record_id']: r for r in read(inputs[C])}
    require({r['record_id'] for r in final} == set(old) - {'B:39303'}, 'Unexpected C membership change.')
    require(all({k: str(v) for k, v in r.items()} == old[r['record_id']] for r in final), 'C row values changed.')
    overlap = {}
    for name, rows in [('A', ca), ('B', cb), ('C', final)]:
        require(len({r['text'].strip() for r in rows}) == len(rows), name + ' has exact duplicates.')
        for partition in ['development', 'calibration', 'secondary_test']:
            held = read(inputs[PART + 'expert_' + partition + '.csv'])
            expert_rows = [r for r in rows if r['dataset_source'] == 'expert']
            result = dict(text=len({r['text'].strip() for r in rows} & {r['comment/tweet'].strip() for r in held}),
                          expert_id=len({r['source_post_id'] for r in expert_rows} & {r['id'] for r in held}),
                          expert_author=len({r['username'].strip() for r in expert_rows} & {r['username'].strip() for r in held}))
            require(not any(result.values()), 'Protected overlap: ' + name + '/' + partition)
            overlap[name + '/' + partition] = result
    reserved = read(inputs['Stage 1.1 - MESoc Preparation (Candidate A)/MESocSentiment_Condition_A_v1/mesoc_reserved_test.csv'])
    reserved_overlap = {name: len({r['text'].strip() for r in rows} & {r['text'].strip() for r in reserved})
                        for name, rows in [('A', ca), ('B', cb), ('C', final)]}
    require(not any(reserved_overlap.values()), 'MESoc reserved text overlap.')
    summary = {source: dict(scanned=sum(r['dataset_source'] == source for r in ca + combine.convert(b, 'B')),
                            flagged=sum(r['dataset_source'] == source for r in audit),
                            flag_counts=dict(Counter(f for r in audit if r['dataset_source'] == source for f in r['flags'].split(';'))))
               for source in ['MESocSentiment', 'expert']}
    counts = {name: dict(Counter(r['label'] for r in rows)) for name, rows in [('A', ca), ('B', cb), ('C', final)]}
    files = {'condition_a_training.csv': inputs[A],
             'condition_b_training.csv': combine.csv_bytes(list(b2[0]), b2),
             'condition_c_training.csv': combine.csv_bytes(combine.FIELDS, final),
             'quality_decisions.csv': combine.csv_bytes(list(audit[0]), audit),
             'expert_duplicate_exclusions.csv': combine.csv_bytes(list(duplicate_log[0]), duplicate_log),
             'neutral_sampling_log.csv': combine.csv_bytes(list(sampling[0]), sampling),
             'cross_source_duplicate_log.csv': combine.csv_bytes(['excluded_a_id','retained_b_id','a_label','b_label','label_conflict','rule','text'], cross),
             'near_duplicate_review.csv': combine.csv_bytes(['a_id','b_id','match_rule','similarity','a_label','b_label','a_text','b_text','action'], near)}
    validation = dict(all_checks_passed=True, protected_overlaps=overlap,
                      mesoc_reserved_text_overlaps=reserved_overlap, exact_text_unique=True,
                      A_byte_identical=True, B_removed_ids=sorted(excluded), C_removed_ids=['B:39303'],
                      C_other_rows_unchanged=True, neutral_target=target, shared_scanner=True,
                      historical_partition_files_unchanged=True, cross_source_author_separation='Unavailable: MESoc lacks author IDs')
    files['validation_report.json'] = combine.json_bytes(validation)
    files['suspicious_text_summary.json'] = combine.json_bytes(dict(datasets=summary, rules=scan.SUSPICIOUS_RULES,
                                                promotion_phrases=scan.PROMOTION_PHRASES))
    report = f'''# Stage 1.5 quality policy applied — final freeze pending

Use the A/B/C CSVs in this package for the next Stage 1.5 checks. Earlier v1 packages remain historical evidence.

## Decisions
- Retain short and expressive text; use the identical MESoc scanner on both training inputs.
- Retain MESoc mesoc_016651 after assistant review: readable neutral promotion, not confirmed unusable. No labels changed.
- Remove redundant exact expert training copy 39303; retain 37432 (lowest numeric ID). Both had the same author, text and negative label.
- The original 800-post expert training partition remains immutable. The derived B input contains 799 posts. No post moves into another partition.
- Preserve previous MESoc near-duplicate exclusions; these historical rules differ from exact-copy deduplication and are not claimed to be identical.
- Regenerate C using the existing seed-42 SHA-256 neutral ranking and expert precedence. Only B:39303 is removed; all other C records and values are unchanged.

## Results
Class counts: {json.dumps(counts, sort_keys=True)}.
Screening counts: {json.dumps(summary, sort_keys=True)}.
Exact-text, protected expert ID/author and MESoc reserved-text checks pass. MESoc author separation cannot be verified.

## Reproduce
Run `python apply_quality_policy.py --output-dir <new-directory>` from the parent stage folder. Inputs and imported processors must match input_lock.json. Existing output folders are refused. This uses only Python's standard library. Output manifests contain all input, script and output SHA-256 hashes.

## Status and superseded decisions
This decision record supersedes the earlier requirement to review all short/repeated-character flags and the decision to retain both expert duplicate copies in training. It does not rewrite historical preparation evidence or partition membership.
The Excel tracker still describes the historical v1 candidates; consult this package for current quality-adjusted inputs.
Final tokenizer-length/truncation checks, hardware trial, shared training configuration and final freeze are still pending. This package is not declared frozen for training.
'''
    files['Quality_Report.md'] = report.encode('utf-8')
    manifest = dict(version='quality_candidates_v2', status='quality policy applied; final freeze pending',
                    input_sha256=lock, script_sha256=sha(Path(__file__).read_bytes()),
                    input_lock_sha256=sha((HERE / 'input_lock.json').read_bytes()),
                    seed=42, class_counts=counts, rows={'A':len(a),'B':len(b2),'C':len(final)},
                    outputs_sha256={name: sha(data) for name, data in sorted(files.items())})
    files['preparation_manifest.json'] = combine.json_bytes(manifest)
    require(all((ROOT / name).read_bytes() == data for name, data in inputs.items()), 'Input changed during run.')
    out.mkdir(parents=True)
    for name, data in files.items():
        (out / name).write_bytes(data)
        require((out / name).read_bytes() == data, 'Saved output mismatch.')
    print(json.dumps(dict(rows=manifest['rows'], class_counts=counts, screening=summary, validation=validation), indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, default=HERE / 'quality_candidates_v2')
    build(parser.parse_args().output_dir.resolve())
