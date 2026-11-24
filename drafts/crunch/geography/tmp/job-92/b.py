import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
p='geo-region-concept-s4.'
H,E='helpful','essential'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
S1='geo-region-concept-s1.'; G='geo-economic-activities-s1.'
d=[
('0.b',1,[L(S1+'0.3',H,'socio-economic criteria'),L(S1+'1.2',H,'multiple indices')]),
('0.0',1,[L(p+'0.1',H,'primary/secondary/tertiary mix'),L(S1+'1.2',H,'multiple indices together')]),
('0.1',1,[]),
('0.2',2,[L(S1+'1.2',H,'peripheral region defined')]),
('0.3',2,[L(p+'0.2',E,'core and periphery idea')]),
('1.b',1,[L(p+'0.2',H,'core in core-periphery')]),
('1.0',1,[L(p+'0.0',H,'GDP per head indicator')]),
('1.1',1,[L(p+'0.1',E,'tertiary sector defined')]),
('1.2',1,[]),
('1.3',1,[]),
('1.4',1,[]),
('1.5',1,[]),
('1.6',2,[]),
('1.7',1,[]),
('2.b',1,[L(p+'1.b',H,'what a core region is')]),
('2.0',1,[L(p+'1.b',H,'core region idea')]),
('2.1',2,[L(G+'25.1',H,'Google docklands cluster','low')]),
('2.2',1,[L(p+'1.b',H,'core region idea')]),
('2.3',2,[L(p+'1.b',H,'core region idea')]),
('3.b',1,[L(p+'0.2',H,'periphery in core-periphery')]),
('3.0',1,[]),
('3.1',1,[]),
('3.2',1,[L(p+'0.1',E,'primary activity defined')]),
('3.3',1,[]),
('3.4',1,[L(p+'1.3',H,'net migration meaning')]),
('3.5',1,[]),
('4.b',1,[L(p+'3.b',H,'peripheral region falling behind')]),
('4.0',1,[]),
('4.1',1,[]),
('4.2',1,[]),
('4.3',1,[]),
('5.b',1,[L(p+'3.b',H,'peripheral region defined')]),
('5.0',1,[L(G+'58.1',H,'West of Ireland economy')]),
('5.1',1,[]),
('5.2',1,[]),
('5.3',1,[]),
('6.b',1,[]),
('6.0',1,[]),
('6.1',1,[L(p+'0.0',H,'GDP per head indicator')]),
('6.2',1,[L(p+'3.b',H,'peripheral region defined')]),
('6.3',2,[L(p+'3.b',E,'peripheral region defined'),L(p+'6.0',E,'less-developed region defined')]),
('6.4',2,[L(G+'58.2',H,'BMW region EU designation'),L(p+'6.1',H,'EU aid categories')]),
('6.5',1,[]),
('6.6',1,[]),
('7.b',1,[]),
('7.0',1,[]),
('7.1',2,[]),
('7.2',1,[]),
('7.3',1,[]),
('7.4',1,[]),
('7.5',2,[L(p+'7.3',H,'effects being responded to')]),
('8.b',1,[]),
('8.0',1,[L(p+'7.0',H,'coal and steel decline')]),
('8.1',1,[L(p+'7.0',H,'coal and steel decline')]),
('8.2',2,[L(p+'7.5',H,'reuse of industrial heritage','low')]),
('8.3',1,[L(p+'7.0',H,'coalfield decline')]),
('8.4',1,[]),
('8.5',1,[]),
('8.6',2,[L(G+'32.b',H,'IFSC regeneration case study')]),
('8.7',1,[]),
('9.b',1,[L(p+'0.1',E,'primary/secondary/tertiary')]),
('9.0',1,[]),
('9.1',1,[]),
('9.2',1,[]),
]
out={p+k:{"cost":c,"needs":n} for k,c,n in d}
assert len(out)==len(d)
t=open(P+'packs/geo-region-concept-s4.t1g1.txt').read()
tg=re.findall(r'^\[(geo-region-concept-s4\.[^\]]+)\]',t,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',t,re.M))
assert list(out)==tg,(set(tg)^set(out))
for v in out.values():
  for n in v['needs']: assert n['id'] in allids,n
json.dump(out,open(P+'point-links/geo-region-concept-s4.t1g1.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
