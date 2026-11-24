import json, re, sys
BATCH = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-100.txt'
OUT = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'
text = open(BATCH, encoding='utf-8').read()
blocks = text.split('\n====')  # question blocks separated by '=' lines
expected = {}
for blk in re.split(r'\n=+\n', text):
    m = re.search(r'QUESTION (\S+)', blk)
    if not m:
        continue
    qid = m.group(1)
    labels = re.findall(r'^PART "([^"]+)"', blk, re.M)
    cands = set(re.findall(r'^\[([^\]]+)\]', blk, re.M))
    expected[qid] = (labels, cands)
ok = True
for qid, (labels, cands) in expected.items():
    data = json.load(open(OUT + qid + '.json', encoding='utf-8'))
    if list(data.keys()) != labels:
        print('LABEL MISMATCH', qid, list(data.keys()), labels); ok = False
    mps = 0; empty = []
    for part, mp_list in data.items():
        if not mp_list: empty.append(part)
        for mp in mp_list:
            mps += 1
            of = mp['of']
            if not (1 <= mp['k'] <= len(of)): print('BAD K', qid, part, mp); ok = False
            for i in of:
                if i not in cands: print('BAD ID', qid, part, i); ok = False
    print(qid, 'parts', len(labels), 'marking points', mps, 'empty', empty)
print('ALL OK' if ok else 'FAILURES')
