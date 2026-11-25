"""Inventory + readability metrics for authored notes in content/<subject>/*.json.

Usage: python3 scripts/notes_inventory.py   (writes drafts/notes-inventory.csv)
Re-run after rewriting notes to compare before/after.
"""
import csv, glob, json, os, re, statistics
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'drafts', 'notes-inventory.csv')

# Words that signal the note is explaining or giving context, not just stating.
EXPLAIN = re.compile(r"\b(because|so that|therefore|this means|which means|this is why|as a result|in other words|that is why|this allows|in order to|due to)\b", re.I)
EXAMPLE = re.compile(r"\b(for example|e\.g\.|such as|for instance|like a|imagine|think of)\b", re.I)
XREF = re.compile(r"\b(covered in|described in|see [A-Z]|as in [A-Z])", re.I)


def syllables(word):
    w = re.sub(r'[^a-z]', '', word.lower())
    if not w:
        return 0
    n = len(re.findall(r'[aeiouy]+', w))
    if w.endswith('e') and not w.endswith(('le', 'ee')) and n > 1:
        n -= 1
    return max(1, n)


def stats(texts):
    words = [w for t in texts for w in re.findall(r"[A-Za-z][A-Za-z'’-]*", t)]
    sents = sum(max(1, len(re.findall(r'[.!?](\s|$)', t))) for t in texts)
    if not words:
        return 0, 0, 0, 0
    syl = sum(syllables(w) for w in words)
    hard = sum(1 for w in words if syllables(w) >= 3)
    wps, spw = len(words) / sents, syl / len(words)
    fre = 206.835 - 1.015 * wps - 84.6 * spw  # Flesch reading ease: higher = easier
    fk = 0.39 * wps + 11.8 * spw - 15.59      # Flesch-Kincaid school grade
    return len(words), round(fre, 1), round(fk, 1), round(100 * hard / len(words), 1)


def pct(n, d):
    return round(100 * n / d, 1) if d else 0


rows = []
for f in sorted(glob.glob(os.path.join(ROOT, 'content', '*', '*.json'))):
    d = json.load(open(f))
    if 'notes' not in d:
        continue
    blocks = d.get('notes') or []
    points = [p for n in blocks for p in n.get('points', []) if isinstance(p, str)]
    intros = [n['b'] for n in blocks if n.get('b')]
    texts = points + intros
    words, fre, fk, hard = stats(texts)
    prose = [p for p in points if not p.startswith('Diagram:')]
    rows.append({
        'subject': os.path.basename(os.path.dirname(f)),
        'loId': d.get('loId'), 'subsection': d.get('subsection'),
        'blocks': len(blocks), 'points': len(points), 'introParas': len(intros),
        'words': words, 'wordsPerPoint': round(words / len(texts), 1) if texts else 0,
        'fleschEase': fre, 'fkGrade': fk, 'hardWordPct': hard,
        'explainPct': pct(sum(bool(EXPLAIN.search(p)) for p in prose), len(prose)),
        'examplePct': pct(sum(bool(EXAMPLE.search(p)) for p in prose), len(prose)),
        'diagramPlaceholders': len(points) - len(prose),
        'xrefs': sum(bool(XREF.search(p)) for p in points),
        'semicolonPct': pct(sum(';' in p for p in points), len(points)),
        'keyTerms': len(d.get('keyTerms') or []), 'questions': len(d.get('questions') or []),
    })

assert rows, 'no content found'
assert stats(['The cat sat.'])[0] == 3
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, 'w', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=rows[0].keys())
    w.writeheader(); w.writerows(rows)

by = defaultdict(list)
for r in rows:
    by[r['subject']].append(r)
cols = ['subs', 'points', 'words', 'w/pt', 'ease', 'grade', 'hard%', 'explain%', 'example%', 'diagrams', 'xrefs', 'intro%']
print(f"{'subject':<16}" + ''.join(f'{c:>10}' for c in cols))
for s, rs in sorted(by.items()):
    med = lambda k: statistics.median(r[k] for r in rs)
    blocks = sum(r['blocks'] for r in rs)
    vals = [len(rs), sum(r['points'] for r in rs), sum(r['words'] for r in rs), med('wordsPerPoint'),
            med('fleschEase'), med('fkGrade'), med('hardWordPct'), med('explainPct'), med('examplePct'),
            sum(r['diagramPlaceholders'] for r in rs), sum(r['xrefs'] for r in rs),
            pct(sum(r['introParas'] for r in rs), blocks)]
    print(f'{s:<16}' + ''.join(f'{round(v, 1):>10}' for v in vals))
print(f'\n{len(rows)} subsections -> {os.path.relpath(OUT, ROOT)}  (per-subject values are medians, counts are totals)')
