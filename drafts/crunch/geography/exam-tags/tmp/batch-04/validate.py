import json, os, re, sys

BATCH = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-04.txt'
OUT = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out'

text = open(BATCH, encoding='utf-8').read()
blocks = text.split('=' * 40)
ok = True
for block in blocks:
    m = re.search(r'^QUESTION (\S+)', block, re.M)
    if not m:
        continue
    qid = m.group(1)
    labels = re.findall(r'^PART "(.*?)"', block, re.M)
    cand_ids = set(re.findall(r'^\[([^\]]+)\]', block, re.M))
    path = os.path.join(OUT, qid + '.json')
    try:
        data = json.load(open(path, encoding='utf-8'))
    except Exception as e:
        print(qid, 'PARSE FAIL', e); ok = False; continue
    keys = list(data.keys())
    if keys != labels:
        print(qid, 'LABELS MISMATCH', keys, labels); ok = False
    points = 0; empty = []
    for lab in labels:
        pts = data.get(lab, [])
        if not pts:
            empty.append(lab)
        for p in pts:
            points += 1
            of = p['of']
            if not (1 <= p['k'] <= len(of)):
                print(qid, lab, 'BAD K', p); ok = False
            for i in of:
                if i not in cand_ids:
                    print(qid, lab, 'ID NOT IN CANDIDATES', i); ok = False
            if len(of) > 2:
                print(qid, lab, 'MORE THAN 2 IDS', p); ok = False
    print(f'{qid} parts={len(labels)} points={points} empty={empty}')
print('ALL OK' if ok else 'PROBLEMS')
