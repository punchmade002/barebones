import json,re
B='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
P='hist-eur4-s8.'
def L(i,s,w,c='high'): return dict(id=i,strength=s,why=w,confidence=c)
H='helpful';E='essential'
# id: (cost, links)
d1={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),
'0.2':(1,[L('hist-eur4-s1.11.b',H,'Sovietisation of eastern Europe')]),
'0.3':(1,[L('hist-eur4-s1.9.4',H,'Soviet bloc refused Marshall aid')]),
'0.4':(2,[]),
'1.b':(1,[]),'1.0':(1,[]),'1.1':(1,[]),'1.2':(1,[]),'1.3':(1,[]),'1.4':(2,[]),
'2.b':(1,[L('hist-eur4-s1.11.b',H,'satellite states under Soviet control')]),
'2.0':(2,[L('hist-eur4-s8.1.0',H,'Soviet-pattern five-year plans')]),
'2.1':(2,[]),
'2.2':(2,[L('hist-eur4-s8.1.3',E,'collectivisation of farms')]),
'2.3':(1,[L('hist-eur4-s1.9.b',H,'the Marshall Plan')]),
'2.4':(2,[L('hist-eur4-s8.2.3',H,'trade within Comecon')]),
'2.5':(1,[L('hist-eur4-s8.2.3',H,'Comecon trade system')]),
'2.6':(2,[L('hist-eur4-s1.4.2',H,'reparations from defeated states')]),
'3.b':(1,[]),
'3.0':(1,[L('hist-eur4-s8.1.0',H,'state output targets in plans')]),
'3.1':(1,[L('hist-eur4-s8.1.0',H,'state-set prices')]),
'3.2':(1,[]),'3.3':(1,[]),'3.4':(1,[]),
'4.b':(1,[]),'4.0':(1,[]),'4.1':(1,[]),'4.2':(2,[]),'4.3':(1,[]),
'5.b':(1,[]),'5.0':(1,[]),'5.1':(1,[]),
'5.2':(2,[L('hist-eur4-s8.5.0',H,'ministries Khrushchev had replaced')]),
'5.3':(1,[L('hist-eur4-s8.6.0',H,'1968 invasion of Czechoslovakia')]),
'6.b':(1,[]),
'6.0':(2,[L('hist-eur4-s1.19.5',H,'the Warsaw Pact')]),
'6.1':(1,[]),'6.2':(1,[]),
'6.3':(1,[L('hist-eur4-s8.6.1',H,'Hungary\'s partial reforms')]),
'6.4':(2,[L('hist-eur4-s1.14.3',H,'Tito\'s break with Stalin'),L('hist-eur4-s8.2.3',H,'Comecon membership')]),
'6.5':(1,[]),
'7.b':(1,[]),
'7.0':(1,[L('hist-eur4-s8.5.3',H,'reforms fading, 1968 warning')]),
'7.1':(1,[]),'7.2':(2,[]),
'7.3':(1,[L('hist-eur4-s8.7.2',E,'oil revenue propping the economy')]),
'7.4':(2,[]),'7.5':(1,[]),'7.6':(1,[]),
'8.b':(2,[]),'8.0':(2,[]),
'8.1':(1,[L('hist-eur4-s8.8.0',H,'Gierek replacing Gomułka')]),
'8.2':(1,[]),
'8.3':(2,[L('hist-eur4-s8.8.1',E,'Gierek\'s Western borrowing strategy')]),
'8.4':(1,[L('hist-eur4-s8.8.1',H,'Gierek\'s borrowing from the West')]),
'8.5':(2,[]),
'8.6':(1,[L('hist-eur4-s8.8.5',E,'Solidarity\'s founding')]),
'9.b':(1,[]),
'9.0':(1,[L('hist-eur4-s8.7.3',H,'1986 oil price fall')]),
'9.1':(2,[L('hist-eur4-s8.9.0',H,'perestroika restructuring')]),
'9.2':(1,[L('hist-eur4-s8.9.1',E,'the 1987-88 enterprise laws')]),
'9.3':(1,[L('hist-eur4-s8.9.2','helpful','weakened planning without market','low')]),
'10.b':(1,[]),'10.0':(1,[]),'10.1':(1,[]),'10.2':(1,[]),'10.3':(1,[]),'10.4':(1,[]),
'11.b':(1,[]),'11.0':(1,[]),
'11.1':(1,[L('hist-eur4-s8.6.0',H,'Ota Šik\'s reform')]),
'11.2':(2,[]),'11.3':(1,[]),
'11.4':(1,[L('hist-eur4-s8.10.0',H,'Ceaușescu\'s debt repayment')]),
'11.5':(2,[L('hist-eur4-s8.8.1',H,'Poland\'s Western borrowing'),L('hist-eur4-s8.2.2',H,'Poland\'s private farming')]),
'12.b':(1,[]),'12.0':(1,[]),'12.1':(1,[]),'12.2':(1,[]),'12.3':(1,[]),
'12.4':(2,[]),'12.5':(2,[]),'12.6':(2,[]),
}
d2={
'0.4':[L('hist-eur4-s2.24.0',H,'Khrushchev\'s removal in October 1964')],
'4.0':[L('hist-eur4-s2.6.1',H,'1963 bad harvest, grain imports')],
'4.3':[L('hist-eur4-s2.15.b',H,'the nuclear arms race')],
'5.0':[L('hist-eur4-s2.6.3',H,'1957 regional economic councils')],
'5.1':[L('hist-eur4-s2.7.0',H,'Khrushchev\'s housing and overtaking promises')],
'5.2':[L('hist-eur4-s2.24.1',H,'Brezhnev and Kosygin replace Khrushchev')],
'5.3':[L('hist-eur4-s2.23.4',H,'1968 invasion of Czechoslovakia')],
'6.0':[L('hist-eur4-s2.23.4',H,'1968 Warsaw Pact invasion')],
'6.4':[L('hist-eur4-s2.8.1',H,'Khrushchev mending split with Tito')],
'7.0':[L('hist-eur4-s2.23.4',H,'1968 invasion as warning')],
'7.4':[L('hist-eur4-s2.17.2',H,'rough nuclear parity'),L('hist-eur4-s2.20.0',H,'Afghanistan invasion 1979')],
'11.2':[L('hist-eur4-s2.12.0',H,'building of the Berlin Wall'),L('hist-eur4-s2.10.1',H,'East German refugee flow')],
}
for n,d in((1,d1),):
    out={}
    for k,(c,l) in d.items(): out[P+k]={'cost':c,'needs':l}
    json.dump(out,open(B+'point-links/hist-eur4-s8.t1g1.json','w'),ensure_ascii=False,indent=1)
out={P+k:{'needs':d2.get(k,[])} for k in d1}
json.dump(out,open(B+'point-links/hist-eur4-s8.t1g2.json','w'),ensure_ascii=False,indent=1)
# check
for g in(1,2):
    pk=open(B+f'packs/hist-eur4-s8.t1g{g}.txt').read()
    ids=set(re.findall(r'^\[([^\]]+)\]',pk,re.M))
    tg=[m for m in re.findall(r'^\[([^\]]+)\]',pk.split('CANDIDATES')[0],re.M)]
    j=json.load(open(B+f'point-links/hist-eur4-s8.t1g{g}.json'))
    assert list(j)==tg,(set(tg)^set(j))
    n=[x for v in j.values() for x in v['needs']]
    assert all(x['id'] in ids and x['id'] not in j or g==1 for x in n) or True
    assert all(x['id'] in ids for x in n)
    if g==2: assert all(x['id'] not in j for x in n)
    print(g,len(j),len(n),sum(v.get('cost')==2 for v in j.values()),sum(x['confidence']=='low' for x in n))
