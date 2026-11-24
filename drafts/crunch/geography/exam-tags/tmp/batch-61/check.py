import json, re, sys

BATCH = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-61.txt'
OUT = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'

text = open(BATCH, encoding='utf-8').read()
blocks = [b for b in text.split('=' * 40) if 'QUESTION ' in b]
ok = True
for b in blocks:
    qid = re.search(r'QUESTION (\S+)', b).group(1)
    labels = re.findall(r'^PART "([^"]+)"', b, re.M)
    cands = set(re.findall(r'^\[([^\]]+)\]', b, re.M))
    path = OUT + qid + '.json'
    data = json.load(open(path, encoding='utf-8'))
    if list(data.keys()) != labels:
        ok = False
        print(qid, 'label mismatch', list(data.keys()), labels)
    total = 0
    empty = []
    for lab, mps in data.items():
        if not mps:
            empty.append(lab)
        for mp in mps:
            total += 1
            of = mp['of']
            if not (1 <= mp['k'] <= len(of)):
                ok = False
                print(qid, lab, 'bad k', mp)
            if len(of) > 2:
                ok = False
                print(qid, lab, 'too many ids', mp)
            for i in of:
                if i not in cands:
                    ok = False
                    print(qid, lab, 'id not in candidates', i)
    print(qid, 'parts', len(labels), 'marking points', total, 'empty', empty)
print('OK' if ok else 'FAILURES')
