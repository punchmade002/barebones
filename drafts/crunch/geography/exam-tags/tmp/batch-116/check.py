import json, re, sys
B = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-116.txt'
O = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'
text = open(B, encoding='utf-8').read()
blocks = [b for b in text.split('\n====') if 'QUESTION ' in b]
for b in blocks:
    qid = re.search(r'QUESTION (\S+)', b).group(1)
    cands = set(re.findall(r'^\[([^\]]+)\]', b, re.M))
    labels = re.findall(r'^PART "([^"]+)"', b, re.M)
    d = json.load(open(O + qid + '.json', encoding='utf-8'))
    keys = list(d.keys())
    ok = keys == labels and len(set(keys)) == len(keys)
    mp = 0; empty = []
    for part in keys:
        pts = d[part]
        if not pts: empty.append(part)
        for p in pts:
            mp += 1
            assert 1 <= p['k'] <= len(p['of']), (qid, part, p)
            for i in p['of']:
                assert i in cands, (qid, part, i)
    print(qid, 'parts', len(keys), 'labels_ok', ok, 'points', mp, 'empty', empty, 'cands', len(cands))
