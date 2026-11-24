import json,re
P='hist-eur3-s8.'
H,E,h,l='helpful','essential','high','low'
def L(i,s,w,c=h): return {"id":i,"strength":s,"why":w,"confidence":c}
spec={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),
'0.2':(2,[L('hist-eur3-s7.2.3',H,'shipbuilding collapse in the 1930s')]),
'0.3':(2,[]),'0.4':(1,[]),
'0.5':(2,[L('hist-eur3-s8.0.3',E,'uses National Shipbuilders Security')]),
'0.6':(2,[L('hist-eur3-s8.1.0',H,'uses Ellen Wilkinson')]),
'0.7':(2,[L('hist-eur3-s7.2.4',H,'regional unemployment figures')]),
'0.8':(1,[L('hist-eur3-s7.6.0',H,'Special Areas Act of 1934')]),
'1.b':(1,[]),'1.0':(1,[]),
'1.1':(1,[L('hist-eur3-s8.1.0',H,'uses Ellen Wilkinson')]),
'1.2':(1,[]),'1.3':(1,[]),'1.4':(1,[]),
'2.b':(1,[]),
'2.0':(1,[L('hist-eur3-s8.0.6',H,'the proposed steelworks')]),
'2.1':(1,[]),'2.2':(1,[]),'2.3':(1,[]),
'2.4':(2,[L('hist-eur3-s8.2.5',H,'Communist-led marches feared')]),
'2.5':(1,[L('hist-eur3-s7.5.0',H,'the NUWM and hunger marches')]),
'3.b':(1,[]),'3.0':(1,[]),'3.1':(2,[]),'3.2':(1,[]),'3.3':(1,[]),
'3.4':(1,[L('hist-eur3-s8.2.2',H,'the petition carried')]),
'3.5':(1,[]),
'4.b':(1,[]),
'4.0':(1,[L('hist-eur3-s8.7.0',H,'Baldwin National Government')]),
'4.1':(2,[L('hist-eur3-s8.4.0',E,'answers Baldwin on falling unemployment')]),
'4.2':(1,[L('hist-eur3-s8.2.2',H,'the petition')]),
'4.3':(1,[L('hist-eur3-s7.5.2',H,'Unemployment Assistance Board means test')]),
'4.4':(1,[]),'4.5':(1,[]),
'5.b':(1,[]),
'5.0':(1,[L('hist-eur3-s8.0.5',H,'Palmers site after NSS purchase')]),
'5.1':(2,[L('hist-eur3-s7.6.0',E,'the 1934 Special Areas Act')]),
'5.2':(1,[L('hist-eur3-s7.8.4',H,'rearmament revives depressed regions')]),
'5.3':(1,[]),
'5.4':(1,[L('hist-eur3-s8.1.2',H,'David Riley as march leader')]),
'6.b':(1,[]),
'6.0':(1,[L('hist-eur3-s8.2.3',H,'discipline of the marchers')]),
'6.1':(1,[]),'6.2':(2,[]),'6.3':(1,[]),'6.4':(1,[]),
'7.b':(1,[]),
'7.0':(2,[L('hist-eur3-s7.3.2',H,'formation of the National Government')]),
'7.1':(2,[]),'7.2':(1,[]),
'7.3':(1,[L('hist-eur3-s7.8.3',H,'national unemployment figures')]),
'7.4':(1,[L('hist-eur3-s7.5.2',H,'household means test')]),
'7.5':(2,[L('hist-eur3-s8.1.0',H,'uses Ellen Wilkinson')]),
'8.b':(1,[]),
'8.0':(1,[L('hist-eur3-s8.1.3',H,'cross-party respectable appeal')]),
'8.1':(1,[L('hist-eur3-s8.4.0',H,"Baldwin's unemployment claim")]),
'8.2':(1,[L('hist-eur3-s8.2.4',H,'Labour and TUC feared Communists')]),
'8.3':(1,[]),
'8.4':(1,[L('hist-eur3-s8.5.2',H,'rearmament revived the town',l)]),
'8.5':(1,[]),
'9.b':(1,[]),
'9.0':(1,[L('hist-eur3-s8.4.3',H,'marchers lost benefit')]),
'9.1':(1,[L('hist-eur3-s8.5.2',H,'rearmament and war recovery')]),
'9.2':(1,[]),'9.3':(1,[]),'9.4':(1,[]),'9.5':(1,[]),
}
d='/Users/gabrielwhelan/barebones/drafts/crunch/history/'
txt=open(d+'packs/hist-eur3-s8.t1g1.txt').read()
tgt=[];allid=set();sec=None
for ln in txt.split('\n'):
    if ln.startswith('TARGET'):sec='t'
    elif ln.startswith('CANDIDATES'):sec='c'
    m=re.match(r'\[([^\]]+)\]',ln)
    if m:
        allid.add(m.group(1))
        if sec=='t':tgt.append(m.group(1))
out={}
for t in tgt:
    c,n=spec[t[len(P):]]
    for x in n: assert x['id'] in allid and x['id']!=t,(t,x)
    out[t]={"cost":c,"needs":n}
assert len(out)==len(spec),(len(out),len(spec))
json.dump(out,open(d+'point-links/hist-eur3-s8.t1g1.json','w'),indent=0)
r=json.load(open(d+'point-links/hist-eur3-s8.t1g1.json'))
print(len(r),sum(len(v['needs']) for v in r.values()),sum(v['cost']==2 for v in r.values()),sum(x['confidence']=='low' for v in r.values() for x in v['needs']))
