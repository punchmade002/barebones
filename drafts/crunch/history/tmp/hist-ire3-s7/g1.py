import json,re
H='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
E='essential';L='helpful'
def n(i,s,w,c='high'):return (i,s,w,c)
P='hist-ire3-s7.'
A={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[n(P+'0.0',L,'tariffs defined there')]),'0.2':(1,[]),'0.3':(1,[]),
'0.4':(1,[n(P+'0.3',E,'dispute over land annuities')]),
'0.5':(1,[n(P+'0.0',L,'free trade'),n(P+'0.1',L,'protection')]),
'1.b':(1,[n('hist-ire3-s3.0.b',L,'partition of Ireland')]),
'1.0':(1,[]),'1.1':(2,[]),'1.2':(1,[]),'1.3':(1,[]),'1.4':(1,[]),'1.5':(1,[]),
'2.b':(1,[n(P+'0.0',L,'free trade'),n(P+'0.5',L,'Cumann na nGaedheal policy')]),
'2.0':(1,[n(P+'0.5',L,'Cumann na nGaedheal government')]),
'2.1':(2,[]),'2.2':(1,[]),'2.3':(1,[]),
'2.4':(1,[n(P+'0.1',L,'tariffs and protection')]),
'2.5':(2,[n('hist-ire3-s5.10.2',L,'Shannon Scheme introduced there'),n(P+'0.2',L,'ESB as semi-state body')]),
'2.6':(1,[]),
'3.b':(1,[]),'3.0':(1,[]),'3.1':(1,[]),
'3.2':(1,[n(P+'2.2',L,'Blythe as Finance Minister')]),
'3.3':(1,[]),
'3.4':(2,[n(P+'0.1',L,'industrial protection'),n(P+'5.b',L,'Lemass and protection')]),
'3.5':(1,[n(P+'3.4',L,'Finance opposing new schemes')]),
'3.6':(2,[]),
'4.b':(2,[n(P+'1.0',L,'dependence on farm exports')]),
'4.0':(1,[]),
'4.1':(1,[n(P+'1.0',L,'farm exports to Britain')]),
'4.2':(1,[n(P+'1.3',E,'currency tied to sterling')]),
'4.3':(1,[n(P+'1.0',L,'dependence on British market')]),
'4.4':(1,[n(P+'2.4',L,'limited tariffs policy')]),
'4.5':(1,[n(P+'0.5',L,'Fianna Fail protection policy')]),
'4.6':(1,[n(P+'0.3',E,'land annuities')]),
'5.b':(1,[n(P+'0.1',E,'protection and self-sufficiency'),n(P+'0.5',L,'Fianna Fail')]),
'5.0':(1,[n(P+'0.1',E,'tariffs and quotas')]),
'5.1':(1,[]),'5.2':(1,[]),'5.3':(1,[]),'5.4':(1,[]),
'5.5':(1,[n(P+'5.0',L,'protection and home market')]),
'5.6':(2,[n(P+'5.0',L,'protection policy being judged')]),
'5.7':(1,[n(P+'0.1',L,'self-sufficiency')]),
'6.b':(2,[n(P+'0.4',E,'Economic War over annuities')]),
'6.0':(2,[n(P+'0.3',E,'land annuities')]),
'6.1':(1,[n(P+'6.0',L,'British duties on cattle')]),
'6.2':(1,[n(P+'6.0',L,'lost income from duties')]),
'6.3':(1,[n(P+'6.b',L,'duties on coal and cattle')]),
'6.4':(1,[n(P+'6.0',L,'fall in prices from duties')]),
'6.5':(1,[n('hist-ire3-s6.7.1',L,'financial agreement of 1938')]),
'7.b':(1,[n(P+'5.b',L,'Fianna Fail spending context','low')]),
'7.0':(1,[]),'7.1':(1,[]),'7.2':(1,[]),'7.3':(1,[]),
'7.4':(1,[n(P+'4.1',L,'Depression closed emigration routes')]),
'7.5':(1,[n(P+'4.1',L,'Depression and emigration')]),
'7.6':(1,[]),
'8.b':(1,[n(P+'0.0',L,'free trade'),n(P+'0.1',L,'protection')]),
'8.0':(1,[n(P+'2.5',L,'Shannon Scheme')]),
'8.1':(1,[n(P+'4.b',L,'Depression effects')]),
'8.2':(1,[n(P+'5.3',L,'semi-state companies')]),
'8.3':(1,[n(P+'6.b',E,'Economic War')]),
'8.4':(2,[]),
'8.5':(1,[n(P+'0.1',L,'protection')]),
'8.6':(2,[n(P+'5.6',L,'protection critique','low')]),
}
def run(pack,out,A,pre):
    t=open(H+'packs/'+pack).read()
    ids=re.findall(r'^\[(\S+)\]',t.split('CANDIDATES')[0],re.M)
    allids=set(re.findall(r'^\[(\S+)\]',t,re.M))
    assert set(ids)=={pre+k for k in A} and len(ids)==len(A),(set(ids)^{pre+k for k in A})
    d={}
    for i in ids:
        c,nl=A[i[len(pre):]]
        for x in nl: assert x[0] in allids and x[0]!=i,x
        d[i]={'cost':c,'needs':[{'id':a,'strength':b,'why':w,'confidence':f} for a,b,w,f in nl]}
    json.dump(d,open(H+'point-links/'+out,'w'),indent=1)
    print(len(d),sum(len(v['needs']) for v in d.values()),sum(v['cost']==2 for v in d.values()),sum(x['confidence']=='low' for v in d.values() for x in v['needs']))
run('hist-ire3-s7.t1g1.txt','hist-ire3-s7.t1g1.json',A,'hist-ire3-s7.')
