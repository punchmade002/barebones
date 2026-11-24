import json, re, sys
BASE = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags'
BATCH = BASE + '/batches/batch-60.txt'
text = open(BATCH, encoding='utf-8').read()
blocks = text.split('\n====')
for qid in ['geography-pp-2021-higher-q108', 'geography-pp-2021-higher-q109']:
    # candidates for this question
    qsec = [b for b in re.split(r'={5,}', text) if ('QUESTION ' + qid + ' ') in b][0]
    labels = re.findall(r'^PART "([^"]+)"', qsec, re.M)
    cands = set(re.findall(r'^\[([^\]]+)\]', qsec, re.M))
    data = json.load(open(f'{BASE}/out/{qid}.json', encoding='utf-8'))
    assert list(data.keys()) == labels, (qid, list(data.keys()), labels)
    total = 0
    errs = []
    for lab, mps in data.items():
        for mp in mps:
            total += 1
            if not (1 <= mp['k'] <= len(mp['of'])): errs.append((lab, mp))
            for i in mp['of']:
                if i not in cands: errs.append((lab, 'bad id', i))
    empty = [l for l, m in data.items() if not m]
    print(qid, 'parts', len(labels), 'marking points', total, 'empty', empty, 'errors', errs)
