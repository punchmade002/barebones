"""Flag chemistry answers that still read like a marking scheme, and batch them for the Haiku tidy.

    python3 pipeline/rebuild/chem_tidy_scan.py [--batch]

Scans the shipped bank. Without --batch, prints counts per pattern. With --batch, writes
<DATA>/fill/tidy/tNN.json (one item per line: id, answer, flags), about 45 answers per batch.
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = Path.home() / 'barebones/pipeline/_data/rebuild/chemistry/fill/tidy'
PATTERNS = {
    'mark tally': r'\(\s*\d{1,2}\s*(?:marks?)?\s*\)(?!\s*[\w(×])',
    'double slash': r'//',
    'accept/allow': r'\b(accept(?:ed|able)?|allow(?:ed)?)\b',
    'also works': r'also (acceptable|accepted|correct)|would also (work|be accepted)',
    'scheme range': r'\b\d+(\.\d+)?\s*(to|–)\s*\d+(\.\d+)?\s*(cm³|cm3|g|min|°C|mol|s\b|%)',
    'marker words': r'\b(candidate|award(?:ed)?|marks? for)\b',
}


def bank():
    s = (ROOT / 'chemistry-exam-questions.js').read_text()
    return json.loads(s[s.index('.concat(') + 8:s.rindex(')')])


def flagged():
    out = []
    for q in bank():
        key = q['id'].replace('chemistry-pp-', '')
        for p in q['parts']:
            flags = [k for k, pt in PATTERNS.items() if p['model'] and re.search(pt, p['model'], re.I)]
            if flags:
                out.append({'id': f'{key}|{p["label"]}', 'answer': p['model'], 'flags': flags})
    return out


def main(batch):
    items = flagged()
    print(len(items), 'answers flagged;', dict(Counter(f for it in items for f in it['flags'])))
    if batch:
        OUT.mkdir(parents=True, exist_ok=True)
        for old in OUT.glob('t*.json'):
            old.unlink()
        n = (len(items) + 44) // 45
        for i in range(n):
            chunk = items[i * 45:(i + 1) * 45]
            (OUT / f't{i:02d}.json').write_text('[\n' + ',\n'.join(json.dumps(it, ensure_ascii=False) for it in chunk) + '\n]\n')
        print(n, 'batches; longest line', max(len(json.dumps(it, ensure_ascii=False)) for it in items))


if __name__ == '__main__':
    main('--batch' in sys.argv)
