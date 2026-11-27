import json,re,sys
D='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
P='hom-lipids-s6'
def N(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
H,E='helpful','essential'
S=P+'.'
spec=[
('0.b',1,[]),
('0.0',1,[]),
('0.1',1,[]),
('0.2',2,[N('hom-lipids-s5.1.0',H,'fat-soluble vitamins'),N('hom-lipids-s1.3.0',H,'essential fatty acids')]),
('0.3',1,[N(S+'0.2',H,'fat-soluble vitamins A and D')]),
('0.4',1,[]),
('0.5',1,[]),
('0.6',2,[N('hom-lipids-s3.3.0',H,'saturated animal fats'),N('hom-lipids-s1.5.3',H,'saturated fat raises LDL')]),
('0.7',1,[N('hom-lipids-s3.0.7',H,'visible and hidden fat')]),
('0.8',1,[N('hom-lipids-s5.3.6',H,'Food Pyramid fats shelf')]),
('1.b',1,[]),
('1.0',2,[]),
('1.1',2,[N('hom-lipids-s4.2.6',H,'water-in-oil emulsion')]),
('1.2',2,[N('hom-lipids-s4.0.2',H,'smoke point')]),
('1.3',1,[]),
('1.4',1,[]),
('1.5',2,[]),
('2.b',1,[]),
('2.0',2,[N(S+'7.1',H,'what a label shows')]),
('2.1',1,[N('hom-food-additives-s2.5.1',H,'ingredients in descending order')]),
('2.2',2,[N('hom-lipids-s1.5.4',H,'unsaturated fat lowers LDL'),N(S+'8.3',H,'functional spreads lower cholesterol')]),
('2.3',1,[N('hom-lipids-s1.2.4',H,'trans fat from hydrogenation')]),
('2.4',1,[N('hom-lipids-s4.0.5',H,'smoke point suits frying')]),
('2.5',1,[N('hom-lipids-s4.5.0',H,'plasticity of fat')]),
('2.6',2,[]),
('3.b',1,[]),
('3.0',1,[N('hom-lipids-s4.7.0',H,'oxidative rancidity')]),
('3.1',2,[N(S+'3.0',H,'rancidity causes')]),
('3.2',1,[]),
('3.3',1,[N(S+'3.0',H,'rancidity')]),
('3.4',1,[]),
('3.5',2,[N('hom-lipids-s4.0.4',H,'impurities lower smoke point')]),
('3.6',1,[]),
('4.b',1,[]),
('4.0',2,[]),
('4.1',1,[]),
('4.2',1,[]),
('4.3',1,[]),
('4.4',2,[N('hom-lipids-s4.5.3',H,'plastic fats rubbed into flour','low')]),
('4.5',2,[N('hom-lipids-s4.2.3',H,'emulsions such as mayonnaise','low')]),
('4.6',1,[N('hom-lipids-s3.0.6',H,'dripping from roast meat')]),
('5.b',1,[]),
('5.0',2,[N('hom-lipids-s4.0.2',H,'smoke point'),N('hom-lipids-s4.0.3',H,'acrolein from decomposition')]),
('5.1',1,[N('hom-lipids-s4.0.6',E,'flash point')]),
('5.2',2,[N('hom-lipids-s4.6.0',H,'hydrogenation'),N('hom-lipids-s1.2.4',H,'trans fatty acids')]),
('6.b',1,[]),
('6.0',1,[]),
('6.1',2,[N('hom-lipids-s4.6.0',H,'hydrogenation with nickel catalyst')]),
('6.2',1,[N('hom-lipids-s4.5.0',H,'plasticity')]),
('6.3',2,[N('hom-lipids-s4.4.0',H,'emulsifier action')]),
('6.4',1,[N('hom-lipids-s4.2.6',H,'water-in-oil emulsion')]),
('6.5',1,[N('hom-lipids-s4.5.0',H,'plastic fat')]),
('6.6',1,[]),
('7.b',1,[]),
('7.0',1,[N('hom-food-additives-s2.5.1',H,'ingredients in descending order')]),
('7.1',2,[N('hom-food-additives-s2.6.0',H,'nutrition declaration items')]),
('7.2',1,[N('hom-food-additives-s2.5.0',H,'Irish labelling regulations')]),
('8.b',1,[]),
('8.0',1,[]),
('8.1',1,[]),
('8.2',1,[]),
('8.3',2,[N('hom-lipids-s1.5.1',H,'LDL cholesterol')]),
('8.4',1,[N(S+'8.3',H,'stanol or sterol ester','low')]),
('8.5',1,[N('hom-lipids-s1.5.1',H,'LDL cholesterol')]),
('9.b',1,[]),
('9.0',1,[]),
('9.1',2,[N(S+'7.1',H,'nutrition figures per 100 g')]),
('9.2',1,[N('hom-lipids-s5.3.1',H,'saturated fat and CHD')]),
('9.3',1,[N('hom-lipids-s1.5.4',H,'unsaturated fat protects heart')]),
('9.4',1,[N(S+'8.2',H,'low-fat spreads unsuitable for frying')]),
('9.5',1,[N(S+'0.5',H,'lower fat means more water')]),
('9.6',2,[N(S+'9.2',H,'weight control judgement'),N(S+'9.3',H,'heart protection judgement')]),
]
txt=open(D+'packs/'+P+'.t1g1.txt').read()
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
tgt=[m for m in re.findall(r'^\[([^\]]+)\]',txt.split('CANDIDATES')[0],re.M)]
out={}
for k,c,n in spec:
    out[S+k]={"cost":c,"needs":n}
assert list(out)==tgt,(set(tgt)^set(out))
for k,v in out.items():
    for n in v['needs']: assert n['id'] in allids and n['id']!=k,(k,n)
json.dump(out,open(D+'point-links/'+P+'.t1g1.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
