import json,re,sys
q=sys.argv[1];b='/Users/gabrielwhelan/barebones/drafts/crunch/biology/exam-tags/'
t=open(b+'packages/'+q+'.txt').read()
ids=set(re.findall(r'^\[([^\]]+)\]',t,re.M));parts=re.findall(r'^PART (\S+) ',t,re.M)
d=json.load(open(b+'out/'+q+'.json'))
assert list(d)==parts,(set(parts)^set(d))
bad=[(p,i) for p,v in d.items() for m in v for i in m['of'] if i not in ids]
badk=[p for p,v in d.items() for m in v if not 1<=m['k']<=len(m['of'])]
print(len(parts),sum(len(v) for v in d.values()),[p for p,v in d.items() if not v],bad,badk)
