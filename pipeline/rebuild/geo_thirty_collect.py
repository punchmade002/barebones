"""Collect the Geography 30-marker runs into <DATA>/geography/fill/thirty.json and thirty-flagged.json.

    python3 pipeline/rebuild/geo_thirty_collect.py <workflow output.json> [...]

Each run returns [{pkg, answers: [{id, model, check1, fixedModel?, check2?}]}]. An answer ships if
the independent check gave full marks with no content error or format issue (by sonnet-thirty),
or if its one fix passed the recheck (by sonnet-thirty-fix). Anything else is flagged, with the
last examiner findings, for the user's review and is not shipped. Ids are diffed against the
package files and remapped through fill_collect's matcher. A later run's result for a package
replaces an earlier one's.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from fill_collect import package_ids, remap  # noqa: E402
from fill_packages import BASE  # noqa: E402


def passed(v):
    return bool(v) and v.get('fullMarks') and not v.get('contentErrors') and not v.get('formatIssues')


def main(outputs):
    data = BASE / 'geography' / 'fill'
    ids = package_ids('geography', 't')
    per_pkg = {}
    for path in outputs:
        res = json.loads(Path(path).read_text())
        res = res.get('result', res) if isinstance(res, dict) else res
        for r in res:
            if r:
                per_pkg[r['pkg']] = r
    returned = {a['id']: a for r in per_pkg.values() for a in r['answers']}
    placed, moved, lost = remap(returned, ids)
    ship, flagged, counts = {}, [], {'sonnet-thirty': 0, 'sonnet-thirty-fix': 0, 'flagged': 0}
    for pid, a in placed.items():
        if passed(a.get('check1')):
            ship[pid] = {'model': a['model'], 'by': 'sonnet-thirty'}
        elif a.get('fixedModel') and passed(a.get('check2')):
            ship[pid] = {'model': a['fixedModel'], 'by': 'sonnet-thirty-fix'}
        else:
            v = a.get('check2') or a.get('check1') or {}
            flagged.append({'id': pid, 'model': a.get('fixedModel') or a['model'], 'marks': v.get('marksAwarded'),
                            'issue': '; '.join(v.get('contentErrors', []) + v.get('formatIssues', [])) or 'no verdict'})
            continue
        counts[ship[pid]['by']] += 1
    counts['flagged'] = len(flagged)
    missing = [i for i in ids if i not in placed]
    (data / 'thirty.json').write_text(json.dumps(ship, indent=1, ensure_ascii=False))
    (data / 'thirty-flagged.json').write_text(json.dumps({'flagged': flagged, 'missing': missing}, indent=1, ensure_ascii=False))
    print(f'{len(ids)} package ids; {len(placed)} returned; {counts}; missing {len(missing)}; remapped {len(moved)}; unplaced {lost}')
    for m in moved:
        print('  remapped', m)
    for m in missing:
        print('  missing', m)


if __name__ == '__main__':
    main(sys.argv[1:])
