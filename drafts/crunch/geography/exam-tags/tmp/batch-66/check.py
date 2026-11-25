import json, re, sys, os

BATCH = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-66.txt'
OUT = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out'

text = open(BATCH, encoding='utf-8').read()
blocks = [b for b in text.split('\n====') if b.strip()]
ok = True
for block in re.split(r'\n=+\n', text):
    if 'QUESTION ' not in block:
        continue
    qid = re.search(r'QUESTION (\S+)', block).group(1)
    labels = re.findall(r'^PART "([^"]+)"', block, re.M)
    cands = set(re.findall(r'^\[([^\]]+)\]', block, re.M))
    path = os.path.join(OUT, qid + '.json')
    if not os.path.exists(path):
        print('MISSING', qid); ok = False; continue
    data = json.load(open(path, encoding='utf-8'))
    if list(data.keys()) != labels:
        print(qid, 'label mismatch', list(data.keys()), labels); ok = False
    total = 0; empty = []
    for lab, mps in data.items():
        if not mps:
            empty.append(lab)
        for mp in mps:
            total += 1
            of = mp['of']; k = mp['k']
            if not (1 <= k <= len(of)):
                print(qid, lab, 'bad k', mp); ok = False
            for i in of:
                if i not in cands:
                    print(qid, lab, 'id not in candidates', i); ok = False
    print(qid, 'parts', len(labels), 'marking points', total, 'empty', empty)
print('OK' if ok else 'PROBLEMS')
