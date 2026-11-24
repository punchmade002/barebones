import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
E,H='essential','helpful'
d={
"0.b":(1,[]),"0.0":(1,[]),"0.1":(1,[]),
"0.2":(1,[L("geo-mapwork-s2.0.0",E,"primary versus secondary data")]),
"0.3":(1,[L("geo-mapwork-s2.0.1",E,"uses secondary source definition")]),
"0.4":(1,[L("geo-mapwork-s2.0.1",E,"secondary sources defined")]),
"0.5":(1,[L("geo-mapwork-s2.0.1",E,"secondary sources defined")]),
"1.b":(1,[]),"1.0":(1,[]),"1.1":(1,[]),"1.2":(1,[]),"1.3":(1,[]),"1.4":(1,[]),"1.5":(1,[]),"1.6":(1,[]),
"1.7":(1,[L("geo-mapwork-s1.0.0",H,"uses OS map idea","low")]),
"2.b":(1,[]),"2.0":(1,[]),"2.1":(1,[]),"2.2":(1,[]),
"2.3":(1,[L("geo-mapwork-s1.0.0",H,"OS maps")]),
"2.4":(1,[]),
"3.b":(1,[]),
"3.0":(2,[]),"3.1":(2,[]),
"3.2":(1,[L("geo-mapwork-s1.0.2",H,"scale as ratio of map to ground","low")]),
"3.3":(1,[L("geo-mapwork-s2.3.2",H,"early OS map editions")]),
"3.4":(1,[L("geo-mapwork-s1.0.2",H,"map scale differences","low")]),
"4.b":(1,[]),
"4.0":(1,[L("geo-mapwork-s1.0.2",E,"map scale")]),
"4.1":(1,[]),"4.2":(1,[]),"4.3":(2,[]),
"4.4":(1,[L("geo-mapwork-s2.4.3",H,"explains the described changes")]),
"4.5":(1,[]),
"4.6":(1,[L("geo-mapwork-s2.4.5",E,"compares with the 1840s map")]),
"4.7":(2,[L("geo-mapwork-s2.4.6",H,"explains the changes shown today")]),
"5.b":(1,[]),
"5.0":(1,[L("geo-mapwork-s2.3.0",H,"old photographs as past sources")]),
"5.1":(1,[]),
"6.b":(1,[L("geo-mapwork-s1.16.0",H,"OS sketch-map rules")]),
"6.0":(1,[L("geo-mapwork-s1.16.1",H,"drawing the sketch frame")]),
"6.1":(1,[L("geo-mapwork-s1.16.2",H,"pencil grid on sketch frame")]),
"6.2":(1,[L("geo-mapwork-s2.6.1",H,"grid sections for placing features")]),
"6.3":(1,[L("geo-mapwork-s1.16.7",H,"draw only features asked")]),
"6.4":(1,[L("geo-mapwork-s2.6.1",H,"grid method for sketching")]),
"7.b":(1,[]),"7.0":(1,[]),"7.1":(1,[]),"7.2":(2,[]),"7.3":(2,[]),
"7.4":(1,[L("geo-mapwork-s2.12.0",H,"exam stimulus material","low")]),
"7.5":(1,[]),
"7.6":(1,[L("geo-mapwork-s2.6.2",H,"placing features on sketch map","low")]),
"7.7":(1,[L("geo-mapwork-s2.9.7",H,"agreement with other sources")]),
"8.b":(1,[]),"8.0":(1,[]),
"8.1":(1,[L("geo-mapwork-s2.8.0",E,"the extract being judged")]),
"8.2":(1,[L("geo-mapwork-s2.8.0",E,"the extract being judged")]),
"9.b":(1,[]),"9.0":(1,[]),
"9.1":(1,[L("geo-mapwork-s2.9.0",H,"bias defined")]),
"9.2":(1,[]),"9.3":(1,[]),"9.4":(1,[]),"9.5":(1,[]),"9.6":(1,[]),"9.7":(1,[]),
"10.b":(1,[]),"10.0":(2,[]),
"10.1":(1,[L("geo-mapwork-s2.9.4",E,"purpose check in checklist")]),
"10.2":(1,[L("geo-mapwork-s2.9.5",E,"evidence check in checklist")]),
"10.3":(1,[L("geo-mapwork-s2.2.4",H,"development plans")]),
"11.b":(1,[]),"11.0":(1,[]),
"11.1":(1,[L("geo-mapwork-s2.11.0",H,"listing sources in a report")]),
"11.2":(1,[]),"11.3":(1,[]),
"12.b":(1,[]),"12.0":(1,[]),
"12.1":(1,[L("geo-mapwork-s2.8.b",H,"fact versus opinion skill")]),
"12.2":(2,[]),"12.3":(1,[]),
}
pk=open(P+'packs/geo-mapwork-s2.t1g1.txt').read()
head=pk.split('CANDIDATES')[0]
tids=re.findall(r'^\[(geo-mapwork-s2\.[^\]]+)\]',head,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',pk,re.M))
out={}
for t in tids:
    k=t.split('s2.',1)[1]; c,n=d[k]; out["geo-mapwork-s2."+k]={"cost":c,"needs":n}
assert set(d)==set(t.split('s2.',1)[1] for t in tids),(set(d)^set(t.split('s2.',1)[1] for t in tids))
for v in out.values():
    for n in v["needs"]: assert n["id"] in allids,n
json.dump(out,open(P+'point-links/geo-mapwork-s2.t1g1.json','w'),indent=1)
o=json.load(open(P+'point-links/geo-mapwork-s2.t1g1.json'))
print(len(o),sum(len(v["needs"]) for v in o.values()),sum(v["cost"]==2 for v in o.values()),sum(n["confidence"]=="low" for v in o.values() for n in v["needs"]))
