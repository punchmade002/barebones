import json,re
B='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
def L(i,s,w,c='h'): return (i,'essential' if s=='e' else 'helpful',w,'high' if c=='h' else 'low')
P='hist-ire5-s10.'
S='hist-ire5-s4.'
A={
'0.b':(1,[]),
'0.0':(1,[]),
'0.1':(1,[L(P+'0.0','h','Derry and Londonderry names')]),
'0.2':(1,[]),
'0.3':(2,[]),
'0.4':(2,[L(P+'0.3','e','the Williamite-Jacobite war')]),
'1.b':(1,[L(P+'0.3','h','resisting James II')]),
'1.0':(1,[L(P+'0.3','h','King James II')]),
'1.1':(1,[L(P+'0.3','h','negotiating with James II','l')]),
'1.2':(1,[L(P+'1.1','e','Lundy the governor')]),
'1.3':(2,[L(P+'1.2','h','George Walker introduced')]),
'1.4':(1,[L(P+'1.3','h','the siege')]),
'2.b':(1,[L(P+'1.3','h','the siege','l')]),
'2.0':(1,[L(P+'1.4','h','starving garrison')]),
'2.1':(1,[L(P+'2.0','h','siege lifted by ships'),L(P+'0.3','h','Jacobite means James supporter')]),
'2.2':(1,[]),
'2.3':(1,[L(P+'0.2','e','the walls'),L(P+'2.2','e','crimson flag and Roaring Meg')]),
'2.4':(1,[L(P+'0.4','h','the Boyne 1690')]),
'3.b':(1,[]),
'3.0':(1,[L(P+'1.0','e','thirteen apprentices shut the gates')]),
'3.1':(1,[L(P+'3.0','h','the Apprentice Boys club')]),
'3.2':(1,[L(P+'3.0','h','the parent club')]),
'3.3':(1,[L(P+'3.0','h','the club and its headquarters','l')]),
'4.b':(1,[L(P+'1.0','h','Shutting of the Gates'),L(P+'2.0','h','relief of Derry')]),
'4.0':(1,[L(P+'2.0','e','the Relief of Derry')]),
'4.1':(1,[L(P+'4.0','e','the August parade'),L(P+'0.2','h','city walls')]),
'4.2':(2,[L(P+'1.0','e','Shutting of the Gates'),L(P+'1.2','e','Lundy effigy')]),
'4.3':(2,[L(P+'2.2','h','crimson flags and cannon')]),
'4.4':(1,[L(P+'4.1','h','August route round walls')]),
'5.b':(1,[]),
'5.0':(1,[L(P+'4.0','h','Apprentice Boys parades','l')]),
'5.1':(1,[L(P+'2.4','h','the siege story')]),
'5.2':(1,[]),
'5.3':(1,[L(P+'4.1','h','parade route disputes')]),
'6.b':(1,[]),
'6.0':(1,[L(P+'2.4','h','story of 1688-89')]),
'6.1':(1,[L(P+'1.0','h','siege defiance origin','l')]),
'6.2':(2,[L(P+'2.0','h','relief of 1689'),L(P+'0.3','e','Catholic monarch vs 1689 Protestant monarchy')]),
'6.3':(1,[L(P+'4.1','e','route past the Bogside')]),
'6.4':(1,[L(P+'4.1','h','parade beside Catholic district')]),
'7.b':(1,[L(P+'4.1','h','the parade route')]),
'7.0':(1,[L(S+'0.2','h','voting discrimination against Catholics')]),
'7.1':(1,[]),
'7.2':(1,[L(P+'4.1','e','August parade route')]),
'7.3':(1,[L(S+'0.2','e','civil rights grievances'),L(P+'7.0','h','unionist power structure')]),
'8.b':(1,[L(S+'4.2.b'.replace('4.2.b','2.b'),'h','August 1969 and British army')]),
'8.0':(2,[L(P+'7.1','h','the Bogside')]),
'8.1':(1,[L(P+'8.0','e','the 1969 parade')]),
'8.2':(1,[L(P+'8.0','e','12 August 1969 clashes')]),
'8.3':(1,[L(P+'8.2','h','barricades of August 1969')]),
'8.4':(1,[L(P+'8.2','h','Battle of the Bogside')]),
'9.b':(1,[L(P+'8.4','h','after 1969 troops')]),
'9.0':(1,[L(P+'4.0','h','the parades')]),
'9.1':(1,[L(P+'9.0','e','parade restrictions')]),
'9.2':(1,[L(P+'1.2','e','George Walker'),L(S+'4.0','h','the IRA','l')]),
'9.3':(1,[L(P+'9.0','h','parade restrictions and routes')]),
'9.4':(1,[L(P+'7.0','h','Catholic majority in Derry','l')]),
'10.b':(1,[L(P+'6.4','h','parades as painful display')]),
'10.0':(1,[L(P+'6.2','h','defence of Protestant liberty')]),
'10.1':(1,[L(P+'6.3','h','ascendancy view of parades'),L(P+'7.0','h','exclusion in the city')]),
'10.2':(1,[L(P+'7.3','e','civil rights agenda in Derry')]),
'10.3':(1,[L(P+'7.2','h','tension over routes')]),
'10.4':(1,[L(P+'10.2','h','commemoration taking political meaning')]),
'11.b':(1,[L(P+'8.4','h','events of 1969')]),
'11.0':(1,[L(P+'8.2','e','Battle of the Bogside'),L(P+'7.3','h','civil rights crisis')]),
'11.1':(1,[L(P+'8.4','e','British troops deployed')]),
'11.2':(1,[L(P+'3.3','e','the Memorial Hall')]),
'11.3':(1,[L(P+'7.2','h','parade route disputes')]),
'11.4':(1,[L(P+'9.3','h','security planning for parades')]),
'11.5':(1,[L(P+'9.4','e','Protestant numbers falling on west bank')]),
'12.b':(1,[]),
'12.0':(1,[L(P+'3.0','h','the Apprentice Boys club')]),
'12.1':(1,[L(P+'7.2','e','route past the Bogside')]),
'12.2':(1,[L(P+'9.1','h','resisting restrictions')]),
'12.3':(1,[L(P+'6.4','e','triumphalism')]),
'12.4':(2,[L(P+'10.4','h','commemoration taking political meaning')]),
}
A['8.b']=(1,[L(S+'2.b','h','August 1969 and British army')])
pack='packs/hist-ire5-s10.t1g1.txt';out='point-links/hist-ire5-s10.t1g1.json';pre=P
t=open(B+pack).read()
ids=re.findall(r'^\[([^\]]+)\]',t,re.M)
tgt=[m.group(1) for l in t.split('CANDIDATES')[0].splitlines() for m in [re.match(r'\[([^\]]+)\]',l)] if m]
assert [pre+k for k in A]==tgt,set(tgt)^set(pre+k for k in A)
d={};n=lo=c2=0
for k,(c,ns) in A.items():
    for i,*_ in ns: assert i in ids and i!=pre+k,(k,i)
    d[pre+k]={'cost':c,'needs':[{'id':i,'strength':s,'why':w,'confidence':cf} for i,s,w,cf in ns]}
    n+=len(ns);lo+=sum(x[3]=='low' for x in ns);c2+=c==2
json.dump(d,open(B+out,'w'),indent=1);json.loads(open(B+out).read())
print(len(d),n,c2,lo)
