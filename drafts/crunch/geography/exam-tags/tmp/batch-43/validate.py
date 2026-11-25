import json, re, sys
BASE = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags'
batch = open(BASE + '/batches/batch-43.txt', encoding='utf-8').read()
blocks = re.split(r'\n=+\n', batch)
ok = True
for blk in blocks:
    m = re.search(r'QUESTION (\S+)', blk)
    if not m:
        continue
    qid = m.group(1)
    cand_part = blk.split('CANDIDATES (shortlist):')[1]
    cands = set(re.findall(r'^\[([^\]]+)\]', cand_part, re.M))
    labels = re.findall(r'^PART "([^"]+)"', blk, re.M)
    data = json.load(open(f'{BASE}/out/{qid}.json', encoding='utf-8'))
    keys = list(data.keys())
    if keys != labels:
        print(qid, 'LABEL MISMATCH', keys, labels); ok = False
    n = 0
    for lab, pts in data.items():
        for p in pts:
            n += 1
            if not (1 <= p['k'] <= len(p['of'])):
                print(qid, lab, 'bad k', p); ok = False
            for i in p['of']:
                if i not in cands:
                    print(qid, lab, 'bad id', i); ok = False
            if len(p['of']) > 2:
                print(qid, lab, 'more than 2 ids', p); ok = False
    empties = [l for l, p in data.items() if not p]
    print(qid, 'parts', len(data), 'points', n, 'empty', empties)
print('OK' if ok else 'FAILURES')
