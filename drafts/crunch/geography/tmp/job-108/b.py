import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
S='geo-region-continental-s2.'
# every target id with its explicit cost
COST="""93.2:1 93.3:1 94.b:1 94.0:1 94.1:1 94.2:1 94.3:1 95.b:1 95.0:1 95.1:1 95.2:1 95.3:2 95.4:2
96.b:1 96.0:1 96.1:1 96.2:2 96.3:1 97.b:1 97.0:2 97.1:1 97.2:1 97.3:1 98.b:1 98.0:1 98.1:2 98.2:1 98.3:1
99.b:1 99.0:1 99.1:1 99.2:1 100.b:1 100.0:2 100.1:1 100.2:1 100.3:1 101.b:1 101.0:1 101.1:1 101.2:1
102.b:1 102.0:1 102.1:1 102.2:2 103.b:1 103.0:1 103.1:1 103.2:1 104.b:1 104.0:1 104.1:1 104.2:1
105.b:1 105.0:2 105.1:1 105.2:2 105.3:1 106.b:1 106.0:1 106.1:1 106.2:1 107.b:1 107.0:1 107.1:2 107.2:1 107.3:1
108.b:1 108.0:1 108.1:1 108.2:1 108.3:1 109.b:1 109.0:1 109.1:1 109.2:1 109.3:1
110.b:1 110.0:2 110.1:2 110.2:1 111.b:1 111.0:2 111.1:1 111.2:1 111.3:1
112.b:1 112.0:1 112.1:1 112.2:1 112.3:1 112.4:1 112.5:1 113.b:1 113.0:2 113.1:1 113.2:1 113.3:1 113.4:1
114.b:1 114.0:2 114.1:1 114.2:1 114.3:1 115.b:1 115.0:1 115.1:1 115.2:1 115.3:2 115.4:1
116.b:1 116.0:1 116.1:2 116.2:1 116.3:1 117.b:1 117.0:1 117.1:1 117.2:1 117.3:2
118.b:1 118.0:1 118.1:1 118.2:1 118.3:1 119.b:1 119.0:1 119.1:1 119.2:1 119.3:1
120.b:1 120.0:1 120.1:1 120.2:1 121.b:1 121.0:2 121.1:1 121.2:2 121.3:1 121.4:1
122.b:1 122.0:2 122.1:1 122.2:2 123.b:1 123.0:1 123.1:1 123.2:2 123.3:2 123.4:1
124.b:1 124.0:2 124.1:2 124.2:1 124.3:1""".split()
cost={S+a.split(':')[0]:int(a.split(':')[1]) for a in COST}
ids=list(cost)
H,L='helpful','low'
E='essential'
def mk(rows):
    out={}
    for k,v in rows.items():
        out[S+k]=[{"id":(i if i.startswith('geo-') else S+i),"strength":s,"why":w,"confidence":c} for i,s,w,c in v]
    return out
L1=mk({
'93.3':[('13.1',H,'poor leached soils','high')],
'94.b':[('2.b',H,'macro-region names','high')],
'94.0':[('7.b',H,'sertão defined','high')],
'94.1':[('7.b',H,'drought in the sertão','high')],
'94.3':[('2.2',H,'Centre-West region','high')],
'95.2':[('2.4',H,'South region settlement','high')],
'99.0':[('28.3',H,'favelas as informal housing','high')],
'98.3':[('34.3',H,'Belo Monte Dam and Kayapó','high')],
'103.1':[('95.3',H,'Japanese immigration from 1908','high')],
'106.1':[('106.0',H,'Afro-Brazilian religions','high')],
'109.3':[('7.b',H,'drought in the sertão','high')],
'110.2':[('0.4',H,'Brasília is the capital','high')],
'111.0':[('23.0',H,'Serra do Mar escarpment','high')],
'111.3':[('9.0',H,'temperature falls with altitude','high')],
'112.4':[('94.0',H,'Northeast migration to São Paulo','high')],
'113.3':[('35.2',H,'Tietê pollution','high')],
'114.2':[('113.0',H,'favelas','high')],
'115.3':[('28.3',H,'favelas on steep hills','high'),('11.3',H,'2011 landslides','high')],
'117.0':[('30.4',H,'ocean ships reach Manaus','high')],
'119.0':[('2.b',H,'macro-region names','high')],
'119.1':[('7.b',H,'sertão drought','high')],
'120.2':[('120.0',H,'MST','high')],
'122.0':[('14.1',H,'liming','high')],
'122.1':[('7.b',H,'low unreliable rain','high'),('17.0',H,'thin sertão soils','high')],
'122.2':[('122.0',E,'Mato Grosso case','high'),('122.1',E,'sertão case','high')],
'123.0':[('2.b',H,'macro-region names','high')],
'123.2':[('7.b',H,'drought in the sertão','high')],
'124.0':[('15.1',E,'terra roxa and coffee','high')],
'124.1':[('14.3',E,'liming and EMBRAPA lead to soya','high')],
'124.2':[('12.2',H,'rainfall feeds hydroelectricity','high')],
})
L2=mk({
'93.2':[('79.4',H,'BR-364 and Rondônia clearings','high'),('93.0',H,'the settlement programme','high')],
'93.3':[('93.b',H,'failed Amazon settlement schemes','high')],
'94.1':[('47.0',H,'land concentration','high')],
'94.2':[('60.2',H,'ABC region car plants','high')],
'94.3':[('92.2',H,'Centre-West soya frontier','high')],
'95.2':[('40.0',H,'coffee and immigrant labour','high')],
'104.2':[('48.1',H,'Mercosur','high')],
'109.2':[('47.0',H,'land concentration','high')],
'112.0':[('40.0',H,'coffee exported via Santos','high')],
'112.3':[('59.1',H,'coffee profits financed factories','high'),('60.2',H,'ABC region','high')],
'112.5':[('72.1',H,'São Paulo financial centre','high')],
'114.0':[('81.2',H,'rodízio scheme','high')],
'116.2':[('92.b',H,'opening the empty interior','high')],
'117.1':[('50.2',H,'rubber boom and Teatro Amazonas','high'),('68.1',H,'Manaus Free Trade Zone','high')],
'117.3':[('81.1',H,'Curitiba bus rapid transit','high')],
'119.2':[('47.0',H,'land concentration','high')],
'120.0':[('47.1',H,'MST landless movement','high')],
'121.4':[('68.2',H,'SUDENE','high'),('48.4',H,'farm credit for family farms','high')],
'122.0':[('41.2',H,'flat land and reliable rain','high')],
'123.2':[('59.1',H,'coffee profits moved industry south','low')],
'123.3':[('68.2',H,'SUDENE','high'),('68.3',H,'SUDAM','high'),('68.1',H,'Manaus Free Trade Zone','high')],
'124.0':[('40.0',H,'coffee boom','high')],
'124.1':[('79.3',H,'BR-163 soya route','high'),('80.3',H,'northern Amazon ports','high')],
'124.2':[('56.0',H,'hydroelectricity from rainfall','high')],
})
L3=mk({
'97.b':[('geo-population-migration-s1.1.1',H,'census as a count','high')],
'119.3':[('geo-population-migration-s1.7.3',H,'few jobs make young people leave','low')],
})
def w(name,L,withcost):
    d={}
    for i in ids:
        k=i[len(S):]
        e={"needs":L.get(i,[])}
        if withcost: e={"cost":cost[i],**e}
        d[i]=e
    json.dump(d,open(P+'point-links/geo-region-continental-s2.'+name+'.json','w'),ensure_ascii=False,indent=1)
    txt=open(P+'packs/geo-region-continental-s2.'+name+'.txt').read()
    tg=re.findall(r'^\[(\S+?)\]',txt.split('CANDIDATES')[0],re.M)
    allid=set(re.findall(r'^\[(\S+?)\]',txt,re.M))
    assert tg==ids,(name,set(tg)^set(ids))
    n=sum(len(v['needs']) for v in d.values())
    assert all(x['id'] in allid and x['id']!=k for k,v in d.items() for x in v['needs']),name
    for k in L: assert k in d
    print(name,len(d),n,sum(v.get('cost')==2 for v in d.values()),sum(x['confidence']=='low' for v in d.values() for x in v['needs']))
w('t4g1',L1,True);w('t4g2',L2,False);w('t4g3',L3,False)
