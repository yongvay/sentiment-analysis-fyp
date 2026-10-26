"""Reproducible MESocSentiment preparation; standard library only.
Run: python prepare_mesoc.py --root <RQ1 folder> --output <new output folder>
The RQ1 folder must contain Training Datasets; the output folder must not exist.
Outputs are candidates, not a frozen train split. Never changes source files.
"""
import argparse
import csv
import hashlib
import json
import re
import unicodedata
from collections import Counter, defaultdict
from difflib import SequenceMatcher
from html import unescape
from pathlib import Path

LABELS = {'negative': 0, 'neutral': 1, 'positive': 2}
FIELDS = ['post_id', 'source_row', 'raw_text', 'text', 'label', 'label_id', 'label_source', 'dataset_source']

def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def read(p):
    with p.open(encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))

def write(p, rows, fields):
    with p.open('w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

def review_key(text):
    return re.sub(r'\s+', ' ', unicodedata.normalize('NFKC', text).casefold()).strip()

SUSPICIOUS_RULES = {
    'empty_text': 'Empty after stripping whitespace.',
    'invalid_label': 'Label outside negative, neutral, positive.',
    'replacement_character': 'Contains U+FFFD; possible decoding damage.',
    'control_character': 'Unicode Cc character other than tab, CR or LF.',
    'invisible_format_character': 'Unicode Cf character other than joiners U+200C/U+200D.',
    'possible_mojibake': 'Common broken UTF-8 sequences; heuristic only.',
    'html_tag': 'Tag-like HTML element.',
    'html_entity': 'Named or numeric entity that html.unescape changes.',
    'url_or_mention_only': 'Only URLs/mentions, whitespace and surrounding punctuation.',
    'short_text': 'Fewer than 3 whitespace-separated units OR fewer than 10 characters.',
    'no_letters_or_numbers': 'No Unicode letters or numbers; may be valid emoji sentiment.',
    'repeated_character_run': 'Same non-whitespace character repeated at least 6 times.',
    'possible_promotion': 'At least 2 distinct promotion phrases; heuristic only.',
}
PROMOTION_PHRASES = ('buy now', 'shop now', 'free shipping', 'click here', 'order now',
                     'limited offer', 'discount code', 'promo code', 'beli sekarang',
                     'penghantaran percuma', 'klik sini', 'order sekarang', 'stok terhad')


def suspicious_flags(text, label):
    flags = []
    def flag(name, condition):
        if condition:
            flags.append(name)
    flag('empty_text', not text.strip())
    flag('invalid_label', label not in LABELS)
    flag('replacement_character', '\ufffd' in text)
    flag('control_character', any(unicodedata.category(c) == 'Cc' and c not in '\t\r\n' for c in text))
    flag('invisible_format_character', any(unicodedata.category(c) == 'Cf' and c not in '\u200c\u200d' for c in text))
    flag('possible_mojibake', any(s in text for s in ('\u00c3\u00a9', '\u00c2\u00a0', '\u00e2\u20ac', '\u00f0\u0178')))
    flag('html_tag', re.search(r'</?[A-Za-z][A-Za-z0-9]*(?:\s+[^<>]*)?\s*/?>', text) is not None)
    entities = re.findall(r'&(?:#[0-9]+|#x[0-9a-fA-F]+|[A-Za-z][A-Za-z0-9]+);', text)
    flag('html_entity', any(unescape(e) != e for e in entities))
    remainder = re.sub(r'https?://\S+|www\.\S+|(?<!\w)@\w+', '', text, flags=re.I)
    flag('url_or_mention_only', remainder != text and all(c.isspace() or unicodedata.category(c).startswith('P') for c in remainder))
    flag('short_text', bool(text.strip()) and (len(text.split()) < 3 or len(text) < 10))
    flag('no_letters_or_numbers', bool(text.strip()) and not any(c.isalnum() for c in text))
    flag('repeated_character_run', re.search(r'(\S)\1{5,}', text) is not None)
    flag('possible_promotion', sum(bool(re.search(r'(?<!\w)' + re.escape(p) + r'(?!\w)', text.casefold())) for p in PROMOTION_PHRASES) >= 2)
    return flags


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', type=Path, required=True,
                    help='RQ1 folder containing Training Datasets')
    ap.add_argument('--output', type=Path, required=True,
                    help='New output directory; must not already exist')
    args = ap.parse_args()
    source = args.root / 'Training Datasets/MESocSentiment-main/MESocSentiment Corpus'
    paths = {name: source / name for name in ['MESocSentiment Corpus.csv', 'Test Set.csv', 'Train Set.csv']}
    hashes = {k: digest(v) for k, v in paths.items()}
    corpus, test, train = [read(paths[k]) for k in paths]
    assert corpus and set(corpus[0]) == {'Tweets', 'Sentiment (All)'}
    assert test and {'Tweets', 'Sentiment (MESocSentiment)', 'Sentiment (Manual)'} <= set(test[0])
    testkeys = {r['Tweets'].strip() for r in test}
    groups = defaultdict(list)
    records = []
    for i, r in enumerate(corpus, 1):
        label = r['Sentiment (All)'].strip().lower()
        item = dict(post_id=f'mesoc_{i:06d}', source_row=i, raw_text=r['Tweets'],
                    text=r['Tweets'].strip(), label=label, label_id=LABELS.get(label, ''),
                    label_source='automatic', dataset_source='MESocSentiment')
        records.append(item)
        groups[item['text']].append(item)
    candidates, exclusions = [], []
    for r in records:
        group = groups[r['text']]
        reason = ''
        if r['text'] in testkeys:
            reason = 'reserved_supplied_test_text'
        elif not r['text']:
            reason = 'empty_text'
        elif r['label'] not in LABELS:
            reason = 'invalid_label'
        elif len({x['label'] for x in group}) > 1:
            reason = 'conflicting_labels_same_prepared_text'
        elif r['post_id'] != group[0]['post_id']:
            reason = 'duplicate_prepared_text_same_label'
        if reason:
            exclusions.append({**r, 'reason': reason})
        else:
            candidates.append(r)
    audit = []
    for i, r in enumerate(test, 1):
        matched = groups.get(r['Tweets'].strip(), [])
        assert matched, 'Supplied test text not found in corpus'
        audit.append(dict(audit_id=f'mesoc_test_{i:06d}', source_row=i,
                          corpus_post_ids=';'.join(x['post_id'] for x in matched),
                          raw_text=r['Tweets'], text=r['Tweets'].strip(),
                          automatic_label=r['Sentiment (MESocSentiment)'].strip().lower(),
                          manual_label=r['Sentiment (Manual)'].strip().lower()))
    # Screen once, then exclude every flagged candidate endpoint by user policy.
    review = []
    candidate_ids = {r['post_id'] for r in candidates}
    keyed = defaultdict(list)
    for r in records:
        keyed[review_key(r['text'])].append(r)
    for group in keyed.values():
        if len(group) > 1 and any(r['post_id'] in candidate_ids for r in group):
            for other in group[1:]:
                review.append(dict(post_id_a=group[0]['post_id'], post_id_b=other['post_id'],
                    reason='case_unicode_or_whitespace_equivalent', similarity=1.0,
                    a_reserved=group[0]['text'] in testkeys, b_reserved=other['text'] in testkeys,
                    text_a=group[0]['text'], text_b=other['text'], decision='pending'))
    ordered = sorted(records, key=lambda r: review_key(r['text']))
    for a, b in zip(ordered, ordered[1:]):
        x, y = review_key(a['text']), review_key(b['text'])
        if x == y or min(len(x), len(y)) < 30 or x[:12] != y[:12]:
            continue
        if a['post_id'] not in candidate_ids and b['post_id'] not in candidate_ids:
            continue
        score = SequenceMatcher(None, x, y, autojunk=False).ratio()
        if score >= .95:
            review.append(dict(post_id_a=a['post_id'], post_id_b=b['post_id'],
                reason='adjacent_sorted_text_similarity_at_least_0.95', similarity=round(score, 6),
                a_reserved=a['text'] in testkeys, b_reserved=b['text'] in testkeys,
                text_a=a['text'], text_b=b['text'], decision='pending'))
    flagged_ids = {pair[k] for pair in review for k in ('post_id_a', 'post_id_b')} & candidate_ids
    exclusions.extend(dict(r, reason='flagged_near_duplicate_user_policy')
                      for r in candidates if r['post_id'] in flagged_ids)
    candidates = [r for r in candidates if r['post_id'] not in flagged_ids]
    for pair in review:
        pair['decision'] = 'exclude_all_candidate_endpoints_preserve_reserved'
    candidate_ids = {r['post_id'] for r in candidates}
    exclusion_reasons = {r['post_id']: r['reason'] for r in exclusions}
    suspicious = []
    for r in records:
        flags = suspicious_flags(r['text'], r['label'])
        if flags:
            suspicious.append(dict(r, disposition='candidate' if r['post_id'] in candidate_ids else 'excluded',
                exclusion_reason=exclusion_reasons.get(r['post_id'], ''), flags=';'.join(flags), flag_count=len(flags),
                character_count=len(r['text']), whitespace_unit_count=len(r['text'].split()),
                decision='flag_only_no_additional_removal'))
    assert not (candidate_ids & flagged_ids)
    assert len(candidates) + len(exclusions) == len(corpus)
    assert len({r['post_id'] for r in candidates}) == len(candidates)
    assert len({r['text'] for r in candidates}) == len(candidates)
    assert not ({r['text'] for r in candidates} & testkeys)
    assert all(r['label_id'] == LABELS[r['label']] for r in candidates)
    assert hashes == {k: digest(v) for k, v in paths.items()}, 'Source changed during processing'
    args.output.mkdir(parents=True, exist_ok=False)
    write(args.output/'condition_a_training.csv', candidates, FIELDS)
    write(args.output/'mesoc_exclusions.csv', exclusions, FIELDS+['reason'])
    write(args.output/'mesoc_reserved_test.csv', audit, list(audit[0]))
    review_fields=['post_id_a','post_id_b','reason','similarity','a_reserved','b_reserved','text_a','text_b','decision']
    write(args.output/'mesoc_duplicate_review.csv', review, review_fields)
    write(args.output/'mesoc_suspicious_text.csv', suspicious,
          FIELDS + ['disposition', 'exclusion_reason', 'flags', 'flag_count',
                    'character_count', 'whitespace_unit_count', 'decision'])
    suspicious_summary = dict(scanned_rows=len(records), flagged_rows=len(suspicious),
        flagged_candidate_rows=sum(r['disposition'] == 'candidate' for r in suspicious),
        flag_counts=dict(Counter(f for r in suspicious for f in r['flags'].split(';'))),
        candidate_flag_counts=dict(Counter(f for r in suspicious if r['disposition'] == 'candidate' for f in r['flags'].split(';'))),
        rules=SUSPICIOUS_RULES, promotion_phrases=PROMOTION_PHRASES,
        policy='Flag only; no additional removal or text modification. Flags are not confirmed errors.')
    (args.output/'suspicious_text_summary.json').write_text(json.dumps(suspicious_summary, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
    summary = dict(status='CANDIDATE: suspicious-text assessment, expert overlap and training freeze pending',
        input_rows=len(corpus), supplied_train_rows=len(train), supplied_test_rows=len(test),
        candidate_rows=len(candidates), class_counts=dict(Counter(r['label'] for r in candidates)),
        exclusions=dict(Counter(r['reason'] for r in exclusions)),
        whitespace_trimmed_rows=sum(r['raw_text'] != r['text'] for r in records),
        duplicate_review_pairs=len(review), near_duplicate_excluded_rows=len(flagged_ids),
        suspicious_text=suspicious_summary, source_sha256=hashes,
        script_sha256=digest(Path(__file__)), label_mapping=LABELS,
        checks='row reconciliation, unique IDs/text, no prepared exact audit overlap, valid labels, originals unchanged: PASS',
        rules=dict(cleaning='strip leading/trailing whitespace only', balancing='none',
        random_split='none; expert development set will be used', supplied_train='not used for training',
        fuzzy_screen='NFKC/casefold/whitespace equivalence plus adjacent sorted pairs with common first 12 characters, minimum 30 chars and SequenceMatcher >=0.95; not exhaustive',
        near_duplicate_policy='User-selected exclusion of every candidate endpoint in original flagged pairs, regardless of label; preserve reserved records; no iterative rescreening',
        suspicious_text_policy='Flag only; preserve text and do not automatically exclude suspicious rows'))
    (args.output/'preparation_manifest.json').write_text(json.dumps(summary, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
    counts='\n'.join(f'| {k} | {v:,} |' for k,v in summary['class_counts'].items())
    report=f'''# MESocSentiment Condition A preparation report

Status: **Candidate dataset. Not frozen for training.**

## Result

- Original corpus: {len(corpus):,} records.
- Reserved supplied test file: {len(test):,} records, retaining both manual and automatic labels.
- Candidate training pool: {len(candidates):,} records.
- Excluded corpus records: {len(exclusions):,}.
- Source rows whose surrounding whitespace was trimmed: {summary['whitespace_trimmed_rows']:,}.
- Original duplicate pairs handled by exclusion policy: {len(review):,}.
- Unique candidate rows excluded by that policy: {len(flagged_ids):,}.
- Suspicious rows flagged across the original corpus: {len(suspicious):,}.
- Remaining candidate rows with suspicious-text flags: {suspicious_summary['flagged_candidate_rows']:,}.

| Candidate label | Count |
|---|---:|
{counts}

## Processing decisions

Original CSVs were not changed. IDs use original data-row positions (header excluded) and are tied to source SHA-256 hashes in the manifest. Raw text is preserved. The training text only has leading/trailing whitespace removed. Sentiment labels are mapped to negative=0, neutral=1, positive=2. Labels remain automatic; they have not been corrected by a person.

All texts matching the supplied test file after trimming are reserved. This follows the preparation decision discussed for this project; it does not replace the expert development/test design. Invalid and empty records are excluded. All members of a conflicting-label exact-text group are quarantined; same-label exact duplicates retain the first source row. Each exclusion is recorded with its reason.

No class balancing, model tokenisation, length filtering, spam filtering, label correction, or random 80/20 split was performed. The supplied Train Set.csv is inventoried but not used as training input.

By the user's decision, every candidate post participating in an originally flagged near-duplicate pair is excluded, including both endpoints of candidate-candidate pairs. Reserved test records are preserved. This conservative policy does not establish semantic equivalence and may discard distinct posts. The original screen is applied once, without iterative rescreening after removal. Excluded rows remain recoverable in mesoc_exclusions.csv; each pair records its policy decision.

Suspicious-text scanning checks all original corpus records, including excluded records, for empty text, invalid labels, possible encoding damage, control/invisible characters, HTML, URL/mention-only content, short or non-alphanumeric text, repeated characters and possible promotion. It only flags these conditions; it does not remove or modify additional rows. Emoji, negation, capitalisation and Manglish spelling are preserved. Exact rules and thresholds are recorded in suspicious_text_summary.json. A row can have multiple flags, so flag counts do not sum to unique flagged rows. Character counts and whitespace-unit counts are not model-token lengths.

## Verification

{summary['checks']}

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
'''
    (args.output/'Preparation_Report.md').write_text(report, encoding='utf-8')
    (args.output/'prepare_mesoc.py').write_bytes(Path(__file__).read_bytes())
    # Read back every CSV so encoding, multiline text and numeric mapping survive serialization.
    reread = read(args.output/'condition_a_training.csv')
    assert len(reread) == len(candidates)
    assert all(a['text'] == b['text'] and str(a['label_id']) == b['label_id'] for a,b in zip(candidates,reread))
    print(json.dumps(summary, indent=2))

if __name__ == '__main__':
    main()
