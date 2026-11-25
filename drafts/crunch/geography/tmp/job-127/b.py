import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
n='geo-rocks-weathering-s3.'
def L(i,s,w,c='high'): return {"id":i if i.startswith('geo-') else n+i,"strength":s,"why":w,"confidence":c}
H,E='helpful','essential'
d={
'0.b':(1,[]),
'0.0':(1,[]),
'0.1':(1,[L('0.0',H,'weathering versus erosion')]),
'0.2':(1,[]),
'0.3':(1,[]),
'0.4':(1,[]),
'0.5':(1,[L('0.3',H,'physical weathering'),L('0.4',H,'chemical weathering')]),
'1.b':(1,[L('0.3',H,'physical weathering type')]),
'1.0':(1,[]),'1.1':(1,[]),'1.2':(1,[]),'1.3':(1,[]),
'1.4':(2,[]),
'1.5':(1,[L('1.3',H,'angular fragments from freeze-thaw')]),
'2.b':(1,[L('0.3',H,'physical weathering type')]),
'2.0':(1,[L('2.b',H,'insolation heating and cooling')]),
'2.1':(1,[L('2.0',E,'uses exfoliation')]),
'2.2':(1,[L('2.1',E,'stress from uneven heating')]),
'2.3':(1,[L('2.0',E,'exfoliation needs moisture')]),
'2.4':(1,[L('2.b',H,'insolation expansion')]),
'3.b':(1,[]),
'3.0':(2,[]),
'3.1':(1,[L('3.0',E,'sheeting from pressure release')]),
'3.2':(1,[]),
'3.3':(1,[L('3.2',H,'salt crystallisation')]),
'4.b':(1,[L('0.5',H,'biological weathering')]),
'4.0':(1,[L('0.3',H,'physical weathering')]),
'4.1':(1,[L('0.4',H,'chemical weathering')]),
'5.b':(1,[L('0.4',H,'chemical weathering')]),
'5.0':(1,[]),
'5.1':(2,[L('5.0',E,'carbonic acid reacts'),L('geo-rocks-weathering-s1.8.1',H,'limestone from sea creatures')]),
'5.2':(1,[L('5.1',E,'the reaction summarised')]),
'5.3':(2,[L('5.1',H,'carbonation dissolving limestone'),L('geo-rocks-weathering-s1.9.0',H,'Carboniferous limestone, Burren','low')]),
'6.b':(1,[L('0.4',H,'chemical weathering')]),
'6.0':(2,[L('geo-rocks-weathering-s1.4.0',H,'granite minerals quartz feldspar')]),
'6.1':(1,[L('6.0',E,'clay from hydrolysis')]),
'6.2':(1,[]),'6.3':(1,[]),'6.4':(1,[]),
'7.b':(1,[]),
'7.0':(1,[]),
'7.1':(2,[L('0.4',H,'chemical weathering')]),
'7.2':(1,[L('1.b',H,'freeze-thaw'),L('2.b',H,'desert insolation')]),
'7.3':(1,[L('7.1',H,'warm wet favours chemical')]),
'7.4':(1,[L('5.b',H,'carbonation of limestone'),L('6.0',H,'hydrolysis of granite')]),
'8.b':(1,[]),
'8.0':(1,[L('geo-rocks-weathering-s1.7.1',H,'bedding planes'),L('geo-rocks-weathering-s1.7.2',H,'joints','low')]),
'8.1':(1,[L('4.1',H,'humic acids')]),
'8.2':(1,[]),'8.3':(1,[]),
'8.4':(1,[L('1.b',H,'freeze-thaw')]),
'9.b':(1,[]),
'9.0':(2,[]),
'9.1':(2,[L('1.b',E,'freeze-thaw'),L('2.0',H,'exfoliation'),L('2.4',H,'granular disintegration')]),
'9.2':(1,[L('5.b',H,'carbonation'),L('6.0',H,'hydrolysis')]),
'9.3':(2,[L('1.5',H,'scree from freeze-thaw')]),
}
txt=open(P+'packs/geo-rocks-weathering-s3.t1g1.txt').read()
tl=txt.split('CANDIDATES')[0]
tids=re.findall(r'^\[(\S+?)\]',tl,re.M)
cids=set(re.findall(r'^\[(\S+?)\]',txt,re.M))
out={}
for t in tids:
    k=t[len(n):]; c,nd=d[k]
    for x in nd: assert x['id']!=t and x['id'] in cids,x
    out[t]={"cost":c,"needs":nd}
assert len(out)==len(d)==len(tids)
json.dump(out,open(P+'point-links/geo-rocks-weathering-s3.t1g1.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
