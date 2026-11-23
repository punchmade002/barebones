import json,re
D='/Users/gabrielwhelan/barebones/drafts/crunch/biology'
def n(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
H,E='helpful','essential'
P='bio34-s1.'
R={
'0.b':(1,[]),'0.0':(1,[]),
'0.1':(1,[n('bio31-s7.3.4',H,'energy flows one way')]),
'0.2':(1,[]),'0.3':(2,[]),
'0.4':(1,[n(P+'0.3',H,'stores of carbon')]),
'0.5':(1,[n('bio14-s1.0.0',H,'photosynthesis uses CO2')]),
'1.b':(1,[]),
'1.0':(1,[n('bio14-s1.0.0',E,'photosynthesis makes glucose from CO2')]),
'1.1':(1,[n(P+'1.0',H,'photosynthesis fixes carbon')]),
'1.2':(1,[n('bio14-s1.2.1',H,'aquatic plants use dissolved CO2')]),
'1.3':(2,[n(P+'1.2',H,'dissolved CO2 in water','low')]),
'1.4':(1,[n(P+'1.3',E,'calcium carbonate shells')]),
'2.b':(1,[]),
'2.0':(2,[n('bio15-s1.0.5',H,'respiration releases carbon as CO2'),n('bio31-s7.0.2',H,'herbivores and carnivores as consumers')]),
'2.1':(1,[n('bio31-s7.1.0',E,'trophic levels')]),
'2.2':(1,[n(P+'0.3',H,'dead organic matter as a store'),n('bio31-s7.0.5',H,'decomposers feed on dead matter')]),
'3.b':(1,[]),
'3.0':(1,[n('bio15-s1.1.0',E,'respiration breaks glucose to CO2')]),
'3.1':(2,[n(P+'3.0',E,'respiration releases CO2'),n(P+'1.0',H,'photosynthesis takes in carbon')]),
'3.2':(1,[]),'3.3':(1,[]),
'4.b':(1,[]),
'4.0':(2,[n('bio31-s7.0.5',H,'saprophytic nutrition by decomposers')]),
'4.1':(1,[n(P+'4.0',E,'decomposers digest then respire')]),
'4.2':(1,[n(P+'4.0',E,'decomposers return CO2')]),
'4.3':(1,[n('bio15-s1.1.0',H,'aerobic respiration needs oxygen')]),
'4.4':(1,[n(P+'4.3',E,'conditions for fast decomposition')]),
'4.5':(2,[n('bio15-s1.2.0',H,'anaerobic respiration without oxygen')]),
'4.6':(1,[n(P+'4.5',E,'methane-producing microorganisms')]),
'5.b':(1,[]),'5.0':(1,[]),
'5.1':(1,[n(P+'5.0',E,'what fossil fuels are')]),
'5.2':(1,[n('bio14-s1.0.2',H,'light energy stored as chemical energy')]),
'5.3':(1,[n(P+'5.0',H,'fossil fuel store')]),
'5.4':(2,[n(P+'5.0',E,'fossil fuels as carbon store'),n(P+'1.0',H,'photosynthesis removes CO2')]),
'6.b':(1,[]),
'6.0':(1,[n('bio14-s1.4.0',H,'carbon sink definition')]),
'6.1':(1,[n(P+'6.0',E,'sink versus source')]),
'6.2':(2,[n(P+'6.0',H,'sinks and stores')]),
'6.3':(1,[]),
'6.4':(2,[n(P+'6.0',H,'inputs balancing outputs')]),
'6.5':(1,[n(P+'6.4',E,'balanced CO2 uptake and release')]),
'6.6':(2,[n(P+'3.1',H,'photosynthesis versus respiration balance')]),
'7.b':(1,[]),
'7.0':(1,[n(P+'0.3',E,'stores as boxes')]),
'7.1':(2,[n(P+'7.0',E,'labelled boxes for the arrows')]),
'7.2':(1,[n(P+'7.1',E,'continues the arrow list')]),
'7.3':(1,[n(P+'3.2',H,'combustion releases CO2')]),
'7.4':(1,[n(P+'4.3',H,'aerobic decomposers need air')]),
'7.5':(1,[n(P+'4.2',E,'decomposers return minerals and CO2')]),
'7.6':(1,[n(P+'7.1',H,'diagram of the cycle')]),
'7.7':(1,[n(P+'4.3',H,'warmth speeds decomposition')]),
}
out={P+k:{"cost":c,"needs":v} for k,(c,v) in R.items()}
t=open(D+'/points/bio34-s1.txt').read()
ids=re.findall(r'^\[([^\]]+)\]',t,re.M)
tg=[i for i in ids if i.startswith(P)]
assert list(out)==tg,(set(tg)^set(out))
for v in out.values():
  for x in v['needs']: assert x['id'] in ids
json.dump(out,open(D+'/point-links/bio34-s1.json','w'),indent=0)
json.load(open(D+'/point-links/bio34-s1.json'))
l=sum(len(v['needs']) for v in out.values())
print(len(out),l,sum(v['cost']==2 for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
