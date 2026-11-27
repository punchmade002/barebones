import json,re
S='hom-dairy-eggs-s5.'
def n(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
H='helpful';E='essential'
d={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),'0.2':(1,[]),'0.3':(1,[]),'0.4':(1,[]),
'0.5':(1,[n(S+'0.4',E,'air cell size')]),'0.6':(1,[]),
'1.b':(1,[]),
'1.0':(2,[n('hom-proteins-s4.1.0',H,'albumin is egg white protein')]),
'1.1':(1,[]),'1.2':(1,[]),'1.3':(2,[]),'1.4':(1,[]),
'1.5':(1,[n(S+'1.3',H,'sits on the yolk')]),
'1.6':(2,[n(S+'0.6',H,'extends the shell diagram','low')]),
'2.b':(1,[]),
'2.0':(2,[n('hom-proteins-s7.0.0',E,'high biological value protein')]),
'2.1':(1,[n('hom-proteins-s4.1.0',H,'albumin','high')]),
'2.2':(2,[]),'2.3':(1,[]),'2.4':(1,[]),'2.5':(2,[]),'2.6':(2,[]),'2.7':(2,[]),
'3.b':(1,[]),
'3.0':(1,[n('hom-proteins-s4.0.0',H,'eggs as animal protein','low')]),
'3.1':(1,[n('hom-proteins-s7.0.0',H,'HBV protein')]),
'3.2':(1,[n(S+'2.2',H,'fat emulsified by lecithin')]),
'3.3':(1,[n(S+'2.0',H,'protein for growth and repair')]),
'3.4':(1,[]),
'3.5':(1,[n(S+'2.2',H,'saturated fat and cholesterol')]),
'3.6':(1,[n(S+'2.4',H,'no fibre or carbohydrate')]),
'3.7':(1,[]),
}
out={S+k:{"cost":c,"needs":v} for k,(c,v) in d.items()}
f='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
txt=open(f+'packs/hom-dairy-eggs-s5.t1g1.txt').read()
ids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
tg=re.findall(r'^\[([^\]]+)\]',txt.split('CANDIDATES')[0],re.M)
assert list(out)==tg,(set(tg)^set(out))
for v in out.values():
  for x in v['needs']: assert x['id'] in ids and x['id'] not in out or x['id'] in ids
json.dump(out,open(f+'point-links/hom-dairy-eggs-s5.t1g1.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
