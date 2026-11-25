import json,re
B='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
def L(i,s,w,c='h'): return (i,'essential' if s=='e' else 'helpful',w,'high' if c=='h' else 'low')
P='hist-eur6-s8.'
S='hist-eur6-s6.'
A={
'0.b':(1,[L(S+'0.3','h','uses wartime savings'),L(S+'0.4','h','uses pent-up demand')]),
'0.0':(2,[]),
'0.1':(1,[L(P+'0.0','h','larger families from baby boom')]),
'0.2':(1,[L(P+'0.0','h','boom generation')]),
'0.3':(1,[]),
'0.4':(1,[L(P+'0.3','e','suburbs growing drew people from cities')]),
'0.5':(1,[L(S+'2.2','h','federal defence spending')]),
'0.6':(1,[L(P+'0.5','h','Sun Belt growth')]),
'0.7':(2,[L(P+'0.3','h','white families moving to suburbs')]),
'1.b':(1,[L(P+'1.3','h','federal mortgage guarantees')]),
'1.0':(1,[L(S+'0.5','h','GI Bill benefits'),L(S+'0.4','h','pent-up demand')]),
'1.1':(1,[]),
'1.2':(1,[L(P+'1.1','e','first Levittown houses')]),
'1.3':(1,[L(S+'0.5','h','veterans loans from GI Bill','l')]),
'1.4':(2,[L(P+'1.1','e','Levittown leases'),L(P+'1.3','h','lending practices')]),
'1.5':(1,[L(P+'0.3','h','suburbs'),L(S+'2.0','h','new highways','l')]),
'1.6':(1,[]),
'1.7':(2,[L(P+'1.b','h','suburban abundance, American Dream'),L(S+'1.b','h','Cold War, capitalism vs communism','l')]),
'2.b':(1,[L(P+'2.1','h','credit and instalment buying')]),
'2.0':(2,[L(P+'2.1','h','credit buying')]),
'2.1':(1,[]),
'2.2':(1,[L(P+'0.3','h','spread through suburbs')]),
'2.3':(2,[]),
'2.4':(1,[L(P+'2.3','h','television advertising')]),
'2.5':(1,[L(P+'2.4','h','advertisers creating demand')]),
'2.6':(2,[L(P+'2.4','h','advertising creating wants')]),
'2.7':(1,[L(P+'1.5','h','car and family holiday','l')]),
'3.b':(1,[L(P+'3.3','h','Organization Man')]),
'3.0':(1,[]),
'3.1':(1,[L(P+'2.3','h','television'),L(P+'1.5','h','car culture')]),
'3.2':(1,[]),
'3.3':(2,[L(S+'6.4.1'.replace('6.4.1','4.1'),'h','Whyte social ethic of conformity'),L(P+'3.2','h','salaried white-collar employee')]),
'3.4':(1,[L(P+'0.3','h','suburban culture','l')]),
'4.b':(1,[L(P+'3.4','h','domestic ideal','l')]),
'4.0':(1,[L(P+'3.4','h','domestic ideal')]),
'4.1':(1,[L(P+'4.0','h','women leaving jobs after 1945')]),
'4.2':(2,[L(P+'4.1','h','women in workforce')]),
'4.3':(1,[L(P+'3.4','h','traditional nuclear family')]),
'4.4':(1,[]),
'4.5':(1,[L(P+'4.4','h','contraception')]),
'5.b':(1,[L(P+'5.5','h','Equal Rights Amendment')]),
'5.0':(1,[L(P+'4.2','h','low pay for women')]),
'5.1':(2,[]),
'5.2':(1,[L(P+'5.1','e','contrast with Title VII')]),
'5.3':(1,[L(P+'2.1','h','credit in consumer life')]),
'5.4':(1,[]),
'5.5':(2,[]),
'5.6':(1,[L(P+'5.5','e','the Equal Rights Amendment')]),
'6.b':(1,[L(P+'3.4','h','domestic ideal')]),
'6.0':(2,[]),
'6.1':(1,[L(P+'6.0','h','Friedan studied at Smith')]),
'6.2':(2,[L(P+'3.4','h','domestic ideal'),L(P+'6.1','h','survey basis of book')]),
'6.3':(1,[L(P+'6.2','e','The Feminine Mystique')]),
'6.4':(2,[L(P+'5.5','e','Equal Rights Amendment')]),
'6.5':(2,[]),
'6.6':(1,[L(P+'6.3','h','Friedan as feminist leader')]),
'6.7':(2,[L(P+'6.2','h','Feminine Mystique focus'),L(P+'6.4','h','NOW')]),
'7.b':(1,[L(P+'2.b','h','consumer culture')]),
'7.0':(1,[]),
'7.1':(2,[L(P+'7.0','h','Monroe background')]),
'7.2':(1,[L(P+'2.4','h','advertising and consumer culture')]),
'7.3':(2,[L(P+'7.1','e','sex symbol image')]),
'7.4':(1,[L(P+'7.3','h','sex symbol typecasting')]),
'7.5':(1,[L(P+'7.3','h','limited roles in Hollywood')]),
'7.6':(1,[L(P+'6.2','e','Friedan attacked feminine ideal')]),
'8.b':(1,[]),
'8.0':(1,[L(P+'1.b','h','home ownership and the Dream')]),
'8.1':(1,[L(P+'1.4','e','lending exclusion from suburbs')]),
'8.2':(1,[L(P+'5.0','e','1963 Equal Pay Act'),L(P+'5.1','e','Title VII 1964')]),
'8.3':(1,[L(P+'4.2','h','low pay, narrow jobs'),L(P+'6.2','e','Friedan domestic ideal evidence')]),
'8.4':(2,[L(P+'2.6','e','Galbraith'),L(P+'2.5','e','Packard'),L(P+'3.3','e','Whyte')]),
'8.5':(1,[L(P+'4.3','h','divorce and single-parent families'),L(P+'4.1','h','women employment rose')]),
}
# fix the one odd id built above
A['3.3']=(2,[L('hist-eur6-s6.4.1','h','Whyte social ethic of conformity'),L(P+'3.2','h','salaried white-collar employee')])
import sys
def fin(pack,out,A,pre):
    t=open(B+pack).read()
    ids=[m for m in re.findall(r'^\[([^\]]+)\]',t,re.M)]
    tgt=[]
    for l in t.split('CANDIDATES')[0].splitlines():
        m=re.match(r'\[([^\]]+)\]',l)
        if m: tgt.append(m.group(1))
    assert [pre+k for k in A]==tgt,(set(tgt)^set(pre+k for k in A))
    d={};n=lo=c2=0
    for k,(c,ns) in A.items():
        for i,*_ in ns: assert i in ids and i!=pre+k,(k,i)
        d[pre+k]={'cost':c,'needs':[{'id':i,'strength':s,'why':w,'confidence':cf} for i,s,w,cf in ns]}
        n+=len(ns);lo+=sum(x[3]=='low' for x in ns);c2+=c==2
    json.dump(d,open(B+out,'w'),indent=1)
    json.loads(open(B+out).read())
    print(len(d),n,c2,lo)
fin('packs/hist-eur6-s8.t1g1.txt','point-links/hist-eur6-s8.t1g1.json',A,'hist-eur6-s8.')
