import json, re, sys
batch = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-67.txt'
out = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'
text = open(batch, encoding='utf-8').read()
for block in text.split('='*40):
    m = re.search(r'^QUESTION (\S+)', block, re.M)
    if not m: continue
    qid = m.group(1)
    labels = re.findall(r'^PART "([^"]+)"', block, re.M)
    cands = set(re.findall(r'^\[([^\]]+)\]', block, re.M))
    d = json.load(open(out + qid + '.json', encoding='utf-8'))
    assert list(d.keys()) == labels, (qid, list(d.keys()), labels)
    total = 0; empty = []
    for lab, mps in d.items():
        if not mps: empty.append(lab)
        for mp in mps:
            total += 1
            assert 1 <= mp['k'] <= len(mp['of']), (qid, lab, mp)
            for i in mp['of']:
                assert i in cands, (qid, lab, i)
    print(qid, 'parts', len(labels), 'marking points', total, 'empty', empty)
