import json, re, sys

BATCH = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-45.txt'
OUT = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'

text = open(BATCH, encoding='utf-8').read()
questions = [q for q in text.split('\n' + '=' * 40 + '\n')]
ok = True
for block in questions:
    m = re.search(r'^QUESTION (\S+)', block, re.M)
    if not m:
        continue
    qid = m.group(1)
    cands = set(re.findall(r'^\[([^\]]+)\]', block, re.M))
    labels = re.findall(r'^PART "([^"]+)"', block, re.M)
    try:
        data = json.load(open(OUT + qid + '.json', encoding='utf-8'))
    except Exception as e:
        print(qid, 'PARSE FAIL', e); ok = False; continue
    if list(data.keys()) != labels:
        print(qid, 'LABEL MISMATCH', list(data.keys()), labels); ok = False
    total = 0
    empty = []
    for lab, mps in data.items():
        if not mps:
            empty.append(lab)
        for mp in mps:
            total += 1
            of = mp['of']
            if not (1 <= mp['k'] <= len(of)):
                print(qid, lab, 'BAD K', mp); ok = False
            if len(of) > 2:
                print(qid, lab, 'TOO MANY IDS', mp); ok = False
            for i in of:
                if i not in cands:
                    print(qid, lab, 'UNKNOWN ID', i); ok = False
    print(qid, 'parts', len(labels), 'marking points', total, 'empty', empty)
print('ALL OK' if ok else 'PROBLEMS')
