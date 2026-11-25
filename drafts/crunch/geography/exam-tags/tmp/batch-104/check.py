import json, re, sys
batch = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-104.txt'
out = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'
text = open(batch, encoding='utf-8').read()
qs = text.split('\n====')  # split by separator lines
for block in re.split(r'\n=+\n', text):
    m = re.search(r'QUESTION (\S+)', block)
    if not m: continue
    qid = m.group(1)
    labels = re.findall(r'^PART "([^"]+)"', block, re.M)
    cands = set(re.findall(r'^\[([^\]]+)\]', block, re.M))
    data = json.load(open(out + qid + '.json', encoding='utf-8'))
    assert list(data.keys()) == labels, (qid, list(data.keys()), labels)
    n_pts = 0; empty = []
    for part, pts in data.items():
        if not pts: empty.append(part)
        for p in pts:
            assert 1 <= p['k'] <= len(p['of']), (qid, part, p)
            assert len(p['of']) <= 2, (qid, part, p)
            for i in p['of']:
                assert i in cands, (qid, part, i)
            n_pts += 1
    print(qid, 'parts', len(labels), 'points', n_pts, 'empty', empty)
