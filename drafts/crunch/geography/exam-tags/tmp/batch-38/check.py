import json, re, sys
base = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags'
batch = open(base + '/batches/batch-38.txt', encoding='utf-8').read()
qid = 'geography-pp-2019-higher-q108'
cands = set(re.findall(r'^\[([^\]]+)\]', batch, re.M))
labels = re.findall(r'^PART "([^"]+)"', batch, re.M)
data = json.load(open(base + '/out/' + qid + '.json', encoding='utf-8'))
errs = []
if list(data.keys()) != labels:
    errs.append(('label mismatch', list(data.keys()), labels))
total = 0
empty = []
for lab, pts in data.items():
    if not pts: empty.append(lab)
    for p in pts:
        total += 1
        if not (1 <= p['k'] <= len(p['of'])): errs.append(('k', lab, p))
        if len(p['of']) > 2: errs.append(('too many ids', lab, p))
        for i in p['of']:
            if i not in cands: errs.append(('bad id', lab, i))
print('parts', len(data), 'points', total, 'empty', empty, 'errors', errs)
