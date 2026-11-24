import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
S='geo-region-continental-s1.'
sec={ '29':(['1','2','3'],[2,1,1]),
'30':(['b','0','1','2','3'],[1,2,1,1,1]),
'31':(['b','0','1'],[1,1,2]),
'32':(['b','0','1','2','3'],[1,1,1,2,1]),
'33':(['b','0','1','2','3','4','5'],[1,1,1,2,1,1,1]),
'34':(['b','0','1','2','3'],[1,1,1,1,1]),
'35':(['b','0','1','2'],[1,1,1,1]),
'36':(['b','0','1','2'],[1,1,1,1]),
'37':(['b','0','1','2','3','4','5'],[1,1,1,1,2,2,1]),
'38':(['b','0','1','2','3'],[1,2,1,1,1]),
'39':(['b','0','1','2','3','4'],[1,1,1,1,1,1]),
'40':(['b','0','1','2','3','4'],[1,1,1,1,1,1]),
'41':(['b','0','1','2','3'],[1,1,1,1,1]),
'42':(['b','0','1','2','3','4','5','6'],[1,1,2,1,1,1,1,1]),
'43':(['b','0','1','2','3'],[1,2,1,1,1]),
'44':(['b','0','1','2','3','4','5'],[1,1,1,1,1,1,1]),
'45':(['b','0','1','2','3'],[1,1,1,1,1]),
'46':(['b','0','1','2','3'],[1,1,1,1,1]),
'47':(['b','0','1','2','3','4'],[1,1,1,1,1,1]),
'48':(['b','0','1','2','3','4','5'],[1,1,1,1,1,1,1]),
'49':(['b','0','1','2','3'],[1,1,1,1,1]),
'50':(['b','0','1','2','3'],[1,1,1,1,1]),
'51':(['b','0','1','2'],[1,1,1,1]),
'52':(['b','0','1'],[1,1,1]),
'53':(['b','0','1','2','3'],[1,1,1,1,1]),
'54':(['b','0','1','2','3'],[1,1,1,1,1]),
'55':(['b','0','1','2','3'],[1,1,2,1,1]),
'56':(['b','0','1','2','3'],[1,1,1,1,1]),
'57':(['b','0','1','2','3'],[1,1,1,1,1]),
'58':(['b'],[1])}
cost={}
for k,(sf,cs) in sec.items():
    assert len(sf)==len(cs),k
    for s,c in zip(sf,cs): cost[S+k+'.'+s]=c
H,E='high','essential'
def L(i,st,why,c='high',pre=S): return {"id":pre+i,"strength":st,"why":why,"confidence":c}
R='geo-rivers-s1.'
n1={
'29.2':[L('29.b','helpful','Indus mostly outside India')],
'29.3':[L('29.0','helpful','Indus flows into Pakistan')],
'30.b':[L('21.2',E,'plateau tilts west to east')],
'30.0':[L('21.2','helpful','plateau tilt gives east flow')],
'30.2':[L('24.1','helpful','eastern coast deltas')],
'31.b':[L('21.2','helpful','general eastward tilt')],
'31.0':[L('23.1','helpful','Narmada flows west between ranges')],
'31.1':[L('30.2','helpful','contrast with deltas','low')],
'32.0':[L('2.3','helpful','monsoon rain season')],
'32.1':[L('20.1','helpful','alluvium deposited by rivers')],
'32.3':[L('20.0','helpful','flat plains')],
'33.2':[L('31.0','helpful','Narmada flows west')],
'33.3':[L('33.2',E,'displacement by the dam')],
'33.5':[L('30.3','helpful','Kaveri dispute'),L('29.3','helpful','Indus Waters Treaty')],
'34.1':[L('27.2','helpful','Varanasi on the Ganges','low')],
'34.2':[L('34.0','helpful','pollution being cleaned up')],
'34.3':[L('34.0','helpful','pollution being cleaned up')],
'35.2':[L('20.1','helpful','alluvium on the plains')],
'36.1':[L('9.2','helpful','GDP meaning')],
'36.2':[L('36.0','helpful','employment share')],
'37.1':[L('24.1','helpful','deltas suit rice','low')],
'37.4':[L('11.3','helpful','cotton on black soil')],
'37.5':[L('43.b','helpful','White Revolution co-operatives')],
'38.b':[L('2.3',E,'monsoon season')],
'38.0':[L('2.3',E,'monsoon sowing and rain')],
'38.1':[L('38.0','helpful','contrast with kharif')],
'38.2':[L('6.3',E,'western disturbances rain')],
'38.3':[L('38.0','helpful','kharif crops')],
'39.0':[L('0.2','helpful','tropics')],
'39.1':[L('2.3','helpful','monsoon rain')],
'39.2':[L('10.0','helpful','alluvial soils'),L('11.0','helpful','black soils')],
'39.3':[L('20.0','helpful','flat plains')],
'39.4':[L('19.2',E,'perennial Himalayan rivers')],
'40.0':[L('8.0','helpful','drought and floods from monsoon')],
'40.1':[L('13.2','helpful','laterite infertile'),L('10.2','helpful','desert soils')],
'40.2':[L('14.0','helpful','thin mountain soils')],
'40.3':[L('15.0','helpful','erosion'),L('15.1','helpful','salinisation')],
'40.4':[L('41.3','helpful','overused groundwater')],
'41.0':[L('10.3','helpful','Indira Gandhi Canal in Thar')],
'41.2':[L('42.1','helpful','Green Revolution package')],
'41.3':[L('40.4',E,'water table falling')],
'42.4':[L('41.2','helpful','irrigation for Green Revolution')],
'42.5':[L('42.1','helpful','package of seed fertiliser machinery')],
'42.6':[L('41.3','helpful','groundwater depletion'),L('15.2','helpful','nutrient exhaustion','low')],
'43.0':[L('43.b','helpful','co-operatives')],
'43.1':[L('43.0','helpful','co-operative dairying system')],
'43.2':[L('43.0',E,'Operation Flood')],
'44.1':[L('44.0','helpful','small holdings')],
'46.0':[L('44.3','helpful','farmer debt')],
'46.1':[L('38.0','helpful','kharif rice harvest','low')],
'46.3':[L('46.2',E,'the farm laws protests')],
'47.3':[L('43.2','helpful','White Revolution')],
'48.3':[L('27.6','helpful','Sundarbans mangrove')],
'48.5':[L('48.4','helpful','forest loss to respond to')],
'50.0':[L('21.3','helpful','Chota Nagpur Plateau')],
'50.1':[L('50.0',E,'Chota Nagpur Plateau')],
'50.2':[L('50.0','helpful','Chota Nagpur Plateau')],
'53.0':[L('19.3',E,'Himalayan hydroelectric potential')],
'54.2':[L('27.7','helpful','Hooghly river port')],
'54.3':[L('50.1','helpful','Chota Nagpur coal and iron ore')],
'56.3':[L('56.1','helpful','trade barriers lowered')],
}
n2={
'29.1':[L('0.2','helpful','tributary','high',R)],
'30.2':[L('13.0','helpful','delta formation','high',R)],
'31.1':[L('0.7','helpful','estuary','high',R)],
'32.1':[L('12.1','helpful','flood silt deposition','high',R)],
'32.3':[L('12.0','helpful','lateral erosion shifts channel','low',R)],
'35.2':[L('12.1','helpful','floods deposit alluvium','high',R)],
'36.0':[L('79.b','helpful','census meaning','low')],
'45.0':[L('79.2','helpful','population over 1.4 billion','low')],
}
n3={'31.1':[L('19.2','helpful','rift valley (graben)','low','geo-volcanoes-earthquakes-s5.')]}
ids=[S+k+'.'+s for k,(sf,_) in sec.items() for s in sf]
assert len(ids)==len(set(ids))==len(cost)
def lk(n): return {S+k:v for k,v in n.items()}
def write(name,d):
    json.dump(d,open(P+'point-links/'+name+'.json','w'),indent=1)
a=lk(n1);b=lk(n2);c=lk(n3)
assert all(k in cost for d in (a,b,c) for k in d)
write('geo-region-continental-s1.t2g1',{i:{"cost":cost[i],"needs":a.get(i,[])} for i in ids})
write('geo-region-continental-s1.t2g2',{i:{"needs":b.get(i,[])} for i in ids})
write('geo-region-continental-s1.t2g3',{i:{"needs":c.get(i,[])} for i in ids})
# verify
for n in ('t2g1','t2g2','t2g3'):
    txt=open(P+'packs/geo-region-continental-s1.'+n+'.txt').read()
    pk=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    tg=re.findall(r'^\[([^\]]+)\]',txt.split('CANDIDATES')[0],re.M)
    d=json.load(open(P+'point-links/geo-region-continental-s1.'+n+'.json'))
    assert list(d)==tg,n
    links=[x for v in d.values() for x in v['needs']]
    assert all(x['id'] in pk for x in links),[x['id'] for x in links if x['id'] not in pk]
    assert all(k!=x['id'] for k,v in d.items() for x in v['needs'])
    print(n,len(d),len(links),sum(v.get('cost')==2 for v in d.values()),sum(x['confidence']=='low' for x in links))
