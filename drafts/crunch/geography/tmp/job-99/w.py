import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
C='geo-region-continental-s1.'
# section: last bullet index (all sections also have .b)
S={58:2,59:2,60:1,61:3,62:1,63:6,64:5,65:6,66:1,67:5,68:5,69:5,70:3,71:4,72:4,73:3,74:5,75:4,76:2,77:3,78:2,79:3,80:2,81:2,82:2,83:4,84:2,85:1,86:3,87:1}
ids=[]
for s,n in S.items():
    if s!=58: ids.append(f'{C}{s}.b')
    ids+= [f'{C}{s}.{i}' for i in range(n+1)]
ids=[i for i in ids]
# 58 has no .b
E='geo-economic-activities-s2.';U='geo-urban-s7.';
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
g4={ '86.0':[L('geo-rivers-s4.3.3','helpful','floodplain silt deposition (alluvium)','low')],
     '74.1':[L('geo-rocks-weathering-s1.12.0','helpful','limestone becomes marble','low')]}
g5={
'58.0':[L(E+'2.0','helpful','weight-losing raw materials pull processing','low')],
'58.1':[L(E+'0.0','helpful','plant near raw material (bulk-reducing)','low')],
'58.2':[L(E+'0.0','helpful','plant near raw material (bulk-reducing)','low')],
'59.b':[L(E+'2.2','helpful','labour as a location factor','low')],
'59.0':[L(E+'2.2','helpful','labour cost as location factor')],
'59.1':[L(E+'2.3','helpful','high-tech firms seek graduates')],
'59.2':[L(U+'4.b','helpful','informal sector meaning')],
'60.b':[L(E+'3.0','helpful','market as location factor')],
'60.0':[L(E+'3.0','helpful','size and wealth of market')],
'60.1':[L(E+'16.3','helpful','removal of trade barriers','low')],
'61.0':[L(E+'3.1','helpful','ports as location factor')],
'61.2':[L(E+'3.6','helpful','freight modes road and rail')],
'61.3':[L(E+'1.7','helpful','infrastructure as location factor')],
'62.b':[L(E+'4.b','helpful','government policy and location')],
'62.0':[L(E+'4.4','helpful','regional policy steers firms')],
'62.1':[L(E+'4.4','helpful','incentives steer firms to sites','low')],
'63.5':[L(E+'1.5','helpful','cluster or agglomeration')],
'65.0':[L(E+'1.7','helpful','infrastructure as location factor')],
'65.1':[L(E+'7.b','helpful','local opposition delaying projects','low')],
'65.5':[L(U+'26.0','helpful','Great Bombay textile strike of 1982')],
'67.b':[L(E+'19.2','helpful','outsourcing meaning','low')],
'67.5':[L(E+'16.4','helpful','multinationals move capital')],
'68.2':[L(E+'2.2','helpful','low wages as labour factor')],
'68.4':[L(E+'16.3','helpful','removal of trade barriers','low')],
'73.2':[L(E+'1.7','helpful','infrastructure meaning')],
'74.5':[L(E+'1.7','helpful','infrastructure meaning','low')],
'75.2':[L(E+'3.6','helpful','freight modes bulky goods','low')],
'76.2':[L(U+'5.0','helpful','road congestion causes','low')],
'77.3':[L(U+'13.0','helpful','metros and public transport')],
}
g6={'86.2':[L('geo-population-migration-s6.2.0','helpful','city jobs pull people','low')]}
def out(name,d,extra=None):
    o={}
    for i in ids:
        k=i[len(C):]
        o[i]={"needs":d.get(k,[])}
    json.dump(o,open(P+'point-links/'+name+'.json','w'),indent=1)
out('geo-region-continental-s1.t3g4',g4)
out('geo-region-continental-s1.t3g5',g5)
out('geo-region-continental-s1.t3g6',g6)
for n,d in [('t3g4',g4),('t3g5',g5),('t3g6',g6)]:
    pk=open(P+f'packs/geo-region-continental-s1.{n}.txt').read()
    tgt=re.findall(r'^\[(geo-region-continental-s1\.[^\]]+)\]',pk,re.M)
    o=json.load(open(P+f'point-links/geo-region-continental-s1.{n}.json'))
    allids=set(re.findall(r'^\[([^\]]+)\]',pk,re.M))
    assert list(o)==tgt,(n,set(tgt)^set(o))
    links=[x for v in o.values() for x in v['needs']]
    assert all(x['id'] in allids for x in links),n
    print(n,len(o),len(links),sum(x['confidence']=='low' for x in links))
