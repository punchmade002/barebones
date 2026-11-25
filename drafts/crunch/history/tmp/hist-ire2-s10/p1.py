import json,re
P='hist-ire2-s10.'
H,L='high','low'
def n(i,s,w,c=H): return {"id":i if i.startswith('hist-') else P+i,"strength":s,"why":w,"confidence":c}
h='helpful'; e='essential'
D={
'0.b':(1,[]),'0.0':(1,[]),
'0.1':(2,[n('0.0',h,'the 1892 lecture')]),
'0.2':(1,[n('0.1',h,'Hyde’s anglicisation argument')]),
'0.3':(1,[]),
'0.4':(1,[n('hist-ire2-s9.1.b',h,'the GAA’s founding'),n('1.0',h,'the Gaelic League’s founding')]),
'1.b':(1,[]),'1.0':(1,[n('2.0',h,'Douglas Hyde')]),'1.1':(1,[]),'1.2':(1,[]),'1.3':(1,[]),'1.4':(1,[]),
'1.5':(2,[]),'1.6':(1,[]),
'1.7':(2,[n('hist-ire2-s4.7.1',h,'the IRB','low'),n('2.4',h,'Hyde’s resignation')]),
'2.b':(1,[]),'2.0':(1,[]),'2.1':(1,[]),
'2.2':(1,[n('0.0',h,'the 1892 lecture'),n('1.0',h,'founding the League')]),
'2.3':(2,[n('3.b',h,'Moran and the Irish Irelanders')]),
'2.4':(1,[n('1.7',h,'the League’s political turn')]),
'2.5':(2,[n('2.2',h,'Hyde’s role in the revival')]),
'3.b':(1,[]),'3.0':(1,[]),
'3.1':(1,[n('4.b',h,'the Anglo-Irish literary movement')]),
'3.2':(1,[]),
'3.3':(1,[n('3.0',h,'Moran’s Irish Ireland')]),
'3.4':(1,[n('3.0',h,'The Leader')]),
'3.5':(2,[n('2.b',h,'Hyde’s inclusive approach'),n('3.2',h,'Moran’s Gaelic Catholic nation')]),
'4.b':(1,[]),
'4.0':(1,[n('0.0',h,'Hyde’s 1892 lecture')]),
'4.1':(2,[]),'4.2':(1,[]),
'4.3':(2,[n('4.1',h,'Yeats and Lady Gregory’s theatre')]),
'4.4':(1,[]),
'4.5':(1,[n('4.3',h,'the Abbey Theatre')]),
'5.b':(1,[]),'5.0':(1,[]),
'5.1':(1,[n('4.0',h,'National Literary Society'),n('4.1',h,'Irish Literary Theatre'),n('4.3',h,'the Abbey')]),
'5.2':(1,[]),
'5.3':(2,[n('3.0',h,'Moran’s attacks'),n('6.0',h,'Church attack on Countess Cathleen')]),
'5.4':(2,[n('6.2',e,'the Hugh Lane gallery dispute')]),
'5.5':(1,[]),'5.6':(1,[]),
'6.b':(1,[]),
'6.0':(1,[n('4.1',h,'The Countess Cathleen')]),
'6.1':(1,[n('4.5',e,'the Playboy riots')]),
'6.2':(2,[]),
'6.3':(1,[n('6.2',e,'the Hugh Lane dispute')]),
'6.4':(1,[n('3.2',h,'Gaelic and Catholic nation')]),
'6.5':(2,[n('6.4',e,'the two competing visions')]),
'7.b':(1,[]),'7.0':(1,[]),'7.1':(1,[]),'7.2':(1,[]),'7.3':(1,[]),'7.4':(1,[]),'7.5':(1,[]),'7.6':(1,[]),'7.7':(1,[]),
'7.8':(2,[n('7.7',e,'bishops’ support for Home Rule'),n('7.5',h,'the Ne Temere decree'),n('hist-ire2-s4.1.b',h,'the Parnell split')]),
'8.b':(1,[n('hist-ire2-s9.1.b',h,'the GAA’s founding'),n('1.b',h,'the Gaelic League')]),
'8.0':(1,[n('hist-ire2-s9.6.5',h,'the GAA’s recovery')]),
'8.1':(1,[n('hist-ire2-s9.5.0',e,'IRB involvement in the GAA'),n('hist-ire2-s9.3.2',h,'the foreign games ban')]),
'8.2':(2,[n('hist-ire2-s9.1.b',h,'the GAA'),n('1.b',h,'the Gaelic League')]),
'8.3':(1,[n('hist-ire2-s9.5.0',h,'GAA political ties','low'),n('1.7',h,'League politicised in 1915')]),
'8.4':(1,[n('0.0',h,'de-anglicisation')]),
'8.5':(1,[n('1.5',h,'compulsory Irish campaign')]),
'9.b':(1,[]),
'9.0':(1,[n('1.b',h,'the Gaelic League'),n('4.3',h,'the Abbey Theatre')]),
'9.1':(1,[n('3.2',h,'Catholic and Gaelic emphasis')]),
'9.2':(2,[n('3.b',h,'Moran’s Irish Ireland')]),
'9.3':(2,[n('1.7',h,'IRB in the League','low')]),
}
txt=open('/Users/gabrielwhelan/barebones/drafts/crunch/history/packs/hist-ire2-s10.t1g1.txt').read()
tg=re.findall(r'^\[(hist-ire2-s10\.[^\]]+)\]',txt.split('CANDIDATES')[0],re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
out={}
for t in tg:
    k=t[len(P):]
    c,nd=D[k]; out[t]={"cost":c,"needs":nd}
assert len(D)==len(tg)==len(out),(len(D),len(tg))
for t,v in out.items():
    for x in v['needs']: assert x['id'] in allids and x['id']!=t,(t,x)
json.dump(out,open('/Users/gabrielwhelan/barebones/drafts/crunch/history/point-links/hist-ire2-s10.t1g1.json','w'),ensure_ascii=False,indent=1)
nl=sum(len(v['needs']) for v in out.values())
print(len(out),nl,sum(v['cost']==2 for v in out.values()),sum(x['confidence']==L for v in out.values() for x in v['needs']))
