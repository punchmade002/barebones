import json,re
D='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history'
P='hist-eur4-'
E,H='essential','helpful'
def n(i,s,w,c='high'): return {"id":P+i,"strength":s,"why":w,"confidence":c}
R={
"s13.0.b":(1,[]),"s13.0.0":(1,[]),"s13.0.1":(1,[]),
"s13.0.2":(1,[n("s2.0.0",H,"Cold War rivalry between blocs")]),
"s13.0.3":(1,[]),"s13.0.4":(1,[]),
"s13.1.b":(1,[]),"s13.1.0":(2,[]),
"s13.1.1":(1,[n("s13.1.0",E,"penicillin and its discoverers")]),
"s13.1.2":(1,[]),
"s13.1.3":(1,[n("s13.1.0",H,"antibiotics such as penicillin")]),
"s13.1.4":(1,[]),"s13.1.5":(1,[]),
"s13.1.6":(1,[n("s13.1.5",H,"vaccination campaigns")]),
"s13.1.7":(1,[n("s13.0.1",E,"the welfare state")]),
"s13.2.b":(1,[]),"s13.2.0":(1,[]),"s13.2.1":(1,[]),"s13.2.2":(1,[]),
"s13.2.3":(2,[]),"s13.2.4":(2,[]),
"s13.3.b":(1,[]),
"s13.3.0":(1,[n("s13.3.b",H,"DNA structure")]),
"s13.3.1":(2,[n("s13.3.0",E,"Watson and Crick's double helix")]),
"s13.3.2":(1,[n("s13.3.0",E,"Watson and Crick's DNA model"),n("s13.3.1",H,"Franklin and Wilkins's evidence")]),
"s13.3.3":(1,[n("s13.3.b",H,"genetic engineering of DNA")]),
"s13.3.4":(1,[n("s13.3.0",H,"DNA structure discovery")]),
"s13.3.5":(1,[n("s13.3.3",E,"recombinant DNA techniques")]),
"s13.3.6":(1,[]),
"s13.4.b":(1,[]),"s13.4.0":(2,[]),
"s13.4.1":(2,[n("s13.3.6",H,"IVF"),n("s13.3.b",H,"genetic engineering")]),
"s13.4.2":(1,[n("s13.3.6",E,"IVF")]),
"s13.4.3":(1,[n("s13.3.b",H,"DNA")]),
"s13.4.4":(1,[n("s13.4.1",H,"ethical debates over IVF and genetics")]),
"s13.4.5":(1,[]),
"s13.5.b":(1,[n("s13.0.0",H,"atomic bombs of 1945")]),
"s13.5.0":(1,[n("s13.5.b",H,"civil nuclear power")]),
"s13.5.1":(1,[]),"s13.5.2":(1,[]),"s13.5.3":(1,[]),"s13.5.4":(1,[]),"s13.5.5":(1,[]),
"s13.6.b":(1,[n("s13.0.3",E,"the 1973 oil crisis")]),
"s13.6.0":(1,[n("s13.6.b",H,"nuclear energy independence after 1973")]),
"s13.6.1":(1,[n("s13.6.0",H,"French reactor programme")]),
"s13.6.2":(1,[n("s13.6.b",H,"nuclear expansion after 1973")]),
"s13.6.3":(1,[n("s13.8.0",H,"Chernobyl reactor")]),
"s13.6.4":(1,[]),
"s13.7.b":(1,[]),"s13.7.0":(1,[]),"s13.7.1":(1,[]),"s13.7.2":(1,[]),"s13.7.3":(1,[]),
"s13.7.4":(1,[]),"s13.7.5":(1,[]),
"s13.8.b":(1,[]),
"s13.8.0":(1,[n("s13.6.3",H,"RBMK reactors")]),
"s13.8.1":(1,[n("s13.8.0",E,"the Chernobyl explosion")]),
"s13.8.2":(1,[n("s13.8.0",E,"the Chernobyl accident")]),
"s13.8.3":(1,[n("s13.8.1",H,"evacuation after Chernobyl")]),
"s13.8.4":(1,[n("s13.8.2",E,"Soviet secrecy over the accident")]),
"s13.8.5":(2,[n("s13.8.0",H,"Chernobyl accident")]),
"s13.9.b":(1,[n("s13.0.0",H,"wartime research")]),
"s13.9.0":(1,[]),
"s13.9.1":(1,[n("s13.9.2",H,"general-purpose computer","low")]),
"s13.9.2":(1,[]),"s13.9.3":(1,[]),"s13.9.4":(1,[]),
"s13.9.5":(2,[n("s13.9.4",H,"transistor miniaturisation")]),
"s13.10.b":(1,[]),"s13.10.0":(1,[]),
"s13.10.1":(1,[n("s13.10.0",H,"mainframes")]),
"s13.10.2":(1,[n("s13.9.5",H,"microprocessors")]),
"s13.10.3":(2,[n("s13.10.2",E,"personal computers")]),
"s13.10.4":(1,[]),
"s13.10.5":(2,[n("s13.5.1",H,"CERN",'low')]),
"s13.11.b":(1,[]),"s13.11.0":(1,[]),
"s13.11.1":(1,[n("s13.11.0",H,"automation of routine work")]),
"s13.11.2":(1,[]),
"s13.11.3":(1,[n("s13.0.4",E,"information technology")]),
"s13.12.b":(1,[n("s2.0.0",H,"East-West Cold War contest")]),
"s13.12.0":(1,[n("s2.0.0",H,"Soviet bloc and the West")]),
"s13.12.1":(1,[n("s13.12.0",H,"COCOM restrictions on the bloc")]),
"s13.12.2":(1,[n("s13.12.1",H,"Soviet lag in computing")]),
"s13.12.3":(1,[n("s13.0.4",H,"information technology")]),
"s13.13.b":(1,[]),
"s13.13.0":(2,[n("s13.1.7",H,"longer life expectancy"),n("s13.5.b",H,"nuclear electricity")]),
"s13.13.1":(2,[n("s13.7.2",H,"nuclear accidents"),n("s13.4.1",H,"reproductive and genetic ethics")]),
"s13.13.2":(1,[n("s13.8.0",H,"Chernobyl"),n("s13.7.2",H,"Three Mile Island")]),
"s13.13.3":(1,[]),
"s13.13.4":(2,[n("s13.1.7",H,"medicine and longer lives"),n("s13.11.1",H,"computers changing work"),n("s13.6.1",H,"French nuclear electricity share")]),
}
txt=open(D+'/packs/hist-eur4-s13.t1g1.txt').read()
tids=re.findall(r'^\[(hist-eur4-s13\.[^\]]+)\]',txt.split('CANDIDATES')[0],re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
out={}
for t in tids:
    c,nd=R[t[len(P):]]
    for x in nd: assert x['id'] in allids and x['id']!=t,(t,x)
    out[t]={"cost":c,"needs":nd}
assert len(R)==len(tids)==len(out),(len(R),len(tids))
json.dump(out,open(D+'/point-links/hist-eur4-s13.t1g1.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
