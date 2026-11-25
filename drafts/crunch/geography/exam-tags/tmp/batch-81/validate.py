import json, re, sys
base = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags'
batch = open(base + '/batches/batch-81.txt', encoding='utf-8').read()
blocks = batch.split('\n====')
ok = True
for blk in re.split(r'\n=+\n', batch):
    m = re.search(r'QUESTION (\S+)', blk)
    if not m: continue
    qid = m.group(1)
    cands = set(re.findall(r'^\[([^\]]+)\]', blk, re.M))
    parts = re.findall(r'^PART "([^"]+)"', blk, re.M)
    try:
        data = json.load(open(f'{base}/out/{qid}.json', encoding='utf-8'))
    except Exception as e:
        print(qid, 'PARSE FAIL', e); ok = False; continue
    if list(data.keys()) != parts:
        print(qid, 'PART MISMATCH', list(data.keys()), parts); ok = False
    total = 0; empty = []
    for p, pts in data.items():
        if not pts: empty.append(p)
        for pt in pts:
            total += 1
            if not (1 <= pt['k'] <= len(pt['of'])): print(qid, p, 'BAD K', pt); ok = False
            for i in pt['of']:
                if i not in cands: print(qid, p, 'BAD ID', i); ok = False
    print(qid, 'parts', len(parts), 'points', total, 'empty', empty)
print('ALL OK' if ok else 'ERRORS')
