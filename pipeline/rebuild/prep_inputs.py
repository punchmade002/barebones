"""Build the agent inputs for a subject's rebuild (as done by hand for Biology):

    python3 pipeline/rebuild/prep_inputs.py chemistry

  <DATA>/<subject>/crops-png/<key>-<k>.png       PNG copies of the question crops (agents read PNG)
  <DATA>/<subject>/scheme/<year>-<level>/scheme.txt  scheme text, pages split by "===== PAGE n ====="
  <DATA>/<subject>/scheme/<year>-<level>/pNN.png     scheme page images (for scanned or scrambled text)
  <DATA>/<subject>/notes/<loId>.md + INDEX.md       the app's notes, one file per subsection
Also fills a missing crop section (old papers print no "Section A/B" header): Q1-3 are A, the rest B.
"""
import json
import sys
from pathlib import Path

import fitz
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / 'pipeline/_data/rebuild'
RAW = ROOT / 'pipeline/_data/raw'


def main(subject):
    base = DATA / subject
    crops = json.loads((base / 'crops.json').read_text())
    (base / 'crops-png').mkdir(exist_ok=True)
    for key, c in crops.items():
        if c.get('section') is None:
            c['section'] = 'A' if c['number'] <= 3 else 'B'
        for k, img in enumerate(c['images'], 1):
            out = base / 'crops-png' / f'{key}-{k}.png'
            if not out.exists():
                Image.open(ROOT / img).save(out)
    (base / 'crops.json').write_text(json.dumps(crops, indent=1))

    papers = sorted({f"{c['year']}-{c['level']}" for c in crops.values()})
    for paper in papers:
        pdf = RAW / subject / f'{paper}-EV-scheme.pdf'
        if not pdf.exists():
            pdf = RAW / subject / f'{paper}-EV-scheme-REF.pdf'
        out = base / 'scheme' / paper
        out.mkdir(parents=True, exist_ok=True)
        if not pdf.exists():
            (out / 'scheme.txt').write_text('NO MARKING SCHEME PUBLISHED FOR THIS PAPER\n')
            continue
        doc = fitz.open(pdf)
        text = []
        for i, page in enumerate(doc, 1):
            text.append(f'===== PAGE {i} =====\n{page.get_text()}')
            png = out / f'p{i:02d}.png'
            if not png.exists():
                page.get_pixmap(dpi=110).save(png)
        (out / 'scheme.txt').write_text('\n'.join(text))

    notes = base / 'notes'
    notes.mkdir(exist_ok=True)
    titles = {}
    for f in sorted((ROOT / 'content' / subject).glob('*.json'), key=lambda p: [int(x) if x.isdigit() else x for x in p.stem.replace('-s', '-').replace(subject[:4], '').split('-')]):
        d = json.loads(f.read_text())
        lo, ch = d['loId'], d['chapterId']
        lines = [f"# {lo} — {d.get('subsection', '')} [{d.get('syllabusRef', '')}] (chapter {ch})", '']
        for sec in d.get('notes', []):
            lines += [f"## {sec.get('h', '')}"]
            if sec.get('b'):
                lines.append(sec['b'])
            lines += [f'- {p}' for p in sec.get('points', [])]
            lines.append('')
        if d.get('keyTerms'):
            lines += ['## Key terms'] + [f"- {t['term']}: {t['definition']}" for t in d['keyTerms']] + ['']
        (notes / f'{lo}.md').write_text('\n'.join(lines))
        titles.setdefault(ch, []).append(f"- {lo} — [{d.get('syllabusRef', '')}] {d.get('subsection', '')}  -> notes/{lo}.md")
    index = [f'# {subject.title()} notes index (chapterId / section loId — syllabusRef — title)', '']
    for ch in sorted(titles, key=lambda c: int(''.join(x for x in c if x.isdigit()))):
        index += [f'## {ch}'] + titles[ch] + ['']
    (notes / 'INDEX.md').write_text('\n'.join(index))
    print(f'{len(crops)} crops, {len(papers)} scheme folders, {sum(len(v) for v in titles.values())} notes files')


if __name__ == '__main__':
    main(sys.argv[1])
