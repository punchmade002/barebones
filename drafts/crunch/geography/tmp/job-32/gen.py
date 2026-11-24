import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
pk=open(P+'packs/geo-mapwork-s1.t1g4.txt').read()
t,c=pk.split('CANDIDATES')
targets=re.findall(r'^\[(geo-mapwork-s1\.[^\]]+)\]',t,re.M)
cands=set(re.findall(r'^\[([^\]]+)\]',c,re.M))
G='geo-graph-skills-s1.'
L={ # every other target judged: no candidate link
 'geo-mapwork-s1.0.1':[(G+'0.0','helpful','reading the key or legend','low')],
 'geo-mapwork-s1.5.0':[(G+'5.4','helpful','rounding to one decimal place','low')],
 'geo-mapwork-s1.11.0':[(G+'10.3','helpful','gradient shows steepness as rate','low')],
 'geo-mapwork-s1.12.2':[(G+'6.2','helpful','labelled horizontal and vertical axes','low')],
 'geo-mapwork-s1.12.3':[(G+'6.5','helpful','plotting values accurately','low')],
 'geo-mapwork-s1.12.4':[(G+'6.1','helpful','title says what data shows','low')],
 'geo-mapwork-s1.13.0':[(G+'0.0','helpful','reading axes, labels and units','high')],
 'geo-mapwork-s1.13.3':[(G+'0.1','helpful','reading a value off the axis','high')],
}
out={}
for i in targets:
    out[i]={"needs":[{"id":a,"strength":b,"why":w,"confidence":cf} for a,b,w,cf in L.get(i,[])]}
assert all(n['id'] in cands for v in out.values() for n in v['needs'])
json.dump(out,open(P+'point-links/geo-mapwork-s1.t1g4.json','w'),indent=1)
r=json.load(open(P+'point-links/geo-mapwork-s1.t1g4.json'))
print(len(r),len(targets)==len(set(targets)),sum(len(v['needs']) for v in r.values()),sum(n['confidence']=='low' for v in r.values() for n in v['needs']))
