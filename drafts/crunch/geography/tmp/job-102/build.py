import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
S='geo-region-continental-s2.'
costs={0:'111111',1:'11111',2:'111111',3:'1212112',4:'1121111',5:'1121',6:'12111',7:'112211',8:'11211',9:'1111',10:'11111',11:'111112',12:'11111',13:'11221',14:'11111',15:'11111',16:'1111',17:'11111',18:'111211',19:'11111',20:'111111',21:'1221',22:'1121',23:'11111',24:'1211',25:'11111',26:'11111',27:'1111',28:'11111',29:'11111',30:'1112'}
cost={}
for g,s in costs.items():
    ids=[f'{g}.b']+[f'{g}.{i}' for i in range(len(s)-1)]
    for i,c in zip(ids,s): cost[S+i]=int(c)
def L(t,st,why,cf='high'):
    return {'id':t if '-s' in t else S+t,'strength':st,'why':why,'confidence':cf}
h,e='helpful','essential'
p1={'1.3':[L('2.b',h,'five macro-regions named')],
'2.1':[L('7.b',h,'sertão defined')],
'3.1':[L('20.0',h,'Brazilian Highlands location'),L('20.1',h,'Amazon lowland location')],
'3.2':[L('30.3',h,'Amazon estuary and Marajó'),L('30.2',h,'Manaus and Rio Negro')],
'3.3':[L('0.1',h,'Tropic of Capricorn position')],
'3.4':[L('41.3',h,'Mato Grosso soya region')],
'3.5':[L('69.0',h,'industrial triangle')],
'4.0':[L('0.1',h,'equator and Tropic of Capricorn')],
'5.2':[L('18.0',h,'Amazon rainforest biome')],
'6.b':[L('4.1',e,'ITCZ movement')],'6.0':[L('4.1',e,'ITCZ moves south')],'6.1':[L('4.1',e,'ITCZ moves north')],
'6.2':[L('6.0',h,'wet and dry pattern')],'6.3':[L('6.0',h,'first rains of wet season')],
'7.2':[L('4.1',e,'ITCZ reaches area briefly')],
'8.0':[L('4.2',h,'trade winds bring moisture')],'8.1':[L('4.4',h,'escarpment relief rain')],
'8.2':[L('18.2',h,'Atlantic Forest biome')],'8.3':[L('7.b',h,'sertão semi-arid')],
'9.0':[L('4.3',h,'altitude cools air')],'9.1':[L('9.0',h,'plateau cooler with altitude')],
'10.0':[L('4.5',h,'cold fronts from south')],'10.3':[L('40.1',h,'1975 black frost coffee')],
'11.0':[L('7.4',h,'2012-2017 drought')],'11.4':[L('7.3',e,'El Niño drought link')],
'12.1':[L('7.b',h,'sertão unreliable rain')],
'13.1':[L('13.0',h,'latosols')],'13.2':[L('13.1',h,'leaching of nutrients')],'13.3':[L('13.1',h,'leached latosols')],
'14.0':[L('13.1',h,'acidic leached soils')],'14.1':[L('14.0',h,'acidic aluminium soils')],'14.3':[L('14.1',h,'liming makes soil productive')],
'15.1':[L('24.0',h,'basalt plateau')],'16.2':[L('16.1',h,'terra preta')],
'19.0':[L('6.b',h,'wet-dry climate'),L('14.0',h,'acidic Cerrado soils')],
'19.1':[L('7.b',h,'semi-arid sertão'),L('18.3',h,'Caatinga biome')],
'19.2':[L('8.2',h,'wet east coast')],'19.3':[L('18.4',h,'Pampa and Pantanal','low')],
'20.4':[L('3.1',h,'sketch map relief feature')],
'21.2':[L('21.1',h,'Gondwanaland')],
'22.1':[L('20.0',h,'Brazilian Highlands')],'22.2':[L('22.1',e,'tilt of the Highlands')],
'23.2':[L('23.0',h,'steep escarpment behind coast')],'23.3':[L('8.1',e,'relief rain from escarpment')],
'24.1':[L('15.0',h,'terra roxa')],'25.1':[L('25.0',h,'Amazon lowland')],
'28.0':[L('9.2',h,'cooler plateau climate')],'28.1':[L('23.2',h,'escarpment barrier')],
'28.2':[L('25.0',h,'Amazon lowland')],'28.3':[L('11.3',h,'Rio landslides','low')],
'30.2':[L('31.2',h,'black and white water')]}
p2={'0.2':[L('87.0',h,'settlers clustered near ports','low')],
'1.1':[L('100.0',h,'Portuguese language origin','low')],
'2.1':[L('123.0',h,'Northeast poorest periphery')],
'2.3':[L('123.0',h,'Southeast economic core')],
'2.4':[L('95.2',h,'European immigrant settlement')],
'3.2':[L('geo-rivers-s1.0.7',h,'estuary','low'),L('geo-rivers-s1.0.3',h,'confluence of Rio Negro','low')],
'3.3':[L('111.0',h,'São Paulo location')],
'12.1':[L('94.1',h,'drought pushes migration')],
'16.0':[L('geo-rivers-s1.12.1',h,'flood silt alluvium')],
'18.2':[L('86.3',h,'population dense on coast','low')],
'22.1':[L('geo-rivers-s1.0.0',h,'river source','low')],
'25.0':[L('geo-rivers-s1.12.1',h,'alluvium deposition')],
'26.1':[L('geo-rivers-s1.12.1',h,'flooding over flat land')],
'29.b':[L('geo-rivers-s1.0.4',h,'drainage basin')],
'30.0':[L('geo-rivers-s1.0.4',h,'drainage basin','low')],
'30.1':[L('geo-rivers-s1.0.2',h,'tributaries')],
'30.2':[L('geo-rivers-s1.0.3',h,'confluence of two rivers')]}
p3={'0.2':[L('geo-population-migration-s1.8.3',h,'people live near coasts')],
'12.b':[L('geo-population-migration-s1.5.1',h,'climate affects settlement','low')],
'12.2':[L('geo-rivers-s4.1.0',h,'dam turbines make electricity','low')],
'28.b':[L('geo-population-migration-s1.5.0',h,'relief affects settlement')],
'28.0':[L('geo-population-migration-s1.5.0',h,'lowland plateau attracts people','low')],
'28.2':[L('geo-population-migration-s1.7.1',h,'dense forest low density')]}
def pk(n):
    t=open(P+f'packs/geo-region-continental-s2.{n}.txt').read()
    tg,cd=set(),set()
    mode=None
    ids=[]
    for ln in t.split('\n'):
        if ln.startswith('TARGET'):mode='t'
        elif ln.startswith('CANDIDATES'):mode='c'
        m=re.match(r'\[([^\]]+)\]',ln)
        if m:(ids if mode=='t' else []).append(m.group(1)); (cd if mode=='c' else tg).add(m.group(1))
    return ids,cd|tg
for n,links,withcost in (('t1g1',p1,1),('t1g2',p2,0),('t1g3',p3,0)):
    ids,allids=pk(n)
    out={};nl=0;low=0;c2=0
    for i in ids:
        short=i[len(S):]
        nd=[dict(x) for x in links.get(short,[])]
        for x in nd: assert x['id'] in allids and x['id']!=i,(i,x)
        nl+=len(nd);low+=sum(x['confidence']=='low' for x in nd)
        o={}
        if withcost: o['cost']=cost[i];c2+=cost[i]==2
        o['needs']=nd;out[i]=o
    if withcost: assert set(cost)==set(ids)
    assert set(links)<={i[len(S):] for i in ids}
    json.dump(out,open(P+f'point-links/geo-region-continental-s2.{n}.json','w'),ensure_ascii=False,indent=0)
    json.load(open(P+f'point-links/geo-region-continental-s2.{n}.json'))
    print(n,len(ids),nl,c2 if withcost else '-',low)
