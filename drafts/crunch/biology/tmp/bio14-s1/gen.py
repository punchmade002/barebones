import json,re
P='bio14-s1.'
# id: (cost, [(need, strength, why, conf)])
S={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),'0.2':(1,[]),
'0.3':(1,[('0.0','helpful','oxygen as by-product','high')]),
'0.4':(1,[('0.0','helpful','reactants, products, light, chlorophyll','high')]),
'0.5':(2,[('0.4','essential','word equation being balanced','high')]),
'1.b':(1,[]),'1.0':(1,[]),
'1.1':(1,[('1.0','essential','anabolic definition, part one','high')]),
'1.2':(1,[('1.0','essential','anabolic definition, energy part','high')]),
'1.3':(1,[('bio8-s1.2.3','helpful','catabolism definition','high')]),
'2.b':(1,[]),
'2.0':(1,[('0.0','helpful','CO2 as photosynthesis reactant','high'),('5.0','helpful','mesophyll cells as site','low')]),
'2.1':(1,[]),'2.2':(2,[]),'2.3':(1,[]),
'2.4':(1,[('0.0','helpful','chlorophyll absorbs light','high')]),
'2.5':(1,[('0.0','helpful','oxygen by-product','high')]),
'2.6':(2,[('5.3','helpful','photolysis splits water','high')]),
'2.7':(1,[('3.b','helpful','glucose converted to other carbohydrates','high')]),
'3.b':(1,[]),
'3.0':(2,[('bio8-s2.2.4','helpful','sucrose as glucose plus fructose','high')]),
'3.1':(2,[('3.0','essential','sucrose and phloem transport','high')]),
'3.2':(1,[('bio8-s2.3.1','helpful','starch structure and storage','high')]),
'3.3':(2,[('3.2','essential','starch as storage carbohydrate','high')]),
'3.4':(1,[('bio8-s2.3.4','helpful','cellulose structure','high')]),
'3.5':(1,[('bio8-s1.3.2','helpful','nitrate used for amino acids','high')]),
'4.b':(1,[]),'4.0':(1,[]),
'4.1':(1,[('4.0','helpful','carbon sink idea','low')]),
'4.2':(1,[('4.1','helpful','carbon fixed in biomass','high')]),
'4.3':(1,[('4.1','helpful','carbon fixation','high')]),
'4.4':(1,[('4.0','helpful','release of stored carbon','high')]),
'4.5':(2,[('4.0','essential','carbon sink definition','high')]),
'4.6':(1,[('4.1','helpful','carbon fixed by photosynthesis','high')]),
'5.b':(1,[]),'5.0':(1,[]),'5.1':(1,[]),
'5.2':(1,[('5.1','helpful','stage 1 steps','high')]),
'5.3':(2,[('5.2','helpful','light energy absorbed first','high')]),
'5.4':(1,[('5.3','essential','oxygen from photolysis','high')]),
'5.5':(2,[('bio8-s1.2.5','essential','ATP as energy carrier','high')]),
'5.6':(1,[]),
'5.7':(2,[('5.5','essential','ATP and hydrogen from stage 1','high')]),
'6.b':(1,[]),
'6.0':(1,[('5.5','essential','ATP and hydrogen carrier','high')]),
'6.1':(2,[('6.0','essential','ATP and carrier supplied by stage 1','high')]),
'6.2':(1,[('bio13-s1.0.2','helpful','enzymes as biological catalysts','high')]),
'6.3':(2,[('6.0','essential','stage 2 depends on ATP and hydrogen','high')]),
'6.4':(1,[('5.6','helpful','light-independent stage','high')]),
'6.5':(2,[('5.7','helpful','stage 2 inputs and outputs','low')]),
}
pk=open('/Users/gabrielwhelan/barebones/drafts/crunch/biology/points/bio14-s1.txt').read()
tg=pk.split('CANDIDATES')[0]
tids=re.findall(r'^\[(bio14-s1\.[^\]]+)\]',tg,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',pk,re.M))
out={}
for t in tids:
    k=t[len(P):]
    c,n=S[k]
    out[t]={"cost":c,"needs":[{"id":(x if x.startswith('bio') else P+x),"strength":s,"why":w,"confidence":f} for x,s,w,f in n]}
json.dump(out,open('/Users/gabrielwhelan/barebones/drafts/crunch/biology/point-links/bio14-s1.json','w'),indent=1,ensure_ascii=False)
d=json.load(open('/Users/gabrielwhelan/barebones/drafts/crunch/biology/point-links/bio14-s1.json'))
assert list(d)==tids and len(set(tids))==len(tids)
l=[x for v in d.values() for x in v['needs']]
assert all(x['id'] in allids for x in l)
assert all(x['id']!=k for k,v in d.items() for x in v['needs'])
print(len(d),len(l),sum(v['cost']==2 for v in d.values()),sum(x['confidence']=='low' for x in l))
