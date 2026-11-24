import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
S='geo-population-migration-s1.'
def L(i,s,w,c='high'):
    return {"id":i if i.startswith('geo-') else S+i,"strength":s,"why":w,"confidence":c}
E,H='essential','helpful'
D={
'24.2':(1,[L('16.b',H,'stage 2 death rate fall')]),
'24.3':(1,[]),
'25.b':(1,[]),
'25.0':(1,[]),
'25.1':(1,[L('25.0',H,'what a pyramid shows')]),
'26.b':(1,[L('25.0',E,'reading pyramid shape')]),
'26.0':(1,[L('20.4',H,'Niger pyramid base','low')]),
'26.1':(1,[L('18.b',H,'stage 4 steady rates','low')]),
'26.2':(1,[L('21.4',H,'Japan top-heavy pyramid')]),
'26.3':(1,[L('26.0',H,'pyramid shapes','low')]),
'27.b':(1,[L('25.0',E,'pyramid sides')]),
'27.0':(1,[L('25.0',H,'age bands on pyramid')]),
'27.1':(1,[L('0.3',H,'emigration and migration')]),
'27.2':(1,[L('0.7',H,'life expectancy')]),
'28.b':(1,[L('geo-graph-skills-s2.8.0',H,'age groups, dependants')]),
'28.0':(1,[L('geo-graph-skills-s2.8.0',H,'age groups used')]),
'28.1':(1,[L('28.0',E,'dependency ratio formula')]),
'28.2':(1,[L('28.0',E,'formula applied')]),
'29.b':(1,[L('28.b',H,'dependency ratio')]),
'29.0':(1,[L('28.0',E,'dependency ratio')]),
'29.1':(1,[L('28.0',E,'share of dependants')]),
'30.b':(1,[L('28.1',E,'old-age dependency ratio')]),
'30.0':(1,[]),'30.1':(1,[]),'30.2':(1,[]),'30.3':(1,[]),'30.4':(1,[]),
'30.5':(2,[L('23.1',H,'responses to ageing','low')]),
'31.b':(1,[L('28.1',H,'young dependency ratio')]),
'31.0':(1,[]),
'31.1':(2,[]),
'32.b':(1,[]),'32.0':(1,[]),'32.1':(1,[]),'32.2':(1,[]),'32.3':(1,[]),'32.4':(1,[]),
'32.5':(1,[L('0.6',H,'infant mortality rate')]),
'32.6':(1,[]),
'33.b':(1,[]),'33.0':(1,[]),'33.1':(1,[]),'33.2':(1,[]),'33.3':(1,[]),
'34.b':(1,[L('25.0',E,'pyramid base and top')]),
'34.0':(1,[L('25.0',E,'pyramid base')]),
'34.1':(1,[L('0.7',H,'life expectancy'),L('25.0',E,'pyramid top')]),
'34.2':(1,[L('20.3',H,'median age')]),
'35.b':(1,[L('0.7',H,'life expectancy')]),
'35.0':(1,[]),'35.1':(1,[]),'35.2':(1,[]),'35.3':(1,[]),'35.4':(1,[]),'35.5':(1,[]),
'36.b':(1,[L('0.7',H,'life expectancy')]),
'36.0':(1,[]),'36.1':(1,[]),'36.2':(1,[]),'36.3':(1,[]),'36.4':(1,[]),
'37.b':(1,[L('1.1.1',H,'census counts')]),
'37.0':(1,[]),'37.1':(1,[]),'37.2':(1,[]),'37.3':(1,[]),'37.4':(1,[]),
'38.b':(1,[]),'38.0':(1,[]),'38.1':(1,[]),
'38.2':(2,[]),
'38.3':(1,[]),
'39.b':(1,[]),'39.0':(1,[]),'39.1':(1,[]),
'39.2':(2,[L('0.5',E,'replacement level'),L('0.4',E,'total fertility rate')]),
'39.3':(1,[L('0.2',E,'natural increase')]),
'40.b':(1,[]),'40.0':(1,[]),'40.1':(1,[]),'40.2':(1,[]),'40.3':(1,[]),'40.4':(1,[]),
'41.b':(1,[]),
'41.0':(1,[L('0.7',E,'life expectancy')]),
'41.1':(1,[L('27.2',H,'women outnumber men old')]),
'41.2':(1,[L('0.6',E,'infant mortality rate')]),
'42.b':(1,[L('0.3',H,'net migration')]),
'42.0':(2,[L('0.3',E,'net migration')]),
'42.1':(1,[L('0.3',H,'net migration')]),
'43.b':(1,[]),
'43.0':(1,[L('geo-graph-skills-s2.8.0',H,'65 and over group','low')]),
'43.1':(1,[]),'43.2':(1,[]),
'43.3':(1,[L('26.2',H,'ageing pyramid shape')]),
'43.4':(1,[]),
'44.b':(1,[]),'44.0':(1,[]),'44.1':(1,[]),
'44.2':(1,[L('10.b',H,'east-west distribution')]),
'44.3':(1,[]),
'45.b':(1,[]),'45.0':(1,[]),
'45.1':(1,[L('0.5',E,'replacement level')]),
'45.2':(1,[L('0.2',E,'natural decrease')]),
'45.3':(1,[L('20.3',H,'median age')]),
'46.b':(1,[L('19.b',E,'stage 5')]),
'46.0':(1,[L('0.2',E,'natural decrease')]),
'46.1':(1,[L('0.3',H,'immigration drives growth')]),
'47.b':(1,[L('19.b',E,'stage 5')]),
'47.0':(1,[L('0.4',E,'total fertility rate')]),
'47.1':(1,[]),'47.2':(1,[]),
'48.b':(1,[]),'48.0':(1,[]),
'48.1':(1,[L('0.3',H,'emigration')]),
'49.b':(1,[L('0.5',H,'replacement level')]),
'49.0':(1,[L('0.4',E,'total fertility rate')]),
'49.1':(1,[L('20.2',H,'Niger fertility figure')]),
}
txt=open(P+'packs/geo-population-migration-s1.t2g1.txt').read()
tg=txt.split('CANDIDATES')[0]
tids=re.findall(r'^\[([^\]]+)\]',tg,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
out={}
for t in tids:
    k=t[len(S):]
    c,n=D[k]; out[t]={"cost":c,"needs":n}
assert len(out)==len(D)==len(tids),(len(out),len(D),len(tids))
for t,v in out.items():
    for n in v['needs']: assert n['id'] in allids and n['id']!=t,n
json.dump(out,open(P+'point-links/geo-population-migration-s1.t2g1.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
