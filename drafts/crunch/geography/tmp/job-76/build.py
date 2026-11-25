import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
S='geo-option-global-interdependence-s4.'
def L(sid,st,why,c='high'): return {"id":sid,"strength":st,"why":why,"confidence":c}
E,H='essential','helpful'
s4=lambda x:S+x
# package 1: id -> (cost, needs)
g1={
'20.4':(1,[L(s4('20.b'),H,'Kuapa Kokoo co-operative described')]),
'20.5':(1,[L(s4('20.1'),H,'Divine Chocolate part-owned by farmers')]),
'21.b':(1,[L(s4('18.4'),H,'democratic co-operatives')]),
'21.0':(1,[]),
'21.1':(1,[L(s4('16.1'),E,'middlemen take share of price')]),
'21.2':(1,[L(s4('18.2'),E,'Fairtrade Premium')]),
'21.3':(1,[]),
'21.4':(1,[]),
'22.b':(1,[L(s4('17.0'),H,'definition of fair trade')]),
'22.0':(1,[L(s4('18.0'),H,'minimum price gives stable income')]),
'22.1':(1,[L(s4('18.2'),E,'Fairtrade Premium')]),
'22.2':(1,[L(s4('18.4'),E,'democratic co-operatives')]),
'22.3':(1,[L(s4('20.4'),H,'women in co-operative example','low')]),
'22.4':(1,[L(s4('18.6'),H,'environmental standards')]),
'22.5':(1,[L(s4('16.2'),H,'child labour as a problem')]),
'22.6':(1,[L(s4('16.4'),H,'tariff escalation blocks processing','low')]),
'22.7':(1,[L(s4('18.7'),H,'Fairtrade Mark shows standards')]),
'23.b':(1,[]),
'23.0':(1,[L(s4('17.2'),E,'Fairtrade Mark certification')]),
'23.1':(1,[L(s4('17.3'),H,'first Fairtrade town idea','low')]),
'23.2':(1,[]),
'23.3':(1,[]),
'23.4':(1,[]),
'24.b':(1,[]),
'24.0':(1,[L(s4('19.1'),H,'scale of Fairtrade','low')]),
'24.1':(1,[]),
'24.2':(1,[L(s4('17.2'),H,'certification label','low')]),
'24.3':(2,[L(s4('17.2'),H,'Fairtrade-certified farms','low')]),
'24.4':(1,[L(s4('18.4'),H,'co-operative membership')]),
'24.5':(1,[L(s4('18.1'),E,'minimum is a floor')]),
'24.6':(1,[L(s4('16.4'),E,'tariff escalation')]),
'24.7':(2,[L(s4('20.1'),H,'Divine Chocolate processing'),L(s4('16.4'),H,'value added in rich countries','low')]),
'25.b':(1,[]),
'25.0':(1,[L(s4('24.0'),H,'small scale of fair trade'),L(s4('24.6'),H,'trade rules unchanged')]),
'26.b':(1,[L(s4('0.0'),H,'social pillar of sustainability')]),
'26.0':(1,[L(s4('0.0'),H,'social pillar')]),
'26.1':(1,[]),
'27.b':(1,[]),
'27.0':(1,[]),
'27.1':(1,[]),
'27.2':(2,[L(s4('27.b'),H,'indigenous peoples defined')]),
'28.b':(1,[L(s4('26.0'),H,'harm to groups is unsustainable')]),
'28.0':(1,[L(s4('26.1'),H,'minorities lose land to projects')]),
'28.1':(1,[]),
'28.2':(1,[]),
'28.3':(1,[]),
'28.4':(1,[L(s4('5.4'),H,'involve local people in resource decisions')]),
'29.b':(1,[]),
'29.0':(1,[]),
'29.1':(1,[L(s4('5.0'),H,'sustainable use of renewable resource','low')]),
'30.b':(1,[]),
'30.0':(1,[]),
'30.1':(1,[]),
'30.2':(2,[]),
'30.3':(1,[]),
'30.4':(1,[]),
'30.5':(1,[]),
'30.6':(1,[]),
'30.7':(2,[L(s4('30.6'),H,'equality law'),L(s4('30.0'),H,'ethnic status recognition')]),
'31.b':(1,[]),
'31.0':(2,[]),
'31.1':(1,[]),
'31.2':(2,[L(s4('31.1'),H,'discrimination in schools')]),
'31.3':(2,[]),
'32.b':(1,[L(s4('26.0'),H,'just development')]),
'32.0':(1,[]),
'32.1':(1,[]),
'32.2':(2,[L(s4('32.1'),H,'Fosen wind farm')]),
'32.3':(1,[L(s4('32.2'),E,'the court ruling')]),
'32.4':(1,[L(s4('32.3'),E,'cause of protests')]),
'32.5':(1,[]),
'33.b':(1,[]),
'33.0':(1,[]),
'33.1':(1,[]),
'34.b':(1,[]),
'34.0':(1,[]),
'34.1':(2,[L(s4('34.0'),H,'self-reliance meaning')]),
'35.b':(1,[]),
'35.0':(1,[]),
'35.1':(2,[L(s4('34.0'),H,'self-reliance meaning')]),
'35.2':(1,[L(s4('35.1'),E,'Ujamaa defined')]),
'35.3':(1,[]),
'35.4':(1,[]),
'35.5':(1,[]),
'35.6':(1,[]),
'35.7':(2,[]),
'35.8':(2,[L(s4('35.5'),E,'forced villagisation'),L(s4('35.6'),H,'economic failure')]),
'36.b':(1,[]),
'36.0':(2,[L(s4('34.0'),H,'self-reliance meaning')]),
'37.b':(1,[]),
'37.0':(1,[]),
'37.1':(1,[L(s4('37.0'),H,'what appropriate technology is')]),
'37.2':(1,[L(s4('37.0'),H,'intermediate technology')]),
'38.b':(1,[]),
'38.0':(2,[]),
'38.1':(1,[L(s4('38.0'),H,'Maathai and Green Belt')]),
'38.2':(1,[]),
'38.3':(1,[]),
'38.4':(1,[]),
'39.b':(1,[]),
'39.0':(1,[]),
'40.b':(1,[]),
'40.0':(1,[]),
'40.1':(1,[]),
'40.2':(1,[]),
'40.3':(1,[]),
'41.b':(1,[]),
'41.0':(1,[]),
'41.1':(1,[L(s4('35.8'),H,'Tanzania example')]),
'41.2':(1,[L(s4('17.0'),H,'fair trade','low')]),
}
def out(name,d):
    json.dump(d,open(P+'point-links/'+name+'.json','w'),indent=1,ensure_ascii=False)
out('geo-option-global-interdependence-s4.t2g1',{S+k:{"cost":c,"needs":n} for k,(c,n) in g1.items()})
g2={k:[] for k in g1}
g2['20.5']=[L('geo-option-global-interdependence-s1.11.1' if False else 'geo-option-global-interdependence-s1.11.1',H,'cocoa beans exported, processing elsewhere')]
g2['24.7']=[L('geo-option-global-interdependence-s1.11.1',H,'value added elsewhere than growers','low')]
s1='geo-option-global-interdependence-s1.'
g2['34.1']=[L(s1+'16.0',H,'bottom-up development'),L(s1+'14.2',H,'appropriate technology')]
g2['35.7']=[L(s1+'1.4',H,'market reforms of Washington Consensus')]
g2['35.8']=[L(s1+'13.1',H,'self-reliance cutting links failed','low')]
g2['36.b']=[L(s1+'1.0',H,'colonial era dependence')]
g2['36.0']=[L(s1+'1.0',H,'colonial dependence','low')]
g2['37.0']=[L(s1+'14.2',H,'appropriate technology')]
g2['37.1']=[L(s1+'14.2',H,'Small Is Beautiful')]
g2['37.2']=[L(s1+'14.3',H,'Intermediate Technology Development Group')]
g2['41.1']=[L(s1+'13.1',H,'cutting links with world economy')]
# fix: 35.7 and 20.5/24.7 ids must be real
g2['35.7']=[L(s1+'1.4',H,'market reforms of Washington Consensus')]
g2['20.5']=[L(s1+'11.1',H,'cocoa processed elsewhere')]
g2['24.7']=[L(s1+'11.1',H,'processing value added elsewhere','low')]
out('geo-option-global-interdependence-s4.t2g2',{S+k:{"needs":v} for k,v in g2.items()})
g3={k:[] for k in g1}
ed='geo-economic-development-s4.'
rc='geo-region-continental-s2.'
g3['26.b']=[L(ed+'0.b',H,'justice perspective on development','low')]
g3['27.0']=[L(ed+'0.0',H,'Universal Declaration of Human Rights')]
g3['28.0']=[L(ed+'20.1',H,'indigenous peoples lose land')]
g3['28.2']=[L(rc+'35.0',H,'Yanomami mercury mining pollution')]
g3['28.3']=[L(rc+'34.3',H,'Belo Monte dam opposition')]
g3['34.1']=[L(ed+'14.4',H,'aid creates dependency')]
g3['40.3']=[L(ed+'12.4',H,'NGO aid defined','low')]
out('geo-option-global-interdependence-s4.t2g3',{S+k:{"needs":v} for k,v in g3.items()})
# validate
for n,cost in (('t2g1',1),('t2g2',0),('t2g3',0)):
    d=json.load(open(P+'point-links/geo-option-global-interdependence-s4.'+n+'.json'))
    txt=open(P+'packs/geo-option-global-interdependence-s4.'+n+'.txt').read()
    ids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    tg=re.findall(r'^\[([^\]]+)\]',txt.split('CANDIDATES')[0],re.M)
    assert list(d)==tg,(n,set(tg)^set(d))
    links=[x for v in d.values() for x in v['needs']]
    assert all(x['id'] in ids and True for x in links),[x for x in links if x['id'] not in ids]
    assert all(x['id']!=k for k,v in d.items() for x in v['needs'])
    print(n,len(d),len(links),sum(v.get('cost')==2 for v in d.values()),sum(x['confidence']=='low' for x in links))
