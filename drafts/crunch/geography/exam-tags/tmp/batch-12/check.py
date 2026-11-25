import json, re, sys
batch = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-12.txt'
out = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/geography-pp-2017-higher-q103.json'
text = open(batch, encoding='utf-8').read()
qid = re.search(r'QUESTION (\S+)', text).group(1)
labels = re.findall(r'PART "([^"]+)"', text)
cands = set(re.findall(r'^\[([^\]]+)\]', text, re.M))
data = json.load(open(out, encoding='utf-8'))
assert qid == 'geography-pp-2017-higher-q103', qid
assert list(data.keys()) == labels, (list(data.keys()), labels)
total = 0; empty = []
for lab, mps in data.items():
    if not mps: empty.append(lab)
    for mp in mps:
        assert 1 <= mp['k'] <= len(mp['of']), (lab, mp)
        for i in mp['of']:
            assert i in cands, (lab, i)
        total += 1
print('question', qid, '| parts', len(data), '| marking points', total, '| empty', empty)
