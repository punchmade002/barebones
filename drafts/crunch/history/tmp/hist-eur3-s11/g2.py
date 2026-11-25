import json,re
P='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
def n(i,w,c='high',s='helpful'): return {"id":i,"strength":s,"why":w,"confidence":c}
L={
'7.0':[n('hist-eur3-s9.2.1','Soviet invasion of eastern Poland')],
'7.2':[n('hist-eur3-s9.4.0','Britain not defeated in 1940')],
'8.0':[n('hist-eur3-s9.7.0','Operation Barbarossa invasion')],
'11.2':[n('hist-eur3-s9.11.3','Soviet advance 1944-45')],
'12.3':[n('hist-eur3-s9.7.1','rapid German advance in USSR','low')],
'14.0':[n('hist-eur3-s9.3.6','Vichy regime after French defeat')],
'14.6':[n('hist-eur3-s9.19.2','Allied bombing capability','low')],
'15.0':[n('hist-eur3-s9.11.3','Soviet advance into Poland 1944','low')],
}
EMPTY=['0.b','0.0','0.1','0.2','0.3','1.b','1.0','1.1','1.2','1.3','1.4','1.5','2.b','2.0','2.1','2.2','2.3','3.b','3.0','3.1','3.2','3.3','3.4','4.b','4.0','4.1','4.2','4.3','5.b','5.0','5.1','5.2','5.3','5.4','6.b','6.0','6.1','6.2','6.3','7.b','7.1','7.3','7.4','7.5','8.b','8.1','8.2','8.3','9.b','9.0','9.1','9.2','9.3','9.4','9.5','10.b','10.0','10.1','10.2','10.3','10.4','10.5','11.b','11.0','11.1','11.3','11.4','11.5','12.b','12.0','12.1','12.2','12.4','12.5','13.b','13.0','13.1','13.2','13.3','13.4','14.b','14.1','14.2','14.3','14.4','14.5','15.b','15.1','15.2','15.3','15.4','16.b','16.0','16.1','16.2','16.3','16.4','16.5']
keys=set(L)|set(EMPTY); assert not set(L)&set(EMPTY)
txt=open(P+'packs/hist-eur3-s11.t1g2.txt').read()
tgt=[re.match(r'\[(\S+?)\]',l).group(1) for l in txt.split('CANDIDATES')[0].splitlines() if l.startswith('[')]
allids=set(re.findall(r'^\[(\S+?)\]',txt,re.M))
out={}
for t in tgt:
    k=t.replace('hist-eur3-s11.','')
    assert k in keys,k
    out[t]={"needs":L.get(k,[])}
assert len(out)==len(keys)==len(tgt)
for v in out.values():
    for x in v['needs']: assert x['id'] in allids
json.dump(out,open(P+'point-links/hist-eur3-s11.t1g2.json','w'),indent=0)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
