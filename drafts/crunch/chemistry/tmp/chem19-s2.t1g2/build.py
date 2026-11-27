import json,re
D='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/chemistry/'
E='essential';H='helpful'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
links={
'0.b':[L('chem8-s2.2.0',H,'concentration in mol per litre')],
'0.0':[L('chem8-s2.2.0',H,'concentration in mol per litre')],
'1.b':[L('chem8-s2.11.1',H,'g per litre to mol per litre')],
'1.0':[L('chem8-s1.1.5',H,'molar mass')],
'1.1':[L('chem8-s2.10.1',H,'concentration in g per litre')],
'1.2':[L('chem8-s2.11.1',E,'g per litre to mol per litre')],
'2.6':[L('chem8-s2.11.1',H,'g per litre to mol per litre')],
'3.1':[L('chem8-s2.2.0',H,'concentration in mol per litre')],
'4.5':[L('chem8-s1.2.0',E,'moles from mass over molar mass')],
'4.6':[L('chem8-s2.2.1',E,'c = n / V in litres')],
'7.2':[L('chem8-s1.2.0',E,'n = m / M'),L('chem8-s2.2.1',E,'c = n / V')],
'15.b':[L('chem8-s2.2.2',H,'dilution lowers concentration','low')],
'15.0':[L('chem8-s2.2.2',H,'dilution lowers concentration','low')],
}
src=open(D+'packs/chem19-s2.t1g2.txt').read()
tid=re.findall(r'^\[(chem19-s2\.[^\]]+)\]',src,re.M)
allid=set(re.findall(r'^\[([^\]]+)\]',src,re.M))
for k in links: assert 'chem19-s2.'+k in tid,k
out={}
for t in tid:
    n=links.get(t[len('chem19-s2.'):],[])
    for x in n: assert x['id'] in allid
    out[t]={"needs":n}
json.dump(out,open(D+'point-links/chem19-s2.t1g2.json','w'),ensure_ascii=False)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
