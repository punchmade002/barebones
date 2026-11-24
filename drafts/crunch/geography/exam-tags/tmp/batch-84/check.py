import json, re, sys
batch = open('/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-84.txt').read()
blocks = batch.split('=' * 40)
out = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'
ok = True
for b in blocks:
    m = re.search(r'QUESTION (\S+)', b)
    if not m:
        continue
    qid = m.group(1)
    cands = set(re.findall(r'^\[(geo-[^\]]+)\]', b, re.M))
    parts = re.findall(r'^PART "([^"]+)"', b, re.M)
    data = json.load(open(out + qid + '.json'))
    if list(data.keys()) != parts:
        print('PART MISMATCH', qid, list(data.keys()), parts); ok = False
    for p, mps in data.items():
        for mp in mps:
            if not (1 <= mp['k'] <= len(mp['of'])):
                print('BAD K', qid, p, mp); ok = False
            for i in mp['of']:
                if i not in cands:
                    print('BAD ID', qid, p, i); ok = False
    print(qid, 'parts', len(parts), 'MPs', sum(len(v) for v in data.values()), 'empty', [p for p, v in data.items() if not v])
print('OK' if ok else 'FAILED')
