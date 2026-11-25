import json, re, sys
base = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags'
batch = open(base + '/batches/batch-62.txt', encoding='utf-8').read()
qs = batch.split('=' * 40)
expected_parts = {}
cands = {}
for q in qs:
    m = re.search(r'QUESTION (\S+)', q)
    if not m:
        continue
    qid = m.group(1)
    expected_parts[qid] = re.findall(r'^PART "([^"]+)"', q, re.M)
    cands[qid] = set(re.findall(r'^\[([^\]]+)\]', q, re.M))
ok = True
for qid, parts in expected_parts.items():
    data = json.load(open(f'{base}/out/{qid}.json', encoding='utf-8'))
    keys = list(data.keys())
    if keys != parts:
        print('KEY MISMATCH', qid, keys, parts); ok = False
    npts = 0
    for p, pts in data.items():
        for pt in pts:
            npts += 1
            if not (1 <= pt['k'] <= len(pt['of'])): print('BAD k', qid, p, pt); ok = False
            for i in pt['of']:
                if i not in cands[qid]: print('BAD id', qid, p, i); ok = False
    empties = [p for p, pts in data.items() if not pts]
    print(qid, 'parts', len(parts), 'points', npts, 'empty', empties)
print('OK' if ok else 'FAIL')
