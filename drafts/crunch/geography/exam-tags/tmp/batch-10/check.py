import json, os, re, sys

BATCH = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-10.txt'
OUT = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out'

text = open(BATCH, encoding='utf-8').read()
blocks = [b for b in re.split(r'\n=+\n', text) if 'QUESTION ' in b]
ok = True
for block in blocks:
    qid = re.search(r'^QUESTION (\S+)', block, re.M).group(1)
    labels = re.findall(r'^PART "(.*)"', block, re.M)
    cand_part = block.split('CANDIDATES (shortlist):', 1)[1]
    cands = set(re.findall(r'^\[([^\]]+)\]', cand_part, re.M))
    path = os.path.join(OUT, qid + '.json')
    try:
        data = json.load(open(path, encoding='utf-8'))
    except Exception as e:
        print(qid, 'PARSE FAIL', e); ok = False; continue
    if list(data.keys()) != labels:
        print(qid, 'LABEL MISMATCH', list(data.keys()), labels); ok = False
    points = 0
    empty = []
    for label, pts in data.items():
        if not pts:
            empty.append(label)
        for p in pts:
            points += 1
            of = p['of']
            if not (1 <= p['k'] <= len(of)):
                print(qid, label, 'BAD K', p); ok = False
            for i in of:
                if i not in cands:
                    print(qid, label, 'UNKNOWN ID', i); ok = False
    print(qid, 'parts', len(labels), 'points', points, 'empty', empty)
print('ALL OK' if ok else 'PROBLEMS')
