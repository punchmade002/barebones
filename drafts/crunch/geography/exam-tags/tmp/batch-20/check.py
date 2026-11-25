import json, re, sys
base = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags'
batch = open(base + '/batches/batch-20.txt', encoding='utf-8').read()
blocks = batch.split('\n====')
qs = {}
for b in re.split(r'^=+\s*$', batch, flags=re.M):
    m = re.search(r'^QUESTION (\S+)', b, re.M)
    if not m:
        continue
    qid = m.group(1)
    cands = set(re.findall(r'^\[([^\]]+)\]', b, re.M))
    labels = re.findall(r'^PART "([^"]+)"', b, re.M)
    qs[qid] = (cands, labels)
ok = True
for qid, (cands, labels) in qs.items():
    d = json.load(open(f'{base}/out/{qid}.json', encoding='utf-8'))
    if list(d.keys()) != labels:
        print(qid, 'label mismatch', list(d.keys()), labels); ok = False
    for lab, pts in d.items():
        if not pts:
            print(qid, lab, 'EMPTY'); ok = False
        for p in pts:
            if not (1 <= p['k'] <= len(p['of'])) or len(p['of']) > 2:
                print(qid, lab, 'bad k/of', p); ok = False
            for i in p['of']:
                if i not in cands:
                    print(qid, lab, 'unknown id', i); ok = False
    print(qid, {lab: len(p) for lab, p in d.items()})
print('OK' if ok else 'FAIL')
