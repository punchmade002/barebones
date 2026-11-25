import json,re
B='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
P='hist-eur6-s13.'
E,H='essential','helpful'
def L(i,s,w,c='high'): return {"id":i if i.startswith('hist') else P+i,"strength":s,"why":w,"confidence":c}
# id: (cost, links)
D={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),'0.2':(2,[]),'0.3':(1,[]),
'0.4':(1,[L('0.3',E,'uses military-industrial complex')]),
'0.5':(1,[L('0.3',H,'military-industrial complex')]),
'1.b':(1,[]),'1.0':(1,[L('0.1',H,'1949 Soviet atomic test')]),
'1.1':(1,[L('1.b',H,'hydrogen bomb')]),
'1.2':(1,[L('1.1',E,'opposed the hydrogen bomb decision')]),
'1.3':(1,[L('1.b',H,'thermonuclear weapon')]),
'1.4':(1,[L('1.3',H,'American thermonuclear test lead')]),
'2.b':(1,[]),'2.0':(1,[]),'2.1':(2,[]),
'2.2':(1,[L('2.1',E,'uses ICBMs')]),
'2.3':(1,[]),'2.4':(2,[L('2.3',H,'nuclear-powered submarines')]),
'2.5':(2,[L('2.1',H,'Minuteman missiles')]),
'2.6':(1,[L('2.5',E,'uses MIRVs'),L('hist-eur6-s5.4.3',H,'arms control limits on warheads','low')]),
'3.b':(1,[]),'3.0':(1,[]),
'3.1':(1,[L('3.0',E,'the missile gap claim'),L('2.1',H,'ICBM numbers')]),
'3.2':(1,[]),'3.3':(1,[L('3.2',H,'risky U-2 flights')]),
'4.b':(1,[]),'4.0':(1,[L('0.3',E,'military-industrial complex')]),
'4.1':(1,[]),'4.2':(1,[]),'4.3':(1,[]),
'4.4':(1,[L('4.3',E,'uses SDI')]),
'5.b':(1,[]),'5.0':(1,[]),
'5.1':(2,[L('5.0',H,'Sputnik launch'),L('0.2',H,'von Braun')]),
'5.2':(1,[L('5.0',E,'Sputnik launch')]),
'5.3':(1,[L('5.2',H,'alarm over Soviet education')]),
'5.4':(1,[]),
'5.5':(1,[L('5.0',H,'created after Sputnik')]),
'6.b':(1,[]),'6.0':(1,[]),'6.1':(1,[]),
'6.2':(1,[L('6.1',H,'Mercury programme')]),
'6.3':(1,[L('6.2',H,'compared with Shepard flight')]),
'6.4':(1,[]),
'7.b':(1,[]),
'7.0':(1,[L('6.0',E,'Gagarin flight'),L('hist-eur6-s2.9.4',E,'Bay of Pigs invasion')]),
'7.1':(1,[L('7.0',H,'why Kennedy decided')]),
'7.2':(1,[L('7.1',H,'Moon goal')]),
'7.3':(2,[L('9.1',H,'command and lunar modules')]),
'7.4':(2,[L('7.3',H,'rendezvous method')]),
'7.5':(1,[]),
'8.b':(1,[]),
'8.0':(2,[L('9.1',H,'command and lunar modules'),L('9.0',H,'Saturn V stages')]),
'8.1':(1,[]),
'8.2':(2,[L('0.2',H,'von Braun')]),
'8.3':(1,[]),'8.4':(1,[]),'8.5':(1,[]),
'8.6':(1,[L('8.5',H,'cost of Apollo')]),
'9.b':(1,[]),'9.0':(1,[]),'9.1':(1,[]),
'9.2':(1,[L('15.4',H,'integrated circuit','low')]),
'9.3':(1,[L('9.1',H,'Apollo spacecraft')]),
'9.4':(2,[L('9.1',H,'command module')]),
'9.5':(1,[L('9.4',E,'Apollo 8 mission')]),
'9.6':(1,[L('9.1',H,'lunar module')]),
'10.b':(1,[]),
'10.0':(1,[L('9.1',H,'command and lunar modules')]),
'10.1':(1,[L('9.0',H,'Saturn V')]),
'10.2':(1,[L('9.1',H,'lunar module')]),
'10.3':(1,[L('10.2',E,'Eagle landing')]),
'10.4':(1,[L('10.2',H,'Eagle landing')]),
'10.5':(1,[]),'10.6':(1,[]),
'11.b':(1,[]),'11.0':(1,[]),'11.1':(1,[]),'11.2':(1,[]),'11.3':(1,[]),
'11.4':(1,[L('10.2',H,'Apollo 11 on surface','low')]),
'12.b':(1,[]),
'12.0':(1,[L('7.1',E,"Kennedy's 1961 pledge")]),
'12.1':(1,[]),
'12.2':(1,[L('7.5',E,'N1 failure')]),
'12.3':(1,[L('8.6',H,'critics of the cost')]),
'12.4':(1,[L('12.3',H,'protest at spending')]),
'13.b':(1,[]),'13.0':(1,[]),'13.1':(1,[]),
'13.2':(1,[L('13.0',H,'Apollo landings that did happen')]),
'13.3':(1,[]),
'14.b':(1,[]),'14.0':(1,[]),
'14.1':(1,[L('14.0',H,'Shuttle programme')]),
'14.2':(1,[L('14.1',E,'Challenger disaster')]),
'14.3':(1,[L('14.1',E,'Challenger disaster'),L('14.2',H,'O-ring cause')]),
'15.b':(1,[]),'15.0':(1,[]),'15.1':(1,[]),'15.2':(1,[]),'15.3':(1,[]),
'15.4':(1,[L('15.2',H,'transistors')]),
'15.5':(1,[L('15.4',E,'chip components')]),
'15.6':(1,[L('15.4',H,'chip technology')]),
'16.b':(1,[]),
'16.0':(1,[L('5.5',E,'ARPA')]),
'16.1':(1,[]),'16.2':(1,[]),'16.3':(2,[]),
'16.4':(1,[L('15.4',H,'early chips')]),
'16.5':(1,[L('16.4',H,'military and NASA demand')]),
'17.b':(1,[]),'17.0':(1,[]),'17.1':(1,[]),
'17.2':(1,[L('17.1',H,'communications satellites')]),
'17.3':(1,[]),
'18.b':(1,[]),
'18.0':(2,[L('7.1',E,"Kennedy's decade deadline"),L('12.1',H,'Cold War victory')]),
'18.1':(2,[L('8.5',E,'cost of Apollo')]),
'18.2':(2,[L('17.3',H,'technological spin-offs')]),
'18.3':(2,[L('14.3',E,'Challenger management failure'),L('13.2',H,'cuts after race won')]),
'18.4':(2,[L('12.3',H,'critics and poverty')]),
'18.5':(2,[L('13.2',H,'lack of follow-up missions')]),
}
# links-only package 2 (s6 candidates)
S='hist-eur6-s6.'
D2={k:[] for k in D}
D2.update({
'0.5':[L(S+'3.2',H,'defence contractors')],
'4.0':[L(S+'3.2',H,'major defence contractors')],
'4.1':[L(S+'2.3',H,'civilian spin-offs of defence research')],
'5.3':[L(S+'2.6',H,'National Defense Education Act')],
'8.4':[L(S+'3.4',H,'defence contracts in California')],
'12.3':[L(S+'8.5',H,'poverty despite the boom','low')],
'15.3':[L(S+'6.5.1'.replace('6.5.1','5.1'),H,"IBM's growth",'low')],
'16.3':[L(S+'3.4',E,'Silicon Valley and defence contracts')],
'16.4':[L(S+'2.2',H,'federal defence spending')],
})
def check(pack,out,data):
    txt=open(B+'packs/'+pack).read()
    tg=re.findall(r'^\[(hist-eur6-s13\.[^\]]+)\]',txt.split('CANDIDATES')[0],re.M)
    allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    assert set(tg)==set(P+k for k in data) and len(tg)==len(data),(set(tg)^set(P+k for k in data))
    o={}
    for t in tg:
        o[t]=data[t[len(P):]]
    for v in o.values():
        for n in v.get('needs',[]): assert n['id'] in allids and n['id']!=t
    json.dump(o,open(B+'point-links/'+out,'w'),indent=0)
    json.load(open(B+'point-links/'+out))
    return o
o1={}
d1={k:{"cost":c,"needs":l} for k,(c,l) in D.items()}
o=check('hist-eur6-s13.t1g1.txt','hist-eur6-s13.t1g1.json',d1)
for k,v in o.items():
    for n in v['needs']: assert n['id']!=k
print(len(o),sum(len(v['needs']) for v in o.values()),sum(v['cost']==2 for v in o.values()),sum(n['confidence']=='low' for v in o.values() for n in v['needs']))
d2={k:{"needs":l} for k,l in D2.items()}
o=check('hist-eur6-s13.t1g2.txt','hist-eur6-s13.t1g2.json',d2)
print(len(o),sum(len(v['needs']) for v in o.values()),sum(n['confidence']=='low' for v in o.values() for n in v['needs']))
