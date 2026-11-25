import json,re
D='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
counts={0:8,1:8,2:8,3:8,4:8,5:6,6:8,7:8,8:8,9:8,10:6,11:8,12:7,13:8,14:6,15:6,16:6,17:5,18:7,19:8,20:5,21:7,22:6}
ids=[]
for s,n in counts.items():
    ids.append(f'hist-eur4-s4.{s}.b')
    ids+= [f'hist-eur4-s4.{s}.{i}' for i in range(n)]
def L(i,st,w,c='high'): return {"id":i,"strength":st,"why":w,"confidence":c}
links={
'0.4':[L('hist-eur4-s3.8.0','helpful','Soviet tanks crushing Hungary 1956'),L('hist-eur4-s3.7.0','helpful','Hungary leaving the Warsaw Pact')],
'1.3':[L('hist-eur4-s3.3.5','helpful','Polish October, Gomulka elected leader')],
'1.4':[L('hist-eur4-s3.1.4','helpful','the Warsaw Pact')],
'1.5':[L('hist-eur4-s3.1.3','helpful','forced collectivisation under Sovietisation','low')],
'1.7':[L('hist-eur4-s3.13.4','helpful','Hungary crushed, Poland tolerated contrast'),L('hist-eur4-s3.8.0','helpful','Hungary 1956 crushed')],
'2.4':[L('hist-eur4-s3.7.0','essential','Nagy withdrawing Hungary from Warsaw Pact')],
'7.4':[L('hist-eur4-s3.8.0','helpful','Khrushchev using force in Hungary 1956','low')],
'11.3':[L('hist-eur4-s3.12.4','helpful','Kadar, leader since 1956')],
'11.4':[L('hist-eur4-s3.0.b','helpful','Nagy and the 1956 uprising'),L('hist-eur4-s3.14.3','helpful','memory of 1956 as symbol','low')],
'11.6':[L('hist-eur4-s3.4.1','helpful','23 October 1956 march')],
'16.0':[L('hist-eur4-s3.1.4','helpful','the Warsaw Pact')],
'21.6':[L('hist-eur4-s3.8.0','helpful','Khrushchev using force in Hungary','low')],
'22.5':[L('hist-eur4-s3.14.0','helpful','Soviet control resting on force, 1956')],
}
out={i:{"needs":links.get(i.split('s4.')[1],[])} for i in ids}
txt=open(D+'packs/hist-eur4-s4.t1g3.txt').read()
tg=[m for m in re.findall(r'^\[(hist-eur4-s4\.[^\]]+)\]',txt,re.M)]
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
assert tg==ids,(set(tg)^set(ids))
for v in out.values():
    for n in v['needs']: assert n['id'] in allids and n['id'] not in tg
json.dump(out,open(D+'point-links/hist-eur4-s4.t1g3.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
