import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
S='geo-option-global-interdependence-s4.'
E='geo-economic-environment-s4.'
IDS=[('0.b',1),('0.0',1),('0.1',1),('1.b',1),('1.0',1),('1.1',1),('1.2',2),('1.3',2),('1.4',1),('1.5',1),
('2.b',1),('2.0',1),('2.1',1),('2.2',1),('2.3',1),('3.b',1),('3.0',1),('3.1',1),('3.2',1),('3.3',1),
('4.b',1),('4.0',1),('4.1',1),('5.b',1),('5.0',1),('5.1',1),('5.2',1),('5.3',1),('5.4',1),
('6.b',1),('6.0',1),('6.1',2),('6.2',1),('6.3',1),('6.4',1),('6.5',1),
('7.b',1),('7.0',1),('7.1',1),('7.2',1),('7.3',1),('7.4',1),
('8.b',1),('8.0',1),('8.1',2),('8.2',2),('8.3',2),
('9.b',1),('9.0',1),('9.1',2),('9.2',1),('9.3',1),('9.4',1),('9.5',1),('9.6',1),
('10.b',1),('10.0',1),('10.1',1),
('11.b',1),('11.0',1),('11.1',1),('11.2',1),('11.3',1),('11.4',1),
('12.b',1),('12.0',1),('12.1',2),('12.2',1),('12.3',1),('12.4',1),('12.5',1),
('13.b',1),('13.0',2),('13.1',1),('13.2',1),('14.b',1),('14.0',1),('14.1',1),
('15.b',1),('15.0',2),('15.1',1),
('16.b',1),('16.0',1),('16.1',1),('16.2',1),('16.3',2),('16.4',2),('16.5',1),
('17.b',1),('17.0',1),('17.1',1),('17.2',1),('17.3',1),
('18.b',1),('18.0',1),('18.1',2),('18.2',1),('18.3',1),('18.4',1),('18.5',1),('18.6',1),('18.7',1),
('19.b',1),('19.0',1),('19.1',1),
('20.b',1),('20.0',1),('20.1',2),('20.2',1),('20.3',1)]
def n(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
H,E_='helpful','essential'
L1={'0.0':[n(S+'0.b',H,'sustainable development defined')],
'0.1':[n(S+'0.b',H,'contrasts with the definition')],
'1.1':[n(S+'0.b',H,'the definition it gave')],
'1.5':[n(S+'1.3',E_,'uses the SDGs')],
'3.1':[n(S+'0.0',E_,'uses the three pillars')],
'3.3':[n(S+'1.5',H,'SDG progress behind schedule','low')],
'4.0':[n(S+'0.1',H,'income-based output measures')],
'6.b':[n(S+'5.0',H,'renewable resources and yield')],
'6.0':[n(S+'5.0',H,'overfishing exceeds regeneration','low')],
'6.1':[n(S+'5.0',E_,'sustainable yield idea')],
'6.4':[n(S+'6.1',H,'quotas as a limit'),n(E+'14.5',H,'quota system','low')],
'6.5':[n(S+'5.0',H,'overfishing beyond yield','low')],
'7.3':[n(S+'7.2',E_,'rehabilitated cutaway bogs')],
'7.4':[n(S+'7.2',H,'cutaway bog')],
'9.1':[n(S+'9.0',H,'paying farmers for environment','low')],
'9.6':[n(S+'9.3',E_,'dairy herd growth'),n(S+'9.4',H,'emissions'),n(S+'9.5',H,'water quality')],
'11.3':[n(S+'11.0',H,'conifer plantations'),n(S+'5.3',H,'biodiversity')],
'12.1':[n(S+'12.0',H,'forest loss it reverses')],
'12.2':[n(S+'12.1',E_,'the programme being funded')],
'14.1':[n(S+'12.4',H,'protected areas'),n(S+'12.5',H,'ecotourism pressure','low')],
'16.5':[n(S+'16.4',H,'exported as raw beans','low')],
'17.2':[n(S+'17.0',H,'fair trade defined')],
'18.0':[n(S+'16.0',H,'low commodity prices')],
'18.1':[n(S+'18.0',E_,'minimum price floor'),n(S+'18.2',H,'premium')],
'18.2':[n(S+'18.4',H,'co-operatives','low')],
'18.3':[n(S+'16.1',E_,'middlemen')],
'18.5':[n(S+'16.2',H,'child labour problem')],
'18.7':[n(S+'17.2',H,'Fairtrade Mark')],
'20.b':[n(S+'18.4',H,'co-operative')],
'20.1':[n(S+'20.0',H,'Kuapa Kokoo background')],
'20.2':[n(S+'18.2',H,'Fairtrade premium and price')],
'20.3':[n(S+'18.2',E_,'premium spending')]}
R1='geo-option-global-interdependence-s1.'
Q='geo-economic-environment-s1.'
L2={'0.1':[n(R1+'4.0',H,'Rostow stage model'),n(R1+'0.0',H,'output as growth measure')],
'2.0':[n(Q+'0.1',H,'finite non-renewable resources')],
'4.b':[n(R1+'0.4',H,'measures follow views','low')],
'4.0':[n(R1+'0.1',H,'wellbeing beyond income','low')],
'5.0':[n(Q+'0.3',H,'renewable only if managed')],
'5.1':[n(Q+'0.1',H,'non-renewable resources')],
'6.b':[n(Q+'0.3',H,'fish stocks overused')],
'6.0':[n(Q+'0.3',H,'overuse of fish stocks','low')],
'7.b':[n(Q+'1.1',H,'peat as non-renewable fuel')],
'8.b':[n(Q+'1.0',H,'fossil fuels'),n(Q+'0.2',H,'renewable energy')],
'13.0':[n(Q+'0.2',H,'renewable sources')],
'14.0':[n(Q+'1.0',H,'fossil fuels and oil')],
'16.0':[n(R1+'10.1',H,'primary export price instability')],
'16.3':[n(R1+'9.3',H,'terms of trade decline')],
'16.4':[n(R1+'10.2',H,'tariff escalation')],
'16.5':[n(R1+'11.1',H,'cocoa exported as beans','low')]}
G='geo-economic-development-s4.'
B='geo-region-continental-s2.'
L3={'1.5':[n(G+'2.1',H,'what the SDGs are','low')],
'3.2':[n(G+'22.0',H,'unequal responsibility for harm','low')],
'15.1':[n(B+'18.0',H,'Amazon rainforest biome','low')],
'16.0':[n(G+'3.0',H,'primary commodity prices')],
'16.1':[n(G+'3.2',H,'share of value chain')],
'16.2':[n(G+'17.2',H,'exploitation of workers','low')],
'16.3':[n(G+'3.1',H,'terms of trade')],
'16.4':[n(G+'3.3',H,'tariff escalation')],
'16.5':[n(G+'3.0',H,'exporting raw commodities')],
'17.2':[n(G+'6.b',H,'Fairtrade Mark','low')],
'18.5':[n(G+'17.2',H,'child labour exploitation','low')]}
def out(name,mode,L):
    txt=open(P+'packs/'+name+'.txt').read()
    d={}
    for k,c in IDS:
        v={"needs":L.get(k,[])}
        if mode: v={"cost":c,**v}
        d[S+k]=v
    for v in d.values():
        for x in v['needs']: assert '['+x['id']+']' in txt,x['id']
    tg=set(re.findall(r'^\[(geo-option-global-interdependence-s4\.[^\]]+)\]',txt.split('CANDIDATES')[0],re.M))
    assert tg==set(d),(tg^set(d))
    json.dump(d,open(P+'point-links/'+name+'.json','w'),ensure_ascii=False,indent=1)
    print(name,len(d),sum(len(v['needs']) for v in d.values()),sum(v.get('cost')==2 for v in d.values()),sum(x['confidence']=='low' for v in d.values() for x in v['needs']))
b='geo-option-global-interdependence-s4.t1g'
out(b+'1',1,L1);out(b+'2',0,L2);out(b+'3',0,L3)
