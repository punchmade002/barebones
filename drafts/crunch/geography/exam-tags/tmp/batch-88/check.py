import json, re, sys
batch = open('/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-88.txt', encoding='utf-8').read()
questions = re.split(r'^=+\s*$', batch, flags=re.M)
out = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'
ok = True
for q in batch.split('QUESTION ')[1:]:
    qid = q.split()[0]
    parts = re.findall(r'^PART "([^"]+)"', q, flags=re.M)
    cands = set(re.findall(r'^\[([^\]]+)\]', q, flags=re.M))
    data = json.load(open(out + qid + '.json', encoding='utf-8'))
    keys = list(data.keys())
    if keys != parts:
        ok = False; print('PART MISMATCH', qid, keys, parts)
    total = 0; empty = []
    for p, mps in data.items():
        if not mps: empty.append(p)
        for mp in mps:
            total += 1
            if not (1 <= mp['k'] <= len(mp['of'])): ok = False; print('BAD K', qid, p, mp)
            if len(set(mp['of'])) != len(mp['of']): ok = False; print('DUP', qid, p, mp)
            for i in mp['of']:
                if i not in cands: ok = False; print('BAD ID', qid, p, i)
    print(qid, 'parts', len(parts), 'marking points', total, 'empty', empty)
print('ALL OK' if ok else 'PROBLEMS')
