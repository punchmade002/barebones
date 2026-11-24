import json,re
P='geo-glaciation-s2.'
E,H='essential','helpful'
def L(i,s,w,c='high'): return (i if i.startswith('geo-') else P+i,s,w,c)
D={
'0.b':(1,[]),
'0.0':(1,[]),
'0.1':(1,[]),
'0.2':(1,[L('0.0',E,'endogenetic forces'),L('0.1',E,'exogenetic forces')]),
'1.b':(1,[]),
'1.0':(1,[]),
'1.1':(1,[L('1.0',H,'isostasy as crust-mantle balance')]),
'1.2':(2,[L('1.0',E,'uses isostasy balance')]),
'2.b':(1,[]),
'2.0':(1,[L('1.1',H,'crust floating on mantle')]),
'2.1':(1,[L('2.0',E,'load removal reverses depression')]),
'2.2':(1,[L('2.1',E,'rebound after melting')]),
'2.3':(2,[L('2.1',E,'rebound still continuing')]),
'3.b':(1,[]),
'3.0':(1,[L('1.2',H,'removing load raises crust')]),
'3.1':(1,[L('1.2',H,'adding load lowers crust')]),
'4.b':(1,[]),
'4.0':(1,[L('1.2',H,'isostatic change definition')]),
'4.1':(1,[]),
'4.2':(1,[L('4.1',E,'eustatic worldwide sea level')]),
'4.3':(1,[L('4.2',H,'reverse of sea level fall')]),
'4.4':(2,[L('4.0',E,'isostatic change'),L('4.1',E,'eustatic change')]),
'5.b':(1,[]),
'5.0':(1,[L('5.b',H,'base level definition')]),
'5.1':(2,[L('0.0',E,'uplift as endogenetic force'),L('3.0',H,'denudation wearing land down')]),
'5.2':(1,[L('4.4',H,'relative land and sea change')]),
'5.3':(2,[L('0.2',E,'balance of endogenetic and exogenetic')]),
'6.b':(1,[L('4.4',H,'land rising relative to sea')]),
'6.0':(1,[L('2.1',E,'isostatic uplift is rebound'),L('6.b',H,'emergent coast')]),
'6.1':(1,[L('6.0',H,'raised beach with cliffs')]),
'6.2':(1,[L('geo-sea-s1.7.0',H,'wave-cut notch formation')]),
'6.3':(1,[L('geo-sea-s1.8.2',H,'sea stack formation')]),
'6.4':(1,[L('geo-sea-s1.11.3',H,'beach of shingle')]),
'6.5':(1,[L('geo-sea-s1.7.3',H,'wave-cut platform')]),
'6.6':(1,[L('6.0',H,'raised beach')]),
'7.b':(1,[L('4.4',H,'sea rising relative to land')]),
'7.0':(1,[L('geo-rivers-s1.7.2',H,'V-shaped river valley'),L('7.b',H,'submergent coast')]),
'7.1':(2,[L('7.0',E,'ria definition')]),
'7.2':(2,[L('geo-glaciation-s1.9.3',E,'glacial trough U-shaped valley')]),
'7.3':(1,[L('7.2',E,'fjord definition')]),
'7.4':(1,[L('geo-glaciation-s1.17.1',H,'drumlin shape and formation')]),
'7.5':(1,[L('7.4',E,'drowned drumlins')]),
'8.b':(1,[]),
'8.0':(1,[L('2.1',E,'isostatic rebound'),L('6.0',H,'raised beaches')]),
'8.1':(1,[L('7.1',H,'ria examples'),L('7.0',H,'ria definition')]),
'9.b':(1,[L('5.0',E,'base level fall')]),
'9.0':(1,[L('9.b',E,'rejuvenation')]),
'9.1':(2,[L('geo-rivers-s1.1.b',H,'river long profile'),L('9.0',H,'renewed erosion upstream')]),
'9.2':(2,[L('geo-rivers-s1.10.b',E,'meanders'),L('9.0',H,'renewed downward erosion')]),
'9.3':(1,[L('9.0',E,'lowered channel from rejuvenation')]),
'10.b':(1,[L('5.0',H,'base level')]),
'10.0':(1,[L('10.b',E,'rising base level')]),
'10.1':(1,[L('10.0',E,'drowned lower course'),L('geo-rivers-s1.0.7',H,'estuary')]),
}
txt=open('/Users/gabrielwhelan/barebones/drafts/crunch/geography/packs/geo-glaciation-s2.t1g1.txt').read()
tid=[m for m in re.findall(r'^\[(geo-[^\]]+)\]',txt,re.M)]
tgt=[i for i in tid if i.startswith(P)]
assert [t[len(P):] for t in tgt]==list(D), (set(D)^set(t[len(P):] for t in tgt))
out={}
for t in tgt:
    c,n=D[t[len(P):]]
    out[t]={'cost':c,'needs':[{'id':i,'strength':s,'why':w,'confidence':f} for i,s,w,f in n]}
for v in out.values():
    for n in v['needs']: assert n['id'] in tid
open('/Users/gabrielwhelan/barebones/drafts/crunch/geography/point-links/geo-glaciation-s2.t1g1.json','w').write(json.dumps(out,indent=1))
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
