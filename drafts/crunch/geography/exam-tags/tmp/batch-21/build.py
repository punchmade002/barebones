import json, re, sys

BATCH = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/batches/batch-21.txt'
OUT = '/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/'
PREFIX = 'geo-option-atmosphere-ocean-'

# Parse candidate ids per question from the batch file
text = open(BATCH, encoding='utf-8').read()
blocks = text.split('=' * 40)
cands = {}
for b in blocks:
    m = re.search(r'QUESTION (\S+)', b)
    if not m:
        continue
    qid = m.group(1)
    ids = set(re.findall(r'^\[([^\]]+)\]', b, re.M))
    cands[qid] = ids

def sid(s):
    return PREFIX + s

# Each question: part label -> list of marking points; each point = (list of short ids, k)
Q = {}

Q['geography-pp-2017-higher-q122'] = {
 '22': [
  (['s3.36.b']),
  (['s3.3.0', 's3.3.1']),
  (['s3.9.0']),
  (['s3.8.1', 's3.8.2']),
  (['s3.5.0']),
  (['s3.8.0']),
  (['s3.4.0', 's3.4.1']),
  (['s3.6.2', 's3.5.3']),
  (['s3.10.0', 's3.10.1']),
  (['s3.12.3']),
  (['s3.27.b', 's3.27.1']),
  (['s3.28.b', 's3.28.5']),
  (['s3.28.5']),
  (['s3.29.0', 's3.29.2']),
  (['s3.24.1', 's3.25.b']),
  (['s3.31.0']),
  (['s3.36.0']),
  (['s3.36.1', 's3.33.1']),
  (['s3.31.1']),
  (['s3.35.0', 's3.35.1']),
  (['s3.31.2']),
  (['s3.32.4']),
  (['s3.36.3']),
  (['s3.33.4']),
  (['s3.34.1', 's3.34.0']),
  (['s3.34.2']),
  (['s3.32.3']),
  (['s3.14.3']),
  (['s3.31.3']),
 ]
}

Q['geography-pp-2017-higher-q123'] = {
 '23': [
  (['s1.18.0']),
  (['s1.18.1']),
  (['s1.18.3', 's1.18.4']),
  (['s1.18.2']),
  (['s1.26.2', 's1.26.0']),
  (['s1.28.4']),
  (['s1.28.6']),
  (['s1.19.0']),
  (['s1.19.1']),
  (['s1.19.1']),
  (['s1.19.2']),
  (['s1.19.4']),
  (['s1.19.2', 's1.28.2']),
  (['s1.28.0', 's1.28.1']),
  (['s1.20.0']),
  (['s1.20.1']),
  (['s1.20.2']),
  (['s1.21.0', 's1.21.1']),
  (['s1.28.5']),
  (['s1.26.0', 's1.28.3']),
  (['s1.28.3', 's1.28.2']),
  (['s1.22.0']),
  (['s1.22.0']),
  (['s1.22.1']),
  (['s1.22.2']),
  (['s1.22.3', 's1.22.4']),
  (['s1.24.0']),
 ]
}

Q['geography-pp-2017-higher-q124'] = {
 '24': [
  (['s5.8.b']),
  (['s5.8.0', 's5.8.b']),
  (['s5.8.1', 's5.8.2']),
  (['s5.8.1']),
  (['s5.10.1']),
  (['s5.10.2']),
  (['s5.14.4', 's5.18.1']),
  (['s5.10.0']),
  (['s5.9.0']),
  (['s5.9.1']),
  (['s5.9.2', 's5.10.3']),
  (['s5.9.2']),
  (['s5.9.2', 's5.9.b']),
  (['s5.10.0']),
  (['s5.9.2', 's5.18.4']),
  (['s5.10.0']),
  (['s5.10.4']),
  (['s5.15.4']),
  (['s5.10.3']),
  (['s5.9.3']),
  (['s5.9.4']),
  (['s5.9.5']),
 ]
}

ok = True
for qid, parts in Q.items():
    out = {}
    for label, points in parts.items():
        arr = []
        for pt in points:
            full = [sid(x) for x in pt]
            k = 1
            for f in full:
                if f not in cands[qid]:
                    print('BAD ID', qid, label, f)
                    ok = False
            arr.append({'k': k, 'of': full})
        out[label] = arr
    path = OUT + qid + '.json'
    if ok:
        with open(path, 'w', encoding='utf-8') as fh:
            json.dump(out, fh, ensure_ascii=False)
            fh.write('\n')
    # verify
    data = json.load(open(path, encoding='utf-8'))
    assert list(data.keys()) == list(parts.keys())
    for label, arr in data.items():
        for p in arr:
            assert 1 <= p['k'] <= len(p['of'])
            for i in p['of']:
                assert i in cands[qid], (qid, i)
    print(qid, 'parts', len(data), 'points', sum(len(v) for v in data.values()), 'empty', [k for k, v in data.items() if not v])
print('OK' if ok else 'FAILED')
