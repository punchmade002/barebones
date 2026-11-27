import json,re
P='hom-sociological-concepts-s3.'
H,L='high','low'
E,Hp='essential','helpful'
def n(i,w,s=Hp,c=H): return {"id":i,"strength":s,"why":w,"confidence":c}
d={}
def a(k,cost,*needs): d[P+k]={"cost":cost,"needs":list(needs)}
S1='hom-sociological-concepts-s1.'; F='hom-family-society-s1.'
a('0.b',1); a('0.0',1)
a('0.1',1,n(P+'3.1','primary socialisation'))
a('0.2',1); a('0.3',1)
a('0.4',2,n(P+'0.0','primary group traits',E),n(P+'0.2','secondary group traits',E))
a('0.5',1)
a('0.6',1,n(S1+'2.0','norms'))
a('0.7',1,n(P+'4.b','agents of socialisation'))
a('1.b',1); a('1.0',1)
a('1.1',1,n(P+'1.0','blood kinship'))
a('1.2',1,n(P+'1.0','marriage kinship'))
a('1.3',1)
a('1.4',1,n(P+'1.3','nuclear family'))
a('1.5',1)
a('1.6',1,n(F+'2.0','family in every society'))
a('1.7',1,n(F+'3.2','descent patterns'))
a('2.b',1); a('2.0',1); a('2.1',1); a('2.2',1)
a('3.b',1); a('3.0',1)
a('3.1',2,n(S1+'2.0','norms learned','helpful',L))
a('3.2',2,n(S1+'2.0','norms and roles learned','helpful',L),n(P+'3.1','primary versus secondary','helpful'))
a('3.3',1,n(S1+'1.0','culture passed on'))
a('3.4',2,n(S1+'3.0','rewards and punishments'))
a('3.5',1,n(S1+'2.0','norms of a group'))
a('3.6',1)
a('4.b',1); a('4.0',1)
a('4.1',1,n(P+'3.3.2' if False else P+'3.2','secondary socialisation','helpful'))
a('4.2',1,n(P+'0.7','peer group'))
a('4.3',1)
a('5.b',1); a('5.0',1); a('5.1',1)
a('5.2',2,n(F+'3.1','polygamy terms'))
a('5.3',1,n(P+'5.2','polygamy'))
a('5.4',1,n(P+'5.0','monogamy'))
a('5.5',1,n(P+'5.0','monogamy',E))
a('5.6',1)
a('5.7',1,n(P+'5.0','monogamy'))
txt=open('../../packs/hom-sociological-concepts-s3.t1g1.txt').read()
ids=re.findall(r'^\[([^\]]+)\]',txt.split('CANDIDATES')[0],re.M); allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
assert set(ids)==set(d) and len(ids)==len(d),(set(ids)^set(d))
out={i:d[i] for i in ids}
for k,v in out.items():
    for x in v['needs']: assert x['id'] in allids and x['id']!=k,x['id']
json.dump(out,open('../../point-links/hom-sociological-concepts-s3.t1g1.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
