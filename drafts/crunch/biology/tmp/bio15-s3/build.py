import json,re
D='/Users/gabrielwhelan/barebones/drafts/crunch/biology'
txt=open(D+'/points/bio15-s3.txt').read()
tg=[];allids=set()
sec=None
for l in txt.split('\n'):
    if l.startswith('TARGET'): sec='t'
    elif l.startswith('CANDIDATES'): sec='c'
    m=re.match(r'\[([^\]]+)\]',l)
    if m:
        allids.add(m.group(1))
        if sec=='t': tg.append(m.group(1))
def n(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
E,H='essential','helpful'
S={
'0.b':(1,[]),'0.0':(1,[]),
'0.1':(2,[n('bio9-s1.1.0',H,'ATP and phosphate groups')]),
'0.2':(1,[]),
'0.3':(2,[n('bio9-s2.1.1',E,'dehydrogenases load NAD+ with hydrogen')]),
'0.4':(2,[n('bio9-s1.3.0',E,'phosphate added to ADP makes ATP')]),
'0.5':(1,[]),
'0.6':(2,[n('bio15-s3.0.4',H,'net ATP yield of glycolysis','low')]),
'1.b':(1,[]),'1.0':(1,[]),
'1.1':(1,[n('bio15-s3.0.0',H,'glycolysis pathway itself')]),
'2.b':(1,[n('bio9-s2.0.b',H,'NAD+ as hydrogen carrier')]),
'2.0':(1,[n('bio15-s3.0.4',H,'ATP used and made in glycolysis')]),
'2.1':(2,[n('bio15-s3.0.3',E,'NAD+ accepts hydrogen forming NADH')]),
'2.2':(2,[n('bio9-s2.2.1',E,'NADH to electron transport chain')]),
'2.3':(2,[n('bio9-s2.2.3',E,'fermentation passes hydrogen to pyruvate')]),
'3.b':(1,[n('bio15-s3.2.1',H,'NAD+ must be regenerated')]),
'3.0':(2,[n('bio15-s3.2.1',E,'NAD+ regeneration needed for glycolysis')]),
'3.1':(1,[n('bio15-s3.2.0',H,'net 2 ATP from glycolysis','low')]),
'3.2':(2,[n('bio15-s3.0.5',E,'pyruvate as glycolysis product')]),
'3.3':(1,[n('bio15-s3.3.2',E,'lactic acid fermentation overall')]),
'3.4':(2,[n('bio15-s3.0.5',E,'pyruvate loses carbon as CO2')]),
'3.5':(2,[n('bio15-s3.3.4',E,'alcoholic fermentation steps')]),
'3.6':(1,[n('bio15-s3.3.4',H,'carbon lost as CO2 in ethanol')]),
'4.b':(1,[]),
'4.0':(1,[n('bio15-s3.3.2',H,'lactic acid fermentation')]),
'4.1':(1,[n('bio15-s3.3.0',H,'fermentation when oxygen absent')]),
'4.2':(1,[n('bio15-s1.2.0',H,'anaerobic releases less energy')]),
'4.3':(2,[n('bio15-s3.3.0',H,'fermentation branch of pathway')]),
}
out={}
for i in tg:
    c,nd=S[i.split('bio15-s3.')[1]]
    out[i]={"cost":c,"needs":nd}
json.dump(out,open(D+'/point-links/bio15-s3.json','w'),indent=1)
o=json.load(open(D+'/point-links/bio15-s3.json'))
assert list(o)==tg and len(set(tg))==len(tg)
for k,v in o.items():
    for x in v['needs']: assert x['id'] in allids and x['id']!=k,(k,x)
print(len(o),sum(len(v['needs']) for v in o.values()),sum(v['cost']==2 for v in o.values()),sum(x['confidence']=='low' for v in o.values() for x in v['needs']))
