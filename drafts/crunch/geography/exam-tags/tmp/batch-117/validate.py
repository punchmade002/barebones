import json, re, sys

BASE = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags'
BATCH = BASE + '/batches/batch-117.txt'
OUT = BASE + '/out/'

text = open(BATCH, encoding='utf-8').read()
blocks = [b for b in text.split('\n====') if b.strip()]
ok = True
for block in re.split(r'\n=+\n', text):
    if 'QUESTION ' not in block:
        continue
    qid = re.search(r'QUESTION (\S+)', block).group(1)
    labels = re.findall(r'^PART "([^"]+)"', block, re.M)
    cands = set(re.findall(r'^\[([^\]]+)\]', block, re.M))
    try:
        data = json.load(open(OUT + qid + '.json', encoding='utf-8'))
    except Exception as e:
        print(qid, 'PARSE FAIL', e); ok = False; continue
    if list(data.keys()) != labels:
        print(qid, 'LABEL MISMATCH', list(data.keys()), labels); ok = False
    for lab, pts in data.items():
        for i, p in enumerate(pts):
            if not (1 <= p['k'] <= len(p['of'])):
                print(qid, lab, i, 'bad k'); ok = False
            for idv in p['of']:
                if idv not in cands:
                    print(qid, lab, i, 'id not in candidates:', idv); ok = False
    print(qid, {lab: len(p) for lab, p in data.items()},
          'empty:', [lab for lab, p in data.items() if not p])
print('ALL OK' if ok else 'FAILURES')
