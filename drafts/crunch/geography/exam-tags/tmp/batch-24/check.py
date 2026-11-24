import json, re, sys
batch = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-24.txt'
out = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'
text = open(batch, encoding='utf-8').read()
blocks = re.split(r'^=+$', text, flags=re.M)
ok = True
for b in blocks:
    m = re.search(r'^QUESTION (\S+)', b, re.M)
    if not m:
        continue
    qid = m.group(1)
    labels = re.findall(r'^PART "([^"]+)"', b, re.M)
    cands = set(re.findall(r'^\[([^\]]+)\]', b, re.M))
    data = json.load(open(out + qid + '.json', encoding='utf-8'))
    assert list(data.keys()) == labels, (qid, list(data.keys()), labels)
    mp = 0
    empty = []
    for lab, mps in data.items():
        if not mps:
            empty.append(lab)
        for mpt in mps:
            mp += 1
            assert 1 <= mpt['k'] <= len(mpt['of']), (qid, lab, mpt)
            for i in mpt['of']:
                if i not in cands:
                    ok = False
                    print('BAD ID', qid, lab, i)
    print(qid, 'parts', len(labels), 'marking points', mp, 'empty', empty)
print('ALL OK' if ok else 'PROBLEMS')
