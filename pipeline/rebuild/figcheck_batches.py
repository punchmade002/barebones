"""Batch every Haiku answer whose part uses a figure for the Sonnet figure check (20 questions each).

    python3 pipeline/rebuild/figcheck_batches.py <subject>

Reads fill/short.json and the short packages; writes fill/figcheck/fNN.json, one item per line:
the package item plus answer. Prints the batch names for figcheck_workflow.js.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from fill_packages import BASE, write  # noqa: E402

PER = 20


def main(subject):
    fill = BASE / subject / 'fill'
    answers = json.loads((fill / 'short.json').read_text())
    items = {}
    for f in sorted(fill.glob('p[0-9][0-9].json')):
        for it in json.loads(f.read_text()):
            if 'id' in it and it.get('figure') and answers.get(it['id'], {}).get('by') == 'haiku':
                slim = {k: v for k, v in it.items() if not k.startswith('hint')}  # hints are not needed to check
                items.setdefault(it['id'].split('|')[0], []).append({**slim, 'answer': answers[it['id']]['model']})
    keys = sorted(items)
    out = fill / 'figcheck'
    out.mkdir(exist_ok=True)
    names = []
    for i in range(0, len(keys), PER):
        name = f'f{len(names):02d}'
        write(out / f'{name}.json', [x for k in keys[i:i + PER] for x in items[k]])
        names.append(name)
    print(f'{sum(len(v) for v in items.values())} figure parts in {len(keys)} questions -> {names}')


if __name__ == '__main__':
    main(sys.argv[1])
