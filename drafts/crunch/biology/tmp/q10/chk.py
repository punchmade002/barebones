import json,re,sys
q=sys.argv[1]
d=json.load(open(f'out/{q}.json'))
t=open(f'packages/{q}.txt').read()
parts=re.findall(r'^PART (\S+) ',t,re.M)
assert list(d)==parts,(list(d),parts)
for p,v in d.items():
    for m in v:
        assert 1<=m['k']<=len(m['of'])
        for i in m['of']: assert f'[{i}]' in t,i
print(q,len(parts),sum(len(v) for v in d.values()),[p for p,v in d.items() if not v])
