import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
txt=open(P+'packs/geo-mapwork-s1.t2g4.txt').read()
tgt=re.findall(r'^\[(geo-mapwork-s1\.[^\]]+)\]',txt,re.M)
cand=set(re.findall(r'^\[(geo-graph-skills-s1\.[^\]]+)\]',txt,re.M))
L={'geo-mapwork-s1.37.b':[('geo-graph-skills-s1.16.b','helpful','statistical maps overview')],
'geo-mapwork-s1.37.0':[('geo-graph-skills-s1.16.5','helpful','isoline map type')],
'geo-mapwork-s1.37.1':[('geo-graph-skills-s1.16.b','helpful','statistical map types taught there')]}
out={}
for t in tgt:
    out[t]={'needs':[{'id':i,'strength':s,'why':w,'confidence':'high'} for i,s,w in L.get(t,[])]}
for v in out.values():
    for n in v['needs']: assert n['id'] in cand
json.dump(out,open(P+'point-links/geo-mapwork-s1.t2g4.json','w'),indent=1)
print(len(tgt),len(set(tgt)),sum(len(v['needs']) for v in out.values()))
