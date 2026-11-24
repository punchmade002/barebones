import json, re, sys
out = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/geography-pp-2020-higher-q107.json'
batch = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-48.txt'
data = json.load(open(out))
text = open(batch).read()
cands = set(re.findall(r'^\[([^\]]+)\]', text, re.M))
labels = re.findall(r'^PART "([^"]+)"', text, re.M)
assert list(data.keys()) == labels, (list(data.keys()), labels)
total = 0
for part, pts in data.items():
    total += len(pts)
    for p in pts:
        assert 1 <= p['k'] <= len(p['of']), p
        for i in p['of']:
            assert i in cands, i
    print(part, len(pts), [p['k'] for p in pts].count(2))
print('total', total, 'empty', [p for p, v in data.items() if not v])
