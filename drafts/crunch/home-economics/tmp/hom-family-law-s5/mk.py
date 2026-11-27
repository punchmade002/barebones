import json,re
B='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
P='hom-family-law-s5.'
def L(i,s,w,c='high'): return {"id":P+i,"strength":s,"why":w,"confidence":c}
D={
'0.b':(1,[]),'0.0':(1,[]),
'0.1':(1,[L('0.0','helpful','Tusla duty to children')]),
'0.2':(2,[]),
'0.3':(1,[L('0.2','helpful','child at risk definition')]),
'0.4':(1,[]),'0.5':(1,[]),'0.6':(1,[]),'0.7':(1,[]),
'1.b':(1,[]),
'1.0':(1,[L('0.0','helpful','Tusla takes child into care')]),
'1.1':(1,[L('0.3','helpful','immediate risk to child','low')]),
'1.2':(1,[L('1.1','essential','emergency care order')]),
'1.3':(1,[]),
'1.4':(1,[L('1.1','helpful','emergency care order'),L('1.3','helpful','interim care order')]),
'2.b':(1,[]),
'2.0':(1,[L('0.0','helpful','Tusla applies on child welfare')]),
'2.1':(1,[L('2.0','essential','care order')]),
'2.2':(1,[L('2.0','essential','care order')]),
'2.3':(1,[L('2.0','essential','care order')]),
'3.b':(1,[]),
'3.0':(1,[L('0.4','helpful','Tusla applies to court')]),
'3.1':(1,[L('3.0','essential','supervision order')]),
'3.2':(1,[L('3.0','essential','supervision order')]),
'3.3':(1,[L('3.0','helpful','supervision order')]),
'3.4':(1,[L('3.0','helpful','supervision order')]),
}
txt=open(B+'packs/hom-family-law-s5.t1g1.txt').read()
ids=re.findall(r'^\[(hom-family-law-s5\.[^\]]+)\]',txt,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
out={}
for i in ids:
    c,n=D[i[len(P):]]; out[i]={"cost":c,"needs":n}
assert len(D)==len(ids)==len(out)
for k,v in out.items():
    for n in v['needs']: assert n['id'] in allids and n['id']!=k,n
json.dump(out,open(B+'point-links/hom-family-law-s5.t1g1.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
