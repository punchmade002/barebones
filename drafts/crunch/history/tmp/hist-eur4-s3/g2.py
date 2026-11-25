import json,re
H='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
hp='helpful'
L={ # short target -> [(s2 id, why, conf)]
'0.2':[('2.3.2','Malenkov\'s fall as premier','high')],
'1.4':[('2.0.2','NATO and Warsaw Pact alliances','low')],
'1.5':[('2.0.5','Stalin\'s death and succession','high')],
'3.1':[('2.4.0','Khrushchev\'s secret speech','high')],
'3.5':[('2.4.3','Polish October and Gomułka','high')],
'6.4':[('2.0.4','Soviet Presidium','high')],
'7.3':[('2.8.1','Khrushchev\'s rapprochement with Tito','low')],
'10.2':[('2.15.1','Dulles and massive retaliation','low')],
'10.3':[('2.0.6','Soviet nuclear power','low')],
'13.2':[('2.15.0','nuclear deterrence and war risk','low')],
'13.4':[('2.4.3','Gomułka and Polish October','high')],
'14.0':[('2.4.1','limits of de-Stalinisation','high'),('2.23.4','1968 Czechoslovak invasion','low')],
}
txt=open(H+'packs/hist-eur4-s3.t1g2.txt').read()
tids=re.findall(r'^\[(hist-eur4-s3\.[\w.]+)\]',txt.split('CANDIDATES')[0],re.M)
allids=set(re.findall(r'^\[([\w.\-]+)\]',txt,re.M))
out={}
for t in tids:
    k=t[len('hist-eur4-s3.'):]
    out[t]={'needs':[{'id':'hist-eur4-s'+i,'strength':hp,'why':w,'confidence':c} for i,w,c in L.get(k,[])]}
for v in out.values():
    for n in v['needs']: assert n['id'] in allids,n
assert all(k in [t[13:] for t in tids] for k in L)
json.dump(out,open(H+'point-links/hist-eur4-s3.t1g2.json','w'),ensure_ascii=False,indent=0)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
