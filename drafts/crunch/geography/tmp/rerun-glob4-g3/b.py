import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/packs/geo-economic-globalisation-s4.t1g3.txt'
O='/Users/gabrielwhelan/barebones/drafts/crunch/geography/point-links/geo-economic-globalisation-s4.t1g3.json'
L={
'1.4':[('geo-economic-development-s4.17.2','helpful','sweatshop-style exploitation of workers','low')],
'3.2':[('geo-economic-development-s4.17.2','helpful','low wages and exploitation of workers','high')],
'4.2':[('geo-economic-development-s4.3.0','helpful','periphery raw material commodity dependence','low')],
'7.3':[('geo-economic-development-s4.3.0','helpful','commodity prices low and unstable','high')],
'10.5':[('geo-economic-development-s4.8.b','helpful','how developing-country debt arose','high')],
'10.7':[('geo-economic-development-s4.3.3','helpful','tariff escalation explained','high')],
'11.0':[('geo-economic-development-s4.11.1','helpful','HIPC initiative debt relief','high')],
'11.3':[('geo-economic-development-s4.6.b','helpful','fair trade model','high')],
'12.1':[('geo-economic-development-s4.3.2','helpful','value chain idea','low')],
'12.5':[('geo-economic-development-s4.4.2','helpful','WTO as trade body','low')],
'13.4':[('geo-economic-development-s4.18.0','helpful','Rana Plaza collapse facts','high')],
'17.1':[('geo-economic-development-s4.3.0','helpful','world commodity prices unstable','high')],
'19.2':[('geo-economic-development-s4.18.0','helpful','Rana Plaza collapse facts','high')],
'19.3':[('geo-economic-development-s4.18.3','helpful','Accord on Fire and Building Safety','high')],
}
ids=[m.group(1) for l in open(P) if (m:=re.match(r'\[(\S+)\]',l))]
tgt=[];seen=False
for l in open(P):
    if l.startswith('TARGET'):seen=True
    elif l.startswith('CANDIDATES'):seen=False
    elif seen and (m:=re.match(r'\[(\S+)\]',l)):tgt.append(m.group(1))
out={}
for t in tgt:
    k=t.split('s4.',1)[1]
    out[t]={"needs":[{"id":i,"strength":s,"why":w,"confidence":c} for i,s,w,c in L.get(k,[])]}
assert all(n['id'] in ids for v in out.values() for n in v['needs'])
assert set(L)<= {t.split('s4.',1)[1] for t in tgt}
json.dump(out,open(O,'w'),indent=1)
d=json.load(open(O))
print(len(d),sum(len(v['needs']) for v in d.values()),sum(n['confidence']=='low' for v in d.values() for n in v['needs']))
