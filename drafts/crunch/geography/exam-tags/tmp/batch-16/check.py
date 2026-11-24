import json, re, sys
base = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags'
batch = open(base + '/batches/batch-16.txt', encoding='utf-8').read()
qs = re.split(r'\n=+\n', batch)
ok = True
for block in batch.split('QUESTION ')[1:]:
    qid = block.split()[0]
    cands = set(re.findall(r'^\[([^\]]+)\]', block, re.M))
    labels = re.findall(r'^PART "([^"]+)"', block, re.M)
    d = json.load(open(f'{base}/out/{qid}.json', encoding='utf-8'))
    if list(d.keys()) != labels:
        print(qid, 'label mismatch', list(d.keys()), labels); ok = False
    total = 0
    empty = []
    for lab, mps in d.items():
        if not mps: empty.append(lab)
        total += len(mps)
        for mp in mps:
            assert 1 <= mp['k'] <= len(mp['of']), (qid, lab, mp)
            for i in mp['of']:
                if i not in cands:
                    print('BAD ID', qid, lab, i); ok = False
    print(qid, 'parts', len(labels), 'mps', total, 'empty', empty)
print('OK' if ok else 'FAIL')
