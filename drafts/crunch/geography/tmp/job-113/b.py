import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
p='geo-region-european-s3.'
def n(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
D={
'0.b':(1,[]),'0.0':(2,[]),'0.1':(1,[]),'0.2':(1,[]),
'1.b':(1,[]),'1.0':(1,[]),'1.1':(1,[]),'1.2':(1,[]),'1.3':(1,[]),'1.4':(1,[]),
'2.b':(1,[]),'2.0':(1,[]),'2.1':(2,[]),
'2.2':(1,[n(p+'2.1','helpful','the Agreement of 1998')]),
'2.3':(1,[]),
'2.4':(1,[n(p+'2.3','helpful','Northern Ireland executive and Assembly')]),
'2.5':(1,[]),
'3.b':(1,[]),'3.0':(1,[n(p+'2.3','essential','Assembly and power-sharing')]),
'3.1':(1,[n(p+'3.0','essential','the Assembly collapse and restoration'),n(p+'1.0','helpful','nationalist identity','low')]),
'4.b':(1,[]),'4.0':(1,[n(p+'2.0','helpful','conflict (the Troubles) deterring investment')]),
'4.1':(1,[n(p+'2.4','helpful','cross-border bodies')]),
'4.2':(1,[]),'4.3':(1,[]),'4.4':(2,[]),
'5.b':(1,[]),'5.0':(1,[]),'5.1':(1,[]),'5.2':(1,[]),
'6.b':(1,[]),'6.0':(2,[]),'6.1':(1,[]),
'6.2':(1,[n(p+'6.1','helpful','the UK leaving the EU')]),
'6.3':(2,[n(p+'6.2','essential','land border becoming UK-EU border')]),
'6.4':(1,[]),
'7.b':(1,[]),'7.0':(1,[]),
'7.1':(2,[n('geo-region-concept-s3.3.b','helpful','Belgian language border and areas','low')]),
'7.2':(1,[]),'7.3':(1,[]),
'7.4':(1,[n(p+'7.3','helpful','French speakers about 4 in 10')]),
'8.b':(1,[]),'8.0':(2,[n(p+'7.1','helpful','Flanders and Wallonia')]),
'8.1':(1,[]),'8.2':(1,[]),
'8.3':(1,[n(p+'8.2','essential','parties stand in one language community')]),
'8.4':(1,[]),'8.5':(1,[]),'8.6':(1,[]),
'9.b':(1,[]),'9.0':(1,[]),'9.1':(1,[]),'9.2':(1,[]),'9.3':(1,[n(p+'9.2','helpful','Basque separatist context','low')]),
'9.4':(2,[]),'9.5':(1,[]),'9.6':(1,[]),
'10.b':(1,[]),'10.0':(1,[]),
'10.1':(2,[n(p+'8.5','helpful','Belgium federal solution'),n(p+'2.3','helpful','Northern Ireland power-sharing'),n(p+'2.0','helpful','the Troubles as violent conflict')]),
'11.b':(1,[]),'11.0':(1,[]),'11.1':(1,[]),
'11.2':(2,[n(p+'11.3','helpful','qualified majority voting')]),
'11.3':(2,[]),'11.4':(1,[]),'11.5':(1,[]),'11.6':(1,[]),
'12.b':(1,[]),
'12.0':(1,[n('geo-economic-eu-s1.1.0','helpful','four freedoms of the single market')]),
'12.1':(1,[]),'12.2':(2,[]),'12.3':(2,[n(p+'12.1','helpful','the euro membership list')]),'12.4':(1,[]),
'13.b':(1,[]),'13.0':(2,[]),'13.1':(2,[n(p+'13.0','helpful','other convergence criteria')]),'13.2':(1,[]),
'14.b':(1,[]),'14.0':(1,[]),'14.1':(1,[n(p+'14.0','helpful','Ireland bailout comparison')]),'14.2':(1,[]),
'15.b':(1,[]),
'15.0':(1,[n(p+'12.0','helpful','single market as pooled area','low')]),
'15.1':(1,[n(p+'11.3','essential','unanimity lets one state block')]),
'15.2':(1,[n(p+'6.1','helpful','the UK leaving the EU')]),
'15.3':(1,[]),
'16.b':(1,[]),'16.0':(1,[]),
'16.1':(2,[n(p+'11.2','helpful','Lisbon Treaty content','low')]),
'16.2':(1,[]),'16.3':(2,[]),
'16.4':(1,[n(p+'6.4','helpful','Common Travel Area')]),
'17.b':(1,[]),'17.0':(2,[]),'17.1':(1,[]),'17.2':(1,[]),
'17.3':(1,[n(p+'15.1','helpful','unanimity slows decisions'),n(p+'11.3','helpful','unanimity versus qualified majority','low')]),
'18.b':(1,[]),'18.0':(2,[]),'18.1':(2,[]),'18.2':(1,[]),
}
out={}
for k,(c,nd) in D.items(): out[p+'s3.'+k if False else 'geo-region-european-s3.'+k]={"cost":c,"needs":nd}
txt=open(P+'packs/geo-region-european-s3.t1g1.txt').read()
tgt=txt.split('CANDIDATES')[0]
ids=re.findall(r'^\[([^\]]+)\]',tgt,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
assert ids==list(out.keys()),(set(ids)^set(out))
for k,v in out.items():
    for x in v['needs']: assert x['id'] in allids and x['id']!=k,x
json.dump(out,open(P+'point-links/geo-region-european-s3.t1g1.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
