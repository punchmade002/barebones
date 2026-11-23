import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/biology/'
txt=open(P+'points/bio24-s2.txt').read()
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
tgt=[i for i in re.findall(r'^\[([^\]]+)\]',txt.split('CANDIDATES')[0],re.M)]
H,E='helpful','essential'
def n(i,s,w,c='high'):return {"id":i,"strength":s,"why":w,"confidence":c}
S='bio24-s'
d={
"bio24-s2.0.b":(1,[n("bio24-s1.5.b",H,"structure matches pollination agent")]),
"bio24-s2.0.0":(1,[n("bio24-s1.1.3",H,"petals and nectar guides")]),
"bio24-s2.0.1":(1,[n("bio24-s1.1.3",H,"petals in wind-pollinated flowers")]),
"bio24-s2.0.2":(1,[n("bio24-s1.1.4",H,"nectary secretes nectar")]),
"bio24-s2.0.3":(1,[n("bio24-s1.1.4",H,"nectaries and nectar")]),
"bio24-s2.0.4":(1,[]),
"bio24-s2.0.5":(1,[n("bio24-s1.0.5",H,"hazel catkins",'low')]),
"bio24-s2.0.6":(1,[]),
"bio24-s2.0.7":(2,[]),
"bio24-s2.1.b":(1,[n("bio24-s1.2.0",H,"anther and filament"),n("bio24-s1.3.1",H,"stigma receives pollen")]),
"bio24-s2.1.0":(1,[n("bio24-s1.2.2",H,"filament holds anther")]),
"bio24-s2.1.1":(1,[n("bio24-s1.2.2",H,"filament holds anther")]),
"bio24-s2.1.2":(1,[n("bio24-s1.3.1",H,"sticky stigma catches pollen")]),
"bio24-s2.1.3":(1,[n("bio24-s1.3.1",H,"large feathery stigma")]),
"bio24-s2.1.4":(2,[n("bio24-s1.3.6",H,"half-flower diagram labels")]),
"bio24-s2.2.b":(1,[]),
"bio24-s2.2.0":(1,[]),
"bio24-s2.2.1":(1,[n("bio24-s2.2.0",H,"contrast with insect pollen amount")]),
"bio24-s2.2.2":(1,[]),
"bio24-s2.2.3":(1,[]),
"bio24-s2.2.4":(1,[n("bio24-s2.2.2",H,"insect pollen grain features"),n("bio24-s2.2.3",H,"wind pollen grain features")]),
"bio24-s2.3.b":(1,[n("bio2-s2.2.1",H,"control group idea",'low')]),
"bio24-s2.3.0":(1,[]),
"bio24-s2.3.1":(2,[]),
"bio24-s2.3.2":(2,[n("bio2-s2.0.1",H,"independent variable compared",'low')]),
"bio24-s2.3.3":(1,[n("bio24-s2.3.2",H,"qualitative versus quantitative")]),
"bio24-s2.3.4":(2,[n("bio2-s2.0.3",H,"controlled variables kept same"),n("bio2-s2.5.2",H,"means from repeats",'low')]),
"bio24-s2.3.5":(1,[n("bio2-s2.0.3",H,"controlled variables kept same")]),
"bio24-s2.3.6":(2,[]),
"bio24-s2.3.7":(1,[]),
"bio24-s2.4.b":(1,[]),
"bio24-s2.4.0":(1,[n("bio24-s2.1.b",H,"anther and stigma positions")]),
"bio24-s2.4.1":(2,[n("bio24-s1.0.0",H,"flower parts in rings")]),
"bio24-s2.4.2":(1,[n("bio24-s1.1.4",H,"nectaries at petal base"),n("bio24-s1.3.1",H,"sticky stigma",'low')]),
"bio24-s2.4.3":(1,[n("bio24-s1.3.2",H,"style")]),
"bio24-s2.4.4":(1,[n("bio24-s2.4.0",E,"steps 1 to 4")]),
"bio24-s2.4.5":(1,[n("bio24-s1.3.6",H,"half-flower section diagram")]),
"bio24-s2.4.6":(2,[]),
"bio24-s2.4.7":(2,[n("bio24-s2.2.2",H,"pollen size and surface",'low')]),
"bio24-s2.5.b":(1,[n("bio2-s2.7.0",H,"risk assessment control measures",'low')]),
"bio24-s2.5.0":(1,[n("bio2-s2.7.4",H,"scalpel cutting precaution",'low')]),
"bio24-s2.5.1":(1,[]),
"bio24-s2.5.2":(1,[]),
"bio24-s2.5.3":(1,[]),
"bio24-s2.5.4":(1,[]),
"bio24-s2.6.b":(1,[]),
"bio24-s2.6.0":(2,[n("bio24-s2.3.2",H,"features recorded"),n("bio24-s2.3.3",H,"measured features",'low')]),
"bio24-s2.6.1":(2,[n("bio24-s2.6.0",H,"results table rows")]),
"bio24-s2.6.2":(2,[n("bio24-s2.6.1",H,"insect flower comparison")]),
"bio24-s2.7.b":(1,[]),
"bio24-s2.7.0":(2,[n("bio24-s2.3.1",H,"hypothesis to check"),n("bio24-s2.1.3",H,"feathery stigma adaptation",'low')]),
"bio24-s2.7.1":(1,[n("bio24-s2.2.2",H,"pollen grain surface")]),
"bio24-s2.7.2":(1,[n("bio24-s2.7.3",H,"secondary data meaning",'low')]),
"bio24-s2.7.3":(1,[]),
"bio24-s2.8.b":(1,[]),
"bio24-s2.8.0":(1,[n("bio2-s2.5.4",H,"sample size and representativeness")]),
"bio24-s2.8.1":(1,[n("bio2-s2.0.3",H,"controlled variables")]),
"bio24-s2.8.2":(1,[n("bio2-s2.4.3",H,"instrument resolution",'low')]),
"bio24-s2.8.3":(1,[n("bio2-s2.4.3",H,"precision of measurement",'low')]),
"bio24-s2.8.4":(1,[n("bio24-s2.7.1",H,"SEM images of pollen")]),
"bio24-s2.8.5":(1,[n("bio24-s2.3.2",H,"qualitative features")]),
"bio24-s2.8.6":(1,[]),
}
assert set(d)==set(tgt) and len(tgt)==len(d),(set(tgt)^set(d))
out={}
for i in tgt:
    c,nd=d[i]
    for x in nd: assert x['id'] in allids and x['id']!=i,x
    out[i]={"cost":c,"needs":nd}
json.dump(out,open(P+'point-links/bio24-s2.json','w'),indent=1)
o=json.load(open(P+'point-links/bio24-s2.json'))
L=[x for v in o.values() for x in v['needs']]
print(len(o),len(L),sum(v['cost']==2 for v in o.values()),sum(x['confidence']=='low' for x in L))
