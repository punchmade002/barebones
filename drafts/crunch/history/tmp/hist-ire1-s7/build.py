import json,re,sys
P='/Users/gabrielwhelan/barebones/drafts/crunch/history/'
H,E='essential','helpful'
def L(i,s,w,c='high'): return dict(id=i,strength=s,why=w,confidence=c)
p='hist-ire1-s7.'
D={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),'0.2':(2,[]),'0.3':(2,[]),
'0.4':(1,[L(p+'0.b',E,'uses Larkin and devotional revolution')]),
'0.5':(2,[L('hist-ire1-s4.7.1',E,'Famine hit poor cottiers hardest')]),
'0.6':(1,[L(p+'0.0',E,'church building programme','low')]),
'1.b':(1,[]),'1.0':(1,[]),
'1.1':(1,[L(p+'1.0',H,'uses evangelical revival')]),
'1.2':(1,[L(p+'1.1',H,'examples of Second Reformation')]),
'1.3':(1,[L('hist-ire1-s4.3.3',H,'souperism and Famine soup kitchens')]),
'1.4':(1,[L('hist-ire1-s2.0.5',H,'Orange Order dissolved 1836','low')]),
'1.5':(1,[L(p+'1.0',H,'Ulster evangelical')]),
'1.6':(1,[L(p+'1.0',H,'evangelical revival')]),
'1.7':(1,[]),
'2.b':(1,[]),
'2.0':(1,[L('hist-ire1-s2.5.b',H,'Young Ireland idea of nation')]),
'2.1':(1,[L('hist-ire1-s2.5.0',H,'founding of The Nation')]),
'2.2':(1,[]),'2.3':(1,[]),
'2.4':(1,[L('hist-ire1-s4.8.4',H,'Famine hit Irish-speaking west')]),
'2.5':(1,[]),
'2.6':(1,[L(p+'2.0',H,'cultural nationalism of Young Ireland')]),
'3.b':(1,[L(p+'6.1',H,'Romanisation of the Church')]),
'3.0':(1,[]),
'3.1':(1,[L(p+'5.b',H,'Synod of Thurles')]),
'3.2':(1,[]),
'3.3':(2,[L(p+'6.0',H,'ultramontanism')]),
'3.4':(1,[L(p+'5.2',H,'Catholic University founding')]),
'3.5':(2,[L('hist-ire1-s2.5.b',H,'Young Ireland'),L('hist-ire1-s2.6.8',H,'Fenian movement origins'),L('hist-ire1-s2.6.7',H,'MacManus transported after 1848','low')]),
'3.6':(1,[L(p+'1.7',H,'disestablishment of Church of Ireland')]),
'3.7':(1,[L(p+'4.3',H,'MacHale opposed colleges')]),
'3.8':(2,[L(p+'0.b',E,'devotional revolution')]),
'4.b':(1,[]),'4.0':(1,[]),'4.1':(1,[]),
'4.2':(1,[L('hist-ire1-s2.4.4',H,'Queen\'s Colleges founded 1845')]),
'4.3':(1,[L(p+'4.2',E,'uses Queen\'s Colleges dispute')]),
'4.4':(1,[L(p+'4.2',H,'Queen\'s Colleges condemned')]),
'4.5':(1,[L(p+'3.b',H,'Paul Cullen introduced')]),
'5.b':(1,[]),
'5.0':(1,[L(p+'3.b',H,'Cullen as presiding delegate')]),
'5.1':(1,[L(p+'4.2',E,'uses Queen\'s Colleges')]),
'5.2':(1,[]),'5.3':(1,[]),'5.4':(1,[]),'5.5':(1,[]),
'5.6':(1,[L(p+'4.3',H,'MacHale and Queen\'s Colleges')]),
'5.7':(1,[]),
'6.b':(1,[]),'6.0':(1,[]),'6.1':(1,[]),
'6.2':(1,[L(p+'5.2',E,'uses the Catholic University')]),
'6.3':(1,[L(p+'6.2',H,'Catholic University weakness')]),
'6.4':(1,[L(p+'3.b',H,'Cullen as leading figure')]),
'6.5':(1,[L(p+'6.1',H,'Romanisation criticised or praised')]),
'6.6':(2,[L(p+'0.b',E,'devotional revolution and Larkin')]),
'7.b':(1,[]),'7.0':(1,[]),
'7.1':(2,[L(p+'4.3',H,'Daniel Murray of Dublin','low')]),
'7.2':(1,[L(p+'7.1',E,'uses the Sisters of Charity')]),
'7.3':(2,[L(p+'7.1',H,'Sisters of Charity founded')]),
'7.4':(1,[L(p+'7.1',H,'order she founded')]),
'7.5':(1,[]),
'7.6':(1,[L(p+'7.3',H,'running hospital as invalid','low')]),
'7.7':(2,[L(p+'0.2',H,'growth of religious orders')]),
'8.b':(1,[]),'8.0':(1,[]),
'8.1':(1,[L(p+'1.0',H,'evangelical Protestant outlook','low')]),
'8.2':(2,[]),'8.3':(1,[]),'8.4':(1,[]),
'8.5':(1,[L(p+'8.1',E,'uses his anti-Catholic early writing')]),
'8.6':(1,[L(p+'8.2',H,'his pre-Famine rural writing')]),
'9.b':(1,[]),
'9.0':(1,[L('hist-ire1-s2.5.0',H,'founding of The Nation')]),
'9.1':(1,[]),'9.2':(1,[]),
'9.3':(1,[L('hist-ire1-s2.5.2',H,'non-sectarian nationality idea')]),
'9.4':(1,[]),'9.5':(1,[]),
'9.6':(1,[L(p+'2.0',H,'cultural nationalism idea')]),
'10.b':(1,[]),'10.0':(1,[]),
'10.1':(1,[L(p+'2.1',H,'The Nation')]),
'10.2':(1,[]),'10.3':(1,[]),
'10.4':(1,[L(p+'10.3',H,'O\'Donovan in Ordnance Survey'),L(p+'5.2',H,'Catholic University')]),
'10.5':(1,[]),
'11.b':(1,[]),'11.0':(1,[]),'11.1':(1,[]),
'11.2':(1,[L(p+'11.1',E,'the Leviathan telescope')]),
'11.3':(1,[]),
'11.4':(1,[L(p+'4.2',H,'Queen\'s Colleges','low')]),
'11.5':(1,[L(p+'4.2',H,'Queen\'s Colleges','low')]),
'11.6':(1,[L(p+'4.2',H,'Queen\'s Colleges')]),
'12.b':(1,[]),
'12.0':(2,[L(p+'0.b',E,'devotional revolution')]),
'12.1':(2,[L(p+'6.2',H,'weak Catholic University'),L(p+'6.5',H,'Protestant and liberal alienation')]),
'12.2':(2,[L(p+'6.5',H,'Protestant and Catholic views of Cullen')]),
'12.3':(2,[L(p+'0.6',H,'Catholic identity tied to nationality')]),
'12.4':(2,[L(p+'10.0',H,'Moore'),L(p+'8.2',H,'Carleton'),L(p+'10.2',H,'Petrie'),L(p+'10.4',H,'O\'Donovan'),L(p+'11.0',H,'Hamilton'),L(p+'11.1',H,'Rosse'),L(p+'11.4',H,'Boole')]),
'12.5':(1,[L('hist-ire1-s4.8.4',H,'language declined after Famine'),L(p+'2.4',H,'Irish language decline')]),
}
pk=P+'packs/hist-ire1-s7.t1g1.txt'
txt=open(pk).read()
tgt=re.findall(r'^\[(hist-ire1-s7\.[^\]]+)\]',txt.split('CANDIDATES')[0],re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
out={}
for t in tgt:
    k=t[len(p):]
    c,n=D[k]; out[t]={'cost':c,'needs':n}
assert len(D)==len(tgt)
for t,v in out.items():
    for n in v['needs']: assert n['id'] in allids and n['id']!=t,(t,n)
json.dump(out,open(P+'point-links/hist-ire1-s7.t1g1.json','w'),indent=1)
r=json.load(open(P+'point-links/hist-ire1-s7.t1g1.json'))
ln=[n for v in r.values() for n in v['needs']]
print(len(r),len(ln),sum(v['cost']==2 for v in r.values()),sum(n['confidence']=='low' for n in ln))
