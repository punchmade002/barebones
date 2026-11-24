import json,re
B='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
P='geo-economic-environment-s5'
E,H='essential','helpful'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
T=lambda x:f'{P}.{x}'
R='geo-rocks-weathering-s4.'; S='geo-region-continental-s2.'
g4={
'4.0':[L(T('3.1'),H,'processed gas, Bellanaboy terminal')],
'4.1':[L(T('4.0'),E,'raw gas piped onshore near homes')],
'4.2':[L(T('2.2'),H,'EU law protects habitats (SAC)')],
'5.0':[L(T('4.0'),H,'pipeline work at Rossport')],
'5.2':[L(T('4.0'),H,'pipeline too close to houses'),L(T('4.2'),E,'protected bay on pipeline route')],
'6.2':[L(T('6.1'),E,'national quotas and share of catch')],
'7.0':[L(T('6.1'),E,'quotas under Common Fisheries Policy')],
'7.1':[L(T('7.0'),E,'smaller quota cut fleet size')],
'8.1':[L(T('2.3'),H,'compensation to make restriction acceptable')],
'8.2':[L(T('8.0'),E,'the drift-net ban')],
'9.0':[L(T('6.1'),H,'quotas and shared stocks')],
'9.1':[L(T('9.0'),E,'the mackerel quota dispute')],
'10.0':[L(R+'1.b',H,'limestone pavement')],
'10.1':[L(R+'1.4',H,'Mullaghmore folded terraced limestone')],
'10.2':[L(T('10.1'),H,'location of Mullaghmore')],
'11.0':[L(T('10.2'),E,'the visitor centre proposal')],
'11.1':[L(T('10.2'),E,'the visitor centre proposal')],
'12.0':[L(T('2.0'),E,'planning permission rules')],
'12.1':[L(T('10.2'),H,'partly built centre site')],
'13.1':[L(T('13.0'),H,'the island and monastery')],
'13.2':[L(T('13.0'),H,'the island itself','low')],
'14.1':[L(T('14.0'),E,'film-driven rise in demand')],
'14.2':[L(T('14.1'),H,'pressure from visitor demand')],
'14.3':[L(T('14.2'),H,'landing and licensed boats')],
'15.1':[L(T('15.0'),H,'Hill of Tara setting')],
'16.1':[L(T('16.0'),E,'the M3 and its commuter towns')],
'16.2':[L(T('15.1'),H,'Tara-Skryne archaeological valley')],
'17.0':[L(T('15.1'),E,'archaeological landscape being destroyed')],
'17.1':[L(T('16.0'),H,'the M3 route')],
'17.2':[L(T('16.0'),H,'the M3 motorway')],
'18.2':[L(T('18.1'),H,'raised bogs'),L(T('2.2'),H,'Habitats Directive protects habitats')],
'19.0':[L(T('18.2'),E,'raised-bog SACs')],
'19.1':[L(T('2.3'),H,'compensation idea'),L(T('19.0'),E,'the turf-cutting ban')],
'19.2':[L(T('19.0'),E,'the turf-cutting ban')],
'20.3':[L(T('20.2'),H,'Derrybrien wind farm'),L(T('2.1'),H,'environmental impact assessment')],
'20.4':[L(T('20.0'),H,'Climate Action Plan targets')],
'21.1':[L(T('21.0'),E,'more milk after quotas ended')],
'21.2':[L(T('21.0'),H,'growth of the dairy herd')],
'21.3':[L(T('21.2'),H,'agriculture water pressure')],
'21.4':[L(T('21.2'),H,'agriculture emissions share')],
'22.2':[L(T('22.1'),H,'data centre electricity use')],
'22.3':[L(T('22.2'),E,'grid strain from demand')],
'23.0':[L(S+'18.0',H,'Amazon biome in Brazil','low')],
'23.1':[L(S+'38.2',H,'extensive cattle ranching'),L(S+'38.0',H,'soya on Cerrado farms','low')],
'23.3':[L(T('23.0'),H,'the Amazon forest')],
'23.5':[L(S+'34.3',H,'Belo Monte opposed by Kayapo')],
'24.0':[L(T('23.0'),H,'the Amazon rainforest')],
'24.1':[L(T('24.0'),E,'carbon stored in the forest')],
'25.1':[L(T('25.0'),E,'the 2004 starting figure')],
'25.2':[L(T('25.1'),H,'clearing cut by 2012')],
'26.1':[L(T('23.1'),H,'soya expanding into forest')],
'26.3':[L(T('25.2'),H,'clearing rates rising and falling','low')],
'27.1':[L(T('27.0'),E,'Chico Mendes murder')],
'28.1':[L(T('28.0'),E,'the Hambach lignite mine')],
'28.2':[L(T('28.0'),H,'the Hambach forest and mine')],
'28.3':[L(T('29.1'),H,'German coal phase-out law')],
'29.0':[L(T('28.0'),H,'lignite mining conflict')],
'29.1':[L(T('28.0'),H,'lignite mining context','low')],
'30.1':[L(T('30.0'),H,'the Three Gorges Dam')],
'31.0':[L(T('30.0'),H,'the dam and its reservoir')],
'31.1':[L(T('30.0'),H,'the dam reservoir')],
'31.2':[L(T('30.0'),H,'the dam on the Yangtze')],
'33.1':[L(T('33.0'),E,'the development being assessed')],
'33.2':[L(T('1.0'),H,'developers and government stakeholders')],
'33.3':[L(T('33.2'),E,'groups for and against')],
}
g5={
'23.1':[L(S+'43.2',H,'cattle ranching causes clearance')],
'23.2':[L(S+'50.0',H,'Amazon timber logging')],
'23.3':[L(S+'61.1',H,'Trans-Amazonian Highway built 1970')],
'23.4':[L(S+'54.0',H,'Carajas iron-ore mine')],
'25.0':[L(S+'52.2',H,'PRODES clearance figures')],
'26.0':[L(S+'52.4',H,'Forest Code 80% rule')],
'26.1':[L(S+'48.3',H,'Amazon soy moratorium')],
'26.2':[L(S+'52.4',H,'Amazon Fund donors')],
'27.0':[L(S+'51.0',H,'Chico Mendes rubber tapper')],
}
g6={'23.3':[L(S+'79.4',H,'fishbone clearings along roads')]}
ids=[]
for l in open(B+f'packs/{P}.t1g4.txt'):
    m=re.match(r'\[(%s\.[^\]]+)\]'%P,l)
    if m: ids.append(m.group(1))
    if l.startswith('CANDIDATES'): break
for name,g in(('g4',g4),('g5',g5),('g6',g6)):
    out={i:{"needs":g.get(i[len(P)+1:],[])} for i in ids}
    assert all(T(k) in ids for k in g), [k for k in g if T(k) not in ids]
    pk=open(B+f'packs/{P}.t1{name}.txt').read()
    for v in out.values():
        for n in v['needs']: assert '['+n['id']+']' in pk,n['id']
    json.dump(out,open(B+f'point-links/{P}.t1{name}.json','w'),indent=0)
    nl=sum(len(v['needs']) for v in out.values()); lo=sum(n['confidence']=='low' for v in out.values() for n in v['needs'])
    print(name,len(out),nl,lo)
