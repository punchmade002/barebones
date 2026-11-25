import json, re, sys
batch = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-17.txt'
out = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'
text = open(batch, encoding='utf-8').read()
blocks = [b for b in text.split('\n=') if 'QUESTION' in b]
ok = True
for b in blocks:
    qid = re.search(r'QUESTION (\S+)', b).group(1)
    parts = re.findall(r'^PART "([^"]+)"', b, re.M)
    cands = set(re.findall(r'^\[([^\]]+)\]', b, re.M))
    data = json.load(open(out + qid + '.json', encoding='utf-8'))
    if list(data.keys()) != parts:
        print(qid, 'PART MISMATCH', list(data.keys()), parts); ok = False
    mp = 0; empty = []
    for p, pts in data.items():
        if not pts: empty.append(p)
        for pt in pts:
            mp += 1
            if not (1 <= pt['k'] <= len(pt['of'])): print(qid, p, 'bad k', pt); ok = False
            for i in pt['of']:
                if i not in cands: print(qid, p, 'unknown id', i); ok = False
    print(qid, 'parts', len(parts), 'marking points', mp, 'empty', empty)
print('OK' if ok else 'FAILURES')
