import json, re, sys
batch = open('/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-49.txt', encoding='utf-8').read()
qid = 'geography-pp-2020-higher-q108'
labels = re.findall(r'^PART "([^"]+)"', batch, re.M)
cands = set(re.findall(r'^\[([^\]]+)\]', batch, re.M))
out = json.load(open(f'/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/{qid}.json', encoding='utf-8'))
assert list(out.keys()) == labels, (list(out.keys()), labels)
total = 0
for part, pts in out.items():
    if not pts:
        print('EMPTY', part)
    for p in pts:
        total += 1
        assert 1 <= p['k'] <= len(p['of']), (part, p)
        assert len(p['of']) <= 2 or part, p
        for i in p['of']:
            assert i in cands, (part, i)
print('ok parts', len(labels), 'points', total)
