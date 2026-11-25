import json,re
B='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
P='hist-eur4-s7'
# (item, cost, [(need, strength, why, conf)])
E,H='essential','helpful'
def n(i,s,w,c='high'): return (i,s,w,c)
S6='hist-eur4-s6.';S5='hist-eur4-s5.';T=P+'.'
D=[
('0.b',1,[]),
('0.0',1,[n(S6+'2.2',H,'Marshall Aid recovery programme')]),
('0.1',1,[n(S6+'12.3',H,'Keynes demand management')]),
('0.2',1,[n(S6+'12.1',H,'cheap oil fuelling the boom','low')]),
('0.3',1,[]),
('0.4',1,[n(S6+'4.0',E,'Bretton Woods fixed exchange rates')]),
('0.5',1,[]),
('1.b',1,[]),
('1.0',1,[]),
('1.1',2,[n(T+'1.0',H,'Arab–Israeli conflict background')]),
('1.2',1,[]),
('1.3',1,[n(T+'1.2',H,'contrast with OPEC'),n(T+'1.1',H,'the occupied territories')]),
('1.4',1,[]),
('2.b',1,[]),
('2.0',1,[n(T+'1.0',H,'Arab–Israeli conflict')]),
('2.1',1,[n(T+'2.0',E,'the Yom Kippur War')]),
('2.2',1,[n(T+'1.2',H,'OPEC'),n(T+'2.0',H,'Yom Kippur War context')]),
('2.3',1,[n(T+'1.3',E,'OAPEC'),n(T+'1.1',E,'occupied territories demand')]),
('3.b',1,[]),
('3.0',1,[n(T+'2.1',H,'US support for Israel')]),
('3.1',1,[n(T+'3.0',E,'the embargo on the Netherlands')]),
('3.2',1,[n(T+'2.0',E,'the Yom Kippur War')]),
('3.3',1,[n(T+'2.2',E,'the October price rise')]),
('3.4',1,[n(T+'3.0',E,'the embargo'),n(T+'3.3',H,'the higher prices')]),
('4.b',1,[]),
('4.0',1,[]),
('4.1',1,[]),
('4.2',1,[]),
('4.3',1,[]),
('5.b',1,[]),
('5.0',1,[n(T+'3.3',H,'higher energy costs from price rise')]),
('5.1',1,[n(T+'5.0',H,'inflation and recession together','low')]),
('5.2',1,[n(T+'3.3',H,'quadrupled oil prices')]),
('5.3',1,[n(T+'3.3',H,'oil price rise creating revenues')]),
('5.4',1,[]),
('5.5',2,[n(T+'5.4',E,'stagflation'),n(T+'0.1',E,'Keynesian demand policy')]),
('6.b',1,[]),
('6.0',1,[n(T+'2.0',H,'first shock after Yom Kippur War')]),
('6.1',1,[n(T+'6.0',E,'the second oil shock')]),
('6.2',1,[n(T+'5.1',H,'unemployment rise after 1973')]),
('6.3',2,[n(T+'6.2',H,'unemployment rising in the EEC'),n(T+'7.0',H,'declining heavy industry','low')]),
('6.4',1,[n(T+'6.3',H,'unemployment during recession','low')]),
('6.5',1,[n(T+'10.1',H,'the welfare state')]),
('7.b',1,[]),
('7.0',1,[]),
('7.1',1,[]),
('7.2',2,[n(T+'7.1',H,'declining steel industry')]),
('7.3',1,[n(T+'7.0',H,'contrast with Britain')]),
('8.b',1,[]),
('8.0',1,[]),
('8.1',1,[n(T+'6.0',H,'second oil shock')]),
('8.2',1,[]),
('8.3',1,[]),
('9.b',1,[]),
('9.0',1,[n(T+'0.0',H,'the post-war boom')]),
('9.1',1,[n(S5+'9.4',H,'European Monetary System')]),
('9.2',1,[n(T+'3.0',H,'the embargo')]),
('9.3',2,[n(T+'0.4',E,'end of Bretton Woods'),n(T+'0.5',E,'inflation before the shock')]),
('9.4',1,[n(T+'8.3',H,'energy independence measures')]),
('9.5',1,[n(T+'6.2',H,'unemployment staying high','low')]),
('10.b',1,[]),
('10.0',1,[n(S6+'0.2',H,'capitalism and mixed economy')]),
('10.1',1,[n(S6+'0.3',E,'the welfare state')]),
('10.2',1,[n(T+'0.1',E,'Keynesian demand management')]),
('10.3',1,[]),
('10.4',1,[]),
('11.b',1,[n(T+'10.2',H,'monetarist policies')]),
('11.0',2,[]),
('11.1',1,[]),
('11.2',2,[n(T+'10.2',H,'monetarism'),n(T+'11.1',H,'Heath government')]),
('11.3',2,[n(T+'11.2',H,'break with Heath')]),
('11.4',2,[n(T+'11.3',H,'her leadership of the party','low')]),
('11.5',1,[]),
('11.6',1,[n(T+'11.2',H,'Heath and Joseph')]),
('12.b',1,[]),
('12.0',1,[n(T+'10.2',E,'monetarism')]),
('12.1',1,[n(T+'12.0',H,'Howe monetarist policy')]),
('12.2',1,[]),
('12.3',1,[n(T+'6.3',H,'unemployment hitting heavy industry')]),
('12.4',1,[n(T+'0.1',E,'post-war consensus')]),
('13.b',1,[]),
('13.0',1,[]),
('13.1',1,[]),
('13.2',1,[n(T+'10.3',E,'privatisation')]),
('13.3',1,[n(T+'10.3',E,'deregulation')]),
('13.4',1,[n(T+'10.4',H,'trade union laws')]),
('13.5',1,[n(T+'13.4',E,'closed shop limits')]),
('13.6',1,[n(T+'10.4',H,'trade union laws')]),
('14.b',1,[]),
('14.0',1,[]),
('14.1',1,[n(T+'14.0',E,'the Falklands task force')]),
('14.2',1,[n(T+'14.0',E,'the Falklands victory')]),
('15.b',1,[n(T+'10.4',H,'trade union policy')]),
('15.0',1,[]),
('15.1',1,[n(T+'15.0',H,'the strike')]),
('15.2',1,[n(T+'15.0',H,'the strike')]),
('15.3',1,[n(T+'15.0',H,'the strike')]),
('16.b',1,[]),
('16.0',1,[]),
('16.1',1,[n(T+'16.0',E,'Reagan alliance')]),
('16.2',1,[]),
('16.3',1,[n(T+'16.0',H,'influence on Reagan')]),
('16.4',1,[]),
('17.b',1,[]),
('17.0',1,[n(S5+'10.1',H,'Fontainebleau rebate')]),
('17.1',1,[n(S5+'10.2',E,'Single European Act')]),
('17.2',1,[n(T+'17.1',H,'her view of the single market')]),
('17.3',1,[n(S5+'11.4',H,'the Social Charter')]),
('17.4',1,[n(S5+'9.4',E,'Exchange Rate Mechanism')]),
('18.b',1,[]),
('18.0',1,[]),
('18.1',1,[n(T+'17.b',H,'her European policy','low')]),
('18.2',1,[n(T+'18.1',E,'Howe\'s resignation')]),
('18.3',1,[n(T+'18.2',E,'the leadership challenge')]),
('19.b',1,[]),
('19.0',1,[]),
('19.1',2,[n(T+'6.3',H,'unemployment passing three million'),n(T+'7.b',H,'deindustrialisation'),n(T+'18.0',H,'the poll tax')]),
('19.2',2,[n(T+'9.3',H,'trends already under way','low')]),
('19.3',1,[n(T+'10.3',H,'privatisation')]),
('20.b',1,[]),
('20.0',2,[n(T+'12.2',H,'inflation reduced')]),
('20.1',2,[n(T+'19.1',H,'critics\' case')]),
('20.2',1,[n(T+'20.1',H,'manufacturing decline')]),
('20.3',1,[n(T+'9.3',E,'earlier weaknesses in the boom')]),
('20.4',2,[n(T+'9.2',H,'contemporaries blaming OPEC'),n(T+'19.2',H,'historians on break or continuity')]),
]
ids=[P+'.'+d[0] for d in D]
pk=open(B+'packs/'+P+'.t1g1.txt').read()
tg=re.findall(r'^\[('+P+r'\.\d+\.[b\d]+)\]',pk,re.M)
tg=[t for t in tg if t.startswith(P+'.')]
ids_all=re.findall(r'^\[([^\]]+)\]',pk.split('CANDIDATES')[0],re.M)
assert ids==ids_all,(set(ids)^set(ids_all))
allp=set(re.findall(r'^\[([^\]]+)\]',pk,re.M))
out={}
for (i,c,nd) in D:
    k=P+'.'+i
    for x in nd: assert x[0] in allp and x[0]!=k,x
    out[k]={'cost':c,'needs':[{'id':a,'strength':s,'why':w,'confidence':cf} for a,s,w,cf in nd]}
json.dump(out,open(B+'point-links/'+P+'.t1g1.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))

# package 2
S2='hist-eur4-s2.'
L2={'16.0':[n(S2+'22.0',H,'Reagan\'s hard line on USSR')],
'16.1':[n(S2+'21.1',E,'NATO cruise missile deployment')],
'16.2':[n(S2+'0.0',H,'Cold War rivalry')],
'16.3':[n(S2+'22.2',H,'Gorbachev as Soviet leader')]}
pk2=open(B+'packs/'+P+'.t1g2.txt').read()
ids2=re.findall(r'^\[([^\]]+)\]',pk2.split('CANDIDATES')[0],re.M)
assert ids2==ids
all2=set(re.findall(r'^\[([^\]]+)\]',pk2,re.M))
o2={}
for i in ids:
    nd=L2.get(i[len(P)+1:],[])  # explicit: items not in L2 judged to have no s2 link
    for x in nd: assert x[0] in all2
    o2[i]={'needs':[{'id':a,'strength':s,'why':w,'confidence':cf} for a,s,w,cf in nd]}
json.dump(o2,open(B+'point-links/'+P+'.t1g2.json','w'),indent=1)
print(len(o2),sum(len(v['needs']) for v in o2.values()),0,0)
