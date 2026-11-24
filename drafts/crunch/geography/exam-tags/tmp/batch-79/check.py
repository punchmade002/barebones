import json, re, sys
BATCH = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-79.txt'
OUT = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'
text = open(BATCH, encoding='utf-8').read()
# split questions
blocks = re.split(r'^=+$', text, flags=re.M)
ok = True
for b in blocks:
    m = re.search(r'^QUESTION (\S+)', b, re.M)
    if not m:
        continue
    qid = m.group(1)
    parts = re.findall(r'^PART "([^"]+)"', b, re.M)
    cands = set(re.findall(r'^\[([^\]]+)\]', b, re.M))
    data = json.load(open(OUT + qid + '.json', encoding='utf-8'))
    if list(data.keys()) != parts:
        print('PART MISMATCH', qid, list(data.keys()), parts); ok = False
    n = 0
    for p, mps in data.items():
        for mp in mps:
            n += 1
            k, of = mp['k'], mp['of']
            if not (1 <= k <= len(of)):
                print('BAD K', qid, p, mp); ok = False
            for i in of:
                if i not in cands:
                    print('BAD ID', qid, p, i); ok = False
    empty = [p for p, v in data.items() if not v]
    print(qid, 'parts', len(parts), 'marking points', n, 'empty', empty)
print('OK' if ok else 'FAILED')
