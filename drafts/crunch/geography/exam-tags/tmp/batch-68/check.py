import json, re, sys
batch = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-68.txt'
out = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'
text = open(batch, encoding='utf-8').read()
blocks = re.split(r'\n=+\n', text)
ok = True
for b in blocks:
    m = re.search(r'QUESTION (\S+)', b)
    if not m:
        continue
    qid = m.group(1)
    parts = re.findall(r'PART "([^"]+)"', b)
    cand = set(re.findall(r'^\[([^\]]+)\]', b, re.M))
    data = json.load(open(out + qid + '.json', encoding='utf-8'))
    if list(data.keys()) != parts:
        print(qid, 'PART ORDER/LABEL MISMATCH', list(data.keys()), parts); ok = False
    total = 0; empty = []
    for p, mps in data.items():
        if not mps: empty.append(p)
        for mp in mps:
            total += 1
            if not (1 <= mp['k'] <= len(mp['of'])): print(qid, p, 'bad k', mp); ok = False
            for i in mp['of']:
                if i not in cand: print(qid, p, 'id not in candidates', i); ok = False
    print(qid, 'parts', len(parts), 'marking points', total, 'empty', empty)
print('OK' if ok else 'ERRORS')
