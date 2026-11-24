import json,re,sys
b='/Users/gabrielwhelan/barebones/drafts/crunch/biology/exam-tags/'
q=sys.argv[1]
t=open(b+'packages/'+q+'.txt').read()
parts=re.findall(r'^PART (\S+) ',t,re.M)
ids=set(re.findall(r'^\[([^\]]+)\]',t,re.M))
d=json.load(open(b+'out/'+q+'.json'))
assert list(d)==parts,(list(d),parts)
n=0
for p,v in d.items():
  for m in v:
    assert 1<=m['k']<=len(m['of']),p
    for i in m['of']: assert i in ids,(p,i)
    n+=1
print(q,len(parts),n,[p for p in d if not d[p]])
