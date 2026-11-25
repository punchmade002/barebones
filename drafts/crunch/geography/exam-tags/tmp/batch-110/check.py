import json, re, sys

BATCH = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-110.txt'
OUT = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'

text = open(BATCH, encoding='utf-8').read()
blocks = [b for b in text.split('\n====') if b.strip()]
ok = True
for block in re.split(r'\n=+\n', text):
    m = re.search(r'QUESTION (\S+)', block)
    if not m:
        continue
    qid = m.group(1)
    cands = set(re.findall(r'^\[([^\]]+)\]', block, re.M))
    parts = re.findall(r'^PART "([^"]+)"', block, re.M)
    try:
        data = json.load(open(OUT + qid + '.json', encoding='utf-8'))
    except Exception as e:
        print(qid, 'PARSE FAIL', e); ok = False; continue
    if list(data.keys()) != parts:
        print(qid, 'PART MISMATCH', list(data.keys()), parts); ok = False
    total = 0
    empty = []
    for label, pts in data.items():
        if not pts:
            empty.append(label)
        for p in pts:
            total += 1
            of = p['of']
            if not (1 <= p['k'] <= len(of)):
                print(qid, label, 'BAD K', p); ok = False
            for i in of:
                if i not in cands:
                    print(qid, label, 'UNKNOWN ID', i); ok = False
    print(qid, 'parts', len(parts), 'points', total, 'empty', empty)
print('OK' if ok else 'FAILURES')
