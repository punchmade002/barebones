import json,re,sys
D='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
P='hist-ire5-s4.'
E,H='essential','helpful'
def L(i,s,w,c='high'):
    if not i.startswith('hist-'): i=P+i
    return {"id":i,"strength":s,"why":w,"confidence":c}
S2='hist-ire5-s2.'
S1='hist-ire5-s1.'
d={
'0.b':(1,[]),
'0.0':(1,[]),
'0.1':(1,[L('0.0',H,'uses Stormont parliament')]),
'0.2':(1,[]),
'0.3':(2,[L('0.2',E,'uses NICRA'),L(S2+'8.1',H,'5 October 1968 Derry march'),L(S2+'10.2',H,'Burntollet attack on march')]),
'0.4':(1,[]),
'0.5':(1,[L('1.2',H,'uses internment'),L(S1+'11.0',H,'IRA border campaign')]),
'1.b':(1,[]),'1.0':(1,[]),'1.1':(1,[]),'1.2':(1,[]),'1.3':(1,[]),
'2.b':(1,[]),
'2.0':(1,[L('0.4',H,'uses the RUC')]),
'2.1':(1,[L('2.0',H,'clashes in the Bogside')]),
'2.2':(1,[L('2.1',H,'troops sent after Bogside')]),
'2.3':(1,[]),'2.4':(1,[]),
'2.5':(1,[L('0.1',H,'Ireland Act consent principle'),L('3.0',H,'Chichester-Clark as Prime Minister','low')]),
'2.6':(1,[L('0.4',E,'RUC and B Specials')]),
'2.7':(1,[L('2.6',E,'Hunt recommended replacing Specials')]),
'3.b':(1,[]),
'3.0':(1,[L(S2+'11.5',H,'how Chichester-Clark became PM')]),
'3.1':(1,[L('2.1',H,'Battle of the Bogside'),L('2.7',H,'B Specials disbanded'),L('2.6',E,'Hunt Report reforms')]),
'3.2':(1,[L(S1+'6.1',H,'housing points system')]),
'3.3':(1,[L('3.2',E,'uses these reform steps')]),
'3.4':(1,[L('3.0',H,'uses his premiership')]),
'3.5':(1,[L('3.0',E,'narrow 1969 vote'),L('3.4',H,'his predecessor resigned')]),
'4.b':(1,[]),
'4.0':(2,[L('0.5',H,'weak IRA before 1969','low')]),
'4.1':(2,[L('4.0',E,'uses the IRA split'),L('2.3',H,'August 1969 failure to defend')]),
'4.2':(1,[L('4.0',E,'uses the Provisionals')]),
'4.3':(1,[L('4.0',E,'uses the Provisionals')]),
'4.4':(1,[L('2.2',H,'army deployment')]),
'4.5':(1,[]),
'4.6':(2,[]),
'4.7':(1,[L('4.6',E,'uses the SDLP')]),
'4.8':(1,[L('4.0',E,'Official IRA and Provisionals')]),
'5.b':(1,[]),'5.0':(1,[]),
'5.1':(1,[L('5.0',E,'compared with the UVF')]),
'5.2':(2,[L('5.0',E,'uses the UVF')]),
'5.3':(1,[L('1.1',E,'defines sectarian')]),
'5.4':(1,[L(S2+'3.3',H,'William Craig'),L('9.1',H,'loss of Stormont powers')]),
'6.b':(1,[]),
'6.0':(1,[L(S2+'1.0',H,"O'Neill's cabinet",'low')]),
'6.1':(1,[L('3.0',E,'1969 party vote'),L('3.5',H,'became PM in 1971')]),
'6.2':(1,[L('1.2',E,'uses internment'),L('7.0',H,'how internment began')]),
'6.3':(2,[L('4.6',E,'uses the SDLP'),L('4.7',E,'SDLP withdrawal in July 1971')]),
'6.4':(2,[L('9.0',H,'London security demand')]),
'6.5':(2,[L('4.7',H,'SDLP withdrawal'),L('8.1',E,'uses Bloody Sunday'),L('9.0',E,"London's demand for security powers")]),
'6.6':(1,[L('6.2',E,'uses internment')]),
'6.7':(2,[]),
'7.b':(1,[]),
'7.0':(2,[L('1.2',E,'uses internment')]),
'7.1':(1,[L('7.0',E,'those arrested in internment')]),
'7.2':(1,[L('7.0',E,'used on internees')]),
'7.3':(2,[L('7.2',E,'uses five techniques')]),
'7.4':(2,[L('7.0',H,'August 1971 internment operations')]),
'7.5':(1,[L('4.0',H,'uses the Provisional IRA')]),
'8.b':(1,[]),
'8.0':(1,[L('0.2',E,'uses NICRA'),L('7.0',H,'protest against internment')]),
'8.1':(2,[L('8.0',E,'the banned march')]),
'8.2':(1,[L('8.1',E,'the thirteen killed')]),
'8.3':(1,[L('8.1',E,'report on Bloody Sunday')]),
'8.4':(1,[L('8.1',E,'inquiry into killings'),L('8.3',H,'contrasts with Widgery')]),
'8.5':(1,[L('8.4',E,'responds to Saville findings')]),
'8.6':(2,[L('8.1',E,'uses the killings'),L('4.0',H,'Provisional IRA recruitment')]),
'9.b':(1,[]),
'9.0':(1,[L('6.1',H,"Faulkner's government")]),
'9.1':(1,[L('9.0',E,'the refusal that led to resignation')]),
'9.2':(1,[L('1.3',H,'defines Direct Rule')]),
'9.3':(1,[L('9.2',H,'Secretary of State under Direct Rule')]),
'9.4':(2,[L('9.3',E,'uses Whitelaw'),L('4.0',H,'Provisional IRA leaders')]),
'9.5':(1,[L('5.4',E,'Craig and Vanguard'),L('9.1',E,'loss of Stormont')]),
'9.6':(2,[L('9.2',E,'uses Direct Rule')]),
'9.7':(2,[L('9.6',E,'explains why Direct Rule lasted')]),
'10.b':(1,[]),
'10.0':(1,[L('4.0',E,'uses the Provisional IRA')]),
'10.1':(1,[L('10.0',E,'uses Bloody Friday')]),
'10.2':(2,[L('2.1',H,'Free Derry barricades')]),
'10.3':(1,[L('10.2',E,'uses Operation Motorman')]),
'10.4':(1,[L('10.2',H,'campaign continued after Motorman')]),
'11.b':(1,[]),
'11.0':(1,[L('0.2',H,'civil rights movement')]),
'11.1':(1,[L('0.4',E,'uses B Specials and RUC')]),
'11.2':(1,[L('0.0',H,'London left NI alone')]),
'11.3':(1,[L('4.0',H,'uses the Provisional IRA')]),
'11.4':(1,[L('5.3',H,'loyalist attacks on Catholics')]),
'11.5':(2,[L('7.1',H,'uses internment'),L('8.1',E,'uses Bloody Sunday')]),
'11.6':(1,[L('0.0',H,'Stormont and unionist rule','low')]),
'11.7':(2,[L('9.0',E,'British decision on security'),L('0.2',H,'civil rights protest')]),
'12.b':(1,[]),
'12.0':(1,[L('9.2',E,'the end of Stormont')]),
'12.1':(1,[L('7.0',E,'uses internment')]),
'12.2':(1,[L('9.1',E,'suspension of Stormont')]),
'12.3':(1,[L('9.6',H,'Direct Rule lasted long')]),
'12.4':(2,[L('9.7',H,'why Direct Rule came','low')]),
}
txt=open(D+'packs/hist-ire5-s4.t1g1.txt').read()
tgt=[]
sec=None
allids=set()
for ln in txt.splitlines():
    if ln.startswith('TARGET'): sec='t'
    elif ln.startswith('CANDIDATES'): sec='c'
    m=re.match(r'\[([^\]]+)\]',ln)
    if m:
        allids.add(m.group(1))
        if sec=='t': tgt.append(m.group(1))
out={}
for t in tgt:
    k=t[len(P):]
    c,n=d[k]
    out[t]={"cost":c,"needs":n}
assert set(d)=={t[len(P):] for t in tgt},set(d)^{t[len(P):] for t in tgt}
for t,v in out.items():
    for n in v['needs']:
        assert n['id'] in allids and n['id']!=t,(t,n)
json.dump(out,open(D+'point-links/hist-ire5-s4.t1g1.json','w'),indent=1)
r=json.load(open(D+'point-links/hist-ire5-s4.t1g1.json'))
print(len(r),sum(len(v['needs']) for v in r.values()),sum(v['cost']==2 for v in r.values()),sum(n['confidence']=='low' for v in r.values() for n in v['needs']))
