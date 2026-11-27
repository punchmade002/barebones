import json,re
P='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/chemistry/'
def L(i,s,w,c='high'): return {"id":'chem1-'+i,"strength":s,"why":w,"confidence":c}
E,H='essential','helpful'
d={}
def a(i,c,*n): d['chem1-s5.'+i]=(c,list(n))
a('0.b',1);a('0.0',1)
a('0.1',1,L('s3.4.0',H,'plan contents'))
a('0.2',1,L('s4.3.2',H,'raw data vs processed'))
a('0.3',1);a('0.4',1)
a('1.b',1)
a('1.0',1,L('s3.5.1',E,'valid and fair test'),L('s3.1.2',H,'controlling variables','low'))
a('1.1',2,L('s3.5.2',H,'reliability from repeats'),L('s4.8.0',H,'anomalous results'))
a('1.2',1,L('s4.2.3',H,'systematic error examples','low'))
a('1.3',1,L('s4.2.1',H,'meniscus reading error','low'))
a('1.4',1,L('s3.6.6',H,'data-loggers and equipment'))
a('1.5',1)
a('1.6',1,L('s4.8.4',H,'justifying conclusion with limits','low'))
a('2.b',1);a('2.0',1);a('2.1',1);a('2.2',1)
a('3.b',1)
a('3.0',1,L('s3.1.2',H,'controlling variables','low'))
a('3.1',1);a('3.2',1);a('3.3',1)
a('4.b',1)
a('4.0',1,L('s3.2.0',H,'hypothesis'))
a('4.1',1,L('s3.4.0',H,'plan contents'))
a('4.2',1,L('s4.4.0',H,'results tables'))
a('4.3',1,L('s4.8.2',H,'conclusion about hypothesis'))
a('4.4',1)
a('5.b',1);a('5.0',1)
a('5.1',1,L('s4.0.0',H,'SI units'))
a('5.2',2,L('s4.4.0',H,'tables'),L('s4.5.0',H,'graphs'))
a('6.b',1);a('6.0',1);a('6.1',1);a('6.2',1);a('6.3',1)
a('7.b',1)
a('7.0',1,L('s4.8.4',H,'justifying claims with data','low'))
a('7.1',1);a('7.2',1);a('7.3',1)
txt=open(P+'packs/chem1-s5.t1g1.txt').read()
ids=re.findall(r'^\[([^\]]+)\]',txt.split('CANDIDATES')[0],re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
assert set(ids)==set(d) and len(ids)==len(d),(set(ids)^set(d))
out={}
for i in ids:
    c,n=d[i]
    for x in n: assert x['id'] in allids,x
    out[i]={"cost":c,"needs":n}
json.dump(out,open(P+'point-links/chem1-s5.t1g1.json','w'),ensure_ascii=False)
v=out.values()
print(len(out),sum(len(x['needs']) for x in v),sum(x['cost']==2 for x in v),sum(n['confidence']=='low' for x in v for n in x['needs']))
