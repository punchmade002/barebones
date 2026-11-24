import json,re,sys
q=sys.argv[1]
d='/Users/gabrielwhelan/barebones/drafts/crunch/biology/exam-tags/'
t=open(d+'packages/'+q+'.txt').read()
ids=set(re.findall(r'^\[([^\]]+)\]',t,re.M))
parts=re.findall(r'^PART (\S+) ',t,re.M)
j=json.load(open(d+'out/'+q+'.json'))
assert list(j)==parts,(list(j),parts)
n=0;e=[]
for p,l in j.items():
    if not l:e.append(p)
    for m in l:
        n+=1
        assert 1<=m['k']<=len(m['of']),(p,m)
        for i in m['of']:assert i in ids,(p,i)
print(q,len(parts),n,e)
