import json, re, sys, os

BATCH = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-02.txt'
OUT = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out'

text = open(BATCH, encoding='utf-8').read()
blocks = [b for b in text.split('=' * 40) if 'QUESTION' in b]
problems = []
summary = []
for b in blocks:
    qid = re.search(r'QUESTION (\S+)', b).group(1)
    labels = re.findall(r'^PART "(.+?)"', b, re.M)
    cands = set(re.findall(r'^\[([^\]]+)\]', b, re.M))
    path = os.path.join(OUT, qid + '.json')
    try:
        data = json.load(open(path, encoding='utf-8'))
    except Exception as e:
        problems.append(f'{qid}: parse error {e}')
        continue
    if list(data.keys()) != labels:
        problems.append(f'{qid}: keys {list(data.keys())} != labels {labels}')
    points = 0
    empty = []
    for lab, pts in data.items():
        if not pts:
            empty.append(lab)
        for p in pts:
            points += 1
            of = p['of']
            if not (1 <= p['k'] <= len(of)):
                problems.append(f'{qid} {lab}: bad k {p}')
            for i in of:
                if i not in cands:
                    problems.append(f'{qid} {lab}: id not in candidates {i}')
    summary.append(f'{qid} | parts {len(labels)} | marking points {points} | empty {empty}')
print('\n'.join(summary))
print('PROBLEMS:' if problems else 'NO PROBLEMS')
print('\n'.join(problems))
