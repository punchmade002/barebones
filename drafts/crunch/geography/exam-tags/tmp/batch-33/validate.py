import json, re, sys
BATCH = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-33.txt'
OUT = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'
text = open(BATCH, encoding='utf-8').read()
blocks = [b for b in text.split('\n====') if b.strip()]
ok = True
for b in re.split(r'\n=+\n', text):
    m = re.search(r'QUESTION (\S+)', b)
    if not m:
        continue
    qid = m.group(1)
    labels = re.findall(r'^PART "([^"]+)"', b, re.M)
    cands = set(re.findall(r'^\[([^\]]+)\]', b, re.M))
    data = json.load(open(OUT + qid + '.json', encoding='utf-8'))
    if list(data.keys()) != labels:
        print(qid, 'label mismatch', list(data.keys()), labels); ok = False
    for lab, mps in data.items():
        for mp in mps:
            if not (1 <= mp['k'] <= len(mp['of'])):
                print(qid, lab, 'bad k', mp); ok = False
            for i in mp['of']:
                if i not in cands:
                    print(qid, lab, 'unknown id', i); ok = False
    print(qid, 'parts', len(labels), 'mps', sum(len(v) for v in data.values()), 'empty', [k for k, v in data.items() if not v])
print('OK' if ok else 'FAIL')
