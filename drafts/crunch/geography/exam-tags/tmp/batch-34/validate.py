import json, re, sys

BATCH = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-34.txt'
OUT = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'

text = open(BATCH, encoding='utf-8').read()
blocks = re.split(r'\n={3,}\n', text)
ok = True
for blk in blocks:
    m = re.search(r'^QUESTION (\S+)', blk, re.M)
    if not m:
        continue
    qid = m.group(1)
    cands = set(re.findall(r'^\[([^\]]+)\]', blk, re.M))
    labels = re.findall(r'^PART "([^"]+)"', blk, re.M)
    try:
        data = json.load(open(OUT + qid + '.json', encoding='utf-8'))
    except Exception as e:
        print(qid, 'PARSE FAIL', e); ok = False; continue
    problems = []
    if list(data.keys()) != labels:
        problems.append('labels mismatch: %s vs %s' % (list(data.keys()), labels))
    total = 0
    empty = []
    for lab, mps in data.items():
        if not mps:
            empty.append(lab)
        for mp in mps:
            total += 1
            of = mp['of']
            if not (1 <= mp['k'] <= len(of)):
                problems.append('bad k in %s: %s' % (lab, mp))
            if len(of) > 2:
                problems.append('too many ids in %s: %s' % (lab, mp))
            for i in of:
                if i not in cands:
                    problems.append('id not in candidates %s: %s' % (lab, i))
    print(qid, 'parts=%d' % len(data), 'marking_points=%d' % total, 'empty=%s' % empty)
    for p in problems:
        print('  PROBLEM', p); ok = False
print('ALL OK' if ok else 'ISSUES FOUND')
