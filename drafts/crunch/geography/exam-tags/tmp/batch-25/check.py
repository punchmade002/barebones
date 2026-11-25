import json, re, sys
q = 'geography-pp-2018-higher-q107'
batch = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-25.txt'
out = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/' + q + '.json'
text = open(batch).read()
labels = re.findall(r'PART "([^"]+)"', text)
cand_block = text.split('CANDIDATES (shortlist):')[1]
cands = set(re.findall(r'^\[([^\]]+)\]', cand_block, re.M))
d = json.load(open(out))
assert list(d.keys()) == labels, (list(d.keys()), labels)
n = 0
for part, mps in d.items():
    for mp in mps:
        n += 1
        assert 1 <= mp['k'] <= len(mp['of']), mp
        assert all(i in cands for i in mp['of']), mp
print('ok', q, 'parts', len(d), 'marking points', n, 'empty', [p for p in d if not d[p]])
