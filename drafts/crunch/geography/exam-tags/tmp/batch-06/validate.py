import json, re, sys
BATCH = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-06.txt'
OUT = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'
text = open(BATCH, encoding='utf-8').read()
blocks = re.split(r'^QUESTION ', text, flags=re.M)[1:]
ok = True
for b in blocks:
    qid = b.split()[0]
    labels = re.findall(r'^PART "(.*?)"', b, flags=re.M)
    cands = set(re.findall(r'^\[([^\]]+)\]', b, flags=re.M))
    data = json.load(open(OUT + qid + '.json', encoding='utf-8'))
    if sorted(data.keys()) != sorted(labels) or len(data) != len(labels):
        print(qid, 'LABEL MISMATCH', list(data.keys()), labels); ok = False
    npts = 0; empty = []
    for lab, pts in data.items():
        if not pts: empty.append(lab)
        for p in pts:
            npts += 1
            if not (1 <= p['k'] <= len(p['of'])): print(qid, lab, 'bad k', p); ok = False
            for i in p['of']:
                if i not in cands: print(qid, lab, 'id not in candidates', i); ok = False
    print(qid, 'parts', len(data), 'points', npts, 'empty', empty)
print('ALL OK' if ok else 'PROBLEMS')
