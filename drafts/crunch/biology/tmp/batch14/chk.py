import json,re,sys
b='/Users/gabrielwhelan/barebones/drafts/crunch/biology/exam-tags/'
q=sys.argv[1]
t=open(b+'packages/'+q+'.txt').read()
ids=set(re.findall(r'^\[([^\]]+)\]',t,re.M))
parts=re.findall(r'^PART (\S+) ',t,re.M)
d=json.load(open(b+'out/'+q+'.json'))
assert list(d)==parts,(list(d),parts)
n=0
for p,l in d.items():
    for m in l:
        assert 1<=m['k']<=len(m['of']),p
        assert all(i in ids for i in m['of']),(p,[i for i in m['of'] if i not in ids])
        n+=1
print(q,len(parts),n,[p for p,l in d.items() if not l])
