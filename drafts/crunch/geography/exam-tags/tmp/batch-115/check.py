import json, re, sys
BATCH = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-115.txt'
OUT = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'
text = open(BATCH, encoding='utf-8').read()
blocks = text.split('=' * 40)
ok = True
for blk in blocks:
    m = re.search(r'^QUESTION (\S+)', blk, re.M)
    if not m:
        continue
    qid = m.group(1)
    labels = re.findall(r'^PART "([^"]+)"', blk, re.M)
    cand = set(re.findall(r'^\[([^\]]+)\]', blk, re.M))
    data = json.load(open(OUT + qid + '.json', encoding='utf-8'))
    if list(data.keys()) != labels:
        print(qid, 'label mismatch', list(data.keys()), labels); ok = False
    n = 0
    for lab, pts in data.items():
        for p in pts:
            n += 1
            if not (1 <= p['k'] <= len(p['of'])):
                print(qid, lab, 'bad k', p); ok = False
            for i in p['of']:
                if i not in cand:
                    print(qid, lab, 'unknown id', i); ok = False
    empty = [l for l, p in data.items() if not p]
    print(qid, 'parts', len(labels), 'points', n, 'empty', empty, 'cands', len(cand))
print('OK' if ok else 'FAIL')
