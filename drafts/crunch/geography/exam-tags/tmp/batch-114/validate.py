import json, re, sys

BATCH = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-114.txt'
OUT = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'

text = open(BATCH, encoding='utf-8').read()
blocks = [b for b in text.split('\n====') if b.strip()]
ok = True
for block in re.split(r'\n=+\n', text):
    m = re.search(r'QUESTION (\S+)', block)
    if not m:
        continue
    qid = m.group(1)
    parts = re.findall(r'^PART "([^"]+)"', block, re.M)
    cands = dict(re.findall(r'^\[([^\]]+)\] (.*)$', block, re.M))
    path = OUT + qid + '.json'
    try:
        data = json.load(open(path, encoding='utf-8'))
    except Exception as e:
        print(qid, 'PARSE FAIL', e); ok = False; continue
    if list(data.keys()) != parts:
        print(qid, 'LABEL MISMATCH', list(data.keys()), parts); ok = False
    total = 0; empty = []
    for label, mps in data.items():
        if not mps:
            empty.append(label)
        for mp in mps:
            total += 1
            of = mp['of']
            if not (1 <= mp['k'] <= len(of)):
                print(qid, label, 'BAD k', mp); ok = False
            if len(of) > 2:
                print(qid, label, 'more than 2 ids', mp); ok = False
            for i in of:
                if i not in cands:
                    print(qid, label, 'ID NOT IN CANDIDATES', i); ok = False
    print(qid, 'parts', len(parts), 'marking points', total, 'empty', empty)
print('ALL OK' if ok else 'PROBLEMS')
