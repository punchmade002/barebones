import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
S='geo-rocks-weathering-'
V='geo-volcanoes-earthquakes-s3.'
def n(i):
    if i.startswith('s4.'):return S+i
    if i.startswith('s3.') or i.startswith('s1.'):return S+i
    return V+i[2:]
H,L='high','low'
E,HL='essential','helpful'
# id: (cost, [(need,strength,why,conf)])
D={
'0.b':(1,[('s3.5.3',HL,'carbonation behind karst',H)]),
'0.0':(2,[('s3.5.b',HL,'carbonation as chemical weathering',H)]),
'0.1':(1,[]),
'0.2':(1,[('0.1',E,'permeable rock','high'),('s1.7.1',HL,'bedding planes defined',H)]),
'0.3':(1,[]),
'0.4':(1,[]),
'1.b':(1,[('0.2',HL,'jointed bedded limestone',H)]),
'1.0':(1,[('0.2',HL,'bedding planes and joints',H)]),
'1.1':(1,[('0.0',E,'carbonation process',H),('2.0',HL,'grikes defined',H)]),
'1.2':(1,[('2.0',E,'grikes',H)]),
'1.3':(2,[('s1.9.0',HL,'Carboniferous limestone',H)]),
'1.4':(1,[('1.3',HL,'the Burren',L)]),
'2.b':(1,[]),
'2.0':(1,[('0.0',HL,'carbonation widens joints',H)]),
'2.1':(1,[('2.0',E,'grikes bound clints',H)]),
'2.2':(1,[('2.1',E,'clint surfaces',H)]),
'2.3':(1,[('2.1',HL,'clint surfaces',H)]),
'2.4':(1,[('2.0',HL,'clints and grikes',H)]),
'3.b':(1,[('0.2',HL,'water sinks via joints',H)]),
'3.0':(1,[('0.1',E,'impermeable vs permeable rock',H),('0.0',HL,'carbonation widens joint',H)]),
'3.1':(1,[('0.0',HL,'solution of limestone',H)]),
'3.2':(1,[('3.1',E,'dolines',H)]),
'3.3':(1,[]),
'3.4':(2,[('0.1',E,'impermeable frozen ground',H),('0.3',HL,'water table',H)]),
'4.b':(1,[('0.3',HL,'water table',H)]),
'4.0':(1,[('0.3',E,'water table rising and falling',H)]),
'4.1':(1,[('4.0',E,'turlough',H)]),
'4.2':(1,[('3.0',E,'swallow hole reverse',H)]),
'4.3':(1,[('4.2',E,'resurgence',H),('3.0',E,'swallow hole',H)]),
'5.b':(1,[('0.0',HL,'solution widens cracks',H)]),
'5.0':(1,[('0.2',E,'bedding planes and joints',H)]),
'5.1':(1,[('5.0',HL,'caves',H)]),
'5.2':(1,[('6.1',HL,'stalactite',H)]),
'6.b':(1,[('0.0',HL,'dissolved limestone',H)]),
'6.0':(2,[('0.0',E,'calcium bicarbonate',H)]),
'6.1':(1,[('6.0',E,'dripstone deposition',H)]),
'6.2':(1,[('6.0',E,'dripstone deposition',H)]),
'6.3':(1,[('6.1',E,'stalactite',H),('6.2',E,'stalagmite',H)]),
'6.4':(1,[('6.0',HL,'calcite deposition',H)]),
'6.5':(2,[('6.3',E,'pillar, stalactites, stalagmites',H),('3.0',HL,'swallow hole',H)]),
'7.b':(1,[]),
'7.0':(1,[('3.0',E,'swallow holes',H)]),
'7.1':(1,[('7.0',HL,'swallow holes take drainage',H),('3.2',HL,'uvalas',H)]),
'7.2':(1,[('7.1',HL,'caves and dolines',H)]),
'8.b':(1,[('3.0',HL,'streams sinking',H)]),
'8.0':(1,[]),
'8.1':(2,[('3.0',E,'swallow holes',H),('4.2',HL,'re-emergence',H)]),
'8.2':(1,[('8.1',HL,'Cladagh River',H)]),
'8.3':(1,[]),
'8.4':(1,[('0.1',HL,'permeable limestone leaks',H)]),
'9.b':(1,[]),
'9.0':(1,[('3.3',HL,'polje',H)]),
'9.1':(1,[]),
'9.2':(1,[('5.0',HL,'caves',H)]),
'9.3':(1,[]),
'10.b':(1,[('0.1',HL,'impermeable rock',H)]),
'10.0':(1,[('0.1',E,'impermeable rock',H)]),
'10.1':(2,[('s3.6.0',E,'hydrolysis of feldspar',H)]),
'10.2':(1,[('10.1',E,'clay from hydrolysis',H)]),
'10.3':(1,[('s1.4.1',HL,'batholith',H)]),
'10.4':(1,[('geo-volcanoes-earthquakes-s3.13.2',HL,'granite exposed by erosion',H)]),
'10.5':(1,[('10.0',E,'impermeable granite',H)]),
'10.6':(1,[]),
'11.b':(1,[('11.0',HL,'tor defined',H)]),
'11.0':(1,[]),
'11.1':(2,[('s3.6.0',E,'hydrolysis',H)]),
'11.2':(2,[('11.1',E,'stage 1 rotting',H),('s3.0.1',HL,'mass movement',H)]),
'11.3':(1,[('s3.1.b',HL,'freeze-thaw',H)]),
'11.4':(1,[('11.0',E,'tors',H)]),
'11.5':(2,[('11.0',HL,'tors',H)]),
'11.6':(1,[('11.1',E,'rotted zone along joints',H)]),
'12.b':(1,[]),
'12.0':(1,[('s1.9.0',HL,'Carboniferous limestone',H)]),
'12.1':(1,[]),
'12.2':(1,[('12.1',HL,'resistant rock stands up',H)]),
'12.3':(1,[('0.1',E,'permeable vs impermeable',H)]),
'12.4':(1,[('12.0',HL,'limestone lowland vs uplands',H)]),
}
txt=open(P+'packs/geo-rocks-weathering-s4.t1g1.txt').read()
ids=re.findall(r'^\[(geo-rocks-weathering-s4\.[^\]]+)\]',txt,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
out={}
for k in ids:
    c,nd=D[k.split('s4.')[1]]
    out[k]={'cost':c,'needs':[{'id':n(i) if not i.startswith('geo-') else i,'strength':s,'why':w,'confidence':f} for i,s,w,f in
      [(x if x[0] in 'sg' else 's4.'+x,*r) for x,*r in nd]]}
assert len(ids)==len(D)==len(set(ids))
for v in out.values():
    for x in v['needs']: assert x['id'] in allids,x
json.dump(out,open(P+'point-links/geo-rocks-weathering-s4.t1g1.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
