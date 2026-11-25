import json,re
P='hist-ire4-s4.'
D='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
def L(i,s,w,c='high'): return (i,{'E':'essential','H':'helpful'}[s],w,c)
d={
'0.b':(1,[]),
'0.0':(1,[L('hist-ire4-s1.2.3','H','Famine emigration')]),
'0.1':(2,[]),'0.2':(1,[]),
'0.3':(1,[L('hist-ire4-s1.0.0','H','Ulster Presbyterian emigrants')]),
'0.4':(1,[]),
'1.b':(1,[]),
'1.0':(1,[]),
'1.1':(1,[L(P+'1.0','E','the Fenian movement and the IRB')]),
'1.2':(1,[L(P+'1.1','H','American Fenian Brotherhood')]),
'1.3':(2,[L(P+'1.1','E','the Fenian Brotherhood')]),
'1.4':(2,[L(P+'1.3','E','the Fenian raids into Canada')]),
'1.5':(1,[L(P+'1.1','H','the declining Fenian Brotherhood')]),
'1.6':(1,[]),
'1.7':(1,[]),
'2.b':(1,[]),
'2.0':(1,[L(P+'1.0','H','the IRB')]),
'2.1':(2,[L(P+'2.0','H','Devoy and the IRB')]),
'2.2':(1,[L(P+'1.5','H','Clan na Gael')]),
'2.3':(1,[L(P+'1.6','H','Fenian prisoners in Western Australia')]),
'2.4':(2,[L(P+'1.0','H','the Fenians')]),
'2.5':(1,[L(P+'2.2','H','Devoy in Clan na Gael')]),
'3.b':(1,[L(P+'3.0','H','Devoy and the Rising')]),
'3.0':(1,[L(P+'2.2','H','Clan na Gael')]),
'3.1':(1,[L(P+'6.5','H','Devoy-de Valera quarrel')]),
'3.2':(2,[L(P+'3.1','H','his quarrel with de Valera')]),
'3.3':(2,[L(P+'2.2','H','Irish-American support for republicanism','low')]),
'4.b':(1,[]),
'4.0':(2,[L(P+'2.4','H','the New Departure')]),
'4.1':(1,[L(P+'4.0','H','the land question')]),
'4.2':(1,[L(P+'4.1','H','the Land League')]),
'4.3':(1,[L(P+'4.1','H','the Land League')]),
'4.4':(1,[L(P+'4.1','E','the Land League')]),
'4.5':(1,[L(P+'4.1','H','Land League campaign')]),
'5.b':(1,[]),
'5.0':(1,[L(P+'0.1','H','the Irish Parliamentary Party')]),
'5.1':(1,[L(P+'0.2','H','the War of Independence')]),
'5.2':(1,[L(P+'0.1','H','Home Rule')]),
'5.3':(1,[L(P+'0.2','H','the Rising of 1916')]),
'5.4':(1,[L(P+'2.3','E','the Catalpa rescue')]),
'6.b':(1,[]),
'6.0':(1,[L(P+'3.0','H','Devoy and German help')]),
'6.1':(1,[]),
'6.2':(1,[L(P+'6.0','H','German help for the Rising')]),
'6.3':(1,[L(P+'6.1','E','the Friends of Irish Freedom')]),
'6.4':(1,[L(P+'6.3','H','Irish-American support for the Republic')]),
'6.5':(1,[L(P+'6.1','H','Devoy and Cohalan')]),
'7.b':(1,[L(P+'7.0','H','partition')]),
'7.0':(1,[]),
'7.1':(1,[L(P+'7.0','E','partition and the border')]),
'7.2':(1,[L(P+'7.1','H','the anti-partition case')]),
'7.3':(1,[]),
'7.4':(1,[L(P+'7.3','E','the Republic of Ireland Act')]),
'7.5':(1,[L(P+'7.0','H','partition')]),
'7.6':(1,[L(P+'7.0','H','partition')]),
'8.b':(1,[L(P+'8.0','H','Ulster-Scots identity')]),
'8.0':(1,[L(P+'0.3','H','Ulster Presbyterian emigrants')]),
'8.1':(1,[L(P+'8.0','E','Ulster-Scots descent')]),
'8.2':(1,[L(P+'0.1','H','Home Rule crisis')]),
'8.3':(1,[L(P+'0.4','E','the Orange Order')]),
'8.4':(1,[L(P+'0.4','H','the Orange Order')]),
'8.5':(2,[L(P+'8.0','H','Scotch-Irish networks'),L(P+'8.3','H','Orange networks')]),
'9.b':(1,[]),
'9.0':(1,[]),'9.1':(1,[]),'9.2':(1,[]),
'9.3':(1,[L(P+'8.2','H','the Ulster Covenant')]),
'9.4':(1,[L(P+'0.1','H','the Home Rule crisis')]),
'9.5':(2,[]),
'9.6':(1,[]),
'9.7':(2,[L(P+'9.4','H','his Ulster stand')]),
'10.b':(1,[]),
'10.0':(2,[L(P+'1.5','H','Fenian and Clan na Gael networks'),L(P+'4.5','H','Land League funds'),L(P+'6.3','H','Irish America 1916-19')]),
'10.1':(2,[L(P+'1.4','H','the failed Canadian raids'),L(P+'6.5','H','Devoy-de Valera quarrel')]),
'10.2':(1,[L(P+'7.1','H','anti-partition campaigners')]),
'10.3':(2,[L(P+'8.5','H','unionist lobbying abroad')]),
'10.4':(1,[]),
'10.5':(1,[]),
}
txt=open(D+'packs/hist-ire4-s4.t1g1.txt').read()
ids=re.findall(r'^\[(hist-ire4-s4\.[^\]]+)\]',txt,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
out={}
for i in ids:
    k=i.split('s4.',1)[1]
    c,n=d[k]
    out[i]={'cost':c,'needs':[{'id':a,'strength':s,'why':w,'confidence':f} for a,s,w,f in n]}
assert len(out)==len(ids)==len(d),(len(ids),len(d))
for i,v in out.items():
    for n in v['needs']: assert n['id'] in allids and n['id']!=i,n
json.dump(out,open(D+'point-links/hist-ire4-s4.t1g1.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
