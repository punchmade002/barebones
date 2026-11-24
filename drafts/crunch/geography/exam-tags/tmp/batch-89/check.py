import json, re, sys

BATCH = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-89.txt'
OUT = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'

text = open(BATCH, encoding='utf-8').read()
blocks = text.split('\n====')
questions = {}
for b in blocks:
    m = re.search(r'QUESTION (\S+)', b)
    if not m:
        continue
    qid = m.group(1)
    parts = re.findall(r'PART "([^"]+)"', b)
    cands = set(re.findall(r'^\[([^\]]+)\]', b, re.M))
    questions[qid] = (parts, cands)

ok = True
for qid, (parts, cands) in questions.items():
    path = OUT + qid + '.json'
    try:
        data = json.load(open(path, encoding='utf-8'))
    except Exception as e:
        print('PARSE FAIL', qid, e); ok = False; continue
    if list(data.keys()) != parts:
        print('PART MISMATCH', qid, list(data.keys()), parts); ok = False
    total = 0
    empty = []
    for label, pts in data.items():
        if not pts:
            empty.append(label)
        for p in pts:
            total += 1
            of = p.get('of', [])
            k = p.get('k')
            if not isinstance(k, int) or not (1 <= k <= len(of)):
                print('BAD K', qid, label, p); ok = False
            for i in of:
                if i not in cands:
                    print('BAD ID', qid, label, i); ok = False
    print(qid, 'parts', len(parts), 'points', total, 'empty', empty)
print('ALL OK' if ok else 'PROBLEMS')
