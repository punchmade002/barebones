"""Flag shipped answers that still read like a marking scheme, and batch them for the Haiku tidy.

    python3 pipeline/rebuild/tidy_scan.py <subject> [--batch]

Scans <subject>-exam-questions.js (old and new answers alike). Without --batch prints counts per
pattern; with --batch writes <DATA>/<subject>/fill/tidy/tNN.json (id, answer, flags), 45 per batch.
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from fill_packages import BASE, write  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
PER = 45
PATTERNS = {
    'mark tally': r'\(\s*\d{1,2}\s*(?:marks?)?\s*\)(?!\s*[\w(×])',
    'double slash': r'//',
    'accept/allow': r'\b(accept(?:ed|able)?|allow(?:ed)?)\b',
    'also works': r'also (acceptable|accepted|correct)|would also (work|be accepted)',
    'scheme range': r'\b\d+(\.\d+)?\s*(to|–)\s*\d+(\.\d+)?\s*(cm³|cm3|g|min|°C|mol|s\b|%|marks?)',
    'bracket allow': r'\[\s*(allow|accept)',
    'marker words': r'\b(candidate|award(?:ed)?|scheme|marks? for)\b',
    'markdown': r'\*\*|^\s*[-•*]\s',
}


def bank(subject):
    s = (ROOT / f'{subject}-exam-questions.js').read_text()
    return json.loads(s[s.index('.concat(') + 8:s.rindex(')')])


def flagged(subject):
    out = []
    for q in bank(subject):
        key = q['id'].replace(f'{subject}-pp-', '')
        for p in q['parts']:
            flags = [k for k, pt in PATTERNS.items() if p['model'] and re.search(pt, p['model'], re.I | re.M)]
            if flags:
                out.append({'id': f'{key}|{p["label"]}', 'answer': p['model'], 'flags': flags})
    return out


def main(subject, batch):
    items = flagged(subject)
    print(len(items), 'answers flagged;', dict(Counter(f for it in items for f in it['flags'])))
    if batch:
        out = BASE / subject / 'fill' / 'tidy'
        out.mkdir(parents=True, exist_ok=True)
        for old in out.glob('t*.json'):
            old.unlink()
        names = []
        for i in range(0, len(items), PER):
            names.append(f't{len(names):02d}')
            write(out / f'{names[-1]}.json', items[i:i + PER])
        print(names)


if __name__ == '__main__':
    main(sys.argv[1], '--batch' in sys.argv)
