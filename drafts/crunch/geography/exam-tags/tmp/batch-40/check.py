import json, re, sys

BATCH = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-40.txt'
OUT = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'

text = open(BATCH, encoding='utf-8').read()
blocks = [b for b in text.split('=' * 40) if 'QUESTION ' in b]
ok = True
for b in blocks:
    qid = re.search(r'QUESTION (\S+)', b).group(1)
    labels = re.findall(r'^PART "([^"]+)"', b, re.M)
    cand_part = b.split('CANDIDATES (shortlist):')[1]
    cands = set(re.findall(r'^\[([^\]]+)\]', cand_part, re.M))
    data = json.load(open(OUT + qid + '.json', encoding='utf-8'))
    if list(data.keys()) != labels:
        print(qid, 'label mismatch', list(data.keys()), labels); ok = False
    n_points = 0
    for lab, pts in data.items():
        for p in pts:
            n_points += 1
            if not (1 <= p['k'] <= len(p['of'])):
                print(qid, lab, 'bad k', p); ok = False
            for i in p['of']:
                if i not in cands:
                    print(qid, lab, 'unknown id', i); ok = False
    empty = [l for l, p in data.items() if not p]
    print(qid, 'parts', len(data), 'points', n_points, 'empty', empty)
print('OK' if ok else 'FAIL')
