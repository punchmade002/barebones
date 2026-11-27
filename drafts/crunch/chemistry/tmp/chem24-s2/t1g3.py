import json,re
pk=open('packs/chem24-s2.t1g3.txt').read()
tgt=pk.split('CANDIDATES')[0]
ids=re.findall(r'^\[(chem24-s2\.[\w.]+)\]',tgt,re.M)
allids=set(re.findall(r'^\[([\w.\-]+)\]',pk,re.M))
H=lambda i,s,w:{"id":i,"strength":s,"why":w,"confidence":"high"}
L={
"chem24-s2.1.0":[H("chem23-s3.9.0","helpful","hydrocarbons non-polar, London forces only")],
"chem24-s2.7.0":[H("chem23-s3.12.4","helpful","branching reduces contact, lowers boiling point")],
"chem24-s2.12.0":[H("chem23-s3.11.0","helpful","alkanes insoluble in water")],
"chem24-s2.15.0":[H("chem11-s1.0.1","helpful","indicator and litmus colour change"),H("chem11-s1.0.3","helpful","acids react with carbonates")],
"chem24-s2.21.0":[H("chem11-s1.0.1","helpful","litmus turns red in acid"),H("chem11-s1.0.3","helpful","acid plus carbonate gives CO2"),H("chem11-s1.0.2","helpful","acid plus magnesium gives hydrogen")],
"chem24-s2.21.1":[H("chem11-s1.6.0","helpful","acid plus alkali neutralisation equation")],
"chem24-s2.21.3":[H("chem11-s1.0.4","helpful","acids neutralise bases")],
"chem24-s2.21.4":[H("chem11-s1.0.3","helpful","acid plus carbonate gives CO2")],
"chem24-s2.21.5":[H("chem11-s1.0.1","helpful","acid indicator colour")],
}
out={i:{"needs":L.get(i,[])} for i in ids}
assert all(n["id"] in allids for v in out.values() for n in v["needs"]) and set(L)<=set(ids)
json.dump(out,open('point-links/chem24-s2.t1g3.json','w'),ensure_ascii=False,indent=1)
r=json.load(open('point-links/chem24-s2.t1g3.json'))
print(len(r),sum(len(v["needs"]) for v in r.values()),0)
