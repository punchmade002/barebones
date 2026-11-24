import json, re, sys
BATCH = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-75.txt'
OUT = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'
text = open(BATCH, encoding='utf-8').read()
blocks = text.split('\n====')
ok = True
for blk in re.split(r'={5,}', text):
    m = re.search(r'QUESTION (\S+)', blk)
    if not m:
        continue
    qid = m.group(1)
    cands = set(re.findall(r'^\[([^\]]+)\]', blk, re.M))
    labels = re.findall(r'^PART "([^"]+)"', blk, re.M)
    data = json.load(open(OUT + qid + '.json', encoding='utf-8'))
    if list(data.keys()) != labels:
        print(qid, 'label mismatch', list(data.keys()), labels); ok = False
    empty = []
    total = 0
    for lab, mps in data.items():
        if not mps: empty.append(lab)
        for mp in mps:
            total += 1
            of = mp['of']
            if not (1 <= mp['k'] <= len(of)): print(qid, lab, 'bad k', mp); ok = False
            if len(of) > 2: print(qid, lab, 'too many ids', mp); ok = False
            for i in of:
                if i not in cands: print(qid, lab, 'id not in candidates', i); ok = False
    print(qid, 'parts', len(labels), 'marking points', total, 'empty', empty)
print('ALL OK' if ok else 'PROBLEMS')
