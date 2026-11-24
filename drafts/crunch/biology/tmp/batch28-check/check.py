import json,re,sys
q=sys.argv[1]
d=json.load(open(f'out/{q}.json'))
t=open(f'packages/{q}.txt').read()
parts=re.findall(r'^PART (\S+) ',t,re.M)
ids=set(re.findall(r'^\[([^\]]+)\]',t,re.M))
assert list(d)==parts,(list(d),parts)
n=0
for p,l in d.items():
    for m in l:
        assert 1<=m['k']<=len(m['of']),p
        assert all(i in ids for i in m['of']),(p,m)
        n+=1
print(q,len(parts),n,[p for p,l in d.items() if not l])
