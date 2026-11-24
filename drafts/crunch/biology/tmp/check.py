import json,re,sys
q=sys.argv[1]
base='/Users/gabrielwhelan/barebones/drafts/crunch/biology/exam-tags/'
t=open(base+'packages/'+q+'.txt').read()
parts=re.findall(r'^PART (\S+) ',t,re.M)
ids=set(re.findall(r'^\[([^\]]+)\]',t,re.M))
d=json.load(open(base+'out/'+q+'.json'))
assert list(d)==parts,(list(d),parts)
mp=0;emp=[]
for p,l in d.items():
    if not l: emp.append(p)
    for m in l:
        mp+=1
        assert 1<=m['k']<=len(m['of']),p
        for i in m['of']: assert i in ids,(p,i)
print(q,len(parts),mp,emp)
