import json,re
P='hist-ire6-s4.'
D='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
def L(i,s,w,c='high'): return (i,{'E':'essential','H':'helpful'}[s],w,c)
d={
'0.b':(1,[]),
'0.0':(1,[L('hist-ire6-s2.6.0','H','Lemass as Taoiseach before Lynch')]),
'0.1':(1,[]),'0.2':(1,[]),'0.3':(1,[]),'0.4':(1,[]),'0.5':(1,[]),'0.6':(1,[]),
'1.b':(1,[L(P+'0.3','H','EEC entry in 1973')]),
'1.0':(1,[]),
'1.1':(1,[L(P+'1.0','E','the oil price rise')]),
'1.2':(1,[L(P+'0.4','H','balance of payments deficit'),L(P+'1.1','H','recession from oil shock','low')]),
'1.3':(1,[L(P+'1.0','E','the first oil shock')]),
'1.4':(1,[L('hist-ire6-s1.8.6','H','Irish pound linked to sterling')]),
'1.5':(1,[L(P+'0.6','H','national debt')]),
'1.6':(1,[L(P+'0.6','E','national debt')]),
'2.b':(1,[]),
'2.0':(2,[]),
'2.1':(2,[]),
'2.2':(2,[L(P+'1.2','H','the National Coalition')]),
'2.3':(2,[L(P+'0.2','H','the Troubles')]),
'2.4':(2,[L(P+'0.2','H','the Troubles')]),
'2.5':(1,[]),
'2.6':(1,[L(P+'3.b','E','the Arms Crisis'),L(P+'4.4','H','the 1979 by-elections','low')]),
'2.7':(2,[L(P+'3.1','H','slow to remove Haughey and Blaney'),L(P+'4.2','H','the 1977 programme')]),
'2.8':(2,[L(P+'2.7','H','his strengths and weaknesses'),L(P+'3.b','H','the Arms Crisis')]),
'3.b':(1,[L(P+'0.2','H','Troubles context')]),
'3.0':(1,[L(P+'0.2','H','arms for Northern nationalists')]),
'3.1':(1,[L(P+'3.0','H','the Special Branch information')]),
'3.2':(2,[L(P+'3.1','H','Haughey and Blaney dismissed')]),
'3.3':(1,[L(P+'3.2','E','the charges of conspiracy')]),
'3.4':(1,[L(P+'3.1','H','Lynch dismissing the ministers')]),
'3.5':(1,[L(P+'3.1','H','Haughey dismissed from cabinet')]),
'4.b':(1,[]),
'4.0':(1,[]),
'4.1':(1,[L(P+'4.0','H','the 1977 manifesto')]),
'4.2':(1,[L(P+'4.0','E','the manifesto promises'),L(P+'0.6','H','national debt')]),
'4.3':(2,[L(P+'4.2','E','manifesto spending and borrowing'),L(P+'1.3','H','second oil crisis')]),
'4.4':(1,[L(P+'4.3','H','crisis by 1979')]),
'4.5':(1,[L(P+'4.4','E','Lynch resigning')]),
'5.b':(1,[L(P+'5.5','H','Programme for National Recovery')]),
'5.0':(1,[]),
'5.1':(2,[L(P+'3.1','H','dismissal in the Arms Crisis')]),
'5.2':(2,[L(P+'4.5','H','defeating Colley in 1979')]),
'5.3':(1,[L(P+'5.2','H','first term as Taoiseach')]),
'5.4':(2,[L(P+'5.2','H','third term from 1987')]),
'5.5':(2,[L(P+'5.4','H','the spending cuts of 1987')]),
'5.6':(2,[]),
'5.7':(2,[L(P+'5.6','H','his strengths and weaknesses')]),
'5.8':(2,[L(P+'5.3','H','poor finances before 1987'),L(P+'5.5','H','the PNR')]),
'6.b':(1,[]),
'6.0':(1,[L(P+'7.0','H','Garret FitzGerald')]),
'6.1':(1,[L(P+'6.0','E','the 1981 coalition')]),
'6.2':(1,[L(P+'6.1','H','the government falling in 1982')]),
'6.3':(2,[L(P+'6.2','H','Haughey back in government 1982')]),
'6.4':(1,[L(P+'6.3','E','the 1982 scandals')]),
'6.5':(1,[L(P+'6.2','E','Haughey government of 1982')]),
'7.b':(1,[]),
'7.0':(1,[L(P+'1.2','H','the National Coalition 1973-77','low')]),
'7.1':(1,[L(P+'6.5','H','return as Taoiseach in 1982')]),
'7.2':(1,[L(P+'0.5','E','pluralism and liberalisation')]),
'7.3':(2,[L(P+'7.2','E','the constitutional crusade'),L(P+'8.0','H','the Eighth Amendment'),L(P+'8.2','H','the 1986 divorce referendum')]),
'7.4':(1,[L(P+'0.5','H','liberalisation')]),
'7.5':(1,[L(P+'0.2','H','Northern Ireland conflict')]),
'7.6':(2,[L(P+'0.6','H','deficit and national debt')]),
'7.7':(2,[L(P+'7.2','H','vision of a tolerant Ireland'),L(P+'7.6','H','coalition and economic policy')]),
'7.8':(2,[L(P+'7.7','H','his strengths and weaknesses')]),
'8.b':(1,[L(P+'7.2','H','his liberalising aim')]),
'8.0':(1,[]),
'8.1':(1,[L(P+'8.0','E','the Eighth Amendment')]),
'8.2':(1,[L(P+'7.2','H','divorce reform aim')]),
'8.3':(2,[L(P+'8.2','E','the divorce referendum result'),L(P+'8.0','H','the Eighth Amendment result')]),
'8.4':(1,[L(P+'7.2','H','pluralism debates')]),
'9.b':(1,[]),
'9.0':(2,[]),
'9.1':(1,[]),
'9.2':(1,[L(P+'1.6','H','interest on the national debt')]),
'9.3':(1,[]),
'9.4':(1,[L(P+'5.5','E','the PNR'),L(P+'5.4','H','1987 spending cuts')]),
'10.b':(1,[]),
'10.0':(2,[L(P+'2.7','H','Lynch assessment'),L(P+'4.2','H','1977 borrowing programme')]),
'10.1':(2,[L(P+'6.4','E','GUBU'),L(P+'5.5','H','1987 financial discipline')]),
'10.2':(2,[L(P+'8.3','H','referendum defeats'),L(P+'7.6','H','economic record')]),
'10.3':(1,[L(P+'6.b','H','repeated elections')]),
'10.4':(2,[L(P+'5.4','H','MacSharry and Dukes'),L(P+'9.4','H','recovery after 1987')]),
}
txt=open(D+'packs/hist-ire6-s4.t1g1.txt').read()
ids=re.findall(r'^\[(hist-ire6-s4\.[^\]]+)\]',txt,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
out={}
for i in ids:
    k=i.split('s4.',1)[1]
    c,n=d[k]
    out[i]={'cost':c,'needs':[{'id':a,'strength':s,'why':w,'confidence':f} for a,s,w,f in n]}
assert len(out)==len(ids)==len(d),(len(ids),len(d))
for v in out.values():
    for n in v['needs']: assert n['id'] in allids,n
for i,v in out.items():
    assert all(n['id']!=i for n in v['needs'])
json.dump(out,open(D+'point-links/hist-ire6-s4.t1g1.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
