import json, re, sys

BATCH = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-108.txt'
OUT = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'

text = open(BATCH, encoding='utf-8').read()
blocks = text.split('=' * 40)
report = []
ok = True
for block in blocks:
    m = re.search(r'^QUESTION (\S+)', block, re.M)
    if not m:
        continue
    qid = m.group(1)
    parts = re.findall(r'^PART "([^"]+)"', block, re.M)
    cands = set(re.findall(r'^\[([^\]]+)\]', block, re.M))
    data = json.load(open(OUT + qid + '.json', encoding='utf-8'))
    if list(data.keys()) != parts:
        ok = False
        print('PART MISMATCH', qid, list(data.keys()), parts)
    total = 0
    empty = []
    for label, mps in data.items():
        if not mps:
            empty.append(label)
        for mp in mps:
            total += 1
            if not (1 <= mp['k'] <= len(mp['of'])):
                ok = False
                print('BAD K', qid, label, mp)
            for pid in mp['of']:
                if pid not in cands:
                    ok = False
                    print('BAD ID', qid, label, pid)
    report.append((qid, len(parts), total, empty))
for r in report:
    print(r)
print('OK' if ok else 'FAILED')
