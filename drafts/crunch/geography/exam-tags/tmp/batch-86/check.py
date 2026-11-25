import json, re, sys
batch = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-86.txt'
out = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'
text = open(batch, encoding='utf-8').read()
blocks = text.split('\n====')
ok = True
for blk in re.split(r'\n=+\n', text):
    m = re.search(r'^QUESTION (\S+)', blk, re.M)
    if not m:
        continue
    qid = m.group(1)
    cands = set(re.findall(r'^\[([^\]]+)\]', blk, re.M))
    parts = re.findall(r'^PART "([^"]+)"', blk, re.M)
    data = json.load(open(out + qid + '.json', encoding='utf-8'))
    assert list(data.keys()) == parts, (qid, list(data.keys()), parts)
    n = 0
    empty = []
    for label, pts in data.items():
        if not pts:
            empty.append(label)
        for p in pts:
            n += 1
            assert 1 <= p['k'] <= len(p['of']), (qid, label, p)
            assert len(p['of']) <= 2, (qid, label, p)
            for i in p['of']:
                if i not in cands:
                    ok = False
                    print('BAD ID', qid, label, i)
    print(qid, 'parts', len(parts), 'points', n, 'empty', empty)
print('OK' if ok else 'FAIL')
