import json, re, sys

BATCH = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-47.txt'
OUT = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'

text = open(BATCH, encoding='utf-8').read()
blocks = text.split('====')
ok = True
for block in blocks:
    m = re.search(r'QUESTION (\S+)', block)
    if not m:
        continue
    qid = m.group(1)
    labels = re.findall(r'^PART "([^"]+)"', block, re.M)
    cands = set(re.findall(r'^\[([^\]]+)\]', block, re.M))
    path = OUT + qid + '.json'
    try:
        data = json.load(open(path, encoding='utf-8'))
    except Exception as e:
        print('PARSE FAIL', qid, e); ok = False; continue
    if list(data.keys()) != labels:
        print('LABEL MISMATCH', qid, list(data.keys()), labels); ok = False
    total = 0
    for part, mps in data.items():
        for mp in mps:
            total += 1
            of = mp['of']
            if not (1 <= mp['k'] <= len(of)):
                print('K BAD', qid, part, mp); ok = False
            if len(of) > 2:
                print('TOO MANY IDS', qid, part, mp); ok = False
            for i in of:
                if i not in cands:
                    print('UNKNOWN ID', qid, part, i); ok = False
    empty = [p for p, mps in data.items() if not mps]
    print(qid, 'parts', len(data), 'marking points', total, 'empty', empty)
    marks = dict((m_[0], int(m_[1])) for m_ in re.findall(r'PART "([^"]+)" \((\d+) marks\)', block))
    for part, mps in data.items():
        if marks.get(part, 0) >= 20 and len(mps) > marks[part] // 2:
            print('OVER SRP CAP', qid, part, len(mps)); ok = False
print('ALL OK' if ok else 'FAILURES')
