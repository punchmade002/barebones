import json,re,sys
P='hom-housing-s5.'
H,L='high','low'
def n(i,s,w,c=H): return {"id":i,"strength":s,"why":w,"confidence":c}
D={
'0.b':(1,[]),'0.0':(2,[]),'0.1':(1,[]),'0.2':(1,[]),'0.3':(1,[]),
'0.4':(1,[n('hom-housing-s6.0.1','helpful','aspect and solar heat')]),
'0.5':(1,[]),'0.6':(1,[]),'0.7':(1,[]),
'1.b':(1,[]),
'1.0':(1,[n('hom-housing-s3.7.0','helpful','bungalow vs two-storey suitability',L)]),
'1.1':(1,[n('hom-housing-s3.8.0','helpful','family size decides bedrooms and space')]),
'1.2':(1,[n('hom-housing-s4.1.2','helpful','adaptations for wheelchair users')]),
'1.3':(1,[n(P+'2.0','helpful','planning permission required')]),
'1.4':(1,[]),
'2.b':(1,[]),'2.0':(1,[]),'2.1':(1,[]),
'2.2':(1,[n(P+'2.1','essential','outline permission')]),
'2.3':(2,[]),'2.4':(1,[]),
'2.5':(1,[n(P+'2.1','essential','outline permission')]),
'3.b':(1,[]),'3.0':(1,[]),'3.1':(1,[]),
'3.2':(2,[n(P+'2.3','helpful','full permission contents')]),
'3.3':(1,[]),
'3.4':(1,[n(P+'4.0','helpful','local development plan')]),
'3.5':(1,[]),
'3.6':(1,[n(P+'3.5','helpful','refusal of permission')]),
'3.7':(2,[]),
'4.b':(1,[]),'4.0':(1,[]),'4.1':(1,[]),'4.2':(1,[]),'4.3':(1,[]),'4.4':(1,[]),'4.5':(1,[]),
'5.b':(1,[]),
'5.0':(2,[n(P+'2.3','helpful','planning application contents',L)]),
'5.1':(1,[]),'5.2':(2,[]),'5.3':(2,[]),'5.4':(2,[]),
'5.5':(1,[n('hom-housing-s6.2.4','helpful','BER assessor role')]),
'5.6':(1,[n(P+'5.0','helpful','architect role')]),
}
pk=sys.argv[1]; out=sys.argv[2]
txt=open(pk).read()
tg=txt.split('CANDIDATES')[0]
ids=re.findall(r'^\[([^\]]+)\]',tg,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
res={}
for i in ids:
    c,nd=D[i[len(P):]]; res[i]={"cost":c,"needs":nd}
assert set(D)=={i[len(P):] for i in ids}
for k,v in res.items():
    for x in v['needs']: assert x['id'] in allids and x['id']!=k
json.dump(res,open(out,'w'),indent=1)
print(len(res),sum(len(v['needs']) for v in res.values()),sum(v['cost']==2 for v in res.values()),sum(x['confidence']=='low' for v in res.values() for x in v['needs']))
