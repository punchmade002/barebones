import json,re
P='geo-economic-environment-s5.';B='geo-region-continental-s2.'
pack=open('/Users/gabrielwhelan/barebones/drafts/crunch/geography/packs/geo-economic-environment-s5.t1g6.txt').read()
allids=set(re.findall(r'^\[([^\]]+)\]',pack,re.M))
tgt=[i for i in re.findall(r'^\[([^\]]+)\]',pack,re.M) if i.startswith(P)]
H,E='helpful','essential'
L={ # id:(target,strength,why,conf)
'0.2':('0.0',H,'economic interests defined','high'),
'1.0':('0.0',H,'uses economic interests','low'),
'1.1':('0.0',H,'jobs and income as interests','low'),
'2.2':('0.1',H,'habitats and species protection','high'),
'2.3':('2.2',H,'restriction from EU habitat law','low'),
'3.1':('3.0',H,'the Corrib gas field','high'),
'3.2':('0.0',H,'energy supply as economic interest','low'),
'4.b':('3.b',H,'Corrib gas project','high'),
'4.0':('3.1',H,'raw gas versus processed gas','high'),
'4.1':('4.0',E,'argues against onshore raw gas','high'),
'4.2':('2.2',H,'EU-protected sites','high'),
'5.0':('4.0',H,'pipeline work being obstructed','high'),
'5.1':('4.1',H,'protest campaign context','low'),
'5.2':('4.2',E,'Sruwaddacon Bay protected estuary','high'),
'5.3':('3.b',H,'Corrib project the share was in','high'),
'6.2':('6.1',E,'national quota share','high'),
'7.b':('6.1',H,'quotas shared among EU fleets','low'),
'7.0':('6.1',E,'quotas set under CFP','high'),
'7.1':('7.0',E,'smaller quota needing smaller fleet','high'),
'8.1':('8.0',E,'the drift-net ban','high'),
'8.2':('8.0',E,'the drift-net ban','high'),
'9.0':('6.1',H,'quotas and stocks shared','high'),
'9.1':('9.0',E,'mackerel quota dispute','high'),
'10.1':('10.0',H,'Burren limestone landscape','high'),
'10.2':('10.1',E,'Mullaghmore location','high'),
'11.b':('10.b',H,'Mullaghmore visitor centre','high'),
'11.0':('10.2',E,'the proposed visitor centre','high'),
'11.1':('10.2',E,'the proposed visitor centre','high'),
'12.0':('2.0',E,'planning permission needed','high'),
'12.1':('12.0',H,'continuing planning case','high'),
'13.1':('13.0',H,'Skellig Michael monastery','high'),
'14.0':('13.0',H,'Skellig Michael heritage site','high'),
'14.1':('14.0',H,'filming raised visitor demand','high'),
'14.2':('14.0',H,'demand that access caps manage','high'),
'14.3':('13.0',H,'steep rocky island','low'),
'15.1':('15.0',H,'Hill of Tara','high'),
'16.1':('16.0',E,'the M3 route','high'),
'16.2':('15.1',H,'Tara-Skryne valley','high'),
'17.0':('15.1',E,'archaeological landscape at risk','high'),
'17.1':('15.1',H,'archaeology of the valley','high'),
'17.2':('16.0',H,'the M3 motorway','high'),
'18.2':('2.2',H,'Habitats Directive','high'),
'19.0':('18.2',E,'raised bog SACs','high'),
'19.1':('19.0',E,'the turf cutting ban','high'),
'19.2':('19.0',E,'the turf cutting ban','high'),
'20.3':('20.2',H,'Derrybrien wind farm','high'),
'20.4':('20.0',H,'renewable energy targets','low'),
'21.1':('21.0',E,'milk quota abolition','high'),
'21.2':('21.0',H,'larger dairy herd','low'),
'21.3':('21.2',H,'agriculture water pressure','low'),
'21.4':('21.2',H,'agriculture emissions','high'),
'22.2':('22.1',H,'data centre electricity use','high'),
'22.3':('22.2',E,'grid strain','high'),
'23.1':('23.0',E,'the Amazon rainforest','high'),
'23.3':(B+'79.2',H,'Trans-Amazonian Highway','high'),
'23.4':(B+'80.0',H,'Carajas iron ore','low'),
'23.5':(B+'98.3',H,'Kayapo opposed Belo Monte','high'),
'24.0':('23.0',H,'the Amazon rainforest','high'),
'24.1':('24.0',E,'carbon storage in forest','high'),
'25.0':('23.0',H,'Brazilian Amazon','high'),
'25.1':('25.0',E,'2004 baseline clearing','high'),
'25.2':('25.1',E,'rise after the low','high'),
'26.1':('23.1',H,'soya farming spread','high'),
'26.2':('24.1',H,'carbon and forest global interest','low'),
'26.3':('25.2',H,'clearing rates by period','low'),
'27.1':('27.0',E,'Chico Mendes murder','high'),
'28.1':('28.0',E,'Hambach lignite mine','high'),
'28.2':('28.0',H,'Hambach forest and mine','high'),
'28.3':('28.2',H,'forest clearing halted','low'),
'29.0':('28.0',H,'lignite mining in Germany','high'),
'29.1':('28.3',H,'coal phase-out','high'),
'30.1':('30.0',H,'Three Gorges Dam','high'),
'31.2':('30.0',H,'the dam','low'),
'32.2':('24.1',H,'climate change context','low'),
'33.0':('20.0',H,'wind farm example','low'),
'33.2':('1.2',H,'groups for and against','low'),
'33.3':('0.0',H,'economic interests','low'),
}
out={}
for t in tgt:
    k=t[len(P):]
    needs=[]
    if k in L:
        i,s,w,c=L[k]
        i=i if i.startswith(B) else P+i
        needs=[{"id":i,"strength":s,"why":w,"confidence":c}]
    out[t]=({"needs":needs})
assert len(out)==len(tgt)
for v in out.values():
    for n in v['needs']: assert n['id'] in allids,n
    assert all(len(n['why'].split())<=8 for n in v['needs'])
json.dump(out,open('/Users/gabrielwhelan/barebones/drafts/crunch/geography/point-links/geo-economic-environment-s5.t1g6.json','w'),indent=0)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
