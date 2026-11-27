import json,re
H='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
P='hom-food-preservation-s5.t1g1'
def n(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
F='hom-food-preservation-s5.'
A='hom-food-preservation-s'
D='hom-food-additives-s'
d={
'0.b':(1,[n(A+'1.2.0','helpful','conditions micro-organisms need')]),
'0.0':(1,[n(A+'1.4.b','helpful','osmosis through membrane')]),
'0.1':(1,[n(A+'1.2.0','helpful','pH as growth condition')]),
'0.2':(2,[n(A+'1.3.4','helpful','enzymes as biological catalysts')]),
'0.3':(1,[]),
'0.4':(2,[n(D+'4.3.2','helpful','chemical preservatives such as sulphur dioxide','low')]),
'0.5':(1,[n(A+'1.5.7','helpful','combining preservation principles')]),
'0.6':(1,[]),
'1.b':(1,[n(A+'1.4.b','helpful','osmosis holds water from organisms')]),
'1.0':(1,[n(A+'1.4.b','helpful','osmosis through cell membrane')]),
'1.1':(1,[]),'1.2':(1,[]),
'1.3':(1,[n(A+'1.2.3','helpful','yeasts and moulds tolerate sugar')]),
'1.4':(1,[]),'1.5':(1,[]),
'2.b':(1,[]),
'2.0':(1,[n(A+'1.4.b','helpful','osmosis draws water out')]),
'2.1':(1,[]),'2.2':(1,[]),
'2.3':(2,[n(F+'6.4','helpful','nitrite use and botulinum','low')]),
'2.4':(1,[]),'2.5':(1,[]),'2.6':(1,[]),
'3.b':(1,[]),
'3.0':(1,[n(F+'0.1','helpful','lowering pH inhibits bacteria')]),
'3.1':(1,[n(F+'3.0','helpful','vinegar acts as preservative')]),
'3.2':(1,[n(F+'3.0','helpful','acetic acid strength')]),
'3.3':(1,[]),'3.4':(1,[]),
'4.b':(1,[n(F+'3.b','helpful','vinegar as preservative')]),
'4.0':(1,[n(F+'3.0','helpful','vinegar as preservative')]),
'4.1':(2,[n(A+'1.5.0','helpful','heat destroys micro-organisms and enzymes'),n(F+'3.0','helpful','vinegar acid prevents growth')]),
'4.2':(2,[n(F+'4.0','helpful','chutney ingredients and cooking')]),
'4.3':(1,[]),'4.4':(1,[]),
'4.5':(2,[n(F+'4.1','helpful','roles of vinegar, sugar, cooking')]),
'5.b':(1,[]),
'5.0':(2,[]),
'5.1':(1,[]),
'5.2':(1,[n(F+'2.2','helpful','brining and dry salting')]),
'5.3':(1,[]),'5.4':(1,[]),
'5.5':(2,[n(F+'5.2','helpful','salting before smoking'),n(F+'2.2','helpful','brining method')]),
'5.6':(1,[]),
'6.b':(1,[]),
'6.0':(2,[n(D+'4.0.3','helpful','E numbers as additive codes','low')]),
'6.1':(1,[]),'6.2':(1,[]),'6.3':(1,[]),
'6.4':(1,[n(F+'2.3','helpful','curing meat with nitrite')]),
'6.5':(2,[n(D+'4.3.4','helpful','sulphur dioxide declared as allergen')]),
'6.6':(2,[n(F+'2.6','helpful','high sodium health concern','low')]),
'6.7':(1,[n(D+'4.0.2','helpful','natural does not mean safer','low')]),
}
txt=open(H+'packs/'+P+'.txt').read()
tgt=[];allids=set();sec=None
for l in txt.split('\n'):
    if l.startswith('TARGET'): sec='t'
    elif l.startswith('CANDIDATES'): sec='c'
    m=re.match(r'\[(\S+?)\]',l)
    if m:
        allids.add(m.group(1))
        if sec=='t': tgt.append(m.group(1))
assert len(d)==len(tgt)
out={}
for t in tgt:
    k=t[len(F):]; out[t]={"cost":d[k][0],"needs":d[k][1]}
for v in out.values():
    for x in v['needs']: assert x['id'] in allids, x['id']
json.dump(out,open(H+'point-links/'+P+'.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
