import json,re
src=json.load(open('point-links/hist-eur2-s8.t1g1.json'))
pk=open('packs/hist-eur2-s8.t1g2.txt').read()
tids=re.findall(r'^\[(\S+?)\]',pk.split('CANDIDATES')[0],re.M); allids=set(re.findall(r'^\[(\S+?)\]',pk,re.M))
assert tids==list(src)
def L(i,w,c='high'): return {"id":"hist-eur2-s"+i,"strength":"helpful","why":w,"confidence":c}
X={'3.1':[L('2.1.2','Franco-Russian Alliance')],
'7.0':[L('2.9.2','Port Arthur and Manchuria claims')],
'7.2':[L('2.9.2','Port Arthur lease and spheres','low')],
'7.4':[L('2.9.6','Russo-Japanese War settlement')],
'9.3':[L('2.1.6','French investment in Russia')],
'19.1':[L('2.1.6','dependence on French capital','low')]}
D={k:{"needs":X.get(k[len('hist-eur2-s8.'):],[])} for k in tids}
for v in D.values():
    for n in v['needs']: assert n['id'] in allids
json.dump(D,open('point-links/hist-eur2-s8.t1g2.json','w'),indent=0)
print(len(D),sum(len(v['needs']) for v in D.values()),sum(n['confidence']=='low' for v in D.values() for n in v['needs']))
