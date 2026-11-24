import json, re, sys
base = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/'
batch = open(base + 'batches/batch-93.txt', encoding='utf-8').read()
blocks = batch.split('\n====')
qs = {}
for raw in re.split(r'={5,}', batch):
    m = re.search(r'QUESTION (\S+)', raw)
    if not m:
        continue
    qid = m.group(1)
    parts = re.findall(r'PART "([^"]+)"', raw)
    cands = set(re.findall(r'^\[([^\]]+)\]', raw, re.M))
    qs[qid] = (parts, cands)
ok = True
for qid, (parts, cands) in qs.items():
    data = json.load(open(base + 'out/' + qid + '.json', encoding='utf-8'))
    if list(data.keys()) != parts:
        print('PART MISMATCH', qid, list(data.keys()), parts); ok = False
    total = 0; empty = []
    for p, mps in data.items():
        if not mps: empty.append(p)
        total += len(mps)
        for mp in mps:
            of = mp['of']
            if not (1 <= mp['k'] <= len(of)): print('BAD K', qid, p, mp); ok = False
            if len(of) > 2: print('MANY IDS', qid, p, mp)
            for i in of:
                if i not in cands: print('BAD ID', qid, p, i); ok = False
    print(qid, len(parts), total, empty)
print('OK' if ok else 'FAILED')
