"""Read-only author audit. Uses Python standard library; does not assign partitions.

Run: python analyze_authors.py [--source PATH] [--output-dir PATH]
Author keys use outer-whitespace trimming only, preserving case and source values.
"""
import argparse
import csv
import hashlib
import json
import statistics
from collections import Counter, defaultdict
from pathlib import Path

LABELS = {'positive', 'negative', 'neutral'}
MISSING = {'', '---', 'nan', 'none', 'null', 'n/a'}


def author(row):
    value = row['username'].strip()
    return None if value.lower() in MISSING else value


def summarize(rows):
    counts = Counter(author(r) for r in rows if author(r) is not None)
    values = sorted(counts.values())
    ids = Counter(r['id'].strip() for r in rows if r['id'].strip())
    texts = Counter(r['comment/tweet'].strip() for r in rows if r['comment/tweet'].strip())
    return {
        'posts': len(rows), 'known_authors': len(counts),
        'missing_author_posts': sum(author(r) is None for r in rows),
        'posts_per_author_histogram': dict(sorted(Counter(values).items())),
        'mean_posts_per_author': statistics.mean(values) if values else None,
        'median_posts_per_author': statistics.median(values) if values else None,
        'max_posts_per_author': max(values, default=0),
        'top_10_author_posts': sum(sorted(values, reverse=True)[:10]),
        'sentiments': dict(Counter(r['majority_sent'].strip() for r in rows)),
        'languages': dict(Counter(r['lang_id'].strip() for r in rows)),
        'missing_id_posts': sum(not r['id'].strip() for r in rows),
        'duplicate_id_excess_rows': sum(n - 1 for n in ids.values()),
        'empty_text_posts': sum(not r['comment/tweet'].strip() for r in rows),
        'duplicate_trimmed_text_excess_rows': sum(n - 1 for n in texts.values()),
    }


def main():
    base = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, default=base.parent / 'Training Datasets/Sentiment MC Dataset/annotated_bicodemix_publicsa_v2.csv')
    parser.add_argument('--output-dir', type=Path, default=base / 'author_audit')
    args = parser.parse_args()
    with args.source.open(encoding='utf-8-sig', newline='') as stream:
        reader = csv.DictReader(stream)
        required = {'id', 'comment/tweet', 'username', 'majority_sent', 'lang_id'}
        if not required <= set(reader.fieldnames or []):
            raise ValueError('Missing required columns')
        rows = list(reader)
    if any(None in r or any(r[k] is None for k in required) for r in rows):
        raise ValueError('Malformed CSV rows detected')
    cm = [r for r in rows if r['lang_id'].strip() == 'cm']
    eligible = [r for r in cm if r['majority_sent'].strip() in LABELS]
    mono = [r for r in rows if r['lang_id'].strip() in {'my', 'en'} and r['majority_sent'].strip() in LABELS]
    grouped = defaultdict(list)
    for r in rows:
        if author(r) is not None:
            grouped[author(r)].append(r)
    counts = []
    for key, group in grouped.items():
        selected = [r for r in group if r['lang_id'].strip() == 'cm' and r['majority_sent'].strip() in LABELS]
        labels = Counter(r['majority_sent'].strip() for r in selected)
        counts.append({'author_key': key, 'all_posts': len(group), 'labelled_cm_posts': len(selected),
                       'labelled_monolingual_posts': sum(r['lang_id'].strip() in {'my', 'en'} and r['majority_sent'].strip() in LABELS for r in group),
                       **{label: labels[label] for label in sorted(LABELS)}})
    counts.sort(key=lambda x: (-x['labelled_cm_posts'], -x['all_posts'], x['author_key']))
    cm_authors = {author(r) for r in eligible} - {None}
    shared = cm_authors & ({author(r) for r in mono} - {None})
    summary = {'source': str(args.source.resolve()), 'source_sha256': hashlib.sha256(args.source.read_bytes()).hexdigest(),
               'author_rule': 'Trim outer whitespace; preserve case; blank/---/nan/none/null/n/a treated as unknown, not a shared author.',
               'eligibility_rule': 'lang_id=cm and majority_sent in positive/negative/neutral; provisional, no rows deleted.',
               'all_rows': summarize(rows), 'all_code_mixed': summarize(cm), 'labelled_code_mixed': summarize(eligible),
               'code_mixed_without_valid_sentiment': len(cm) - len(eligible),
               'cm_authors_also_in_labelled_monolingual': len(shared),
               'labelled_monolingual_posts_by_shared_authors': sum(author(r) in shared for r in mono),
               'singleton_cm_authors_by_sentiment': dict(Counter(next(k for k in LABELS if r[k]) for r in counts if r['labelled_cm_posts'] == 1)),
               'top_10_labelled_cm_authors': counts[:10]}
    args.output_dir.mkdir(parents=True, exist_ok=True)
    with (args.output_dir / 'author_counts.csv').open('w', encoding='utf-8-sig', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=['author_key', 'all_posts', 'labelled_cm_posts', 'labelled_monolingual_posts', 'negative', 'neutral', 'positive'])
        writer.writeheader()
        writer.writerows(counts)
    (args.output_dir / 'author_summary.json').write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding='utf-8')
    assert sum(r['all_posts'] for r in counts) + summary['all_rows']['missing_author_posts'] == len(rows)
    assert sum(r['labelled_cm_posts'] for r in counts) + summary['labelled_code_mixed']['missing_author_posts'] == len(eligible)
    print(json.dumps(summary, indent=2, ensure_ascii=True))


if __name__ == '__main__':
    main()
