import json,re
H='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
P='hom-personal-finance-s2.t1g1'
def n(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
F='hom-personal-finance-s2.'
A='hom-personal-finance-s'
R='hom-resource-management-s'
d={
'0.b':(1,[]),
'0.0':(1,[n(F+'1.1','helpful','discretionary spending')]),
'0.1':(1,[n(F+'1.1','helpful','discretionary expenditure')]),
'0.2':(1,[]),'0.3':(1,[]),
'0.4':(1,[n(F+'0.3','helpful','family life cycle stages')]),
'0.5':(1,[]),'0.6':(1,[]),'0.7':(2,[]),
'1.b':(1,[]),'1.0':(1,[]),'1.1':(1,[]),'1.2':(1,[]),'1.3':(1,[]),'1.4':(1,[]),'1.5':(1,[]),
'1.6':(1,[n(F+'1.3','helpful','fixed commitments')]),
'2.b':(1,[n(A+'1.3.1','helpful','net income basis')]),
'2.0':(1,[n(A+'1.3.1','essential','net take-home income')]),
'2.1':(1,[n(F+'1.3','helpful','fixed essential costs'),n(F+'1.4','helpful','irregular essential costs'),n(F+'1.1','helpful','discretionary expenditure')]),
'2.2':(1,[n(F+'1.0','helpful','essential expenditure')]),
'2.3':(1,[]),'2.4':(1,[]),'2.5':(1,[]),
'2.6':(2,[]),
'2.7':(1,[]),
'3.b':(1,[]),'3.0':(1,[]),'3.1':(1,[]),'3.2':(1,[]),'3.3':(1,[]),'3.4':(1,[]),'3.5':(1,[]),
'4.b':(1,[]),'4.0':(1,[]),
'4.1':(1,[n(F+'1.6','helpful','credit repayments as commitments')]),
'4.2':(1,[]),'4.3':(1,[]),
'4.4':(1,[n(R+'2.0.2','helpful','goals as intended outcomes','low')]),
'4.5':(1,[]),
'5.b':(1,[n(A+'1.3.1','helpful','net income')]),
'5.0':(1,[n(F+'1.3','helpful','fixed essential cost')]),
'5.1':(1,[]),'5.2':(1,[]),
'5.3':(1,[n(F+'1.1','helpful','discretionary spending')]),
'5.4':(2,[]),'5.5':(1,[]),'5.6':(1,[]),
'5.7':(1,[n(F+'0.0','helpful','low-income spending pattern','low')]),
'6.b':(1,[]),
'6.0':(1,[n(A+'1.0.4','helpful','MABS as State aid','low')]),
'6.1':(1,[n(F+'2.b','helpful','budget plan')]),
'6.2':(1,[]),
'6.3':(2,[n(A+'1.1.3','helpful','State supports and entitlements','low')]),
'6.4':(1,[]),'6.5':(1,[]),
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
for t,v in out.items():
    for x in v['needs']: assert x['id'] in allids and x['id']!=t, x['id']
json.dump(out,open(H+'point-links/'+P+'.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
