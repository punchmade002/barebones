import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
n='geo-region-concept-s3.'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
H='helpful';E='essential'
D={
'0.b':(1,[L('geo-region-concept-s1.0.2',H,'cultural criteria')]),
'0.0':(1,[]),
'0.1':(1,[L(n+'0.0',H,'culture defined')]),
'0.2':(1,[L('geo-region-concept-s1.0.1',H,'administrative boundaries','low')]),
'0.3':(1,[L('geo-region-concept-s1.1.3',H,'transition zones')]),
'1.b':(1,[]),
'1.0':(2,[]),
'1.1':(2,[]),
'1.2':(1,[L(n+'1.b',H,'Gaeltacht defined')]),
'1.3':(1,[L(n+'1.2',H,'western pockets of Gaeltacht')]),
'1.4':(1,[L(n+'1.3',H,'remote areas kept Irish')]),
'1.5':(1,[L(n+'1.1',H,'Connemara and Meath areas','low')]),
'2.b':(1,[]),
'2.0':(1,[]),
'2.1':(1,[]),
'2.2':(1,[]),
'2.3':(1,[]),
'2.4':(1,[]),
'2.5':(1,[]),
'2.6':(2,[]),
'2.7':(1,[L(n+'1.b',H,'Gaeltacht defined')]),
'3.b':(1,[]),
'3.0':(1,[]),
'3.1':(1,[L(n+'3.0',H,'Flanders Dutch-speaking','low')]),
'3.2':(1,[]),
'3.3':(1,[]),
'3.4':(2,[L(n+'3.1',H,'Wallonia French-speaking','low')]),
'3.5':(1,[]),
'4.b':(1,[]),
'4.0':(1,[]),
'4.1':(1,[L(n+'4.0',H,'federal state'),L(n+'3.2',H,'German-speaking community','low')]),
'4.2':(1,[]),
'4.3':(1,[]),
'4.4':(1,[L(n+'4.2',H,'divided language parties')]),
'4.5':(2,[L(n+'3.0',H,'Flanders region'),L(n+'3.1',H,'Wallonia region')]),
'5.b':(1,[]),
'5.0':(1,[L(n+'0.2',H,'regions crossing state borders')]),
'5.1':(1,[L(n+'0.2',H,'regions within states','low')]),
'5.2':(1,[]),
'5.3':(1,[L(n+'0.2',H,'several regions in one state')]),
'6.b':(1,[]),
'6.0':(1,[]),
'6.1':(1,[]),
'6.2':(1,[]),
'6.3':(1,[]),
'6.4':(1,[L(n+'6.3',H,'Protestant settlers in Ulster')]),
'6.5':(1,[L(n+'6.4',H,'nationalist and unionist identities')]),
'6.6':(1,[]),
'6.7':(1,[]),
'7.b':(1,[]),
'7.0':(1,[]),
'7.1':(1,[L(n+'7.0',H,'Mecca and Medina, Muhammad')]),
'7.2':(1,[]),
'7.3':(1,[]),
'7.4':(1,[]),
'7.5':(2,[L(n+'7.0',H,'Islam origins'),L(n+'7.2',H,'extent of Islamic world')]),
'8.b':(1,[]),
'8.0':(2,[]),
'8.1':(1,[]),
'8.2':(1,[]),
'8.3':(1,[]),
'8.4':(1,[L(n+'7.1',H,'Hijra begins calendar')]),
'8.5':(1,[]),
'9.b':(1,[]),
'9.0':(1,[L(n+'7.5',H,'Ottoman spread of Islam')]),
'9.1':(1,[L(n+'7.5',H,'Arab conquest into Spain')]),
'9.2':(1,[L(n+'7.2',H,'Islamic world origins','low')]),
'10.b':(1,[]),
'10.0':(1,[]),
'10.1':(1,[L(n+'10.4',H,'the Reformation')]),
'10.2':(1,[]),
'10.3':(1,[]),
'10.4':(1,[]),
'10.5':(2,[L(n+'10.0',H,'Catholic Croats','low'),L(n+'10.2',H,'Orthodox Serbs','low')]),
}
txt=open(P+'packs/geo-region-concept-s3.t1g1.txt').read()
tg=txt.split('CANDIDATES')[0]
tids=re.findall(r'^\[(\S+?)\]',tg,re.M)
allids=set(re.findall(r'^\[(\S+?)\]',txt,re.M))
out={}
for t in tids:
    k=t.replace(n,'');c,nd=D[k];out[t]={"cost":c,"needs":nd}
assert len(D)==len(tids)
for v in out.values():
    for x in v['needs']: assert x['id'] in allids
json.dump(out,open(P+'point-links/geo-region-concept-s3.t1g1.json','w'),ensure_ascii=False)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
