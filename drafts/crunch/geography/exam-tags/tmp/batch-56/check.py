import json, re, sys
B = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/'
batch = open(B + 'batches/batch-56.txt', encoding='utf-8').read()
qs = re.split(r'\n=+\n', batch)
for q in qs:
    m = re.search(r'^QUESTION (\S+)', q, re.M)
    if not m: continue
    qid = m.group(1)
    cands = set(re.findall(r'^\[([^\]]+)\]', q, re.M))
    parts = re.findall(r'^PART "([^"]+)"', q, re.M)
    d = json.load(open(B + 'out/' + qid + '.json', encoding='utf-8'))
    ok = True
    if list(d.keys()) != parts:
        print(qid, 'PART KEYS MISMATCH', list(d.keys()), parts); ok = False
    total = 0; empty = []
    for p, pts in d.items():
        if not pts: empty.append(p)
        for pt in pts:
            total += 1
            if not (1 <= pt['k'] <= len(pt['of'])): print(qid, p, 'bad k', pt); ok = False
            for i in pt['of']:
                if i not in cands: print(qid, p, 'unknown id', i); ok = False
    print(qid, 'parts', len(parts), 'points', total, 'empty', empty, 'OK' if ok else 'FAIL')
