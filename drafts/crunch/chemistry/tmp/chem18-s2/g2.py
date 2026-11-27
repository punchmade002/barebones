import json,re
B='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/chemistry/'
H='helpful'
def n(i,w,c='high'): return {"id":i,"strength":H,"why":w,"confidence":c}
P='chem18-s2.'
L={'2.b':[n('chem9-s3.0.b','gas pressure from particle collisions','low')],
'2.3':[n('chem9-s3.0.0','compression raises concentration','low')],
'2.4':[n('chem9-s3.0.0','compression raises concentration','low')],
'4.b':[n('chem17-s3.0.0','catalyst definition')],
'4.0':[n('chem17-s3.1.2','catalyst speeds both directions equally')],
'4.1':[n('chem17-s3.0.1','lower activation energy, faster rate')],
'4.2':[n('chem17-s3.1.2','catalyst does not change amount formed')],
'7.b':[n('chem17-s3.0.0','catalyst speeds reaction')],
'7.0':[n('chem17-s3.2.5','iron catalyst in Haber process')],
'9.2':[n('chem17-s3.0.1','catalyst lowers activation energy')]}
txt=open(B+'packs/chem18-s2.t1g2.txt').read()
ids=re.findall(r'^\[([^\]]+)\]',txt.split('\nCANDIDATES')[0],re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
assert set(k for k in L)<={i[len(P):] for i in ids}
o={}
for i in ids:
    nn=L.get(i[len(P):],[])
    for x in nn: assert x['id'] in allids
    o[i]={"needs":nn}
json.dump(o,open(B+'point-links/chem18-s2.t1g2.json','w'),ensure_ascii=False)
print(len(o),sum(len(v['needs']) for v in o.values()),sum(x['confidence']=='low' for v in o.values() for x in v['needs']))
