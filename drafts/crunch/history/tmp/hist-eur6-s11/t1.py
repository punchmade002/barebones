import json,re
B='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
P='hist-eur6-s11.'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
H,E='helpful','essential'
T=lambda n:P+n
# package 1: id -> (cost, links)
p1={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),'0.2':(1,[]),
'0.3':(1,[]),
'0.4':(1,[L('hist-eur6-s4.1.0',H,"uses Truman's loyalty programme"),L('hist-eur6-s4.0.7',H,"uses McCarthyism")]),
'0.5':(1,[]),'0.6':(1,[]),
'1.b':(1,[]),'1.0':(1,[]),'1.1':(1,[]),'1.2':(2,[]),'1.3':(1,[]),'1.4':(1,[]),'1.5':(2,[]),'1.6':(1,[]),
'1.7':(2,[L(T('3.b'),H,"uses the blacklist")]),
'2.b':(1,[]),'2.0':(1,[]),'2.1':(1,[L(T('2.0'),E,"uses the Production Code")]),
'2.2':(1,[L(T('2.0'),E,"replaces the Production Code")]),
'3.b':(1,[]),
'3.0':(2,[L(T('3.b'),E,"uses HUAC hearings")]),
'3.1':(1,[L(T('3.0'),H,"responds to the hearings"),L(T('3.b'),H,"uses the blacklist")]),
'3.2':(1,[L(T('3.b'),H,"uses the blacklist")]),
'3.3':(1,[L(T('3.2'),E,"uses Dalton Trumbo's pseudonym writing"),L(T('3.b'),H,"breaks the blacklist")]),
'3.4':(2,[L(T('3.b'),H,"uses HUAC")]),
'3.5':(1,[L(T('3.b'),H,"uses the blacklist")]),
'3.6':(1,[L(T('3.1'),H,"loyalty response to suspicion",'low')]),
'4.b':(1,[]),'4.0':(1,[]),'4.1':(1,[]),'4.2':(1,[]),'4.3':(1,[]),'4.4':(1,[]),
'4.5':(2,[L(T('0.2'),H,"uses mass media")]),
'4.6':(1,[]),'4.7':(1,[]),
'5.b':(1,[L(T('0.2'),H,"uses mass media")]),
'5.0':(1,[]),'5.1':(1,[]),
'5.2':(1,[L(T('5.1'),H,"uses rock and roll")]),
'5.3':(1,[]),'5.4':(1,[]),'5.5':(1,[]),
'6.b':(1,[]),'6.0':(1,[]),'6.1':(1,[]),
'6.2':(1,[L('hist-eur6-s4.9.2',H,"the Pentagon march itself")]),
'6.3':(1,[]),
'6.4':(2,[L(T('7.7'),H,"the Ali-Foreman fight")]),
'6.5':(2,[]),
'6.6':(2,[L(T('6.1'),E,"argument of The White Negro")]),
'6.7':(1,[L(T('6.2'),H,"The Armies of the Night")]),
'7.b':(1,[]),'7.0':(1,[]),
'7.1':(1,[L(T('7.0'),H,"same boxer, early career",'low')]),
'7.2':(1,[L(T('7.0'),H,"Clay name and background",'low')]),
'7.3':(2,[L(T('7.2'),H,"Muslim minister, Nation of Islam"),L('hist-eur6-s4.8.3',H,"uses the draft")]),
'7.4':(1,[L(T('7.3'),E,"follows the refusal of induction")]),
'7.5':(1,[L(T('7.4'),E,"overturns the conviction")]),
'7.6':(2,[L(T('7.3'),H,"the ban after refusal")]),
'7.7':(2,[L(T('7.6'),H,"continues his comeback")]),
'7.8':(2,[L(T('7.3'),H,"the draft refusal")]),
'8.b':(1,[]),
'8.0':(1,[L(T('0.6'),H,"uses counter-culture")]),
'8.1':(2,[]),
'8.2':(1,[L(T('8.b'),H,"uses hippies")]),
'8.3':(2,[]),
'9.b':(1,[]),'9.0':(1,[]),'9.1':(1,[]),
'9.2':(1,[L('hist-eur6-s4.8.1',H,"uses SDS"),L('hist-eur6-s9.9.5',H,"uses Black Panther Party")]),
'9.3':(1,[L('hist-eur6-s4.9.3',H,"uses the Chicago convention")]),
'9.4':(1,[]),
'9.5':(1,[L('hist-eur6-s4.9.6',H,"Nixon's silent majority speech")]),
'10.b':(1,[]),'10.0':(1,[]),
'10.1':(2,[L(T('10.0'),E,"uses Chavez and the union")]),
'10.2':(1,[]),
'10.3':(1,[L(T('10.2'),H,"uses AIM")]),
'10.4':(2,[L('hist-eur6-s9.9.4',H,"uses Black Power"),L('hist-eur6-s9.9.5',H,"uses Black Panther Party")]),
'11.b':(1,[]),'11.0':(1,[]),'11.1':(2,[]),
'11.2':(1,[L(T('11.1'),E,"follows Stonewall")]),
'11.3':(1,[]),
'11.4':(1,[L(T('0.0'),E,"uses the concept of consensus")]),
'12.b':(1,[L(T('0.0'),H,"uses consensus")]),
'12.0':(2,[L(T('0.0'),E,"uses the consensus view")]),
'12.1':(2,[L(T('0.0'),E,"uses the consensus view"),L('hist-eur6-s4.0.7',H,"uses the red scare")]),
'12.2':(2,[L(T('8.b'),H,"uses the counter-culture")]),
'12.3':(2,[L(T('0.0'),E,"uses consensus")]),
}
# package 2: links to s3 only
p2={k:[] for k in p1}
p2['0.5']=[L('hist-eur6-s3.10.8',H,"Nixon's 1968 election"),L('hist-eur6-s3.4.b',H,"the Vietnam War escalation")]
p2['6.2']=[L('hist-eur6-s3.7.7',H,"the Pentagon march")]
p2['6.7']=[L('hist-eur6-s3.7.b',H,"the anti-war protest movement")]
p2['7.3']=[L('hist-eur6-s3.0.3',H,"uses the Viet Cong"),L('hist-eur6-s3.6.6',H,"uses the draft")]
p2['7.8']=[L('hist-eur6-s3.7.b',H,"the anti-war movement")]
p2['9.2']=[L('hist-eur6-s3.7.2',H,"uses Students for a Democratic Society")]
p2['9.3']=[L('hist-eur6-s3.10.7',H,"the Chicago convention protests")]
p2['9.5']=[L('hist-eur6-s3.10.8',H,"Nixon's 1968 election")]
p2['12.2']=[L('hist-eur6-s3.10.8',H,"1968 election and the war",'low')]
def full(k): return P+k
o1={full(k):{"cost":c,"needs":n} for k,(c,n) in p1.items()}
o2={full(k):{"needs":n} for k,n in p2.items()}
for name,o in (('t1g1',o1),('t1g2',o2)):
    txt=open(B+f'packs/hist-eur6-s11.{name}.txt').read()
    tgt=[]; ids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    sec=txt.split('CANDIDATES')[0]
    tgt=re.findall(r'^\[([^\]]+)\]',sec,re.M)
    assert list(o)==tgt or set(o)==set(tgt),(set(tgt)^set(o))
    o={k:o[k] for k in tgt}
    for v in o.values():
        for n in v['needs']: assert n['id'] in ids,n
    json.dump(o,open(B+f'point-links/hist-eur6-s11.{name}.json','w'),indent=1)
    json.load(open(B+f'point-links/hist-eur6-s11.{name}.json'))
    ls=[n for v in o.values() for n in v['needs']]
    print(name,len(o),len(ls),sum(v.get('cost')==2 for v in o.values()),sum(n['confidence']=='low' for n in ls))
