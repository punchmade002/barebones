import json,re,sys
q=sys.argv[1]
base='/Users/gabrielwhelan/barebones/drafts/crunch/biology/exam-tags/'
t=open(base+'packages/'+q+'.txt').read()
ids=set(re.findall(r'^\[([^\]]+)\]',t,re.M))
parts=re.findall(r'^PART (\S+) \(',t,re.M)
d=json.load(open(base+'out/'+q+'.json'))
assert list(d)==parts,(list(d),parts)
n=0
for p,v in d.items():
    for m in v:
        n+=1
        assert 1<=m['k']<=len(m['of']),p
        for i in m['of']: assert i in ids,(p,i)
print(len(parts),n,[p for p,v in d.items() if not v])
