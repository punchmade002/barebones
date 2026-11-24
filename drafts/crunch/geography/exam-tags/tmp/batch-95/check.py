import json, re, sys
BATCH = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-95.txt'
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
    parts = re.findall(r'^PART "([^"]+)"', blk, re.M)
    try:
        data = json.load(open(OUT + qid + '.json', encoding='utf-8'))
    except Exception as e:
        print(qid, 'PARSE FAIL', e); ok = False; continue
    if list(data.keys()) != parts:
        print(qid, 'PART MISMATCH', list(data.keys()), parts); ok = False
    n = 0; empty = []
    for p, mps in data.items():
        if not mps: empty.append(p)
        for mp in mps:
            n += 1
            of = mp['of']
            if not (1 <= mp['k'] <= len(of)): print(qid, p, 'bad k', mp); ok = False
            for i in of:
                if i not in cands: print(qid, p, 'bad id', i); ok = False
    print(qid, 'parts', len(data), 'marking points', n, 'empty', empty)
print('ALL OK' if ok else 'PROBLEMS')
