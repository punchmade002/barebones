import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
S='geo-region-european-s2.'; C='geo-region-concept-s4.'; V='geo-volcanoes-earthquakes-s1.'
H,E='helpful','essential'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
# id: (cost, links)
d={
'0.b':(1,[L(C+'3.b',H,'peripheral region defined')]),
'0.0':(2,[]),'0.1':(1,[]),'0.2':(2,[]),'0.3':(1,[]),'0.4':(1,[]),
'1.b':(1,[L(C+'0.2',H,'core-periphery idea')]),
'1.0':(1,[L(S+'1.b',H,'distance from economic core')]),
'1.1':(1,[L(S+'1.b',H,'defines relief')]),
'1.2':(2,[L(S+'8.0',H,'large estates (latifundia)','low')]),
'1.3':(1,[]),'1.4':(2,[]),'1.5':(1,[]),
'1.6':(1,[L(C+'4.2.2'.replace('4.2.2','2.2') if False else C+'2.2'[0:0]+'4.2.2',H,'Paris Basin as core')]),
'2.b':(1,[]),
'2.0':(2,[]),'2.1':(2,[]),
'2.2':(2,[L(S+'4.0',H,'Apennines'),L(S+'4.5',H,'Etna')]),
'2.3':(2,[L(S+'4.3',H,'Tavoliere plain'),L(S+'4.4',H,'Campanian and Catania plains')]),
'2.4':(1,[L(S+'10.0',H,'durum wheat on Tavoliere'),L('geo-region-european-s2.16.2',H,'Bari-Brindisi-Taranto triangle')]),
'3.b':(1,[]),'3.0':(2,[]),'3.1':(1,[]),'3.2':(1,[]),'3.3':(1,[]),'3.4':(1,[]),'3.5':(1,[]),
'3.6':(1,[L(S+'3.0',H,'dry summers')]),
'3.7':(1,[L(S+'3.6',E,'responds to drought and floods')]),
'4.b':(1,[]),'4.0':(1,[]),
'4.1':(1,[L(S+'4.0',H,'Apennines')]),
'4.2':(1,[]),'4.3':(1,[]),'4.4':(1,[]),
'4.5':(1,[L(V+'9.0',H,'fertile volcanic soils')]),
'4.6':(1,[]),
'5.b':(1,[]),
'5.0':(2,[L(V+'4.b',H,'plate boundaries cause volcanoes')]),
'5.1':(2,[]),'5.2':(1,[]),'5.3':(2,[]),'5.4':(2,[]),
'5.5':(1,[L(S+'5.0',E,'plate boundary beneath region')]),
'5.6':(2,[]),
'6.b':(1,[]),'6.0':(1,[]),'6.1':(1,[]),
'6.2':(1,[L(V+'9.0',H,'fertile volcanic soils')]),
'6.3':(1,[]),'6.4':(1,[]),
'6.5':(1,[L(S+'12.0',H,'deforestation exposes slopes')]),
'6.6':(2,[L(V+'1.7',H,'lahars are mudflows')]),
'7.b':(1,[L(S+'3.b',H,'wet winter, dry summer')]),
'7.0':(1,[]),
'7.1':(1,[L(S+'3.2',H,'wet winters')]),
'7.2':(1,[L(S+'3.0',H,'dry summers')]),
'7.3':(1,[]),'7.4':(1,[]),
'7.5':(2,[L(S+'3.4',H,'low rainfall in Puglia','low')]),
'8.b':(1,[]),'8.0':(1,[]),
'8.1':(1,[L(S+'8.0',H,'latifundia')]),
'8.2':(1,[L(S+'8.0',H,'estates')]),
'8.3':(1,[]),
'8.4':(1,[L(S+'8.b',H,'defines productivity')]),
'9.b':(1,[L(S+'8.b',H,'old estate system')]),
'9.0':(1,[L(S+'8.0',H,'large estates')]),
'9.1':(1,[]),
'9.2':(2,[L(S+'9.1',H,'the Cassa')]),
'9.3':(1,[L(S+'9.2',H,'reclaimed lowlands')]),
'9.4':(1,[]),
'9.5':(1,[L(S+'9.1',E,'the Cassa')]),
'10.b':(1,[]),
'10.0':(1,[L(S+'4.3',H,'Tavoliere plain')]),
'10.1':(1,[L(S+'3.7',H,'drought-tolerant crops')]),
'10.2':(1,[L(S+'4.4',H,'plain of Catania')]),
'10.3':(1,[]),
'10.4':(1,[L(S+'4.4',H,'Campanian plain')]),
'10.5':(1,[]),
'10.6':(1,[L(S+'10.b',H,'specialised Mediterranean produce')]),
'11.b':(1,[]),
'11.0':(1,[L(S+'3.6',H,'summer drought')]),
'11.1':(1,[L(S+'6.5',H,'soil erosion causes')]),
'11.2':(1,[]),
'11.3':(1,[L('geo-region-european-s2.26.2',H,'out-migration of young','low')]),
'11.4':(1,[]),'11.5':(1,[]),
'12.b':(1,[]),'12.0':(1,[]),
'12.1':(1,[L(S+'9.1',H,'the Cassa')]),
'12.2':(1,[L(S+'3.0',H,'dry hot summers')]),
'13.b':(1,[]),'13.0':(1,[]),'13.1':(1,[]),'13.2':(1,[]),
'14.b':(1,[]),'14.0':(1,[]),
'14.1':(2,[L(S+'13.0',H,'Mazara del Vallo','low')]),
'14.2':(1,[]),'14.3':(1,[]),
'15.b':(1,[]),
'15.0':(1,[L(S+'1.0',H,'distance raises transport cost')]),
'15.1':(1,[]),
}
d['1.6']=(1,[L(C+'2.2',H,'Paris Basin as core')])
ids=[l.split(']')[0][1:] for l in open(P+'packs/geo-region-european-s2.t1g1.txt').read().split('\n') if l.startswith('[geo-region-european-s2.')]
tg=ids[:ids.index('geo-region-european-s2.15.1')+1]
tg=[i for i in tg]
assert len(tg)==104,len(tg)
out={}
for i in tg:
    k=i.split('s2.')[1]; c,n=d[k]; out[i]={"cost":c,"needs":n}
assert len(d)==104
allids=set(ids)|{l.split(']')[0][1:] for l in open(P+'packs/geo-region-european-s2.t1g1.txt').read().split('\n') if l.startswith('[')}
for v in out.values():
    for n in v['needs']: assert n['id'] in allids,n
json.dump(out,open(P+'point-links/geo-region-european-s2.t1g1.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))

# package 2
E2='geo-economic-activities-s2.'; Q='geo-volcanoes-earthquakes-s2.'
d2={'1.0':[L(E2+'3.0',H,'markets and transport cost','low')],
'5.0':[L(Q+'5.b',H,'earthquakes at plate boundaries')],
'5.1':[L(Q+'11.1',H,'earthquake-triggered tsunami','low')],
'5.3':[L(Q+'4.0',H,'magnitude')],
'15.0':[L(E2+'0.b',H,'transport costs shape location')],
'15.1':[L(E2+'1.7',H,'infrastructure')]}
o2={i:{"needs":d2.get(i.split('s2.')[1],[])} for i in tg}
a2=set(l.split(']')[0][1:] for l in open(P+'packs/geo-region-european-s2.t1g2.txt').read().split('\n') if l.startswith('['))
for v in o2.values():
    for n in v['needs']: assert n['id'] in a2,n
json.dump(o2,open(P+'point-links/geo-region-european-s2.t1g2.json','w'),indent=1)
print(len(o2),sum(len(v['needs']) for v in o2.values()),sum(n['confidence']=='low' for v in o2.values() for n in v['needs']))
