import json, re, sys
batch = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-72.txt'
outdir = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'
text = open(batch, encoding='utf-8').read()
ok = True
for block in text.split('\n====='):
    m = re.search(r'QUESTION (\S+)', block)
    if not m:
        continue
    qid = m.group(1)
    labels = re.findall(r'^PART "([^"]+)"', block, re.M)
    cands = set(re.findall(r'^\[([^\]]+)\]', block, re.M))
    data = json.load(open(outdir + qid + '.json', encoding='utf-8'))
    if list(data.keys()) != labels:
        print(qid, 'label mismatch', list(data.keys()), labels); ok = False
    mp = 0; empty = []
    for part, mps in data.items():
        if not mps: empty.append(part)
        for item in mps:
            mp += 1
            k, of = item['k'], item['of']
            if not (1 <= k <= len(of)) or len(of) > 2:
                print(qid, part, 'bad k/of', item); ok = False
            for i in of:
                if i not in cands:
                    print(qid, part, 'id not in candidates', i); ok = False
    print(qid, 'parts', len(labels), 'marking points', mp, 'empty', empty)
print('OK' if ok else 'FAILED')
