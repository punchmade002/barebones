"""Turn the Geography scan+scheme workflow journal(s) into a scan/scheme journal for state.py.

    python3 pipeline/rebuild/geo_scan_journal.py <out.jsonl> <workflow journal.jsonl> [...]

The Geography pass ran one Haiku agent per paper section (label "scan:<group>"), each returning
{questions: [{key, parts: [...scan and scheme fields...]}]}. This splits every question into the
"scan:<key>" and "scheme:<key>" entries state.py reads, remapping keys Haiku mangled (the key must
be one of its group's crop keys) and reporting keys missing from or added to a group.
"""
import json
import re
import sys
from pathlib import Path

DATA = Path(__file__).resolve().parents[2] / 'pipeline/_data/rebuild/geography'
SCAN_KEYS = ('label', 'text', 'type', 'diagramRelation', 'resource', 'chapterId', 'loIds')
SCHEME_KEYS = ('label', 'marks', 'schemePoints', 'fullMarksRule')


def groups_of(path):
    labels, out = {}, {}
    for line in Path(path).read_text().splitlines():
        e = json.loads(line)
        if e.get('type') == 'started':
            labels[e['key']] = e.get('label', '')
        elif e.get('type') == 'result' and e.get('result') and labels.get(e['key'], '').startswith('scan:'):
            out[labels[e['key']][5:]] = e['result']
    return out


def main(out_path, journals):
    crops = json.loads((DATA / 'crops.json').read_text())
    groups = {g['name']: g for g in json.loads(Path(sys.argv[0]).with_name('geo_groups.json').read_text())}
    fixes_path = DATA / 'scan' / 'manual-fixes.json'   # {key: {label: {field: value}}} from reading the scheme
    fixes = json.loads(fixes_path.read_text()) if fixes_path.exists() else {}
    lines, problems, n = [], [], 0
    for path in journals:
        for name, res in groups_of(path).items():
            want = groups[name]['keys']
            got = {}
            for q in res['questions']:
                key = q['key']
                if key not in want:   # e.g. "q101" or "2023-higher-101": match on the trailing number
                    m = re.search(r'(\d+)\D*$', key)
                    cand = [k for k in want if m and k.endswith(f'q{m.group(1)}')]
                    if len(cand) != 1:
                        problems.append(f'{name}: unmapped key {key!r}')
                        continue
                    key = cand[0]
                got[key] = q
            for k in want:
                if k not in got:
                    problems.append(f'{name}: missing {k}')
            for key, q in got.items():
                parts = q['parts']
                for p in parts:
                    p.update(fixes.get(key, {}).get(p['label'], {}))
                scan = {'attemptRule': q.get('attemptRule', ''), 'context': '', 'cropIssues': q.get('cropIssues', ''),
                        'parts': [{**{k: p.get(k) for k in SCAN_KEYS}, 'offSpec': False, 'offSpecReason': ''} for p in parts]}
                scheme = {'questionMarks': q.get('questionMarks'), 'note': q.get('schemeNote', ''),
                          'parts': [{k: p.get(k) for k in SCHEME_KEYS} for p in parts]}
                for stage, res_ in (('scan', scan), ('scheme', scheme)):
                    lines.append({'type': 'started', 'key': f'{stage}:{key}', 'label': f'{stage}:{key}'})
                    lines.append({'type': 'result', 'key': f'{stage}:{key}', 'result': res_})
                n += 1
    Path(out_path).write_text('\n'.join(json.dumps(x, ensure_ascii=False) for x in lines) + '\n')
    print(f'{n} questions -> {out_path}')
    for p in problems:
        print('PROBLEM', p)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2:])
