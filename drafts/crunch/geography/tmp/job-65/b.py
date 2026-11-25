import json,re
P='geo-option-global-interdependence-s1'
last={0:5,1:8,2:6,3:3,4:6,5:5,6:4,7:6,8:2,9:5,10:6,11:3,12:3,13:3,14:3,15:2,16:2,17:1,18:4,19:3,20:4,21:2,22:6,23:5,24:5,25:5,26:4,27:5,28:1}
ids=[]
for s,n in last.items():
    ids.append(f'{P}.{s}.b'); ids+= [f'{P}.{s}.{i}' for i in range(n+1)]
E='geo-economic-activities-s1.'
def L(i,st,w,c): return {"id":E+i,"strength":st,"why":w,"confidence":c}
a={
 '5.0':[L('2.2','helpful','1950s emigration and unemployment','high')],
 '5.1':[L('3.2','helpful','Whitaker programme and free trade policy','high'),L('3.0','helpful','IDA attracts industry','high')],
 '5.2':[L('4.0','helpful','free secondary education 1967','high'),L('3.4','helpful','EEC membership 1973','high')],
 '5.3':[L('19.0','helpful','foreign direct investment by multinationals','low')],
 '5.4':[L('6.b','helpful','Celtic Tiger rapid growth','high')],
 '5.5':[L('8.0','helpful','EU-IMF bailout 2010','high'),L('7.0','helpful','property bubble crash','high')],
 '10.2':[L('2.1','helpful','tariffs as taxes on imports','low')],
}
b={'10.5':[L('55.1','helpful','emigration of skilled people','low')]}
for name,d in (('t1g4',a),('t1g5',b)):
    out={i:{"needs":d.get(i[len(P)+1:],[])} for i in ids}
    json.dump(out,open(f'point-links/{P}.{name}.json','w'),ensure_ascii=False,indent=1)
    o=json.load(open(f'point-links/{P}.{name}.json'))
    pk=open(f'packs/{P}.{name}.txt').read()
    assert all(f'[{i}]' in pk for i in ids)
    for v in o.values():
        for n in v['needs']: assert f'[{n["id"]}]' in pk
    print(name,len(o),sum(len(v['needs']) for v in o.values()),sum(n['confidence']=='low' for v in o.values() for n in v['needs']))
