import json,re,sys
b='/Users/gabrielwhelan/barebones/drafts/crunch/biology/exam-tags/'
q=sys.argv[1]
t=open(b+'packages/'+q+'.txt').read()
parts=re.findall(r'^PART (.+?) \((\d+) marks\)',t,re.M)
ids=set(re.findall(r'^\[([^\]]+)\]',t,re.M))
d=json.load(open(b+'out/'+q+'.json'))
assert list(d)==[p[0] for p in parts],(list(d),parts)
n=0
for k,v in d.items():
    for m in v:
        assert 1<=m['k']<=len(m['of']) and all(i in ids for i in m['of']),(k,m); n+=1
print(q,len(d),n,[k for k,v in d.items() if not v])
