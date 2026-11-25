import json, re, sys
BATCH = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-44.txt'
OUT = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'
text = open(BATCH, encoding='utf-8').read()
blocks = [b for b in text.split('\n====') if b.strip()]
ok = True
for blk in re.split(r'\n=+\n', text):
    m = re.search(r'^QUESTION (\S+)', blk, re.M)
    if not m:
        continue
    qid = m.group(1)
    cand_section = blk.split('CANDIDATES (shortlist):', 1)[1]
    cands = set(re.findall(r'^\[([^\]]+)\]', cand_section, re.M))
    labels = re.findall(r'^PART "([^"]+)"', blk, re.M)
    data = json.load(open(OUT + qid + '.json', encoding='utf-8'))
    assert list(data.keys()) == labels, (qid, list(data.keys()), labels)
    n = 0
    for part, pts in data.items():
        for p in pts:
            n += 1
            assert 1 <= p['k'] <= len(p['of']), (qid, part, p)
            assert len(p['of']) <= 2, (qid, part, p)
            for i in p['of']:
                assert i in cands, (qid, part, i)
    print(qid, 'parts', len(labels), 'points', n, 'empty', [k for k, v in data.items() if not v])
