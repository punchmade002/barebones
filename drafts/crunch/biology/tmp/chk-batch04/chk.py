import json, re, sys
base = '/Users/gabrielwhelan/barebones/drafts/crunch/biology/exam-tags/'
q = sys.argv[1]
pk = open(base + f'packages/{q}.txt').read()
ids = set(re.findall(r'^\[([^\]]+)\]', pk, re.M))
parts = re.findall(r'^PART (\S+) ', pk, re.M)
d = json.load(open(base + f'out/{q}.json'))
print(q, list(d) == parts, len(parts), sum(len(v) for v in d.values()), [k for k, v in d.items() if not v])
for k, v in d.items():
    for m in v:
        assert 1 <= m['k'] <= len(m['of']), (k, m)
        for i in m['of']:
            assert i in ids, (k, i)
