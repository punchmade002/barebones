import json,re
P='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
E,H='essential','helpful'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
D='hom-dairy-eggs-s1.'
def dl(k,s,w,c='high'): return L(D+k,s,w,c)
d={
'0.b':(1,[]),'0.0':(1,[]),
'0.1':(2,[L('hom-proteins-s4.2.0',H,'casein is the main milk protein')]),
'0.2':(1,[]),'0.3':(2,[]),
'0.4':(1,[L('hom-vitamins-minerals-s1.1.b',H,'fat-soluble vitamins travel with fat')]),
'0.5':(2,[]),
'0.6':(2,[L('hom-vitamins-minerals-s4.1.2',H,'calcium and phosphorus harden bones')]),
'0.7':(2,[dl('0.4',H,'vitamins A and D carried in fat')]),
'0.8':(1,[dl('0.5',H,'lactose supplies energy','low')]),
'1.b':(1,[]),'1.0':(1,[]),'1.1':(1,[]),
'1.2':(1,[dl('0.5',E,'lactose is the milk carbohydrate')]),
'1.3':(1,[dl('0.6',H,'milk is low in iron')]),
'2.b':(1,[]),
'2.0':(1,[dl('0.1',H,'HBV protein for growth and repair','low')]),
'2.1':(2,[]),'2.2':(1,[]),
'3.b':(1,[]),
'3.0':(1,[dl('0.2',H,'protein for growth and repair')]),
'3.1':(1,[dl('0.6',H,'calcium and phosphorus for bones')]),
'3.2':(1,[]),'3.3':(1,[]),
'3.4':(1,[dl('0.3',H,'saturated fat content of milk')]),
'3.5':(1,[]),'3.6':(1,[]),
'3.7':(1,[dl('8.4',H,'fortified milk')]),
'4.b':(1,[]),'4.0':(1,[]),
'4.1':(1,[dl('0.3',H,'milk fat is mostly saturated')]),
'4.2':(1,[dl('0.5',E,'lactose is the milk sugar')]),
'4.3':(1,[dl('0.1',H,'milk protein')]),
'5.b':(1,[]),
'5.0':(1,[L('hom-energy-nutrition-s4.6.0',H,'Food Pyramid shelves')]),
'5.1':(1,[L('hom-energy-nutrition-s4.6.3',H,'pyramid serving numbers','low')]),
'5.2':(1,[]),'5.3':(2,[]),
'6.b':(1,[]),'6.0':(1,[]),'6.1':(1,[]),'6.2':(1,[]),'6.3':(1,[]),
'7.b':(1,[]),
'7.0':(2,[]),
'7.1':(1,[dl('0.4',H,'fat-soluble vitamins A and D')]),
'7.2':(1,[dl('7.1',E,'whole milk supplies energy and A and D')]),
'7.3':(1,[]),'7.4':(1,[]),
'7.5':(2,[dl('1.3',H,'milk is low in iron')]),
'7.6':(1,[dl('8.4',H,'fortified milk')]),
'8.b':(1,[]),'8.0':(1,[]),'8.1':(1,[]),'8.2':(1,[]),
'8.3':(2,[]),
'8.4':(2,[L('hom-vitamins-minerals-s1.9.4',H,'fortified foods have nutrients added','low')]),
'8.5':(1,[dl('8.4',H,'fortified milk')]),
'8.6':(2,[]),
'9.b':(1,[]),'9.0':(1,[]),'9.1':(1,[]),'9.2':(1,[]),
'9.3':(2,[]),
'9.4':(2,[dl('8.3',H,'skimmed milk nutrient profile')]),
'9.5':(2,[]),
}
out={D+k:{"cost":c,"needs":n} for k,(c,n) in d.items()}
f=P+'packs/hom-dairy-eggs-s1.t1g1.txt'
t=open(f).read()
ids=set(re.findall(r'^\[([^\]]+)\]',t,re.M))
tgt=re.findall(r'^\[([^\]]+)\]',t.split('CANDIDATES')[0],re.M)
assert sorted(tgt)==sorted(out),set(tgt)^set(out)
for k,v in out.items():
  for n in v['needs']: assert n['id'] in ids and n['id']!=k,(k,n)
out={k:out[k] for k in tgt}
json.dump(out,open(P+'point-links/hom-dairy-eggs-s1.t1g1.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
