import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
E='geo-economic-activities-s2.';U='geo-urban-s7.';M='geo-population-migration-s6.'
def l(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
H='helpful';S='essential'
p1={
'62.2':[l(E+'4.7',H,'trade agreements open markets')],
'63.b':[l(E+'2.0',H,'raw materials as location factor')],
'63.0':[l(E+'2.0',H,'raw materials pull processing')],
'63.2':[l(E+'0.0',H,'bulk-reducing processing near source','low')],
'64.b':[l(E+'2.1',H,'energy as location factor')],
'64.0':[l(E+'2.1',H,'cheap power attracts industry')],
'64.1':[l(E+'2.1',H,'energy-hungry industry needs power')],
'64.2':[l(E+'2.1',H,'cheap power for industry','low')],
'65.b':[l(E+'2.2',H,'labour as location factor')],
'65.0':[l(E+'2.3',H,'assembly seeks low wages')],
'65.1':[l(E+'2.2',H,'skills as labour factor','low')],
'65.3':[l(E+'2.3',H,'high-tech firms seek skilled graduates')],
'66.b':[l(E+'3.0',H,'markets as location factor')],
'66.0':[l(E+'3.0',H,'size and wealth of market')],
'66.1':[l(E+'3.0',H,'access to trade-bloc markets')],
'66.2':[l(E+'3.0',H,'export markets','low')],
'67.b':[l(E+'4.0',H,'capital as location factor','low')],
'67.0':[l(E+'4.0',H,'capital sources for investment')],
'67.1':[l(E+'3.1',H,'ports as transport link')],
'67.2':[l(E+'3.6',H,'road freight links to markets')],
'67.3':[l(E+'1.7',S,'uses term infrastructure')],
'68.b':[l(E+'4.4',H,'regional policy steers firms')],
'68.0':[l(E+'18.1',H,'tariff means tax on imports')],
'68.1':[l(E+'4.4',H,'incentives steer firms to regions')],
'68.2':[l(E+'4.4',H,'regional policy incentives')],
'68.3':[l(E+'4.4',H,'regional policy incentives')],
'69.1':[l(E+'6.0',H,'agglomeration of linked firms')],
'71.2':[l(E+'19.0',H,'rationalisation closes plants','low')],
'79.b':[l(E+'3.6',H,'freight modes')],
'79.0':[l(E+'3.6',H,'road freight share')],
'80.b':[l(E+'3.6',H,'freight modes')],
'80.0':[l(E+'3.6',H,'rail carries heavy loads')],
'80.1':[l(E+'3.6',H,'water freight mode','low')],
'80.2':[l(E+'3.1',H,'ports for freight')],
'81.0':[l(E+'3.4',H,'airports and air transport','low')],
'81.1':[l(U+'13.0',H,'bus rapid transit defined')],
'81.2':[l(U+'37.0',H,'rodizio car ban explained')],
}
p2={
'65.2':[l(M+'13.0',H,'nordestinos migrated to Sao Paulo')],
'84.2':[l(M+'0.0',H,'urbanisation means growing urban share')],
'85.2':[l(M+'7.3',H,'dependency ratios explained')],
'87.3':[l(M+'2.0',H,'jobs in industry pull migrants')],
'90.1':[l(M+'13.0',H,'sertao drought-prone interior defined')],
'90.2':[l(M+'1.4',H,'drought pushes people out')],
}
ids='62.2 '+' '.join(f'{n}.{k}' for n,ks in [(63,'b01234'),(64,'b012'),(65,'b0123'),(66,'b012'),(67,'b0123'),(68,'b0123'),(69,'b012'),(70,'b012345'),(71,'b0123'),(72,'b01'),(73,'b0123'),(74,'b012345'),(75,'b01234'),(76,'b01234'),(77,'b01234'),(78,'b012345'),(79,'b01234'),(80,'b0123'),(81,'b012'),(82,'b0123'),(83,'b012'),(84,'b0123'),(85,'b0123'),(86,'b0123'),(87,'b01234'),(88,'b0123'),(89,'b0123'),(90,'b0123'),(91,'b012'),(92,'b012'),(93,'b01')] for k in ks)
ids=['geo-region-continental-s2.'+i for i in ids.split()]
for name,d in (('t3g4',p1),('t3g5',p2)):
    d={'geo-region-continental-s2.'+k:v for k,v in d.items()}
    assert set(d)<=set(ids)
    out={i:{"needs":d.get(i,[])} for i in ids}
    json.dump(out,open(P+f'point-links/geo-region-continental-s2.{name}.json','w'),ensure_ascii=False)
    txt=open(P+f'packs/geo-region-continental-s2.{name}.txt').read()
    pack=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    tg=[x for x in re.findall(r'^\[(geo-region-continental-s2\.[^\]]+)\]',txt,re.M)]
    o=json.load(open(P+f'point-links/geo-region-continental-s2.{name}.json'))
    assert tg==list(o),(set(tg)^set(o))
    assert all(n['id'] in pack and n['id'] not in o for v in o.values() for n in v['needs'])
    print(name,len(o),sum(len(v['needs']) for v in o.values()),sum(n['confidence']=='low' for v in o.values() for n in v['needs']))
