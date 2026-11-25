import json,re
B='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
P='hist-eur6-s4.'
E,H='essential','helpful'
def L(i,s,w,c='high'):
    return {"id":i if i.startswith('hist-') else i,"strength":s,"why":w,"confidence":c}
t=lambda x:P+x
# id: (cost, [(id,strength,why,conf)])
d1={
'0.b':(1,[]),
'0.0':(1,[('hist-eur6-s2.2.1',E,'Truman Doctrine'),('hist-eur6-s2.1.1',H,'Soviet atomic test')]),
'0.1':(1,[('hist-eur6-s2.2.3',E,'communist victory in China'),('hist-eur6-s2.7.2',H,'Korean War invasion')]),
'0.2':(1,[]),
'0.3':(1,[('hist-eur6-s3.4.3',H,'Johnson escalation in 1965')]),
'0.4':(1,[]),'0.5':(1,[]),'0.6':(1,[]),'0.7':(1,[]),
'1.b':(1,[]),'1.0':(1,[]),
'1.1':(2,[(t('0.2'),H,'congressional committee powers')]),
'1.2':(1,[(t('1.1'),E,'the Hollywood Ten')]),
'1.3':(1,[(t('1.1'),E,'the Hollywood Ten')]),
'1.4':(1,[(t('1.3'),E,'the Hollywood blacklist')]),
'1.5':(1,[(t('1.1'),E,'HUAC Hollywood hearings'),(t('4.0'),H,"McCarthy's Senate subcommittee")]),
'2.b':(1,[]),
'2.0':(2,[(t('1.1'),H,'HUAC hearings')]),
'2.1':(2,[(t('2.0'),E,'Chambers accusation against Hiss')]),
'2.2':(1,[(t('2.0'),E,'the Hiss case')]),
'2.3':(2,[]),
'2.4':(1,[(t('2.3'),H,'Fuchs led to Rosenbergs')]),
'2.5':(2,[]),
'2.6':(1,[(t('1.0'),H,'loyalty programme','low')]),
'3.b':(1,[]),
'3.0':(2,[]),
'3.1':(2,[(t('3.0'),E,'the Wheeling speech'),(t('2.1'),E,'Hiss conviction'),(t('2.3'),E,'Fuchs arrest'),('hist-eur6-s2.1.1',H,'Soviet bomb'),('hist-eur6-s2.2.3',H,'fall of China')]),
'3.2':(1,[(t('3.0'),E,'the charges McCarthy made')]),
'3.3':(1,[(t('3.0'),H,'his accusations','low')]),
'3.4':(1,[(t('3.3'),H,'smear tactics')]),
'3.5':(1,[]),
'4.b':(1,[]),'4.0':(1,[]),
'4.1':(1,[(t('4.0'),E,'his subcommittee chairmanship')]),
'4.2':(1,[]),
'4.3':(1,[(t('4.1'),E,'Schine and Cohn')]),
'4.4':(1,[(t('4.3'),E,'Army-McCarthy hearings')]),
'4.5':(1,[(t('4.4'),H,'his collapse in 1954')]),
'5.b':(1,[]),
'5.0':(2,[]),
'5.1':(1,[(t('5.0'),H,'his early career')]),
'5.2':(2,[(t('3.0'),E,'the Wheeling speech'),(t('4.0'),E,'Permanent Subcommittee'),(t('3.1'),H,'events he exploited')]),
'5.3':(2,[(t('4.3'),E,'Army-McCarthy hearings'),(t('4.2'),H,'television exposure'),(t('6.2'),H,"Eisenhower's refusal")]),
'5.4':(1,[]),'5.5':(1,[]),'5.6':(1,[]),
'5.7':(2,[(t('0.7'),H,'McCarthyism and Red Scare')]),
'5.8':(2,[(t('3.3'),H,"McCarthy's methods and lists",'low')]),
'6.b':(1,[]),
'6.0':(1,[(t('1.0'),E,"Truman's loyalty standard")]),
'6.1':(1,[(t('6.0'),E,'the new security criteria')]),
'6.2':(1,[(t('4.3'),H,'Army hearings of 1954')]),
'6.3':(1,[(t('2.2'),E,'Nixon and the Hiss case')]),
'7.b':(1,[]),
'7.0':(1,[('hist-eur6-s2.2.3',E,'communist victory in China')]),
'7.1':(1,[(t('3.0'),H,"McCarthy's State Department accusations")]),
'7.2':(1,[(t('7.0'),H,'fall of China charge','low')]),
'7.3':(1,[('hist-eur6-s2.7.2',H,'Korean crisis','low')]),
'7.4':(1,[(t('6.0'),E,'new security standards')]),
'7.5':(1,[(t('11.3'),E,'Little Rock crisis')]),
'8.b':(1,[]),'8.0':(1,[]),'8.1':(2,[]),
'8.2':(1,[(t('8.1'),E,'SDS')]),
'8.3':(1,[]),
'8.4':(1,[(t('8.3'),E,'the draft')]),
'8.5':(1,[(t('8.3'),H,'induction into the draft')]),
'8.6':(1,[(t('8.5'),E,"Ali's refusal of induction")]),
'9.b':(1,[]),'9.0':(1,[]),
'9.1':(1,[(t('9.0'),H,"King's Beyond Vietnam speech")]),
'9.2':(1,[]),'9.3':(1,[]),
'9.4':(1,[(t('9.3'),E,'Democratic convention in Chicago')]),
'9.5':(1,[]),
'9.6':(1,[(t('9.5'),H,'the Moratorium protests')]),
'10.b':(1,[]),
'10.0':(1,[('hist-eur6-s2.14.4',H,'Cambodian incursion')]),
'10.1':(1,[(t('10.0'),H,'protests after Cambodia')]),
'10.2':(1,[]),
'10.3':(1,[('hist-eur6-s3.3.3',E,'Gulf of Tonkin Resolution')]),
'10.4':(1,[('hist-eur6-s2.14.1',E,'Vietnamisation'),('hist-eur6-s3.10.6',E,"Johnson's 1968 decision")]),
'11.b':(1,[]),'11.0':(1,[]),'11.1':(1,[]),
'11.2':(1,[(t('11.1'),E,'Brown v. Board')]),
'11.3':(1,[]),'11.4':(1,[]),
'11.5':(1,[(t('11.3'),H,'Little Rock')]),
'11.6':(1,[(t('9.0'),H,'King and the Vietnam war')]),
'11.7':(1,[]),
'12.b':(1,[]),
'12.0':(2,[(t('5.8'),H,'Venona decrypts'),(t('7.2'),H,'weakened China expertise')]),
'12.1':(2,[(t('10.4'),E,"Johnson's 1968 decision, withdrawals"),(t('9.6'),H,'silent majority')]),
'12.2':(2,[(t('10.4'),H,'protest pressure on policy')]),
'12.3':(2,[(t('11.3'),E,'Little Rock propaganda'),(t('11.4'),H,'Birmingham campaign')]),
'12.4':(2,[]),
'12.5':(2,[(t('5.6'),E,'Rovere'),(t('5.7'),E,'Schrecker'),(t('5.8'),E,'Evans and Venona')]),
}
def mk(d,withcost):
    out={}
    for k,(c,ns) in d.items():
        e={}
        if withcost:e['cost']=c
        e['needs']=[{"id":n[0],"strength":n[1],"why":n[2],"confidence":(n[3] if len(n)>3 else 'high')} for n in ns]
        out[t(k)]=e
    return out
json.dump(mk(d1,True),open(B+'point-links/hist-eur6-s4.t1g1.json','w'),indent=1)
d2={k:(0,[]) for k in d1}
d2.update({
'0.3':(0,[('hist-eur6-s9.3.b',H,'Black freedom struggle','low')]),
'7.5':(0,[('hist-eur6-s9.2.3',H,'Little Rock crisis')]),
'9.0':(0,[('hist-eur6-s9.8.1',H,'Riverside Church speech')]),
'9.1':(0,[('hist-eur6-s9.8.1',H,'King linking rights and war','low')]),
'11.0':(0,[('hist-eur6-s9.0.7',H,'Executive Order 9981')]),
'11.1':(0,[('hist-eur6-s9.1.6',H,'Brown v. Board ruling')]),
'11.2':(0,[('hist-eur6-s9.1.6',H,'Brown v. Board')]),
'11.3':(0,[('hist-eur6-s9.2.3',H,'Little Rock crisis')]),
'11.4':(0,[('hist-eur6-s9.3.2',H,'Freedom Rides'),('hist-eur6-s9.4.0',H,'Birmingham campaign')]),
'11.6':(0,[('hist-eur6-s9.8.1',H,'King on Vietnam'),('hist-eur6-s9.9.1',H,'Malcolm X')]),
'11.7':(0,[('hist-eur6-s9.5.2',H,'Civil Rights Act 1964'),('hist-eur6-s9.6.3',H,'Voting Rights Act 1965')]),
'12.3':(0,[('hist-eur6-s9.4.0',H,'Birmingham campaign')]),
})
json.dump(mk(d2,False),open(B+'point-links/hist-eur6-s4.t1g2.json','w'),indent=1)
# check
for n,pk in (('t1g1','packs/hist-eur6-s4.t1g1.txt'),('t1g2','packs/hist-eur6-s4.t1g2.txt')):
    txt=open(B+pk).read()
    ids=re.findall(r'^\[(hist-[^\]]+)\]',txt,re.M)
    tg=[i for i in ids if i.startswith('hist-eur6-s4.')]
    j=json.load(open(B+f'point-links/hist-eur6-s4.{n}.json'))
    assert list(j)==tg,(set(tg)^set(j))
    links=[x for v in j.values() for x in v['needs']]
    assert all(x['id'] in ids for x in links),[x for x in links if x['id'] not in ids]
    assert all(k!=x['id'] for k,v in j.items() for x in v['needs'])
    print(n,len(j),len(links),sum(v.get('cost')==2 for v in j.values()),sum(x['confidence']=='low' for x in links))
