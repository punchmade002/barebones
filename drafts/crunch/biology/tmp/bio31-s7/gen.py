import json,re
P='bio31-s7.'
E,H='essential','helpful'
# id: (cost, [(target, strength, why, conf)])
d={
'0.b':(1,[]),
'0.0':(1,[('bio14-s1.0.1',H,'autotroph, photosynthesis','high')]),
'0.1':(1,[('0.0',E,'producers defined','high')]),
'0.2':(1,[('0.0',H,'producers eaten by herbivores','high')]),
'0.3':(1,[('0.2',E,'primary consumers','high')]),
'0.4':(1,[('0.3',H,'consumer levels in a chain','high')]),
'0.5':(1,[('0.0',H,'producers reuse released minerals','low')]),
'0.6':(1,[('0.5',E,'decomposers act on dead matter','high')]),
'1.b':(1,[]),
'1.0':(1,[('1.1',H,'food chain sequence','low')]),
'1.1':(1,[('1.0',H,'trophic level','high')]),
'1.2':(1,[('1.1',E,'food chain','high')]),
'1.3':(2,[('1.2',H,'arrow direction','high')]),
'1.4':(2,[('1.2',H,'arrow direction','high')]),
'1.5':(1,[('1.1',E,'food chain','high'),('0.5',H,'decomposers','high')]),
'1.6':(1,[('3.1',E,'energy lost at each transfer','high'),('1.0',H,'trophic levels','high')]),
'2.b':(1,[]),
'2.0':(1,[('1.1',E,'food chain','high')]),
'2.1':(1,[('1.0',E,'trophic level','high')]),
'2.2':(2,[('2.0',H,'food web','high')]),
'2.3':(1,[('0.5',E,'decomposers','high')]),
'2.4':(2,[('2.0',E,'food web','high')]),
'2.5':(2,[('2.2',E,'the food web drawn','high')]),
'3.b':(1,[]),
'3.0':(1,[('bio14-s1.0.2',H,'light to chemical energy','high')]),
'3.1':(1,[('1.0',E,'trophic level','high')]),
'3.2':(1,[('bio15-s1.0.3',H,'respiration energy lost as heat','high')]),
'3.3':(1,[('0.5',H,'decomposers get uneaten matter','high')]),
'3.4':(1,[('3.2',H,'heat loss','high')]),
'3.5':(2,[('3.1',E,'10% transfer figure','high')]),
'3.6':(1,[('3.1',E,'energy lost per level','high')]),
'3.7':(2,[('3.1',E,'energy lost per level','high')]),
'4.b':(1,[]),
'4.0':(1,[('1.1',H,'food chain transfer','low')]),
'4.1':(2,[]),
'4.2':(2,[('bio15-s1.0.5',H,'carbon released as CO2','low')]),
'4.3':(1,[('0.5',E,'decomposers release minerals','high')]),
'4.4':(1,[('3.4',E,'one-way energy flow','high'),('4.3',E,'nutrient cycling','high')]),
'4.5':(2,[('0.4',H,'top consumers','high')]),
'4.6':(1,[('4.5',E,'biomagnification','high')]),
'4.7':(2,[('3.4',H,'energy flow','high'),('4.3',H,'nutrient loop','high')]),
'5.b':(1,[]),
'5.0':(1,[('2.0',H,'food web as model','high')]),
'5.1':(1,[('5.0',E,'five-step method','high')]),
'5.2':(1,[('2.4',H,'competition for food','high')]),
'5.3':(1,[('5.0',E,'five-step method','high')]),
'5.4':(1,[('5.0',E,'five-step method','high')]),
'5.5':(2,[('2.2',E,'the food web above','high'),('5.0',H,'prediction steps','high')]),
'5.6':(2,[('5.5',E,'continues the worked prediction','high')]),
'5.7':(1,[('5.6',H,'predator diet switching','low')]),
'6.b':(1,[]),
'6.0':(2,[('2.4',H,'interdependence in webs','high')]),
'6.1':(2,[('0.0',E,'phytoplankton as producers','high')]),
'6.2':(1,[('2.0',H,'food web','high')]),
'6.3':(1,[('2.0',H,'food web','low')]),
}
out={}
for k,(c,n) in d.items():
    out[P+k]={"cost":c,"needs":[{"id":(t if t.startswith('bio') else P+t),"strength":s,"why":w,"confidence":f} for t,s,w,f in n]}
txt=open('points/bio31-s7.txt').read()
tids=re.findall(r'^\[(bio31-s7\.[^\]]+)\]',txt.split('CANDIDATES')[0],re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
assert list(out)==tids,(set(tids)^set(out))
for k,v in out.items():
    for n in v['needs']: assert n['id'] in allids and n['id']!=k,(k,n)
json.dump(out,open('point-links/bio31-s7.json','w'),indent=1)
l=[n for v in out.values() for n in v['needs']]
print(len(out),len(l),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for n in l))
