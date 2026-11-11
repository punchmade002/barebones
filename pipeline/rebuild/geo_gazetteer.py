"""Index every printed name on each year's OS map with its six-figure grid reference.

    python3 pipeline/rebuild/geo_gazetteer.py

The map PDFs carry a text layer: the easting labels along the top margin, the northing labels
down the left margin, and every place name, feature name and spot height. Fitting the margin
labels gives each name's grid reference, which agents use instead of estimating references
from the image (in the Nov 2026 pilot, two Sonnet checks disagreed by 200 m on the same tomb).
A reference is that of the label's centre: the feature itself sits just beside its label.
Writes <DATA>/geography/resources/<year>-os-map-gazetteer.txt.
"""
import collections
import re
import statistics
from pathlib import Path

import fitz

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'pipeline/_data/rebuild/geography/resources'


def lines(page):
    out = []
    for b in page.get_text('dict')['blocks']:
        for l in b.get('lines', []):
            t = ''.join(s['text'] for s in l['spans']).strip()
            if t:
                out.append((fitz.Rect(l['bbox']), t, max(s['size'] for s in l['spans'])))
    return out


def fit(points):
    """Least-squares km = a + b * pt from (pt, km) pairs, unwrapping the 00/99 rollover."""
    points = sorted(points)
    kms = [points[0][1]]
    for (_, k) in points[1:]:
        prev = kms[-1]
        cand = min((k + 100 * n for n in (-1, 0, 1)), key=lambda v: abs(v - prev))
        kms.append(cand)
    xs = [p for p, _ in points]
    mx, mk = statistics.mean(xs), statistics.mean(kms)
    b = sum((x - mx) * (k - mk) for x, k in zip(xs, kms)) / sum((x - mx) ** 2 for x in xs)
    return lambda x: mk + b * (x - mx), b


def axis(cands, coord):
    """Keep the run of labels with a steady spacing (the grid), drop contour heights."""
    best = []
    for c in cands:
        run = [c]
        for d in sorted(cands, key=coord):
            if coord(d) > coord(run[-1]) + 30 and abs((coord(d) - coord(run[-1])) - 56.7 * round((coord(d) - coord(run[-1])) / 56.7)) < 3:
                run.append(d)
        if len(run) > len(best):
            best = run
    return best


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for year in range(2017, 2027):
        pdf = ROOT / 'exam-papers/geography' / f'{year}-common-ordnance-survey-map.pdf'
        if not pdf.exists():
            continue
        page = fitz.open(pdf)[0]
        L = lines(page)
        W, H = page.rect.width, page.rect.height
        two = [(r, int(t)) for r, t, s in L if re.fullmatch(r'\d{2}', t) and s >= 7]
        top = axis([x for x in two if x[0].y1 < 0.08 * H], lambda x: (x[0].x0 + x[0].x1) / 2)
        left = axis([x for x in two if x[0].x1 < 0.08 * W], lambda x: (x[0].y0 + x[0].y1) / 2)
        if len(top) < 4 or len(left) < 4:
            print(year, 'grid labels not found', len(top), len(left))
            continue
        ex, bx = fit([((r.x0 + r.x1) / 2, k) for r, k in top])
        ny, by = fit([((r.y0 + r.y1) / 2, k) for r, k in left])
        # the 100 km square letter: the one the year's questions use in their references
        refs = collections.Counter(m for f in (ROOT / 'pipeline/_data/rebuild/geography/text').glob(f'{year}-*.txt')
                                   for m in re.findall(r'\b([A-Z]) ?\d{3} ?\d{3}\b', f.read_text()))
        letter = refs.most_common(1)[0][0] + ' ' if refs else ''
        rows = []
        for r, t, s in L:
            cx, cy = (r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2
            if r.y1 < 0.06 * H or r.x1 < 0.05 * W or cx > W - 40 or cy > H - 25:
                continue                      # margin labels
            if re.fullmatch(r'\d{1,3}', t) or len(t) < 2:
                continue                      # contour values, single letters
            e, n = ex(cx) % 100, ny(cy) % 100
            rows.append((t, f'{letter}{int(e * 10) % 1000:03d} {int(n * 10) % 1000:03d}'))
        rows.sort(key=lambda x: x[0].lower())
        head = (f'# {year} OS map: printed names with the grid reference of each label\'s centre '
                f'(the feature sits just beside its label; one grid square = {1 / abs(bx):.1f} pt)\n')
        (OUT / f'{year}-os-map-gazetteer.txt').write_text(head + '\n'.join(f'{t} — {g}' for t, g in rows) + '\n')
        print(year, letter.strip() or '?', len(rows), 'names')


if __name__ == '__main__':
    main()
