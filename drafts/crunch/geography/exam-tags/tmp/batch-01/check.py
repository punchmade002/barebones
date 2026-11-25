import json, re, os

B = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-01.txt'
O = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'
txt = open(B, encoding='utf-8').read()
blocks = [b for b in re.split(r'^=+\s*$', txt, flags=re.M) if 'QUESTION ' in b]

for b in blocks:
    qid = re.search(r'^QUESTION (\S+)', b, re.M).group(1)
    cands = set(re.findall(r'^\[([^\]]+)\]', b, re.M))
    labels = []
    for m in re.finditer(r'^PART\s*(\([^)]*\))?\s*\(\d+ marks?\)', b, re.M):
        labels.append(m.group(1) or '')
    problems = []
    path = os.path.join(O, qid + '.json')
    try:
        data = json.load(open(path, encoding='utf-8'))
    except Exception as e:
        print(qid, 'PARSE FAIL', e)
        continue
    if list(data.keys()) != labels:
        problems.append('labels %r != %r' % (list(data.keys()), labels))
    mp = 0
    empty = []
    for key, mps in data.items():
        if not mps:
            empty.append(key or '(blank)')
        for mpt in mps:
            mp += 1
            of = mpt['of']
            if not (1 <= mpt['k'] <= len(of)):
                problems.append('bad k in %s' % key)
            for i in of:
                if i not in cands:
                    problems.append('unknown id %s in %s' % (i, key))
    print(qid, 'parts=%d' % len(labels), 'marking_points=%d' % mp, 'empty=%s' % empty, 'OK' if not problems else problems)
