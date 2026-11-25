import json, re, sys
B = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-52.txt'
O = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'
text = open(B, encoding='utf-8').read()
qblocks = text.split('=' * 40)
for blk in qblocks:
    m = re.search(r'QUESTION (\S+)', blk)
    if not m:
        continue
    qid = m.group(1)
    labels = re.findall(r'^PART "([^"]+)"', blk, re.M)
    cands = set(re.findall(r'^\[([^\]]+)\]', blk, re.M))
    d = json.load(open(O + qid + '.json', encoding='utf-8'))
    assert list(d.keys()) == labels, (qid, list(d.keys()), labels)
    total = 0; empty = []
    for lab, pts in d.items():
        if not pts: empty.append(lab)
        for p in pts:
            assert 1 <= p['k'] <= len(p['of']), (qid, lab, p)
            assert all(i in cands for i in p['of']), (qid, lab, p)
        total += len(pts)
    print(qid, len(labels), total, empty)
