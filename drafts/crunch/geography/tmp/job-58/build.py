import json,re
P='geo-option-geoecology-s1.'
pk={'W3':'geo-rocks-weathering-s3.','R1':'geo-rocks-weathering-s1.','G1':'geo-glaciation-s1.','g':P,'V1':'geo-rivers-s1.'}
base='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
def tok(t):
    a,rest=t.split(':',1); i,s,c,w=rest.split(',',3)
    return {'id':pk[a]+i,'strength':'essential' if s=='e' else 'helpful','why':w,'confidence':'high' if c=='H' else 'low'}
ids=[l.split('|')[0] for l in open('t1.txt').read().split('\n') if l]
out1={};
for l in open('t1.txt').read().split('\n'):
    if not l: continue
    i,c,n=l.split('|')
    out1[P+i]={'cost':int(c),'needs':[tok(t) for t in n.split(';') if t]}
# package 2: links only to rivers-s1
l2={}
for l in open('t2.txt').read().split('\n'):
    if l: i,t=l.split('|',1); l2[P+i]=[tok(t)]
out2={k:{'needs':l2.get(k,[])} for k in out1}
for k,v in out1.items():
    for n in v['needs']: assert n['id']!=k
json.dump(out1,open(base+'point-links/geo-option-geoecology-s1.t1g1.json','w'),indent=1)
json.dump(out2,open(base+'point-links/geo-option-geoecology-s1.t1g2.json','w'),indent=1)
pack=open(base+'packs/geo-option-geoecology-s1.t1g1.txt').read()
pack2=open(base+'packs/geo-option-geoecology-s1.t1g2.txt').read()
tg=re.findall(r'^\[(geo-option-geoecology-s1\.[^\]]+)\]',pack,re.M)
tg2=re.findall(r'^\[(geo-option-geoecology-s1\.[^\]]+)\]',pack2,re.M)
assert sorted(tg)==sorted(out1) and sorted(tg2)==sorted(out2),(set(tg)^set(out1))
allids=set(re.findall(r'^\[([^\]]+)\]',pack,re.M));allids2=set(re.findall(r'^\[([^\]]+)\]',pack2,re.M))
for v in out1.values():
    for n in v['needs']: assert n['id'] in allids,n
for v in out2.values():
    for n in v['needs']: assert n['id'] in allids2,n
print(len(out1),sum(len(v['needs']) for v in out1.values()),sum(v['cost']==2 for v in out1.values()),sum(n['confidence']=='low' for v in out1.values() for n in v['needs']))
print(len(out2),sum(len(v['needs']) for v in out2.values()),sum(n['confidence']=='low' for v in out2.values() for n in v['needs']))
