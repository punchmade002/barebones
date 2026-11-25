import json,re
P='geo-region-concept-s2'
L=lambda i,s,w,c='high':{"id":i,"strength":s,"why":w,"confidence":c}
d={
'0.b':(1,[]),
'0.0':(1,[L('geo-region-concept-s1.1.3','helpful','transition zones of physical regions')]),
'0.1':(1,[]),
'0.2':(1,[L('geo-economic-eu-s3.20.1','helpful','EU regional funds (ERDF)','low')]),
'0.3':(1,[]),
'1.b':(1,[]),
'1.0':(1,[]),
'1.1':(1,[]),
'1.2':(1,[]),
'1.3':(1,[L('geo-region-concept-s2.6.0','helpful','regional assemblies explained there')]),
'1.4':(1,[]),
'1.5':(1,[]),
'2.b':(1,[]),
'2.0':(1,[]),
'2.1':(1,[]),
'3.b':(1,[]),
'3.0':(1,[]),
'3.1':(2,[]),
'3.2':(1,[L('geo-region-concept-s2.3.1','helpful','Dublin split into councils','low')]),
'4.b':(1,[]),
'4.0':(1,[]),
'4.1':(2,[L('geo-region-concept-s2.4.0','helpful','city corporations became city councils','low')]),
'4.2':(1,[L('geo-region-concept-s2.4.1','helpful','the 2014 Act context')]),
'4.3':(2,[]),
'4.4':(1,[]),
'4.5':(1,[L('geo-region-concept-s2.4.2','helpful','councillors elected','low')]),
'5.b':(1,[]),
'5.0':(1,[]),
'5.1':(1,[]),
'6.b':(1,[]),
'6.0':(2,[L('geo-economic-eu-s3.24.0','helpful','regional assemblies run ERDF programmes','low')]),
'6.1':(1,[L('geo-economic-eu-s3.22.0','helpful','BMW region split of Ireland')]),
'6.2':(1,[L('geo-economic-eu-s3.21.0','helpful','Objective 1 status explained')]),
'6.3':(1,[]),
'7.b':(1,[]),
'7.0':(1,[L('geo-region-concept-s2.7.b','helpful','constituency and TDs defined')]),
'7.1':(1,[L('geo-region-concept-s2.7.b','helpful','TDs and constituencies')]),
'7.2':(1,[L('geo-region-concept-s2.7.1','helpful','boundaries redrawn after census','low')]),
'7.3':(1,[L('geo-region-concept-s2.7.0','helpful','seats per constituency','low')]),
'7.4':(1,[L('geo-region-concept-s2.2.0','helpful','county boundaries','low')]),
'7.5':(1,[L('geo-region-concept-s2.7.1','helpful','seats follow population','low')]),
'7.6':(2,[]),
'8.b':(1,[L('geo-region-concept-s2.9.0','helpful','commune, département, region tiers')]),
'8.0':(1,[]),
'8.1':(1,[]),
'8.2':(1,[]),
'8.3':(2,[]),
'8.4':(2,[]),
'8.5':(2,[]),
'9.b':(1,[]),
'9.0':(1,[]),
'9.1':(1,[L('geo-region-concept-s2.9.0','helpful','regions as the top tier')]),
'9.2':(1,[]),
'9.3':(1,[]),
'10.b':(1,[]),
'10.0':(1,[L('geo-region-concept-s2.9.0','essential','France three tiers')]),
}
out={f'{P}.{k}':{"cost":c,"needs":n} for k,(c,n) in d.items()}
open(f'point-links/{P}.t1g1.json','w').write(json.dumps(out,indent=1))
pk=open(f'packs/{P}.t1g1.txt').read()
ids=set(re.findall(r'^\[([^\]]+)\]',pk,re.M))
tg=[i for i in re.findall(r'^\[([^\]]+)\]',pk.split('CANDIDATES')[0],re.M)]
assert set(tg)==set(out) and len(tg)==len(out),(set(tg)^set(out))
for v in out.values():
  for n in v['needs']: assert n['id'] in ids
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
