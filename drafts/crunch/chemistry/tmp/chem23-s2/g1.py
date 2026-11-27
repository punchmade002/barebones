import json,re,sys
D='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/chemistry/'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
H,E='helpful','essential'
R={
"0.b":(1,[]),
"0.0":(1,[L("chem23-s3.0.4",H,"unsaturated hydrocarbon meaning")]),
"0.1":(1,[L("chem23-s3.2.4",H,"alkene bromine addition decolourises")]),
"0.2":(1,[L("chem24-s1.6.0",H,"ethanol formula")]),
"0.3":(1,[L("chem23-s2.0.2",E,"the dehydration equation")]),
"0.4":(1,[]),
"1.b":(1,[]),"1.0":(1,[]),"1.1":(1,[]),"1.2":(1,[]),"1.3":(1,[]),
"1.4":(1,[L("chem23-s2.0.4",H,"aluminium oxide is the catalyst")]),
"1.5":(2,[L("chem23-s2.1.3",H,"inverted water-filled test tube")]),
"1.6":(1,[]),
"1.7":(2,[L("chem23-s2.1.2",H,"stopper and delivery tube set-up"),L("chem23-s2.1.3",H,"inverted tube on beehive shelf")]),
"2.b":(1,[]),
"2.0":(1,[L("chem23-s2.1.0",E,"glass wool soaked with ethanol")]),
"2.1":(2,[L("chem23-s2.0.4",H,"catalyst role of aluminium oxide"),L("chem23-s2.1.4",E,"heating the aluminium oxide")]),
"2.2":(1,[L("chem23-s2.1.5",H,"collection by displacement of water")]),
"2.3":(1,[L("chem23-s2.1.5",E,"discarding first tubes when collecting")]),
"2.4":(2,[L("chem23-s2.1.6",H,"lifting delivery tube before removing heat")]),
"3.b":(1,[]),
"3.0":(2,[]),
"3.1":(1,[L("chem23-s3.9.0",H,"hydrocarbons are non-polar")]),
"3.2":(1,[L("chem23-s2.3.1",H,"non-polar molecules")]),
"3.3":(1,[L("chem8-s1.1.0",H,"relative molecular mass")]),
"4.b":(1,[]),
"4.0":(1,[L("chem23-s3.2.6",H,"alkenes burn with luminous smoky flame")]),
"4.1":(1,[L("chem23-s3.15.1",H,"alkenes burn to CO2 and H2O")]),
"4.2":(2,[L("chem23-s2.4.1",H,"CO2 is a combustion product")]),
"4.3":(1,[L("chem23-s2.4.1",H,"water is a combustion product")]),
"4.4":(2,[L("chem23-s3.15.2",H,"alkenes' carbon percentage 85.7%")]),
"5.b":(1,[]),
"5.0":(1,[L("chem23-s3.2.4",H,"alkenes decolourise bromine water")]),
"5.1":(2,[L("chem23-s3.2.4",H,"addition across the double bond")]),
"5.2":(1,[]),
"5.3":(2,[L("chem23-s2.5.2",E,"the manganate(VII) test")]),
"5.4":(1,[L("chem23-s3.0.4",E,"unsaturated means multiple C-C bond")]),
"5.5":(1,[L("chem23-s3.17.0",H,"alkanes do not react with bromine water")]),
"6.b":(1,[L("chem8-s1.3.0",H,"s.t.p. and molar volume")]),
"6.0":(1,[L("chem8-s1.3.1",E,"mass from density and volume")]),
"6.1":(1,[L("chem8-s1.2.0",E,"moles from mass and molar mass")]),
"6.2":(1,[L("chem23-s2.0.2",E,"1:1 ethanol to ethene equation")]),
"6.3":(1,[L("chem8-s1.11.1",E,"gas volume from moles at STP")]),
"6.4":(1,[L("chem23-s2.6.3",E,"theoretical volume used in yield")]),
"6.5":(2,[L("chem23-s2.2.3",H,"first tubes discarded contain air","low")]),
"7.b":(1,[]),"7.0":(1,[]),"7.1":(1,[]),"7.2":(1,[]),
"7.3":(1,[L("chem23-s2.2.4",H,"suck-back")]),
"7.4":(1,[L("chem23-s2.2.3",E,"first tubes contain air")]),
"7.5":(2,[L("chem23-s2.5.2",E,"manganate(VII) decolourisation test")]),
"7.6":(1,[L("chem23-s2.5.5",H,"control experiment")]),
"7.7":(1,[L("chem23-s2.5.4",E,"decolourisation shows unsaturation")]),
}
pk=open(D+'packs/chem23-s2.t1g1.txt').read()
tg=[]
sec=None
for ln in pk.split('\n'):
    if ln.startswith('TARGET'): sec='T'
    elif ln.startswith('CANDIDATES'): sec='C'
    m=re.match(r'\[(\S+?)\]',ln)
    if m and sec=='T': tg.append(m.group(1))
allids=set(re.findall(r'^\[(\S+?)\]',pk,re.M))
out={}
for t in tg:
    k=t.split('chem23-s2.')[1]
    c,n=R[k]; out[t]={"cost":c,"needs":n}
assert set(R)=={t.split('chem23-s2.')[1] for t in tg},(set(R)^{t.split('chem23-s2.')[1] for t in tg})
for t,v in out.items():
    for n in v['needs']: assert n['id'] in allids and n['id']!=t,n
json.dump(out,open(D+'point-links/chem23-s2.t1g1.json','w'),indent=0)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
