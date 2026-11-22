"""Material for a skill's Learn phase (the whiteboard before its practice problems).

  python3 pipeline/requirements/maths/learn.py scheme <skill id>   # learn/scheme/<skill>.json: marking-scheme text per exam part

The scheme text comes from the official marking-scheme PDFs, split by question with the page map in
.claude/worktrees/maths-older/pipeline/rebuild/maths_crops.py (scheme_pages). Exam tips are written from it.
"""
import json
import re
import sys
from functools import lru_cache
from pathlib import Path

import fitz

HERE = Path(__file__).parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / '.claude/worktrees/maths-older/pipeline/rebuild'))
import maths_crops as mc  # noqa: E402

SKIP_YEAR = '-2026-'     # 2026 papers are not on this branch's bank


@lru_cache(None)
def pages(year, level):
    return mc.scheme_pages(year, level)[0]


def scheme_text(year, level, paper, q):
    doc = fitz.open(mc.PAPERS / f'{year}-{level}-marking-scheme.pdf')
    return '\n'.join(doc[p - 1].get_text() for p in pages(year, level).get((paper, q), []))


def tidy(t):
    """PDF text keeps one token per line and odd glyphs for superscripts; squash it for reading."""
    t = re.sub(r'[ \t]+', ' ', t.replace('ଶ', '²').replace('ଷ', '³'))
    return re.sub(r'\n\s*\n+', '\n', t).strip()


def scheme(sid):
    tags = json.loads((HERE / 'skill-tags.json').read_text())
    out = []
    for pid, t in sorted(tags.items()):
        if sid not in t['skills'] or SKIP_YEAR in pid:
            continue
        m = re.search(r'(\d{4})-(higher|ordinary)-p(\d)-q(\d+)#(.*)', pid)
        year, level, paper, q, label = int(m[1]), m[2], int(m[3]), int(m[4]), m[5]
        out.append(dict(part=pid, level=level, year=year, paper=paper, question=q, label=label,
                        mainSkill=t['primary'] == sid, scheme=tidy(scheme_text(year, level, paper, q))))
    d = HERE / 'learn' / 'scheme'
    d.mkdir(parents=True, exist_ok=True)
    (d / f'{sid}.json').write_text(json.dumps(out, ensure_ascii=False, indent=1))
    empty = [o['part'] for o in out if not o['scheme']]
    print(f'{sid}: {len(out)} parts, {len(empty)} with no scheme text {empty[:3]}')


if __name__ == '__main__':
    {'scheme': lambda: scheme(sys.argv[2])}[sys.argv[1]]()
