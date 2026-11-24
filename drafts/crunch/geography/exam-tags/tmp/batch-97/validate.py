import json, re, sys
BATCH = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-97.txt'
OUT = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'
text = open(BATCH, encoding='utf-8').read()
blocks = [b for b in re.split(r'\n=+\n', text) if 'QUESTION ' in b]
ok = True
for b in blocks:
    qid = re.search(r'QUESTION (\S+)', b).group(1)
    labels = re.findall(r'^PART "([^"]+)"', b, re.M)
    cands = set(re.findall(r'^\[([^\]]+)\]', b, re.M))
    path = OUT + qid + '.json'
    try:
        data = json.load(open(path, encoding='utf-8'))
    except Exception as e:
        print(qid, 'PARSE FAIL', e); ok = False; continue
    if list(data.keys()) != labels:
        print(qid, 'LABEL MISMATCH', list(data.keys()), labels); ok = False
    mp = 0; empty = []
    for lab, mps in data.items():
        if not mps: empty.append(lab)
        for m in mps:
            mp += 1
            if not (1 <= m['k'] <= len(m['of'])): print(qid, lab, 'BAD k', m); ok = False
            for i in m['of']:
                if i not in cands: print(qid, lab, 'BAD ID', i); ok = False
    print(qid, 'parts', len(labels), 'marking points', mp, 'empty', empty)
print('ALL OK' if ok else 'ERRORS')
