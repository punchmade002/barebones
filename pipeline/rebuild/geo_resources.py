"""Render each year's Ordnance Survey map and aerial photograph for the agents that need them.

    python3 pipeline/rebuild/geo_resources.py

Writes <DATA>/geography/resources/<year>-<os-map|aerial-photo>-full.png (whole sheet, for layout)
and -tile-<r><c>.png (2x2 tiles with 8% overlap, for reading grid references and small labels).
The map and photo are common to both levels and are not in the paper PDFs.
"""
from pathlib import Path

import fitz

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'pipeline/_data/rebuild/geography/resources'
SOURCES = {'os-map': 'ordnance-survey-map', 'aerial-photo': 'photograph'}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for year in range(2017, 2027):
        for kind, name in SOURCES.items():
            pdf = ROOT / 'exam-papers/geography' / f'{year}-common-{name}.pdf'
            if not pdf.exists():
                print('missing', pdf.name)
                continue
            page = fitz.open(pdf)[0]
            r = page.rect
            scale = 1500 / max(r.width, r.height)
            page.get_pixmap(matrix=fitz.Matrix(scale, scale)).save(OUT / f'{year}-{kind}-full.png')
            ox, oy = r.width * 0.08, r.height * 0.08
            for i in range(2):
                for j in range(2):
                    clip = fitz.Rect(r.x0 + j * r.width / 2 - (ox if j else 0), r.y0 + i * r.height / 2 - (oy if i else 0),
                                     r.x0 + (j + 1) * r.width / 2 + (0 if j else ox), r.y0 + (i + 1) * r.height / 2 + (0 if i else oy))
                    s = 1500 / max(clip.width, clip.height)
                    page.get_pixmap(matrix=fitz.Matrix(s, s), clip=clip).save(OUT / f'{year}-{kind}-tile-{i}{j}.png')
    print(len(list(OUT.glob('*.png'))), 'images in', OUT)


if __name__ == '__main__':
    main()
