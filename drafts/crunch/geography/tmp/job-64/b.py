import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
T='geo-option-global-interdependence-s1.'
def L(i,s,w,c='h'):
    return {"id":i if i.startswith('geo-') else T+i,"strength":{'e':'essential','h':'helpful'}[s],"why":w,"confidence":{'h':'high','l':'low'}[c]}
E1='geo-economic-development-s1.';E3='geo-economic-development-s3.';G4='geo-economic-globalisation-s4.';E2='geo-economic-development-s2.'
# package 1: section -> list of (cost, links) aligned with b,0,1,...
S={
0:[(1,[]),(1,[]),(1,[]),(1,[]),(1,[]),(1,[L(E1+'6.b','h','HDI score')]),(2,[L('4.b','e','modernisation view'),L('9.b','e','dependency view')])],
1:[(1,[]),(1,[]),(1,[L('4.0','h','Rostow model')]),(1,[L('9.b','h','dependency theory')]),(1,[]),(2,[]),(1,[L('1.4','e','the Washington Consensus reforms')]),(1,[L('15.1','h','HDI')]),(1,[L('0.2','h','sustainable development')]),(1,[L('16.2','h','Sustainable Development Goals','l')])],
2:[(1,[]),(1,[]),(2,[]),(1,[L('1.0','h','colonialism','l')]),(1,[L('2.0','e','the determinist claim')]),(1,[L('2.0','e','the determinist claim')]),(1,[L('2.0','e','the determinist claim')]),(1,[L('2.b','e','contrasts with determinism')])],
3:[(1,[]),(1,[]),(1,[]),(2,[L('3.0','h','landlocked obstacle')]),(1,[L('3.2','e','Botswana example')])],
4:[(1,[]),(1,[]),(1,[L('4.0','h','Rostow model')]),(1,[L('4.0','h','Rostow model')]),(1,[L('4.0','h','Rostow model')]),(1,[L('4.0','h','Rostow model')]),(1,[L('4.0','h','Rostow model')]),(1,[L('4.0','e','Rostow model')])],
5:[(1,[L('4.0','e','Rostow stages')]),(1,[L('4.1','e','traditional stage')]),(2,[L('4.2','e','preconditions stage')]),(2,[L('4.3','e','take-off stage')]),(1,[L('4.4','e','drive to maturity')]),(1,[L('4.5','e','high mass consumption')]),(1,[L('4.0','e','stages model')])],
6:[(1,[L('4.0','e','Rostow stages')]),(1,[]),(1,[]),(1,[]),(2,[]),(1,[L('4.0','e','Rostow stages')])],
7:[(1,[L('4.b','e','modernisation theory')]),(1,[L('4.b','e','modernisation theory')]),(2,[L('4.0','e','stage-bound model')]),(1,[L('9.b','h','dependency view of colonialism')]),(1,[]),(1,[L('4.5','e','mass consumption stage')]),(1,[]),(1,[L('4.b','h','modernisation advice')])],
8:[(1,[L('4.b','h','modernisation theory')]),(1,[]),(1,[L('1.4','e','Washington Consensus')]),(1,[L('10.4','h','debt','l')])],
9:[(1,[L('4.b','e','modernisation theory')]),(1,[]),(1,[L('9.0','e','core and periphery')]),(2,[]),(2,[]),(1,[L('9.0','e','metropolis and satellite')]),(1,[L('9.1','h','structural dependency')])],
10:[(1,[L('9.b','e','dependency theory')]),(1,[L('1.0','h','colonial era')]),(1,[L('9.3','h','low export prices')]),(2,[]),(1,[]),(1,[]),(1,[]),(1,[L('9.0','h','core and periphery','l')])],
11:[(1,[L('10.1','e','primary export dependence')]),(1,[L('10.1','h','export dependence')]),(1,[L('10.2','h','processing elsewhere')]),(1,[L('10.1','h','one-commodity dependence')]),(1,[L('10.0','h','colonial extraction')])],
12:[(1,[L('9.0','e','core and periphery')]),(1,[L('9.0','e','core and periphery')]),(1,[L('12.0','h','core and periphery zones')]),(1,[L('12.0','e','zones of the system')]),(1,[])],
13:[(1,[L('9.b','e','dependency theory')]),(1,[L('9.b','e','dependency theory'),L(E1+'0.4','h','Asian Tigers')]),(1,[L('9.b','h','dependency theory')]),(1,[L('9.b','h','dependency theory')]),(1,[L('13.1','h','withdrawal from trade','l')])],
14:[(1,[]),(1,[]),(1,[L('14.0','e','basic needs')]),(1,[]),(1,[L('14.2','e','Schumacher')])],
15:[(1,[L('0.1','h','human development')]),(2,[L('0.1','h','human development')]),(2,[L(E1+'6.b','h','how the HDI works')]),(1,[L('0.1','e','human development')])],
16:[(1,[]),(1,[L('8.b','h','top-down contrast')]),(1,[L('0.2','e','sustainable development')]),(1,[L('0.2','h','sustainable development')])],
17:[(1,[L('0.0','h','GNP as measure')]),(1,[L('0.0','h','GNP as goal')]),(2,[L(E1+'0.3','h','income groups','l')])],
18:[(1,[]),(1,[]),(1,[]),(1,[]),(1,[]),(1,[])],
19:[(1,[L('18.0','h','image of Africa')]),(1,[]),(1,[]),(1,[]),(1,[L('18.0','h','image of Africa')])],
20:[(1,[L('18.0','h','image of Africa')]),(1,[]),(1,[L('20.0','e','the Dóchas code')]),(1,[L('20.1','h','dignified images')]),(1,[L('18.1','h','stereotypes','l')]),(1,[])],
21:[(1,[L('18.0','h','image of Africa')]),(2,[]),(2,[]),(1,[L('3.2','e','Botswana growth')])],
22:[(1,[]),(1,[L('0.5','h','underdevelopment')]),(1,[]),(1,[L('4.b','h','Western path')]),(1,[]),(1,[L('24.b','h','North-South split')]),(1,[]),(1,[])],
23:[(1,[]),(2,[]),(1,[L('23.0','h','Third World term')]),(1,[L('23.1','e','three worlds')]),(2,[L('23.2','h','Third World')]),(1,[L('23.1','e','Cold War blocs')]),(1,[L('23.1','h','three worlds')])],
24:[(1,[L('23.1','h','three worlds')]),(1,[]),(1,[L('24.0','e','Brandt Report')]),(1,[L('24.1','e','Brandt Line')]),(1,[L('24.b','h','North-South gap')]),(2,[]),(1,[])],
25:[(1,[L('24.1','e','Brandt Line')]),(1,[L('24.b','e','North and South'),L(E1+'0.4','h','NICs')]),(1,[]),(2,[]),(1,[]),(1,[L('17.1','h','Rosling middle-income view')]),(1,[L(E1+'0.3','h','World Bank income groups')])],
26:[(1,[L('7.0','e','Eurocentrism')]),(2,[]),(1,[L('26.0','e','Mercator distortion')]),(1,[L('26.1','e','area distortion')]),(1,[]),(1,[L('26.b','h','Eurocentric viewpoint')])],
27:[(1,[L('7.0','h','Eurocentrism')]),(1,[]),(2,[]),(1,[]),(1,[]),(1,[L('4.b','h','Western path')]),(1,[L('8.b','h','top-down projects','l')])],
28:[(1,[L('7.0','h','Eurocentrism')]),(2,[]),(1,[L('7.0','h','Eurocentric models','l')])],
}
ids={0:'b012345'}
def idl(k):
    n=len(S[k])-1
    return [T+f'{k}.b']+[T+f'{k}.{j}' for j in range(n)]
all_ids=[i for k in range(29) for i in idl(k)]
pack=open(P+'packs/geo-option-global-interdependence-s1.t1g1.txt').read()
tgt=re.findall(r'^\[(geo-option-global-interdependence-s1\.[^\]]+)\]',pack,re.M)
assert tgt==all_ids,(len(tgt),len(all_ids))
out1={}
for k in range(29):
    for i,(c,n) in zip(idl(k),S[k]): out1[i]={"cost":c,"needs":n}
# package 2 (E3) / 3 (G4,E2): sparse by judged id; all others judged empty
p2={'1.0':[L(E3+'0.4','h','colonies supplied raw materials')],'1.4':[L(E3+'2.2','h','IMF structural adjustment reforms')],'1.5':[L(E3+'2.2','h','privatisation and spending cuts')],
'2.2':[L(E3+'0.b','h','colonialism')],'7.2':[L(E3+'0.4','h','colonial raw-material economy','l')],'8.0':[L(E3+'8.2','h','steelworks example','l')],'8.1':[L(E3+'2.2','h','imposed reforms')],'8.2':[L(E3+'2.2','h','debt and aid conditions','l')],
'10.0':[L(E3+'0.4','h','colonial raw-material extraction')],'10.1':[L(E3+'2.1','h','dependence on few raw exports')],'10.4':[L(E3+'2.2','h','debt crises')],
'11.0':[L(E3+'13.b','h','Brazil export cycles')],'11.3':[L(E3+'21.b','h','Gezira Scheme')],'23.2':[L(E3+'0.b','h','former colonies','l')],'27.1':[L(E3+'0.3','h','Berlin Conference')]}
p3={'2.4':[L(E2+'6.3','h','Singapore tropical but rich')],'3.0':[L(E2+'7.0','h','landlocked countries'),L(E2+'6.4','h','malaria')],'3.2':[L(E2+'14.1','h','Botswana diamonds')],
'5.0':[L(E2+'15.0','h','Irish emigration 1950s')],'5.1':[L(E2+'15.1','h','Whitaker programme')],'5.2':[L(E2+'15.2','h','free education, EEC')],'5.4':[L(E2+'15.3','h','Celtic Tiger')],'5.5':[L(E2+'15.4','h','2008 crash, bailout')],
'6.b':[L(E2+'12.b','h','South Korea growth')],'6.0':[L(E2+'12.0','h','Korean War')],'6.1':[L(E2+'12.1','h','export-led industrialisation')],'6.2':[L(E2+'12.2','h','chaebol')],'6.3':[L(E2+'12.4','h','OECD, UNCTAD 2021')],
'7.1':[L(E2+'16.0','h','Zimbabwe'),L(E2+'16.2','h','Syria')],'7.6':[L(G4+'9.b','h','Africa excluded from industry','l')],
'9.0':[L(G4+'4.b','h','core and periphery')],'12.0':[L(G4+'5.0','h','semi-periphery')],'12.1':[L(G4+'4.0','h','core characteristics')],'12.2':[L(G4+'5.1','h','South Korea and China moving up')],'12.3':[L(G4+'18.2','h','China joining WTO')],
'10.0':[L(G4+'6.1','h','colonial raw materials')],'10.1':[L(G4+'7.0','h','export economies')],'10.2':[L(G4+'10.7','h','tariff escalation')],'10.4':[L(G4+'10.5','h','heavy debt','l')],'10.5':[L(E2+'8.5','h','brain drain')],
'11.2':[L(G4+'9.1','h','Zambia copper')],'13.0':[L(G4+'8.1','h','Asian Tigers and China')],'19.2':[L(E2+'6.1','h','Ethiopian famine and war')],'21.2':[L(E2+'14.b','h','Botswana diamonds')],
'24.0':[L(E2+'0.0','h','Brandt Report')],'24.1':[L(E2+'0.1','h','Brandt Line')],'24.2':[L(E2+'0.0','h','Brandt Line not current')],'24.4':[L(E2+'0.5','h','global wealth inequality')],
'25.0':[L(E2+'0.3','h','rich South countries')],'25.1':[L(G4+'16.6','h','India among top economies','l')],'28.0':[L(G4+'11.2','h','Chinese investment in infrastructure')]}
def build(p):
    o={}
    for i in all_ids:
        o[i]={"needs":p.get(i[len(T):],[])}
    return o
def chk(path,o,pk,cost):
    d=json.load(open(path)); ids=set(re.findall(r'^\[([^\]]+)\]',open(P+'packs/'+pk+'.txt').read(),re.M))
    assert list(d)==all_ids
    links=0;lo=0;c2=0
    for k,v in d.items():
        for n in v['needs']:
            assert n['id'] in ids and n['id']!=k; links+=1; lo+=n['confidence']=='low'
        if cost: c2+=v['cost']==2
    print(pk,len(d),links,c2 if cost else '-',lo)
for name,o,cost in [('t1g1',out1,True),('t1g2',build(p2),False),('t1g3',build(p3),False)]:
    pk='geo-option-global-interdependence-s1.'+name
    path=P+'point-links/'+pk+'.json'
    json.dump(o,open(path,'w'),ensure_ascii=False)
    chk(path,o,pk,cost)
