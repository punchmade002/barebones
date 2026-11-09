"""Package every chemistry part still lacking a checked answer for the Haiku fill run.

    python3 pipeline/rebuild/chem_fill_packages.py

Targets: off-spec parts (answered anyway, still tagged off-spec) and on-spec parts with no audited
old answer under the exact same label. Questions are sorted by paper and cut into packages of ten,
so each Haiku writer sees one or two papers. Each item carries the scanned part text, marks and
scheme points inline (no file reads), plus a hint: an audited old answer whose label contains or
is contained by this part's label. Writes <DATA>/chemistry/fill/packages.json.
"""
import json
import random
import re
from pathlib import Path

DATA = Path.home() / 'barebones/pipeline/_data/rebuild/chemistry'
SIZE = 10
HINT_CHARS = 500


def lab(s):
    return re.sub(r'\s+', '', s or '')


def old_answers(key):
    """{label: answer} from old-answers/<key>.txt (entries may run over several lines)."""
    path = DATA / 'old-answers' / f'{key}.txt'
    out, cur = {}, None
    if not path.exists():
        return out
    for line in path.read_text().splitlines():
        m = re.match(r'(\(\S*\)) \[(?:kept|written)\]: (.*)', line)
        if m:
            cur = lab(m.group(1))
            out[cur] = (out[cur] + '\n' + m.group(2)) if cur in out else m.group(2)
        elif cur:
            out[cur] += '\n' + line
    return out


def order(key):
    y, level, q = key.split('-')
    return int(y), level, int(q[1:])


def main():
    questions = []
    for f in sorted((DATA / 'state').glob('*.json'), key=lambda p: order(p.stem.replace('.scan', ''))):
        if f.name.endswith('.scan.json'):
            continue
        st = json.loads(f.read_text())
        old = old_answers(st['key'])
        items = []
        for p in st['parts']:
            L = lab(p['label'])
            if not p.get('offSpec') and L in old:
                continue
            hint = next((old[o] for o in old if o.startswith(L) or L.startswith(o)), '')
            item = {'id': f'{st["key"]}|{p["label"]}', 'text': p['text'], 'marks': p['marks'],
                    'scheme': p.get('schemePoints') or [], 'rule': p.get('fullMarksRule', '')}
            if p['diagramRelation'] != 'none':
                item['figure'] = p['diagramRelation']
            if hint:
                item['hint'] = hint[:HINT_CHARS]
            items.append(item)
        if items:
            questions.append({'key': st['key'], 'items': items})
    packages = []
    for i in range(0, len(questions), SIZE):
        chunk = questions[i:i + SIZE]
        packages.append({'name': f'p{len(packages):02d}', 'papers': sorted({q['key'].rsplit('-', 1)[0] for q in chunk}),
                         'items': [it for q in chunk for it in q['items']]})
    sample = sorted(random.Random(20261109).sample(range(len(packages)), 5))
    out = {'packages': packages, 'sample': sample}
    (DATA / 'fill' / 'packages.json').write_text(json.dumps(out, ensure_ascii=False))
    for p in packages:                # one item per line, so a Read shows each item whole
        (DATA / 'fill' / f'{p["name"]}.json').write_text(
            '[\n' + ',\n'.join(json.dumps(it, ensure_ascii=False) for it in p['items']) + '\n]\n')
    n = sum(len(p['items']) for p in packages)
    print(f'{len(questions)} questions, {n} parts, {len(packages)} packages; sample {sample}; '
          f'{len(json.dumps(out, ensure_ascii=False)) // 1024} KB; max parts/package {max(len(p["items"]) for p in packages)}')


if __name__ == '__main__':
    main()
