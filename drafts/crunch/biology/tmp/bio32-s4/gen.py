import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/biology/'
txt=open(P+'points/bio32-s4.txt').read()
ids=re.findall(r'^\[([^\]]+)\]',txt,re.M)
tgt=[i for i in ids if i.startswith('bio32-s4.')]
c2={'3.1','3.2','4.0','4.3','5.1','6.2','6.3','7.1','8.6','9.1','10.0','11.1','11.2','12.2','13.1','14.0','15.0','15.2','15.3','16.3','17.1','17.3','17.5'}
H,L='high','low'
S='bio32-s4.'
# (key: [(id,strength,why,conf)])
n={
'0.1':[(S+'0.0','helpful','grazing keeps rosettes lit',H)],
'1.1':[(S+'1.0','essential','decomposition by decomposers',H)],
'3.1':[(S+'3.0','helpful','producers are what herbivores eat',H)],
'3.2':[(S+'3.1','helpful','herbivores are the prey',H)],
'4.b':[('bio31-s7.1.1','helpful','food chain definition',H)],
'4.0':[('bio31-s7.1.2','helpful','arrows point from food to feeder',H)],
'4.1':[('bio31-s7.2.0','helpful','food web joins chains',H)],
'4.2':[(S+'1.0','helpful','detritivores eat dead matter',H)],
'4.3':[(S+'4.0','essential','species and chains to draw',H)],
'5.0':[('bio31-s7.2.4','helpful','interdependence in food webs',H)],
'5.1':[(S+'4.1','essential','fox on several chains',H)],
'5.2':[(S+'4.1','helpful','predator with several prey',L)],
'6.1':[(S+'6.0','essential','predator and prey defined',H)],
'6.2':[(S+'6.0','helpful','predator features',H)],
'6.3':[(S+'6.0','helpful','predator features',H)],
'7.0':[(S+'6.0','helpful','predator detection',H)],
'8.b':[(S+'6.0','helpful','predator and prey',H)],
'8.1':[(S+'8.0','helpful','step in cycle',H)],
'8.2':[(S+'8.1','helpful','step in cycle',H)],
'8.3':[(S+'8.2','helpful','step in cycle',H)],
'8.4':[(S+'8.3','helpful','cycle timing',H)],
'8.6':[(S+'8.4','essential','predator curve lower, later',H)],
'9.1':[('bio31-s5.0.3','helpful','carrying capacity',H)],
'9.2':[(S+'9.1','helpful','predators limit prey numbers',H)],
'10.1':[(S+'10.0','helpful','competition for scarce resource',H)],
'10.2':[(S+'10.0','essential','competition defined',H)],
'10.3':[(S+'10.0','essential','competition defined',H)],
'10.4':[(S+'10.0','helpful','competition defined',H)],
'10.5':[(S+'10.0','helpful','competition defined',H)],
'11.0':[(S+'10.0','essential','competition defined',H)],
'11.1':[('bio31-s10.1.0','helpful','competitive exclusion and niches',H),(S+'10.3','helpful','interspecific competition',H)],
'11.2':[(S+'10.0','helpful','competition for resources',H)],
'12.0':[(S+'10.3','essential','interspecific competition',H)],
'12.1':[(S+'10.3','helpful','interspecific competition',H)],
'12.2':[(S+'12.1','essential','grey vs red squirrel',H)],
'12.3':[(S+'12.1','helpful','grey squirrel decline',H)],
'13.1':[(S+'13.0','essential','symbiosis defined',H)],
'13.2':[(S+'13.1','essential','mutualism type',H)],
'14.0':[(S+'13.1','helpful','mutualism',H)],
'14.1':[(S+'14.0','essential','bacteria in nodules',H)],
'14.2':[(S+'14.0','helpful','root nodules',H)],
'14.3':[(S+'14.0','essential','nitrogen fixation by bacteria',H)],
'14.4':[(S+'14.0','helpful','nodules',H)],
'15.1':[(S+'15.0','essential','cellulose-digesting microorganisms',H)],
'15.2':[(S+'13.1','helpful','mutualism',H)],
'15.3':[(S+'13.1','helpful','mutualism',H)],
'16.0':[(S+'13.1','helpful','commensalism type',H)],
'16.1':[(S+'16.0','essential','commensalism defined',H)],
'16.2':[(S+'16.0','essential','commensalism defined',H)],
'16.3':[(S+'16.0','essential','commensalism defined',H)],
'17.0':[(S+'13.1','helpful','parasitism type',H)],
'17.1':[(S+'17.0','essential','parasitism defined',H)],
'17.2':[(S+'17.1','helpful','rabbit flea',H)],
'17.3':[(S+'17.0','essential','parasitism defined',H)],
'17.4':[(S+'17.0','helpful','parasitism defined',H)],
'17.5':[(S+'17.0','essential','parasitism defined',H)],
'17.6':[(S+'17.0','helpful','parasite takes food',H)],
'18.0':[(S+'17.0','essential','parasite weakens host',H)],
'18.1':[('bio31-s5.5.0','helpful','density-dependent factors',H)],
'19.b':[(S+'13.1','helpful','symbiosis types',H)],
'19.0':[(S+'6.0','essential','predation defined',H)],
'19.1':[(S+'10.0','essential','competition defined',H)],
'19.2':[(S+'13.1','essential','mutualism defined',H)],
'19.3':[(S+'16.0','essential','commensalism defined',H)],
'19.4':[(S+'17.0','essential','parasitism defined',H)],
'19.5':[(S+'6.0','essential','predation defined',H),(S+'17.0','essential','parasitism defined',H)],
}
out={}
for i in tgt:
    k=i[len(S):]
    out[i]={'cost':2 if k in c2 else 1,'needs':[{'id':a,'strength':b,'why':w,'confidence':c} for a,b,w,c in n.get(k,[])]}
allids=set(ids)
for k in n:assert S+k in out,k
for v in out.values():
    for x in v['needs']:assert x['id'] in allids,x
for i,v in out.items():
    assert all(x['id']!=i for x in v['needs'])
json.dump(out,open(P+'point-links/bio32-s4.json','w'),indent=1)
d=json.load(open(P+'point-links/bio32-s4.json'))
assert list(d)==tgt
print(len(d),sum(len(v['needs']) for v in d.values()),sum(v['cost']==2 for v in d.values()),sum(x['confidence']=='low' for v in d.values() for x in v['needs']))
