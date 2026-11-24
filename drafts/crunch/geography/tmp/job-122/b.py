import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
H,E='helpful','essential'
d={
"0.b":(1,[]),
"0.0":(1,[L("geo-rivers-s1.0.2",H,"tributary defined")]),
"0.1":(2,[L("geo-rivers-s1.1.b",H,"long profile, concave slope"),L("geo-rivers-s1.2.1",H,"energy used for erosion and transport")]),
"0.2":(1,[L("geo-rivers-s2.0.1",E,"graded profile being upset")]),
"1.b":(1,[L("geo-rivers-s2.0.b",H,"base level"),L("geo-rivers-s1.2.3",H,"vertical erosion")]),
"1.0":(1,[L("geo-glaciation-s2.4.1",E,"eustatic change defined")]),
"1.1":(1,[L("geo-glaciation-s2.2.1",E,"isostatic rebound after ice melts")]),
"1.2":(1,[L("geo-glaciation-s2.0.0",H,"crustal uplift from endogenetic forces","low")]),
"1.3":(1,[L("geo-rivers-s1.2.0",H,"energy depends on discharge")]),
"2.b":(1,[L("geo-rivers-s1.0.1",H,"river mouth")]),
"2.0":(1,[L("geo-rivers-s1.2.5",E,"headward erosion")]),
"2.1":(1,[L("geo-rivers-s2.0.1",H,"graded section")]),
"2.2":(1,[L("geo-rivers-s2.2.1",H,"two graded sections")]),
"3.b":(1,[L("geo-rivers-s1.1.b",H,"long profile")]),
"3.0":(1,[L("geo-rivers-s2.0.1",H,"graded section")]),
"3.1":(1,[L("geo-rivers-s2.3.0",E,"new and old graded sections")]),
"3.2":(1,[L("geo-rivers-s1.8.b",H,"waterfall")]),
"3.3":(1,[L("geo-rivers-s2.3.1",H,"knickpoint")]),
"3.4":(1,[L("geo-rivers-s2.3.3",H,"knickpoint retreating upstream")]),
"3.5":(1,[L("geo-rivers-s2.3.1",H,"knickpoint at junction")]),
"4.b":(1,[L("geo-rivers-s1.10.b",E,"meanders"),L("geo-rivers-s1.12.b",H,"floodplain")]),
"4.0":(2,[L("geo-rivers-s2.4.b",H,"meanders cut down"),L("geo-rivers-s1.2.4",H,"lateral erosion")]),
"4.1":(1,[L("geo-rivers-s2.4.b",H,"meanders cut down")]),
"4.2":(1,[L("geo-rivers-s2.4.1",E,"entrenched meanders")]),
"4.3":(1,[L("geo-rivers-s2.4.b",H,"incised meanders")]),
"4.4":(1,[L("geo-rivers-s2.4.b",E,"meander cut down into land")]),
"5.b":(1,[L("geo-rivers-s1.12.b",H,"floodplain")]),
"5.0":(1,[L("geo-rivers-s2.5.b",E,"river terraces")]),
"5.1":(1,[L("geo-rivers-s2.5.0",H,"paired terraces contrast"),L("geo-rivers-s1.2.4",H,"lateral erosion","low")]),
"5.2":(1,[L("geo-rivers-s2.5.b",H,"river terraces")]),
"5.3":(1,[L("geo-rivers-s2.5.0",E,"paired terraces")]),
"6.b":(1,[L("geo-rivers-s2.1.2",H,"tectonic uplift")]),
"6.0":(1,[L("geo-rivers-s2.6.b",H,"gorge by deep incision")]),
"6.1":(1,[L("geo-rivers-s2.6.0",H,"gorge from uplift")]),
"7.b":(1,[L("geo-rivers-s2.3.b",H,"knickpoints as marks")]),
"7.0":(1,[L("geo-rivers-s2.3.b",E,"knickpoint on long profile")]),
"7.1":(1,[L("geo-rivers-s2.5.b",E,"river terraces")]),
"7.2":(2,[L("geo-rivers-s2.3.b",H,"knickpoints"),L("geo-rivers-s2.4.b",H,"incised meanders"),L("geo-rivers-s2.5.b",H,"river terraces"),L("geo-rivers-s2.6.b",H,"gorges")]),
"8.b":(1,[L("geo-rivers-s2.0.b",H,"base level")]),
"8.0":(1,[L("geo-glaciation-s2.7.0",H,"ria defined"),L("geo-rivers-s1.0.7",H,"estuary")]),
"8.1":(1,[L("geo-glaciation-s2.6.0",H,"raised beach formation")]),
"8.2":(2,[L("geo-glaciation-s2.8.0",H,"north Ireland more rebound"),L("geo-glaciation-s2.6.6",H,"Malin Head raised beaches","low")]),
}
out={}
for k,(c,n) in d.items():
    out["geo-rivers-s2."+k]={"cost":c,"needs":n}
json.dump(out,open(P+'point-links/geo-rivers-s2.t1g1.json','w'),indent=1)
txt=open(P+'packs/geo-rivers-s2.t1g1.txt').read()
ids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
tg=re.findall(r'^\[(geo-rivers-s2\.[^\]]+)\]',txt.split('CANDIDATES')[0],re.M)
assert sorted(tg)==sorted(out) and len(tg)==len(set(tg))
assert all(n['id'] in ids and n['id']!=k for k,v in out.items() for n in v['needs'])
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
