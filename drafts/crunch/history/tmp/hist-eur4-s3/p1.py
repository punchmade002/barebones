import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/history/'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
H,E='helpful','essential'
d={
"hist-eur4-s3.0.b":(1,[]),
"hist-eur4-s3.0.0":(2,[]),
"hist-eur4-s3.0.1":(1,[L("hist-eur4-s3.1.0",H,"uses Rákosi's Stalinist rule"),L("hist-eur4-s3.1.6",H,"New Course explained there")]),
"hist-eur4-s3.0.2":(1,[L("hist-eur4-s3.1.0",H,"Rákosi's Stalinist leadership")]),
"hist-eur4-s3.0.3":(2,[L("hist-eur4-s1.6.3",H,"the Warsaw Pact")]),
"hist-eur4-s3.0.4":(1,[L("hist-eur4-s3.4.3",H,"Kádár's government")]),
"hist-eur4-s3.0.5":(2,[L("hist-eur4-s3.4.2",H,"Pál Maléter")]),
"hist-eur4-s3.0.6":(1,[L("hist-eur4-s3.0.5",H,"the execution being commemorated")]),
"hist-eur4-s3.1.b":(1,[]),
"hist-eur4-s3.1.0":(1,[]),
"hist-eur4-s3.1.1":(1,[]),
"hist-eur4-s3.1.2":(1,[]),
"hist-eur4-s3.1.3":(1,[L("hist-eur4-s3.1.0",H,"Rákosi's leadership")]),
"hist-eur4-s3.1.4":(2,[]),
"hist-eur4-s3.1.5":(1,[]),
"hist-eur4-s3.1.6":(2,[L("hist-eur4-s3.0.1",H,"Nagy's New Course policies")]),
"hist-eur4-s3.1.7":(1,[L("hist-eur4-s3.1.0",H,"AVH under Rákosi")]),
"hist-eur4-s3.1.8":(1,[]),
"hist-eur4-s3.2.b":(1,[]),
"hist-eur4-s3.2.0":(2,[L("hist-eur4-s3.b" if False else "hist-eur4-s3.0.b",H,"Imre Nagy as reformer")]),
"hist-eur4-s3.2.1":(1,[L("hist-eur4-s3.2.0",H,"the demands being broadcast")]),
"hist-eur4-s3.2.2":(1,[L("hist-eur4-s3.1.7",H,"the AVH secret police")]),
"hist-eur4-s3.2.3":(1,[L("hist-eur4-s3.1.3",H,"Gerő as leader")]),
"hist-eur4-s3.2.4":(1,[]),
"hist-eur4-s3.3.b":(1,[]),
"hist-eur4-s3.3.0":(2,[L("hist-eur4-s3.2.0",H,"demand for Nagy's return")]),
"hist-eur4-s3.3.1":(1,[L("hist-eur4-s3.3.0",H,"Nagy's reinstatement as prime minister")]),
"hist-eur4-s3.3.2":(1,[]),
"hist-eur4-s3.3.3":(1,[L("hist-eur4-s1.6.3",H,"the Warsaw Pact")]),
"hist-eur4-s3.3.4":(2,[L("hist-eur4-s3.4.3",H,"Kádár's Soviet-backed government")]),
"hist-eur4-s3.3.5":(2,[]),
"hist-eur4-s3.3.6":(1,[L("hist-eur4-s3.1.7",H,"the AVH men attacked")]),
"hist-eur4-s3.3.7":(1,[L("hist-eur4-s3.1.5",H,"Mindszenty's 1949 jailing")]),
"hist-eur4-s3.3.8":(2,[L("hist-eur4-s3.3.3",H,"declaration of neutrality"),L("hist-eur4-s3.6.0",H,"the Suez crisis")]),
"hist-eur4-s3.4.b":(1,[]),
"hist-eur4-s3.4.0":(1,[]),
"hist-eur4-s3.4.1":(1,[]),
"hist-eur4-s3.4.2":(1,[]),
"hist-eur4-s3.4.3":(1,[]),
"hist-eur4-s3.4.4":(1,[L("hist-eur4-s3.4.1",E,"Nagy's refuge in the Yugoslav embassy")]),
"hist-eur4-s3.4.5":(1,[L("hist-eur4-s3.3.2",H,"workers' councils")]),
"hist-eur4-s3.5.b":(1,[]),
"hist-eur4-s3.5.0":(2,[]),
"hist-eur4-s3.5.1":(1,[]),
"hist-eur4-s3.5.2":(1,[L("hist-eur4-s3.4.3",H,"Kádár's government")]),
"hist-eur4-s3.5.3":(2,[L("hist-eur4-s3.4.4",H,"leaving the Yugoslav embassy"),L("hist-eur4-s3.4.2",H,"Maléter")]),
"hist-eur4-s3.5.4":(1,[L("hist-eur4-s3.4.3",H,"Kádár's regime")]),
"hist-eur4-s3.6.b":(1,[]),
"hist-eur4-s3.6.0":(2,[]),
"hist-eur4-s3.6.1":(1,[]),
"hist-eur4-s3.6.2":(1,[]),
"hist-eur4-s3.6.3":(1,[]),
"hist-eur4-s3.6.4":(1,[L("hist-eur4-s3.5.1",E,"refugees who fled to Austria")]),
"hist-eur4-s3.6.5":(1,[L("hist-eur4-s3.6.1",H,"Radio Free Europe broadcasts")]),
"hist-eur4-s3.6.6":(1,[]),
"hist-eur4-s3.7.b":(1,[]),
"hist-eur4-s3.7.0":(1,[L("hist-eur4-s1.6.3",H,"the Warsaw Pact")]),
"hist-eur4-s3.7.1":(1,[]),
"hist-eur4-s3.7.2":(2,[]),
"hist-eur4-s3.7.3":(2,[L("hist-eur4-s3.5.4",H,"goulash communism policy")]),
"hist-eur4-s3.7.4":(1,[L("hist-eur4-s3.0.6",H,"Nagy's reburial")]),
"hist-eur4-s3.7.5":(1,[]),
"hist-eur4-s3.7.6":(2,[L("hist-eur4-s3.3.3",E,"neutrality and Pact withdrawal"),L("hist-eur4-s3.1.4",H,"Gomułka's Polish October")]),
"hist-eur4-s3.7.7":(1,[L("hist-eur4-s3.4.0",H,"the second Soviet intervention")]),
"hist-eur4-s3.7.8":(2,[L("hist-eur4-s2.8.3",H,"Prague Spring 1968")]),
"hist-eur4-s3.8.b":(1,[]),
"hist-eur4-s3.8.0":(1,[L("hist-eur4-s3.3.1",H,"multi-party coalition government")]),
"hist-eur4-s3.8.1":(1,[]),
"hist-eur4-s3.8.2":(2,[]),
"hist-eur4-s3.8.3":(2,[L("hist-eur4-s3.0.6",H,"1989 rehabilitation and reburial")]),
}
src=open(P+'packs/hist-eur4-s3.t1g1.txt').read()
tgt=src.split('CANDIDATES')[0]
ids=re.findall(r'^\[([^\]]+)\]',tgt,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',src,re.M))
assert ids==list(d),(set(ids)^set(d))
out={k:{"cost":c,"needs":n} for k,(c,n) in d.items()}
for k,v in out.items():
  for n in v["needs"]: assert n["id"] in allids and n["id"]!=k,(k,n)
json.dump(out,open(P+'point-links/hist-eur4-s3.t1g1.json','w'),ensure_ascii=False,indent=1)
o=json.load(open(P+'point-links/hist-eur4-s3.t1g1.json'))
print(len(o),sum(len(v["needs"]) for v in o.values()),sum(v["cost"]==2 for v in o.values()),sum(n["confidence"]=="low" for v in o.values() for n in v["needs"]))
