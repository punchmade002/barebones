import json, re, sys
BATCH = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-74.txt'
OUT = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'
text = open(BATCH, encoding='utf-8').read()
blocks = text.split('=' * 40)
ok = True
for b in blocks:
    m = re.search(r'QUESTION (\S+)', b)
    if not m:
        continue
    qid = m.group(1)
    cands = set(re.findall(r'^\[([^\]]+)\]', b, re.M))
    labels = re.findall(r'^PART "([^"]+)"', b, re.M)
    data = json.load(open(OUT + qid + '.json', encoding='utf-8'))
    keys = list(data.keys())
    if keys != labels:
        print(qid, 'label mismatch', keys, labels); ok = False
    n = 0
    for key, mps in data.items():
        if key not in labels:
            print(qid, 'unknown key', key); ok = False
        for mp in mps:
            n += 1
            of = mp['of']
            if not (1 <= mp['k'] <= len(of)):
                print(qid, key, 'bad k', mp); ok = False
            if len(of) > 2:
                print(qid, key, 'too many ids', mp); ok = False
            for i in of:
                if i not in cands:
                    print(qid, key, 'id not in candidates', i); ok = False
    print(qid, 'parts', len(keys), 'marking points', n, 'empty', [k for k, v in data.items() if not v])
print('ALL OK' if ok else 'PROBLEMS')
