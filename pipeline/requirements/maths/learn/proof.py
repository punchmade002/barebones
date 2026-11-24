"""Proof-read the Learn phase's worked examples that have no figure (a figure's checker already read the rest).

  python3 proof.py pack     # those skills → proof/in/Pnn.json, 12 per batch
  python3 proof.py apply    # proof/out/Pnn.json fixes → learn/out/Bnn.json, then run learn.py check and assemble

Readers (PROOF.md) write {skill: {"ok": bool, "fixes": [{"find", "replace", "why"}]}}. A fix is an exact
substring of one text field of that skill's source; apply() makes it only if it matches exactly once.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
WORK = HERE / 'proof'
PER = 12


def sources():
    """skill → (file, index) of its latest source, as learn.py outputs() reads them (later files win)"""
    out = {}
    for f in sorted((HERE / 'out').glob('B*.json')):
        for k, o in enumerate(json.loads(f.read_text())):
            out[o['skill']] = (f, k)
    return out


def pack():
    sys.path.insert(0, str(HERE))
    from visuals import learn_data, shown
    L = learn_data()
    figured = set(shown(L))
    src = sources()
    todo = [sid for sid in L if sid not in figured]
    (WORK / 'in').mkdir(parents=True, exist_ok=True)
    for k in range(0, len(todo), PER):
        items = []
        for sid in todo[k:k + PER]:
            f, i = src[sid]
            o = json.loads(f.read_text())[i]
            items.append({'skill': sid, 'title': L[sid]['title'], 'what': o['what'], 'example': o['example']})
        (WORK / 'in' / f'P{k // PER + 1:02d}.json').write_text(json.dumps(items, ensure_ascii=False, indent=1))
    print(f'{len(todo)} skills → {(len(todo) + PER - 1) // PER} batches')


def strings(o, path=()):
    """every (path, string) in a nested object"""
    if isinstance(o, str):
        yield path, o
    elif isinstance(o, dict):
        for k, v in o.items():
            yield from strings(v, path + (k,))
    elif isinstance(o, list):
        for k, v in enumerate(o):
            yield from strings(v, path + (k,))


def put(o, path, value):
    for k in path[:-1]:
        o = o[k]
    o[path[-1]] = value


def apply():
    src, done, skipped = sources(), 0, []
    files = {}
    for f in sorted((WORK / 'out').glob('P*.json')):
        for sid, v in json.loads(f.read_text()).items():
            for fix in v.get('fixes') or []:
                file, i = src[sid]
                data = files.setdefault(file, json.loads(file.read_text()))
                o = {k: data[i][k] for k in ('what', 'example')}
                hits = [(p, s) for p, s in strings(o) if fix['find'] in s]
                if len(hits) != 1 or hits[0][1].count(fix['find']) != 1:
                    skipped.append((sid, fix['find'][:60], f'{len(hits)} fields match'))
                    continue
                p, s = hits[0]
                put(data[i], p, s.replace(fix['find'], fix['replace']))
                done += 1
    for file, data in files.items():
        file.write_text(json.dumps(data, ensure_ascii=False, indent=1))
    print(f'{done} fixes applied, {len(skipped)} skipped')
    for s in skipped:
        print('  skipped', *s)


if __name__ == '__main__':
    assert list(strings({'a': ['x', {'b': 'y'}]})) == [(('a', 0), 'x'), (('a', 1, 'b'), 'y')]
    {'pack': pack, 'apply': apply}[sys.argv[1]]()
