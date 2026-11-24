import json, re, sys
batch = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-71.txt'
out = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'
text = open(batch, encoding='utf-8').read()
blocks = text.split('=' * 40)
ok = True
for blk in blocks:
    m = re.search(r'^QUESTION (\S+)', blk, re.M)
    if not m:
        continue
    qid = m.group(1)
    labels = re.findall(r'^PART "([^"]+)"', blk, re.M)
    cand_part = blk.split('CANDIDATES (shortlist):')[1]
    cands = set(re.findall(r'^\[([^\]]+)\]', cand_part, re.M))
    data = json.load(open(out + qid + '.json', encoding='utf-8'))
    assert list(data.keys()) == labels, (qid, list(data.keys()), labels)
    total = 0; empty = []
    for lab, mps in data.items():
        if not mps: empty.append(lab)
        for mp in mps:
            total += 1
            assert 1 <= mp['k'] <= len(mp['of']), (qid, lab, mp)
            for i in mp['of']:
                assert i in cands, (qid, lab, i)
    print(qid, 'parts', len(labels), 'marking points', total, 'empty', empty)
print('all checks passed')
