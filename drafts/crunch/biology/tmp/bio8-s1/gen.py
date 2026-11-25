import json,re
P='bio8-s1.'
def n(i,s,w,c='high'):return {"id":P+i,"strength":s,"why":w,"confidence":c}
E,H='essential','helpful'
d={
'0.b':(1,[]),'0.0':(1,[]),
'0.1':(1,[n('0.0',H,'four biomolecule groups')]),
'0.2':(1,[n('0.0',H,'biomolecule groups')]),
'0.3':(2,[]),'0.4':(1,[]),
'1.b':(1,[]),'1.0':(1,[]),
'1.1':(2,[n('1.0',E,'monomer and polymer definitions')]),
'1.2':(2,[n('1.0',E,'polymer as repeating monomer chain')]),
'1.3':(2,[n('1.1',H,'glucose and amino acid monomers')]),
'1.4':(1,[n('1.3',E,'condensation as the opposite')]),
'1.5':(2,[n('1.4',E,'hydrolysis splitting molecules')]),
'1.6':(2,[n('1.1',H,'polymers built from monomers','low')]),
'1.7':(2,[n('1.3',E,'condensation reaction'),n('1.4',E,'hydrolysis reaction')]),
'2.b':(1,[]),'2.0':(1,[]),
'2.1':(1,[n('2.0',H,'metabolism as all reactions')]),
'2.2':(2,[n('2.1',E,'anabolism definition')]),
'2.3':(1,[n('2.0',H,'metabolism as all reactions')]),
'2.4':(2,[n('2.3',E,'catabolism definition')]),
'2.5':(2,[n('2.3',E,'catabolic reactions release energy'),n('2.1',E,'anabolic reactions need energy')]),
'2.6':(1,[n('2.5',E,'energy transfer between reactions')]),
'3.b':(1,[]),'3.0':(1,[]),
'3.1':(2,[n('3.0',H,'converting biomolecules')]),
'3.2':(2,[n('3.0',H,'converting biomolecules')]),
'3.3':(1,[n('3.0',H,'converting biomolecules')]),
'4.b':(1,[]),
'4.0':(1,[n('2.1',E,'anabolism definition'),n('2.3',E,'catabolism definition')]),
'4.1':(1,[n('2.1',E,'anabolism needs energy'),n('2.3',E,'catabolism releases energy')]),
'4.2':(1,[n('2.2',H,'anabolic examples'),n('2.4',H,'catabolic examples')]),
}
out={P+k:{"cost":c,"needs":nd} for k,(c,nd) in d.items()}
json.dump(out,open('point-links/bio8-s1.json','w'),indent=1)
t=open('points/bio8-s1.txt').read()
ids=re.findall(r'^\[([^\]]+)\]',t,re.M)
o=json.load(open('point-links/bio8-s1.json'))
assert list(o)==ids,(set(ids)^set(o))
assert all(x['id'] in ids and x['id']!=k for k,v in o.items() for x in v['needs'])
L=[x for v in o.values() for x in v['needs']]
print(len(o),len(L),sum(v['cost']==2 for v in o.values()),sum(x['confidence']=='low' for x in L))
