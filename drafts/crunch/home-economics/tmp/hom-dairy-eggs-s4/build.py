import json,re,sys
P='hom-dairy-eggs-s4.'
H,L='high','low'
def n(i,s,w,c=H): return {"id":i,"strength":s,"why":w,"confidence":c}
D={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),
'0.2':(2,[n('hom-food-safety-s4.2.1','helpful','surface mould ripening')]),
'0.3':(1,[n('hom-food-safety-s4.2.0','helpful','mould grows through blue cheese')]),
'0.4':(1,[]),'0.5':(1,[n(P+'0.4','helpful','processed cheese')]),
'0.6':(2,[]),
'1.b':(1,[]),
'1.0':(2,[n('hom-dairy-eggs-s1.0.1','helpful','HBV protein and essential amino acids'),n('hom-proteins-s4.2.0','helpful','casein is milk protein',L)]),
'1.1':(1,[]),'1.2':(1,[]),'1.3':(1,[]),
'1.4':(1,[n(P+'3.3','helpful','lactose drains away in whey')]),
'1.5':(2,[]),'1.6':(2,[]),'1.7':(2,[]),
'2.b':(1,[]),'2.0':(1,[]),'2.1':(1,[]),
'2.2':(1,[n(P+'1.2','helpful','fat gives energy')]),
'2.3':(2,[n(P+'1.2','helpful','fat content of cheese'),n(P+'1.7','helpful','sodium in cheese',L)]),
'2.4':(1,[n(P+'1.2','helpful','fat content of cheese',L)]),
'2.5':(2,[n(P+'0.2','helpful','mould-ripened soft cheeses'),n(P+'0.3','helpful','blue cheeses')]),
'2.6':(1,[n(P+'1.7','helpful','cheese lacks fibre and vitamin C')]),
'2.7':(1,[]),
'3.b':(1,[]),
'3.0':(1,[n('hom-food-safety-s4.0.2','helpful','lactic acid fermentation of lactose')]),
'3.1':(2,[n('hom-proteins-s4.2.2','helpful','rennin coagulates casein')]),
'3.2':(1,[n(P+'3.1','essential','rennet changes caseinogen to casein')]),
'3.3':(1,[n(P+'3.2','essential','curds and whey separate')]),
'4.b':(1,[]),
'4.0':(1,[n(P+'3.0','helpful','starter culture bacteria')]),
'4.1':(1,[n(P+'3.1','essential','rennet makes curds and whey')]),
'4.2':(1,[]),'4.3':(1,[]),'4.4':(1,[]),'4.5':(1,[]),'4.6':(1,[]),'4.7':(1,[]),
'5.b':(1,[]),
'5.0':(1,[n(P+'0.3','helpful','blue-veined cheese')]),
'5.1':(1,[n(P+'0.2','helpful','soft mould-ripened cheese')]),
'6.b':(1,[]),'6.0':(1,[]),'6.1':(1,[]),'6.2':(1,[]),'6.3':(1,[]),'6.4':(1,[]),
'7.b':(1,[]),'7.0':(1,[]),
'7.1':(1,[n('hom-proteins-s5.0.3','helpful','coagulation of protein')]),
'7.2':(1,[]),'7.3':(1,[]),'7.4':(1,[]),'7.5':(1,[]),
'8.b':(1,[]),'8.0':(1,[]),'8.1':(1,[]),'8.2':(1,[]),'8.3':(1,[]),'8.4':(1,[]),'8.5':(1,[]),
'8.6':(2,[n(P+'0.0','helpful','hard cheese examples')]),
'9.b':(1,[]),'9.0':(1,[]),'9.1':(2,[]),'9.2':(1,[]),'9.3':(1,[]),'9.4':(1,[]),'9.5':(1,[]),'9.6':(1,[]),
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
