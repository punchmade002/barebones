import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/biology/'
pk=open(P+'points/bio34-s4.txt').read()
ids=re.findall(r'^\[([^\]]+)\]',pk,re.M)
tg=[i for i in ids if i.startswith('bio34-s4.')]
S='bio34-s4.'
H,L='high','low'
E,Hp='essential','helpful'
# id suffix: (cost, [(need, strength, why, conf)])
spec={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[('0.0',Hp,'surface warmed by sunlight',H)]),
'0.2':(2,[('0.1',E,'infrared emitted by surface',H)]),
'0.3':(1,[('0.2',E,'re-emitted infrared returns',H)]),
'0.4':(1,[('0.3',Hp,'greenhouse effect warms Earth',H)]),
'0.5':(1,[('0.3',E,'natural greenhouse effect',H)]),
'0.6':(1,[('0.5',E,'enhanced greenhouse effect',H)]),
'0.7':(2,[('0.3',E,'steps of greenhouse effect',H)]),
'1.b':(1,[('0.5',Hp,'enhanced greenhouse effect',H)]),
'1.0':(1,[('bio34-s1.5.4',Hp,'fossil fuel burning raises CO2',H)]),
'1.1':(1,[('1.0',Hp,'CO2 rise and release',H)]),
'1.2':(1,[]),
'1.3':(2,[('bio34-s1.4.5',E,'anaerobic methane-producing archaea',H)]),
'1.4':(2,[('1.1',Hp,'CO2 as comparison baseline',H)]),
'1.5':(1,[('1.1',Hp,'CO2 persists for centuries',H)]),
'1.6':(2,[('bio34-s2.6.0',E,'denitrification of nitrate',H)]),
'2.b':(1,[]),
'2.0':(1,[('1.3',Hp,'methane from cattle',H),('1.6',Hp,'nitrous oxide from fertiliser',H)]),
'2.1':(1,[('2.0',Hp,'agriculture as emission source',L)]),
'3.b':(1,[]),
'3.0':(1,[('0.2',E,'greenhouse gases absorb infrared',H)]),
'3.1':(1,[('1.0',Hp,'CO2 concentration rising',H)]),
'3.2':(2,[('3.1',Hp,'CO2 and temperature link',L)]),
'3.3':(2,[('0.3',E,'greenhouse gases warm lower atmosphere',L)]),
'3.4':(1,[('0.6',Hp,'human-driven climate change',L)]),
'3.5':(1,[]),
'4.b':(1,[]),
'4.0':(1,[('3.0',Hp,'infrared absorption mechanism',H)]),
'4.1':(1,[('4.b',Hp,'feedbacks',L)]),
'4.2':(2,[('bio34-s1.4.0',E,'decomposers respire, releasing CO2',H)]),
'4.3':(1,[('bio34-s1.4.0',Hp,'decomposition releases CO2',L)]),
'4.4':(1,[('bio34-s1.1.2',Hp,'CO2 dissolving in oceans',H)]),
'4.5':(1,[('bio34-s1.6.1',Hp,'forest sink becomes source',H)]),
'5.b':(1,[]),'5.0':(1,[]),'5.1':(1,[]),
'5.2':(2,[('bio34-s1.1.2',E,'CO2 dissolving in oceans',H),('bio34-s1.1.3',Hp,'calcium carbonate shell building',H)]),
'5.3':(1,[]),'5.4':(1,[]),
'6.b':(1,[('bio14-s1.4.0',E,'carbon sink definition',H)]),
'6.0':(1,[('bio14-s1.4.2',Hp,'carbon stored in wood',H)]),
'6.1':(1,[('bio34-s1.6.1',Hp,'forest sink becomes source',H)]),
'6.2':(1,[('bio14-s1.4.3',Hp,'algae fix carbon',H)]),
'6.3':(2,[('6.2',E,'phytoplankton photosynthesis fixing carbon',H)]),
'6.4':(1,[('6.3',Hp,'ocean carbon storage',L)]),
'7.b':(1,[]),
'7.0':(2,[('bio34-s1.4.4',E,'slow decomposition builds peat',H)]),
'7.1':(1,[('7.0',Hp,'peat accumulation in bogs',H)]),
'7.2':(2,[('bio34-s1.4.3',Hp,'aerobic decomposition needs air',H)]),
'8.b':(1,[]),
'8.0':(2,[('7.1',Hp,'bogs hold much carbon',H),('6.0',Hp,'forest carbon storage',H)]),
'8.1':(1,[('bio34-s1.6.0',Hp,'sink concept',H)]),
'9.b':(1,[]),
'9.0':(1,[('6.1',Hp,'stored carbon lost when disturbed',H)]),
'9.1':(1,[]),'9.2':(1,[]),
'9.3':(1,[('9.0',E,'protection avoids emissions',H)]),
'10.b':(1,[]),
'10.0':(1,[('bio14-s1.4.1',E,'carbon fixed into biomass',H)]),
'10.1':(1,[]),
'10.2':(1,[('6.1',Hp,'forest carbon released by fire',H)]),
'10.3':(2,[('7.0',E,'waterlogging prevents peat decomposition',H)]),
'10.4':(1,[]),'10.5':(1,[]),'10.6':(1,[]),
'11.b':(1,[('7.2',Hp,'drained peat releases CO2',H)]),
'11.0':(2,[('7.0',E,'waterlogged conditions stop decomposition',H)]),
'11.1':(1,[('11.0',Hp,'rewetting restores peat',H)]),
'11.2':(2,[('bio34-s1.4.5',E,'anaerobic decomposition makes methane',H)]),
'11.3':(1,[]),
'11.4':(1,[('11.1',Hp,'benefits of rewetting',L)]),
'12.b':(1,[]),
'12.0':(1,[('6.2',Hp,'algae photosynthesis',H)]),
'12.1':(1,[('bio34-s1.3.2',Hp,'burning releases CO2',L)]),
'12.2':(2,[('6.3',Hp,'biological pump to deep ocean',H),('bio34-s3.2.5',Hp,'low oxygen after blooms',L)]),
'12.3':(1,[]),
'12.4':(2,[('7.2',Hp,'soil organic matter stores carbon',H)]),
'12.5':(1,[('12.4',E,'soil carbon increase',H)]),
'12.6':(2,[('bio14-s1.4.1',Hp,'plants fix carbon into biomass',L)]),
'12.7':(1,[('12.6',E,'bioenergy from biomass',H)]),
'13.b':(1,[('1.3',Hp,'rumen methane source',H)]),
'13.0':(2,[('1.3',E,'rumen methane microorganisms',H)]),
'13.1':(1,[('13.0',Hp,'cattle methane production',L)]),
'13.2':(1,[('13.0',Hp,'diet and breeding strategies',H)]),
'13.3':(1,[('13.0',Hp,'additives inhibit rumen microbes',H)]),
'13.4':(1,[('1.3',Hp,'cattle produce methane',H)]),
'13.5':(2,[('13.4',Hp,'fewer livestock strategy',H)]),
'13.6':(1,[('13.4',Hp,'fewer livestock strategy',L)]),
'13.7':(1,[('13.5',Hp,'fewer livestock trade-offs',L)]),
'14.b':(1,[('1.6',Hp,'nitrous oxide from soil',H)]),
'14.0':(2,[('bio34-s1.4.5',E,'anaerobic methane production',H)]),
'14.1':(1,[('14.0',E,'anaerobic digestion process',H)]),
'14.2':(1,[('14.0',E,'anaerobic digestion process',H)]),
'14.3':(1,[('1.3',Hp,'landfill and slurry methane',H)]),
'14.4':(1,[('11.2',Hp,'rewetted bogs give methane',H)]),
'14.5':(2,[('1.6',E,'nitrous oxide formation',H),('bio34-s2.1.5',Hp,'clover reduces fertiliser need',H)]),
'15.b':(1,[]),'15.0':(2,[]),
'15.1':(1,[('14.0',Hp,'biogas from anaerobic digestion',H)]),
'15.2':(1,[]),'15.3':(2,[]),'15.4':(1,[]),
'15.5':(2,[('bio34-s2.1.1',E,'legume nitrogen fixation',H)]),
'15.6':(1,[]),
'15.7':(2,[('12.7',Hp,'bioenergy limits',H)]),
}
def f(x): return x if x.startswith('bio') else S+x
out={}
for t in tg:
    c,n=spec[t[len(S):]]
    out[t]={'cost':c,'needs':[{'id':f(a),'strength':b,'why':w,'confidence':k} for a,b,w,k in n]}
assert set(spec)=={t[len(S):] for t in tg},(set(spec)^{t[len(S):] for t in tg})
json.dump(out,open(P+'point-links/bio34-s4.json','w'),ensure_ascii=False)
d=json.load(open(P+'point-links/bio34-s4.json'))
allids=set(ids)
assert list(d)==tg
for k,v in d.items():
    for n in v['needs']:
        assert n['id'] in allids and n['id']!=k,(k,n)
print(len(d),sum(len(v['needs']) for v in d.values()),sum(v['cost']==2 for v in d.values()),sum(n['confidence']=='low' for v in d.values() for n in v['needs']))
