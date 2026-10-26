# -*- coding: utf-8 -*-
"""
Dr. Ho pre-submission checker.

Runs the mechanical passes from ICON_AI_Master_Comment_Tracker.md over a .docx.
It cannot judge meaning; it catches the patterns he has flagged repeatedly.

    python3 check_section.py "ICON AI 2026 - Section 1 (v15).docx"
    python3 check_section.py paper.docx --from "2. Why Malaysian" --to "References"

Passes:
  1  sentences over 35 words                        (R1 2, R2 45)
  2  same source cited on consecutive sentences      (Rule 16 - R4 1)
  3  Rule 2 trigger words with no citation on the sentence
  4  previously flagged informal wording and metaphors
  5  evaluative adjectives that need an operational definition (Rule 18 - R4 40)
  6  bold runs in the body                           (Rule 11)
  7  (Section X) / (Table X) cross-references        (Rule 12)
  8  sentence-initial demonstratives to eyeball      (Rule 4)
"""
import sys, re, zipfile

T_RE = re.compile(r'<w:t(?:\s[^>]*)?>(.*?)</w:t>', re.S)
P_RE = re.compile(r'<w:p\b.*?</w:p>|<w:p\b[^>]*/>', re.S)
R_RE = re.compile(r'<w:r\b(?:(?!<w:r\b).)*?</w:r>', re.S)

TRIGGERS = (r'\b(most|usually|commonly|normally|often|the literature|elsewhere|'
            r'is treated as|well described|the most widely used|in common use|'
            r'the field|widely|generally accepted)\b')

INFORMAL = ['carries over', 'carry over', 'stay inside', 'how good', ' thin ',
            'unsurprising', 'kind of', ' friction', 'audit', 'on its own',
            'giving up', 'bear on', 'stops there', ' equally ', 'trustworthy',
            'settled practice', 'built to', 'at the expense of', 'stops being',
            'diagnosis', 'regional corpora', 'this material', ' in part',
            ' actually ', ' simply ', 'such text', 'either weakness',
            'the statistic used', 'on that account', 'against that',
            'reach beyond', 'damages the model', 'spread across', 'dilutes',
            'no longer reflects', 'cannot handle', 'fails to', 'corrupts']

EVALUATIVE = ['large', 'small', 'balanced', 'comprehensive', 'strong', 'weak',
              'high', 'low', 'limited', 'significant', 'substantial', 'heavy',
              'casual', 'sound', 'good', 'poor']

DEMONSTRATIVE = r'^(This|These|Those|It|They|Both|Such|The argument|The problem|The field)\b'


def text_of(p):
    return ''.join(T_RE.findall(p)).replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')


def sentences(t):
    t = re.sub(r'\b(et al|e\.g|i\.e|vs|Dr|No|Vol|pp|Fig)\.', r'\1<D>', t)
    t = re.sub(r'\b([A-Z])\.', r'\1<D>', t)
    return [s.replace('<D>', '.').strip()
            for s in re.split(r'(?<=[.?!:])\s+', t) if s.strip()]


def sources(s):
    out = set()
    for m in re.finditer(r'([A-ZÀ-Ž][\wÀ-ž\'’-]+)\s+'
                         r'(?:et al\.|and\s+[A-ZÀ-Ž][\wÀ-ž\'’-]+)?\s*\((\d{4})\)', s):
        out.add(m.group(1) + ' ' + m.group(2))
    for m in re.finditer(r'\(([^)]*\d{4}[^)]*)\)', s):
        for piece in m.group(1).split(';'):
            mm = re.match(r'\s*([A-ZÀ-Ž][\wÀ-ž\'’-]+)[^,]*,\s*(\d{4})', piece.strip())
            if mm:
                out.add(mm.group(1) + ' ' + mm.group(2))
    return out


def has_citation(s):
    return bool(re.search(r'\(\d{4}\)|\([^)]*\d{4}[^)]*\)', s))


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    path = sys.argv[1]
    args = sys.argv[2:]
    start = args[args.index('--from') + 1] if '--from' in args else '1. Introduction'
    stop = args[args.index('--to') + 1] if '--to' in args else 'References'

    doc = zipfile.ZipFile(path).read('word/document.xml').decode('utf8')
    paras = P_RE.findall(doc)
    texts = [text_of(p) for p in paras]

    try:
        i0 = next(i for i, t in enumerate(texts) if t.strip().startswith(start))
        i1 = next(i for i, t in enumerate(texts) if t.strip().startswith(stop) and i > i0)
    except StopIteration:
        print('Could not locate "%s" .. "%s" in %s' % (start, stop, path))
        return 1

    body_p = [(i, texts[i]) for i in range(i0 + 1, i1) if texts[i].strip()]
    blob = ' '.join(t for _, t in body_p)
    issues = 0

    print('=' * 72)
    print('%s   |   %s .. %s' % (path, start, stop))
    print('%d paragraphs, %d words' % (len(body_p), len(blob.split())))
    print('=' * 72)

    print('\n[1] Sentences over 35 words')
    n = 0
    for _, t in body_p:
        for s in sentences(t):
            if len(s.split()) > 35:
                print('    %2d  %s' % (len(s.split()), s[:110]))
                n += 1
    print('    -> %d  (a numbered list may legitimately run long)' % n); issues += n

    print('\n[2] Same source cited on consecutive sentences  (Rule 16)')
    n = 0
    for pi, (_, t) in enumerate(body_p, 1):
        ss = sentences(t)
        for a, b, sb in zip(map(sources, ss), map(sources, ss[1:]), ss[1:]):
            if a & b:
                print('    para %-2d %-22s %s' % (pi, ','.join(sorted(a & b)), sb[:70]))
                n += 1
    print('    -> %d  (must be 0 - merge the two sentences)' % n); issues += n

    print('\n[3] Claim words with no citation on that sentence  (Rule 2)')
    n = 0
    for _, t in body_p:
        for s in sentences(t):
            m = re.search(TRIGGERS, s, re.I)
            if m and not has_citation(s):
                print('    %-14s %s' % ('"%s"' % m.group(1), s[:95]))
                n += 1
    print('    -> %d' % n); issues += n

    print('\n[4] Previously flagged informal wording  (Rule 3)')
    low = blob.lower()
    hits = [w for w in INFORMAL if w in low]
    print('    ' + (', '.join(hits) if hits else 'none')); issues += len(hits)

    print('\n[5] Evaluative adjectives - each needs an operational definition  (Rule 18)')
    n = 0
    for _, t in body_p:
        for s in sentences(t):
            for w in EVALUATIVE:
                if re.search(r'\b%s\b' % w, s, re.I):
                    print('    %-14s %s' % (w, s[:95]))
                    n += 1
                    break
    print('    -> %d to check by hand' % n)

    print('\n[6] Bold runs in the body  (Rule 11)')
    n = 0
    for i in range(i0 + 1, i1):
        for r in R_RE.findall(paras[i]):
            if '<w:b/>' in r.split('<w:t')[0] and T_RE.findall(r):
                print('    %s' % ''.join(T_RE.findall(r))[:80])
                n += 1
    print('    -> %d  (must be 0)' % n); issues += n

    print('\n[7] Parenthetical cross-references  (Rule 12)')
    x = re.findall(r'\((?:Section|Table|Figure)[^)]*\)', blob)
    print('    ' + (', '.join(x) if x else 'none')); issues += len(x)

    print('\n[8] Sentence-initial demonstratives - check each has a clear referent  (Rule 4)')
    for _, t in body_p:
        for s in sentences(t):
            if re.match(DEMONSTRATIVE, s):
                print('    %s' % s[:95])

    print('\n' + '=' * 72)
    print('Hard failures (passes 1,2,3,4,6,7): %d' % issues)
    print('Passes 5 and 8 always need a human read.')
    print('=' * 72)
    return 0


if __name__ == '__main__':
    sys.exit(main())
