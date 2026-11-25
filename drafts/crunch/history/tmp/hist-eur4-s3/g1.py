import json,re,sys
H='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
P='hist-eur4-s3.'
# id: (cost, [(target, strength, why, conf)])  ids starting 's1.' are candidates in hist-eur4-s1
E,H_='essential','helpful'
D={
'0.b':(1,[]),
'0.0':(2,[('s1.11.4',H_,'1945 land reform to peasants','high')]),
'0.1':(2,[('3.2.0',E,'Rákosi criticised and opposed','high'),('3.1.5',H_,'Soviet leadership change after Stalin','low')]),
'0.2':(2,[('0.1',E,'Nagy\'s New Course and premiership','high'),('3.2.0',H_,'Rákosi as first secretary','high')]),
'0.3':(1,[('3.4.0',E,'student demands of 22 October','high'),('0.2',H_,'Nagy removed and expelled earlier','high')]),
'0.4':(2,[('3.7.0',H_,'neutrality declaration of 1 November','high'),('3.8.1',H_,'4 November broadcast and embassy','high')]),
'0.5':(2,[('3.9.2',E,'safe-conduct guarantee and seizure','high'),('3.12.4',H_,'Kádár government','high')]),
'0.6':(1,[('3.15.2',H_,'counter-revolution versus revolution labels','high')]),
'0.7':(1,[('3.14.3',H_,'1989 reburial and reassessment','high')]),
'1.b':(1,[]),
'1.0':(1,[]),
'1.1':(1,[('s1.11.2',H_,'salami tactics','high')]),
'1.2':(1,[]),
'1.3':(1,[]),
'1.4':(1,[('s1.19.5',H_,'Warsaw Pact formation','high')]),
'1.5':(1,[]),
'2.b':(1,[]),
'2.0':(1,[('s1.13.1',H_,'Rajk show trial','high')]),
'2.1':(1,[('3.2.0',H_,'Rákosi\'s rule','high')]),
'2.2':(1,[]),
'2.3':(1,[('3.1.3',H_,'collectivised farms, Sovietisation','high')]),
'2.4':(1,[]),
'2.5':(1,[]),
'3.b':(1,[]),
'3.0':(1,[('0.1',E,'Nagy\'s New Course','high')]),
'3.1':(1,[('3.1.5',H_,'de-Stalinisation','high')]),
'3.2':(1,[]),
'3.3':(1,[('3.2.0',E,'Rákosi\'s rule','high')]),
'3.4':(1,[('3.2.0',E,'Rajk executed under Rákosi','high')]),
'3.5':(1,[('s1.12.4',H_,'Gomułka and Poland','low')]),
'4.b':(1,[]),
'4.0':(2,[('0.3',H_,'why students wanted Nagy','high')]),
'4.1':(1,[('3.3.5',H_,'sympathy with Poland','high')]),
'4.2':(1,[('3.3.3',H_,'Gerő as party leader','high')]),
'4.3':(1,[('3.2.1',E,'the AVH secret police','high')]),
'4.4':(1,[('4.3',H_,'fighting begun at radio building','high')]),
'5.b':(1,[]),
'5.0':(2,[('3.3.3',H_,'Gerő and Mikoyan','high')]),
'5.1':(1,[('3.4.4',H_,'Soviet troops in Budapest','high')]),
'5.2':(1,[]),
'5.3':(1,[]),
'5.4':(1,[('3.2.1',H_,'the AVH','high')]),
'6.b':(1,[]),
'6.0':(1,[('5.4',H_,'promise Soviet troops would leave','high')]),
'6.1':(2,[('s1.12.5',H_,'Smallholders\' 1945 election win','low')]),
'6.2':(1,[('3.2.1',H_,'the AVH','high')]),
'6.3':(1,[('3.2.2',E,'Mindszenty\'s imprisonment','high')]),
'6.4':(1,[('6.0',H_,'Soviet withdrawal from Budapest','high')]),
'7.b':(1,[]),
'7.0':(1,[('1.4',H_,'the Warsaw Pact','high')]),
'7.1':(1,[('7.0',E,'neutrality and Pact withdrawal','high')]),
'7.2':(1,[('3.12.4',H_,'Kádár background','low')]),
'7.3':(1,[('s1.14.3',H_,'Tito\'s break with Stalin','low')]),
'7.4':(1,[('5.2',H_,'Maléter','high')]),
'8.b':(1,[]),
'8.0':(1,[('7.1',H_,'why Moscow attacked','high')]),
'8.1':(1,[('8.0',H_,'the 4 November attack','high')]),
'8.2':(1,[('6.3',E,'Mindszenty freed on 30 October','high')]),
'8.3':(1,[('7.2',E,'Kádár taken to Moscow','high')]),
'9.b':(1,[]),
'9.0':(1,[('8.0',H_,'the Soviet attack','high')]),
'9.1':(1,[('5.3',H_,'workers\' councils','high')]),
'9.2':(1,[('8.1',E,'Nagy in Yugoslav embassy','high'),('8.3',H_,'Kádár\'s government','high')]),
'9.3':(1,[('9.2',E,'seizure from the embassy','high'),('7.3',H_,'Tito accepting intervention','high')]),
'10.b':(1,[]),
'10.0':(2,[]),
'10.1':(1,[('10.0',E,'the Suez crisis','high')]),
'10.2':(1,[('s1.7.2',H_,'containment policy','low')]),
'10.3':(1,[('10.2',H_,'US attitude to satellites','high')]),
'10.4':(1,[('8.0',H_,'4 November attack','high')]),
'10.5':(1,[('10.4',H_,'UN failure to act','high')]),
'11.b':(1,[]),
'11.0':(1,[]),
'11.1':(1,[('11.0',E,'Radio Free Europe broadcasts','high')]),
'11.2':(1,[('12.1',H_,'200,000 fled to Austria','high')]),
'11.3':(1,[('11.2',H_,'refugees welcomed','high')]),
'11.4':(1,[]),
'12.b':(1,[]),
'12.0':(1,[]),
'12.1':(1,[]),
'12.2':(1,[]),
'12.3':(1,[('0.5',H_,'Nagy and Maléter\'s trial','high')]),
'12.4':(2,[('3.2.0',H_,'Rákosi imprisoned Kádár','high'),('7.2',H_,'Kádár\'s 1956 party','low')]),
'12.5':(1,[('12.4',E,'Kádár\'s rule','high')]),
'12.6':(1,[('12.5',H_,'Kádár\'s compromise','high')]),
'13.b':(1,[]),
'13.0':(1,[('7.0',E,'Warsaw Pact exit, one-party end','high')]),
'13.1':(1,[('8.0',H_,'Soviet attack force','high')]),
'13.2':(2,[('10.1',H_,'Suez distracting West','high'),('10.3',H_,'nuclear war fear','high')]),
'13.3':(1,[('8.3',E,'Kádár\'s government installed','high')]),
'13.4':(2,[('3.3.5',E,'Gomułka and Polish October','high'),('7.0',H_,'Hungary leaving Pact','high')]),
'14.b':(1,[]),
'14.0':(1,[('8.0',H_,'Soviet force used','high')]),
'14.1':(1,[('10.2',H_,'liberation talk empty','high')]),
'14.2':(1,[('10.0',H_,'Suez crisis','high')]),
'14.3':(1,[('0.7',H_,'Nagy reburial','high')]),
'14.4':(1,[('14.3',H_,'1989 reassessment','high')]),
'15.b':(1,[]),
'15.0':(2,[('6.1',H_,'multi-party government','high'),('7.0',H_,'neutrality declaration','high')]),
'15.1':(2,[('12.1',H_,'200,000 refugees','high')]),
'15.2':(2,[('0.6',H_,'contemporary disagreement','high')]),
'15.3':(1,[('4.0',H_,'student demands','high')]),
'15.4':(2,[('14.3',H_,'Pozsgay and reburial','high')]),
}
txt=open(H+'packs/hist-eur4-s3.t1g1.txt').read()
tgt=txt.split('CANDIDATES')[0]
tids=re.findall(r'^\[(hist-eur4-s3\.[\w.]+)\]',tgt,re.M)
allids=set(re.findall(r'^\[([\w.\-]+)\]',txt,re.M))
def full(k): return 'hist-eur4-s1.'+k[3:] if k.startswith('s1.') else ('hist-eur4-s'+k if k.count('.')==2 else P+k)
out={}
for t in tids:
    k=t[len(P):]
    assert k in D,k
    c,l=D[k]
    out[t]={'cost':c,'needs':[{'id':full(x),'strength':s,'why':w,'confidence':f} for x,s,w,f in l]}
assert len(out)==len(D)==len(tids)
for v in out.values():
    for n in v['needs']: assert n['id'] in allids,n
for t,v in out.items():
    for n in v['needs']: assert n['id']!=t
json.dump(out,open(H+'point-links/hist-eur4-s3.t1g1.json','w'),ensure_ascii=False,indent=0)
n=sum(len(v['needs']) for v in out.values())
print(len(out),n,sum(v['cost']==2 for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
