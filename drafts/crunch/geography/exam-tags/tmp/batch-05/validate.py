import json, os, re

BATCH = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-05.txt'
OUT = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out'

text = open(BATCH, encoding='utf-8').read()
blocks = [b for b in text.split('\n====') if b.strip()]
questions = {}
for block in blocks:
    m = re.search(r'^QUESTION (\S+)', block, re.M)
    if not m:
        continue
    qid = m.group(1)
    parts = re.findall(r'^PART "([^"]*)"', block, re.M)
    cands = set(re.findall(r'^\[([^\]]+)\]', block, re.M))
    questions[qid] = (parts, cands)

errors = []
for qid, (parts, cands) in questions.items():
    path = os.path.join(OUT, qid + '.json')
    try:
        data = json.load(open(path, encoding='utf-8'))
    except Exception as e:
        errors.append(f'{qid}: parse failed {e}')
        continue
    if list(data.keys()) != parts:
        errors.append(f'{qid}: keys {list(data.keys())} != parts {parts}')
    total = 0
    empty = []
    for label, pts in data.items():
        if not pts:
            empty.append(label)
        for p in pts:
            total += 1
            if not (1 <= p['k'] <= len(p['of'])):
                errors.append(f'{qid} {label}: bad k {p}')
            for i in p['of']:
                if i not in cands:
                    errors.append(f'{qid} {label}: id not in candidates {i}')
    print(f'{qid}: parts={len(parts)} marking_points={total} empty={empty}')

print('ERRORS:' if errors else 'ALL OK')
for e in errors:
    print(e)
