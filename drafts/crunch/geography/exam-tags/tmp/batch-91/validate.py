import json, sys, re
from pathlib import Path
batch = Path('/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-91.txt').read_text().splitlines()
out = Path('/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out')
qid = None; parts = []; cands = {}; cur = None
for line in batch:
    m = re.match(r'QUESTION (\S+)', line)
    if m:
        qid = m.group(1); cands[qid] = set(); parts.append((qid, [])); continue
    m = re.match(r'PART "([^"]+)"', line)
    if m:
        parts[-1][1].append(m.group(1)); continue
    m = re.match(r'\[([^\]]+)\]', line)
    if m:
        cands[qid].add(m.group(1))
ok = True
for qid, labels in parts:
    f = out / f'{qid}.json'
    d = json.loads(f.read_text())
    if list(d.keys()) != labels:
        print('LABEL MISMATCH', qid, list(d.keys()), labels); ok = False
    for lab, mps in d.items():
        for mp in mps:
            if not (1 <= mp['k'] <= len(mp['of'])): print('K BAD', qid, lab, mp); ok = False
            if len(mp['of']) > 2: print('>2 ids', qid, lab, mp)
            for i in mp['of']:
                if i not in cands[qid]: print('BAD ID', qid, lab, i); ok = False
    print(qid, 'parts', len(d), 'points', sum(len(v) for v in d.values()), 'empty', [k for k, v in d.items() if not v])
print('OK' if ok else 'FAIL')
