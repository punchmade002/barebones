import json,re
P='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
C='hom-work-leisure-s5.'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
H,E='helpful','essential'
def c(x): return C+x
d={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),
'0.2':(1,[L(c('0.1'),H,'sex roles')]),
'0.3':(1,[L(c('0.2'),H,'traditional sex roles')]),
'0.4':(1,[L('hom-work-leisure-s2.5.7',H,'paternity and parent\'s leave')]),
'0.5':(1,[L(c('0.3'),H,'change in sex roles')]),
'0.6':(1,[L(c('0.1'),H,'sex roles')]),
'1.b':(1,[]),
'1.0':(1,[L(c('0.1'),H,'role')]),
'1.1':(2,[L(c('1.0'),E,'role overload')]),
'1.2':(2,[L(c('1.0'),E,'role overload')]),
'1.3':(1,[L(c('1.0'),E,'role overload')]),
'1.4':(1,[L(c('1.0'),H,'role overload')]),
'1.5':(1,[L(c('0.2'),H,'women as main carers')]),
'1.6':(2,[L(c('1.0'),E,'role overload')]),
'2.b':(1,[L(c('1.0'),H,'contrast with role overload')]),
'2.0':(1,[L(c('0.1'),H,'role')]),
'2.1':(1,[L(c('2.0'),E,'role conflict')]),
'2.2':(1,[L(c('2.0'),E,'role conflict')]),
'2.3':(1,[L(c('2.0'),E,'role conflict')]),
'2.4':(1,[L(c('2.0'),E,'role conflict')]),
'2.5':(1,[L(c('2.0'),E,'role conflict')]),
'2.6':(1,[L(c('2.0'),E,'role conflict')]),
'3.b':(1,[]),'3.0':(2,[]),'3.1':(2,[]),
'3.2':(1,[L(c('0.3'),H,'modern shared sex roles')]),
'3.3':(1,[]),'3.4':(1,[]),'3.5':(1,[]),
'3.6':(2,[L(c('1.0'),H,'role overload')]),
'3.7':(2,[L(c('3.2'),H,'fair sharing of tasks')]),
'4.b':(1,[]),'4.0':(1,[]),'4.1':(1,[]),'4.2':(1,[]),
'4.3':(1,[L(c('3.2'),H,'sharing tasks')]),
'4.4':(1,[]),'4.5':(1,[]),'4.6':(1,[]),
'4.7':(1,[L(c('1.0'),H,'role overload'),L(c('2.0'),H,'role conflict')]),
'5.b':(1,[]),'5.0':(1,[]),'5.1':(1,[]),'5.2':(2,[]),'5.3':(2,[]),'5.4':(1,[]),'5.5':(1,[]),'5.6':(2,[]),'5.7':(2,[]),
'6.b':(1,[L(c('0.2'),H,'traditional sex roles')]),
'6.0':(1,[]),
'6.1':(1,[L(c('3.1'),H,'home-care tasks')]),
'6.2':(1,[L(c('6.1'),H,'the list of tasks')]),
'6.3':(1,[]),'6.4':(1,[]),
'6.5':(1,[L(c('6.2'),H,'questionnaire categories')]),
'6.6':(1,[L(c('0.2'),H,'traditional sex roles'),L(c('0.0'),H,'dual-earner households')]),
'6.7':(1,[]),
}
txt=open(P+'packs/hom-work-leisure-s5.t1g1.txt').read()
tids=re.findall(r'^\[([^\]]+)\]',txt.split('CANDIDATES')[0],re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
assert [t[len(C):] for t in tids]==list(d.keys()),(len(tids),len(d))
out={C+k:{"cost":v[0],"needs":v[1]} for k,v in d.items()}
for k,v in out.items():
    for n in v['needs']: assert n['id'] in allids and n['id']!=k,n
json.dump(out,open(P+'point-links/hom-work-leisure-s5.t1g1.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
