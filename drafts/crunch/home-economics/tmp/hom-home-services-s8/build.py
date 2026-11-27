import json,re,sys
P='hom-home-services-s8.'
H,L='high','low'
def n(i,s,w,c=H): return {"id":i,"strength":s,"why":w,"confidence":c}
D={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),'0.2':(1,[]),
'0.3':(1,[n(P+'0.0','helpful','translucent materials scatter light')]),
'0.4':(1,[]),'0.5':(1,[]),'0.6':(1,[]),
'1.b':(1,[]),'1.0':(1,[]),'1.1':(2,[]),'1.2':(1,[]),
'1.3':(2,[n('hom-home-interior-s1.9.0','helpful','focal point')]),
'1.4':(1,[n('hom-home-interior-s1.4.4','helpful','aspect of a room',L)]),
'1.5':(1,[n(P+'0.4','helpful','dark surfaces absorb light')]),
'2.b':(1,[]),'2.0':(1,[]),'2.1':(1,[]),
'2.2':(2,[n('hom-home-services-s3.0.7','helpful','fuse rating')]),
'2.3':(1,[]),
'3.b':(1,[]),
'3.0':(1,[n(P+'0.3','helpful','frosted glass scatters light')]),
'3.1':(1,[]),
'3.2':(1,[n(P+'0.1','helpful','mirrors reflect light')]),
'4.b':(1,[]),
'4.0':(2,[n(P+'1.3','helpful','general lighting layer')]),
'4.1':(2,[n(P+'1.3','helpful','task lighting layer')]),
'4.2':(2,[n(P+'1.3','helpful','accent lighting layer')]),
'4.3':(1,[]),
'5.b':(1,[]),'5.0':(1,[]),'5.1':(2,[]),
'5.2':(1,[n(P+'5.1','essential','UV light in CFL tube')]),
'5.3':(2,[n(P+'5.0','helpful','filament bulb comparison')]),
'5.4':(1,[n(P+'5.3','helpful','mercury in CFLs')]),
'5.5':(2,[]),
'5.6':(2,[n(P+'5.0','helpful','filament bulb comparison')]),
'5.7':(1,[n(P+'2.1','helpful','dimmers and timers')]),
'6.b':(1,[]),
'6.0':(1,[n('hom-home-services-s3.0.2','essential','watts measure power')]),
'6.1':(1,[n(P+'0.6','helpful','warm and cool colour temperature')]),
'6.2':(1,[]),
'6.3':(1,[n('hom-home-services-s2.10.4','helpful','EU energy label rescaling')]),
'7.b':(1,[]),
'7.0':(2,[n(P+'5.6','helpful','LED features')]),
'7.1':(1,[]),'7.2':(1,[]),'7.3':(1,[]),
'7.4':(1,[n(P+'1.3','helpful','accent lighting')]),
'7.5':(1,[]),
'7.6':(1,[n(P+'5.6','helpful','dimmable LEDs')]),
'8.b':(1,[]),'8.0':(1,[]),
'8.1':(1,[n(P+'1.3','helpful','general, task, accent lighting')]),
'8.2':(2,[n(P+'2.2','helpful','lighting safety points')]),
}
pk=sys.argv[1]; out=sys.argv[2]
txt=open(pk).read()
tg=txt.split('CANDIDATES')[0]
ids=re.findall(r'^\[([^\]]+)\]',tg,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
res={}
for i in ids:
    k=i[len(P):]
    c,nd=D[k]; res[i]={"cost":c,"needs":nd}
assert set(D)=={i[len(P):] for i in ids}
for v in res.values():
    for x in v['needs']: assert x['id'] in allids
json.dump(res,open(out,'w'),indent=1)
print(len(res),sum(len(v['needs']) for v in res.values()),sum(v['cost']==2 for v in res.values()),sum(x['confidence']=='low' for v in res.values() for x in v['needs']))
