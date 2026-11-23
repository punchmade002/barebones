import json,re
P='points/bio8-s8.txt'
txt=open(P).read()
ids=[]; allids=set(); tgt=True
for l in txt.splitlines():
    if l.startswith('CANDIDATES'): tgt=False
    m=re.match(r'\[(\S+)\]',l)
    if m:
        allids.add(m.group(1))
        if tgt: ids.append(m.group(1))
E,H='essential','helpful'
S={ # id: (cost, [(need,strength,why,conf)])
'0.b':(1,[('s7.0.0',H,'qualitative vs quantitative','high')]),
'0.0':(1,[('s7.4.0',H,'reducing sugar defined','high')]),
'0.1':(1,[('s7.0.1',H,'hypothesis format','low')]),
'0.2':(1,[('s7.4.5',E,'copper(II) reduced to copper(I) oxide','high')]),
'0.3':(1,[('s7.4.4',H,'colour scale and precipitate','high')]),
'0.4':(2,[('s8.0.2',E,'colour change principle','high')]),
'1.b':(1,[('s7.0.3',H,'fair test controls','low')]),
'1.0':(1,[('s7.0.2',E,'independent and dependent variables','high')]),
'1.1':(2,[('s7.0.3',H,'controlled variables','high')]),
'1.2':(1,[('s7.0.4',E,'negative control','high')]),
'1.3':(1,[('s7.0.5',E,'positive control','high')]),
'1.4':(1,[]),'1.5':(1,[]),
'1.6':(1,[('s7.4.0',H,'sucrose non-reducing','high')]),
'2.b':(1,[]),'2.0':(1,[]),
'2.1':(1,[('s8.2.0',E,'stock solution','high')]),
'2.2':(2,[('s8.2.1',E,'dilution range','high')]),
'2.3':(1,[('s8.2.1',H,'range of standards','low')]),
'3.b':(1,[]),
'3.0':(1,[('s7.2.0',H,'preparing food solution','low')]),
'3.1':(1,[('s7.2.0',H,'crushing releases nutrients','high')]),
'3.2':(1,[('s7.2.1',H,'filtering food solution','low')]),
'3.3':(1,[('s8.2.2',H,'dilution calculation','low')]),
'4.b':(1,[('s8.2.1',H,'standards range','low')]),
'4.0':(1,[('s8.2.1',E,'standards to be tested','high')]),
'4.1':(1,[('s7.4.1',H,'Benedict\'s method','high')]),
'4.2':(1,[('s7.4.2',H,'water bath heating','high')]),
'4.3':(1,[]),
'4.4':(1,[('s8.2.1',E,'standards form scale','high')]),
'4.5':(1,[('s7.9.5',H,'repeats check repeatability','low')]),
'4.6':(1,[('s8.0.2',H,'colour scale principle','low')]),
'4.7':(1,[('s8.4.4',H,'matching tubes to scale','high')]),
'5.b':(1,[]),
'5.0':(1,[('bio2-s4.0.2',H,'colorimeter gives objective reading','low')]),
'5.1':(2,[('s8.4.2',E,'heated tubes with precipitate','high')]),
'5.2':(1,[('s8.5.1',H,'prepared tubes','low')]),
'5.3':(2,[('s7.4.5',E,'copper(II) ions used up','high')]),
'5.4':(2,[('s8.5.3',E,'absorbance falls with sugar','high'),('bio2-s4.5.0',H,'axes and variables','low')]),
'5.5':(2,[('s8.5.4',E,'calibration curve','high'),('s8.3.3',H,'dilution factor','low')]),
'6.b':(1,[]),'6.0':(1,[]),
'6.1':(1,[('s8.6.0',H,'strip pad colour','low')]),
'6.2':(2,[('s7.4.0',E,'reducing sugars list','high')]),
'6.3':(1,[('s8.3.3',H,'diluting samples','low')]),
'6.4':(1,[]),
'7.b':(1,[]),'7.0':(1,[]),'7.1':(1,[]),'7.2':(1,[]),
'8.b':(1,[('bio2-s4.0.6',E,'primary data defined','high')]),
'8.0':(1,[('bio2-s4.1.0',H,'results table layout','low')]),
'8.1':(1,[('s8.0.2',H,'colour indicates sugar level','low')]),
'8.2':(1,[('s7.4.0',H,'sucrose non-reducing','high')]),
'8.3':(2,[('bio2-s4.10.1',H,'justifying conclusions','low')]),
'8.4':(1,[('bio2-s4.0.2',H,'objective vs subjective data','low')]),
'9.b':(1,[]),
'9.0':(1,[('s8.5.0',H,'colorimeter','high')]),
'9.1':(1,[]),
'9.2':(1,[('s8.0.4',E,'Benedict\'s in excess','high')]),
'9.3':(1,[]),'9.4':(1,[]),'9.5':(1,[]),
'9.6':(1,[('s8.2.1',H,'range of standards','low')]),
}
def full(i): return i if i.startswith('bio') else 'bio8-'+i
out={}
for i in ids:
    k=i.replace('bio8-s8.','')
    c,ns=S[k]
    out[i]={'cost':c,'needs':[{'id':full(n),'strength':s,'why':w,'confidence':f} for n,s,w,f in ns]}
assert list(out)==ids and len(set(ids))==len(ids)
for v in out.values():
    for n in v['needs']: assert n['id'] in allids, n
json.dump(out,open('point-links/bio8-s8.json','w'),indent=1)
r=json.load(open('point-links/bio8-s8.json'))
ln=[n for v in r.values() for n in v['needs']]
print(len(r),len(ln),sum(v['cost']==2 for v in r.values()),sum(n['confidence']=='low' for n in ln))
