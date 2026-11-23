import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/biology/'
H,L='high','low'
E,HP='essential','helpful'
def n(i,s,w,c=H): return {"id":i,"strength":s,"why":w,"confidence":c}
d={
"bio31-s9.0.b":(1,[n("bio31-s7.1.0",HP,"trophic level")]),
"bio31-s9.0.0":(1,[]),
"bio31-s9.0.1":(1,[n("bio31-s9.0.0",E,"biomass definition"),n("bio31-s7.1.0",HP,"trophic levels")]),
"bio31-s9.0.2":(1,[n("bio31-s9.0.1",HP,"pyramid of biomass layout")]),
"bio31-s9.0.3":(1,[n("bio31-s9.0.0",HP,"dry mass as biomass")]),
"bio31-s9.0.4":(2,[n("bio31-s7.4.2",E,"matter lost by respiration, egestion, excretion")]),
"bio31-s9.1.b":(1,[n("bio31-s9.0.0",HP,"biomass as dry mass")]),
"bio31-s9.1.0":(1,[]),
"bio31-s9.1.1":(1,[]),
"bio31-s9.1.2":(1,[n("bio31-s9.1.1",HP,"oven drying step")]),
"bio31-s9.1.3":(1,[n("bio31-s9.1.0",HP,"sampled area")]),
"bio31-s9.1.4":(1,[n("bio31-s9.1.1",HP,"drying kills organisms",L)]),
"bio31-s9.2.b":(1,[n("bio31-s8.0.0",HP,"pyramid of numbers")]),
"bio31-s9.2.0":(1,[n("bio31-s8.2.1",HP,"narrow-base numbers pyramid")]),
"bio31-s9.2.1":(1,[n("bio31-s9.0.1",HP,"pyramid of biomass")]),
"bio31-s9.2.2":(1,[n("bio31-s9.2.1",HP,"biomass pyramid for oak chain")]),
"bio31-s9.3.b":(1,[]),
"bio31-s9.3.0":(2,[n("bio31-s7.0.0",HP,"phytoplankton as producers")]),
"bio31-s9.3.1":(2,[n("bio31-s9.3.0",E,"inverted pyramid situation")]),
"bio31-s9.3.2":(2,[n("bio31-s9.3.1",E,"standing crop")]),
"bio31-s9.3.3":(1,[n("bio31-s9.3.0",E,"inverted biomass pyramid")]),
"bio31-s9.4.b":(1,[]),
"bio31-s9.4.0":(2,[n("bio31-s9.0.2",HP,"bar layout with producers at base")]),
"bio31-s9.4.1":(1,[n("bio31-s7.0.5",HP,"decomposers")]),
"bio31-s9.4.2":(1,[n("bio31-s9.0.1",HP,"biomass pyramid measure")]),
"bio31-s9.4.3":(1,[n("bio31-s8.3.0",E,"numbers ignore organism size")]),
"bio31-s9.4.4":(2,[n("bio31-s8.2.1",E,"inverted numbers pyramids"),n("bio31-s9.3.0",E,"inverted aquatic biomass pyramid")]),
"bio31-s9.5.b":(1,[]),
"bio31-s9.5.0":(1,[n("bio31-s9.1.4",HP,"drying is destructive")]),
"bio31-s9.5.1":(1,[n("bio31-s8.3.1",HP,"numbers too varied to scale")]),
"bio31-s9.5.2":(1,[n("bio31-s9.3.2",HP,"standing crop not production rate")]),
"bio31-s9.5.3":(1,[]),
"bio31-s9.5.4":(2,[n("bio31-s9.5.0",HP,"data collection difficulty")]),
"bio31-s9.5.5":(1,[n("bio31-s7.3.1",HP,"energy transfer between levels",L)]),
"bio31-s9.6.b":(1,[]),
"bio31-s9.6.0":(1,[]),
"bio31-s9.6.1":(1,[n("bio31-s9.6.0",E,"sample numbers"),n("bio31-s8.2.3",HP,"spindle-shaped pyramid",L)]),
"bio31-s9.6.2":(1,[n("bio31-s9.6.0",E,"sample biomass values")]),
"bio31-s9.6.3":(1,[n("bio31-s9.6.2",HP,"biomass pyramid result")]),
}
out={k:{"cost":c,"needs":nd} for k,(c,nd) in d.items()}
pkg=open(P+'points/bio31-s9.txt').read()
ids=set(re.findall(r'^\[([^\]]+)\]',pkg,re.M))
tg=re.findall(r'^\[(bio31-s9\.[^\]]+)\]',pkg,re.M)
assert list(out)==tg,(set(tg)^set(out))
for k,v in out.items():
    for x in v['needs']: assert x['id'] in ids and x['id']!=k,x
json.dump(out,open(P+'point-links/bio31-s9.json','w'),indent=1)
json.load(open(P+'point-links/bio31-s9.json'))
nn=[x for v in out.values() for x in v['needs']]
print(len(out),len(nn),sum(v['cost']==2 for v in out.values()),sum(x['confidence']=='low' for x in nn))
