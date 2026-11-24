import json, re, sys
batch = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-55.txt'
out = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'
text = open(batch, encoding='utf-8').read()
blocks = text.split('\n====')
ok = True
for blk in re.split(r'\n={5,}\n', text):
    m = re.search(r'^QUESTION (\S+)', blk, re.M)
    if not m:
        continue
    qid = m.group(1)
    cands = set(re.findall(r'^\[([^\]]+)\]', blk, re.M))
    labels = re.findall(r'^PART "([^"]+)"', blk, re.M)
    data = json.load(open(out + qid + '.json', encoding='utf-8'))
    assert set(data.keys()) == set(labels) and len(data) == len(labels), (qid, labels, list(data))
    n = 0
    empty = []
    for lab in labels:
        mps = data[lab]
        if not mps:
            empty.append(lab)
        for mp in mps:
            n += 1
            assert 1 <= mp['k'] <= len(mp['of']), (qid, lab, mp)
            for i in mp['of']:
                assert i in cands, (qid, lab, i)
    print(qid, 'parts', len(labels), 'marking points', n, 'empty', empty)
print('all ok')
