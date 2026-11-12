"""Regroup History long parts into Sonnet packages of 3 similar questions (agent-cost rule).

    python3 pipeline/rebuild/hist_long_packages.py <from-year> [<to-year> [<prefix>]]

Reads the generic long packages (fill/lNN.json, built by fill_packages.py) and writes
fill/<prefix>NNN.json plus fill/hist-long-<prefix>.json {names, essays, dbq4} (prefix h by default,
so a later run over other years keeps the earlier packages). Higher essays are grouped by
chapter (3 per package, by year); Higher DBQ question 4 parts are kept apart and carry their
case-study context line. Each package starts with the notes header for its chapter(s):
"<loId> — [ref] title" lines, each section being notes/<loId>.md.
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from fill_packages import BASE, write  # noqa: E402

PER = 3


def main(lo, hi, prefix='h'):
    fill = BASE / 'history' / 'fill'
    index = (BASE / 'history' / 'notes' / 'INDEX.md').read_text().splitlines()

    def head(chapter):
        lines = [re.sub(r'\s+->\s+notes/.*$', '', l)[2:] for l in index if l.startswith(f'- {chapter}-s')]
        return {'context': f'notes for {chapter}', 'text': '\n'.join(lines)}

    rows = [r for f in sorted(fill.glob('l[0-9][0-9].json')) for r in json.loads(f.read_text())]
    ctx = {r['context']: r for r in rows if 'context' in r and not r['context'].startswith('notes')}
    essays, dbq = {}, []
    for r in rows:
        if 'id' not in r or not lo <= int(r['id'][:4]) <= hi:
            continue
        chapter = re.sub(r'-s\d+$', '', r['notes'][0]) if r.get('notes') else ''
        item = {k: v for k, v in r.items() if k != 'notes'}
        if r['id'].split('|')[0].endswith('-q1'):
            dbq.append((chapter, r['id'], item))
        else:
            essays.setdefault(chapter, []).append(item)
    for f in fill.glob(f'{prefix}[0-9][0-9][0-9].json'):
        f.unlink()
    names = []

    def emit(items):
        names.append(f'{prefix}{len(names):03d}')
        write(fill / f'{names[-1]}.json', items)

    for chapter in sorted(essays):
        its = sorted(essays[chapter], key=lambda x: x['id'])
        for i in range(0, len(its), PER):
            emit([head(chapter)] + its[i:i + PER])
    n_essay = len(names)
    dbq.sort()
    for i in range(0, len(dbq), PER):
        group = dbq[i:i + PER]
        heads = [head(c) for c in sorted({c for c, _, _ in group})]
        body = []
        for _, pid, item in group:
            key = pid.split('|')[0]
            if key in ctx:
                body.append(ctx[key])
            body.append(item)
        emit(heads + body)
    (fill / ('hist-long.json' if prefix == 'h' else f'hist-long-{prefix}.json')).write_text(json.dumps({'names': names, 'essays': names[:n_essay], 'dbq4': names[n_essay:]}, indent=1))
    sizes = sorted((fill / f'{n}.json').stat().st_size for n in names)
    print(f'{len(names)} packages ({n_essay} essay, {len(names) - n_essay} DBQ Q4); '
          f'{sum(len(v) for v in essays.values())} essays in {len(essays)} chapters, {len(dbq)} DBQ Q4; '
          f'size {sizes[0]}-{sizes[-1]} bytes')


if __name__ == '__main__':
    lo = int(sys.argv[1])
    main(lo, int(sys.argv[2]) if len(sys.argv) > 2 else 9999, sys.argv[3] if len(sys.argv) > 3 else 'h')
