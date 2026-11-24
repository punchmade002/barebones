import json,re
P='geo-region-ireland-s1.t2g4'
txt=open(f'packs/{P}.txt').read()
tgt=[];cand=set();sec=None
for l in txt.split('\n'):
    if l.startswith('TARGET'):sec='t'
    elif l.startswith('CANDIDATES'):sec='c'
    m=re.match(r'\[([^\]]+)\]',l)
    if m:(tgt if sec=='t' else cand).add(m.group(1)) if sec=='c' else tgt.append(m.group(1))
L=lambda i,s,w,c='high':{"id":"geo-population-migration-s1."+i,"strength":s,"why":w,"confidence":c}
links={
'32.3':[L('4.1','helpful','uses density formula')],
'33.0':[L('4.0','helpful','uses density idea')],
'33.1':[L('5.0','helpful','relief limits settlement')],
'33.2':[L('6.0','helpful','jobs attract people')],
'33.3':[L('5.0','helpful','lowland relief aids settlement')],
'33.4':[L('6.1','helpful','transport routes attract settlement')],
'34.b':[L('1.0','helpful','population change components')],
'34.0':[L('0.2','essential','natural increase definition')],
'34.1':[L('0.3','helpful','net migration idea')],
'34.2':[L('28.0','helpful','dependency ratio','low')],
}
out={}
for t in tgt:
    k=t.split('geo-region-ireland-s1.')[1]
    out[t]={"needs":links.get(k,[])}
json.dump(out,open(f'point-links/{P}.json','w'),indent=1)
o=json.load(open(f'point-links/{P}.json'))
assert list(o)==tgt and len(set(tgt))==len(tgt)
for v in o.values():
    for n in v['needs']:assert n['id'] in cand,n
print(len(o),sum(len(v['needs']) for v in o.values()),sum(n['confidence']=='low' for v in o.values() for n in v['needs']))
