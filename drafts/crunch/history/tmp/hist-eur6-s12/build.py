import json,re
H='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
def L(i,s,w,c='high'):
    if not i.startswith('hist-'): i='hist-eur6-s12.'+i
    return {"id":i,"strength":s,"why":w,"confidence":c}
h='helpful'; e='essential'
D={
'0.b':(1,[]),'0.0':(1,[]),
'0.1':(1,[L('0.0',h,'the Cold War')]),
'0.2':(1,[]),'0.3':(1,[]),
'1.b':(1,[]),'1.0':(1,[]),
'1.1':(1,[L('0.2',h,'suburbs and the baby boom')]),
'1.2':(1,[]),
'1.3':(1,[L('9.b',h,'what televangelists are','low')]),
'2.b':(1,[L('0.0',h,'opposition to atheistic communism')]),
'2.0':(1,[]),
'2.1':(1,[L('2.0',h,'Pledge and motto changes'),L('0.0',h,'the Cold War')]),
'2.2':(1,[L('0.0',h,'communism as the Cold War enemy')]),
'2.3':(1,[]),
'2.4':(1,[L('2.3',e,'Eisenhower remark on faith'),L('2.b',e,'civil religion')]),
'3.b':(1,[]),
'3.0':(1,[L('hist-eur6-s1.0.1',h,'segregation in the South')]),
'3.1':(1,[L('3.0',h,'Black churches as organising base')]),
'3.2':(1,[L('3.1',h,'King as a Baptist minister','low')]),
'4.b':(1,[L('1.0',h,'the 1950s religious revival')]),
'4.0':(1,[]),'4.1':(1,[]),'4.2':(1,[]),'4.3':(1,[]),
'4.4':(2,[]),'4.5':(1,[]),
'4.6':(1,[L('0.0',h,'Cold War faith against communism')]),
'5.b':(1,[]),'5.0':(1,[]),
'5.1':(2,[L('5.0',h,'Graham as presidential adviser')]),
'5.2':(2,[L('hist-eur6-s1.9.2',h,'the Watergate scandal'),L('11.0',h,'the Moral Majority')]),
'5.3':(1,[L('hist-eur6-s1.0.1',h,'racial segregation','low')]),
'5.4':(1,[L('3.1',h,'King and the civil rights movement')]),
'5.5':(2,[L('4.6',h,'Graham as Cold War patriot','low')]),
'5.6':(2,[L('5.1',h,'closeness to Nixon')]),
'5.7':(1,[L('5.1',h,'Graham and Nixon','low')]),
'6.b':(1,[]),'6.0':(1,[]),
'6.1':(1,[L('1.2',h,'Norman Vincent Peale')]),
'6.2':(1,[L('0.3',h,'separation of church and state')]),
'6.3':(1,[L('hist-eur6-s1.7.4',h,'Kennedy-Nixon election of 1960')]),
'6.4':(1,[]),'6.5':(1,[]),
'7.b':(1,[]),'7.0':(1,[]),'7.1':(1,[]),'7.2':(1,[]),
'7.3':(1,[L('7.2',h,'evangelicalism')]),
'8.b':(1,[L('0.3',h,'separation of church and state')]),
'8.0':(1,[L('0.3',e,'separation of church and state')]),
'8.1':(1,[]),
'8.2':(1,[L('8.0',h,'school prayer ruling')]),
'9.b':(1,[]),'9.0':(1,[]),'9.1':(1,[]),'9.2':(1,[]),'9.3':(1,[]),
'9.4':(1,[L('9.2',e,'the Bakkers and PTL')]),
'9.5':(1,[L('9.4',h,'the Bakker scandal')]),
'10.b':(1,[]),
'10.0':(2,[]),
'10.1':(1,[]),
'10.2':(1,[L('hist-eur6-s1.9.4',h,'Jimmy Carter')]),
'10.3':(1,[L('10.0',e,'abortion and the ERA'),L('10.2',h,'Carter as born-again evangelical')]),
'11.b':(1,[]),
'11.0':(2,[L('9.0',h,'Jerry Falwell'),L('10.0',h,'abortion and the ERA')]),
'11.1':(1,[]),
'11.2':(1,[L('hist-eur6-s1.10.0',h,'Reagan in 1980')]),
'11.3':(1,[]),
'11.4':(1,[L('0.3',h,'separation of church and state')]),
'11.5':(2,[L('9.4',h,'scandals of the late 1980s')]),
'11.6':(1,[L('11.0',e,'the Moral Majority'),L('9.1',h,'Pat Robertson')]),
'12.b':(1,[]),'12.0':(1,[]),'12.1':(1,[]),
'12.2':(1,[L('hist-eur6-s1.7.4',h,'Kennedy-Nixon election of 1960')]),
'12.3':(1,[]),'12.4':(1,[]),
'13.b':(1,[]),'13.0':(1,[]),'13.1':(1,[]),'13.2':(1,[]),'13.3':(1,[]),
'13.4':(2,[]),
'14.b':(1,[]),'14.0':(1,[]),
'14.1':(1,[L('hist-eur6-s1.9.2',h,'Watergate break-in')]),
'14.2':(1,[L('14.1',h,'the Watergate scandal')]),
'14.3':(1,[L('hist-eur6-s1.2.2',h,'US v Nixon over the tapes')]),
'15.b':(1,[]),'15.0':(1,[]),'15.1':(1,[]),'15.2':(1,[]),'15.3':(1,[]),
'16.b':(1,[]),'16.0':(1,[]),'16.1':(1,[]),'16.2':(1,[]),'16.3':(1,[]),'16.4':(1,[]),
'16.5':(1,[L('16.4',h,'the California university system')]),
'17.b':(1,[]),'17.0':(1,[]),
'17.1':(1,[L('16.5',h,'the multiversity')]),
'17.2':(1,[L('17.0',h,'the Berkeley movement')]),
'17.3':(1,[L('17.2',h,'the Sproul Hall sit-in')]),
'17.4':(1,[L('17.0',h,'ban on political activity')]),
'18.b':(1,[]),'18.0':(1,[]),'18.1':(1,[]),
'18.2':(1,[L('18.1',h,'Kent State shootings','low')]),
'18.3':(1,[L('18.1',h,'Kent State shootings')]),
'19.b':(1,[]),
'19.0':(2,[L('3.0',h,'Black churches and civil rights'),L('2.b',h,'faith against communism')]),
'19.1':(2,[L('11.b',h,'the religious right'),L('9.4',h,'the scandals of 1987-88')]),
'19.2':(2,[L('12.2',h,'Kennedy-Nixon debate'),L('13.b',h,'television and Vietnam'),L('14.b',h,'media and Watergate')]),
'19.3':(2,[L('12.3',h,'the quiz show scandal')]),
'19.4':(1,[L('16.b',h,'mass higher education')]),
'19.5':(1,[L('18.b',h,'campus protest and unrest')]),
'19.6':(2,[L('5.5',h,'contemporary views of Graham'),L('5.6',h,'historians on Graham')]),
}
txt=open(H+'packs/hist-eur6-s12.t1g1.txt').read()
tgt=[];sec=None
for ln in txt.split('\n'):
    if ln.startswith('TARGET'): sec='T'
    elif ln.startswith('CANDIDATES'): sec='C'
    m=re.match(r'\[(hist-[^\]]+)\]',ln)
    if m and sec=='T': tgt.append(m.group(1))
allids=set(re.findall(r'^\[(hist-[^\]]+)\]',txt,re.M))
pre='hist-eur6-s12.'
assert set(D)=={t[len(pre):] for t in tgt}, set(D)^{t[len(pre):] for t in tgt}
out={}
for t in tgt:
    c,n=D[t[len(pre):]]; out[t]={"cost":c,"needs":n}
for k,v in out.items():
    for n in v['needs']: assert n['id'] in allids and n['id']!=k,(k,n)
json.dump(out,open(H+'point-links/hist-eur6-s12.t1g1.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
