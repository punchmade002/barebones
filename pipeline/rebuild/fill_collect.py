"""Collect a fill workflow's answers into <DATA>/<subject>/fill/<out>.json, keyed by package id.

    python3 pipeline/rebuild/fill_collect.py <subject> <workflow-output> <short|long> [packages p00 p01 ...]

Haiku sometimes mangles ids (drops the year prefix, respaces the label), so every returned id is
mapped back to a package id: exact match first, then the same question number/level and the same
label with whitespace removed. Prints what was remapped, what is missing and what could not be
placed. For the long run the flagged list goes to fill/long-flagged.json.
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from fill_packages import BASE, lab  # noqa: E402


def package_ids(subject, prefix):
    ids = []
    for f in sorted((BASE / subject / 'fill').glob(f'{prefix}[0-9][0-9].json')):
        ids += [it['id'] for it in json.loads(f.read_text()) if 'id' in it]
    return ids


def norm(i):
    key, _, label = i.partition('|')
    m = re.search(r'(\d{4})?-?(higher|ordinary)-q(\d+)', key)
    return (m.group(1) if m else None, m.group(2) if m else None, m.group(3) if m else key, lab(label))


def remap(returned, ids):
    exact = set(ids)
    by_norm = {}
    for i in ids:
        y, lv, q, L = norm(i)
        by_norm.setdefault((lv, q, L), []).append((y, i))
    out, moved, lost = {}, [], []
    for rid, val in returned.items():
        if rid in exact:
            out[rid] = val
            continue
        y, lv, q, L = norm(rid)
        cands = [i for yy, i in by_norm.get((lv, q, L), []) if y is None or yy == y]
        if len(cands) == 1 and cands[0] not in returned:
            out[cands[0]] = val
            moved.append((rid, cands[0]))
        else:
            lost.append(rid)
    return out, moved, lost


def main(subject, path, kind):
    raw = json.loads(Path(path).read_text())
    res = raw.get('result') or raw
    ids = package_ids(subject, 'p' if kind == 'short' else 'l')
    answers, moved, lost = remap(res['answers'], ids)
    missing = [i for i in ids if i not in answers]
    out = BASE / subject / 'fill'
    (out / f'{kind}.json').write_text(json.dumps(answers, ensure_ascii=False, indent=1))
    if kind == 'long':
        (out / 'long-flagged.json').write_text(json.dumps({'flagged': res.get('flagged', [])}, ensure_ascii=False, indent=1))
    by = {}
    for a in answers.values():
        by[a['by']] = by.get(a['by'], 0) + 1
    print(f'{len(answers)}/{len(ids)} answered {by}; remapped {len(moved)}; unplaced {len(lost)}; missing {len(missing)}')
    for a, b in moved:
        print('  remap', a, '->', b)
    for i in lost:
        print('  unplaced', i)
    for i in missing:
        print('  missing', i)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
