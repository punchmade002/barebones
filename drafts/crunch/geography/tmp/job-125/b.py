import json,re
S='geo-rocks-weathering-s1.'
P='geo-plate-tectonics-s'
def L(i,s,w,c='high'):
    if not i.startswith('geo-'): i=S+i
    return {"id":i,"strength":s,"why":w,"confidence":c}
H,E='helpful','essential'
D={
'0.b':(1,[]),
'0.0':(1,[]),
'0.1':(1,[]),
'0.2':(1,[L('0.1',H,'erosion carries the sediment')]),
'1.b':(1,[]),
'1.0':(1,[L('0.0',H,'magma from endogenic forces')]),
'1.1':(1,[L('0.1',H,'weathering and erosion defined')]),
'1.2':(1,[L('6.2',H,'compaction and cementation (lithification)')]),
'1.3':(1,[L('10.0',H,'heat and pressure metamorphism')]),
'1.4':(1,[]),
'1.5':(1,[L('1.b',H,'uses the rock cycle loop')]),
'1.6':(2,[L('1.b',E,'draws the whole cycle and processes')]),
'2.b':(1,[]),
'2.0':(1,[L(P+'3.0.0',H,'constructive boundaries create crust')]),
'2.1':(1,[L(P+'3.0.1',H,'collision at destructive boundaries')]),
'2.2':(1,[L(P+'3.5.1',E,'subduction zone')]),
'3.b':(1,[]),
'3.0':(1,[]),
'3.1':(1,[L('3.0',E,'slow cooling gives large crystals')]),
'3.2':(1,[L('3.0',E,'fast cooling gives small crystals')]),
'3.3':(1,[L('3.2',H,'basalt is volcanic rock','low')]),
'4.b':(1,[]),
'4.0':(1,[L('3.1',H,'plutonic rock cools slowly')]),
'4.1':(1,[L('3.1',H,'plutonic rock')]),
'4.2':(1,[L('7.1',H,'bedding planes (layers)')]),
'4.3':(1,[L('7.1',E,'bedding planes')]),
'4.4':(1,[L('0.1',H,'erosion removes overlying rock')]),
'5.b':(1,[]),
'5.0':(1,[L('3.2',H,'volcanic rock cools fast')]),
'5.1':(1,[L(P+'3.0.0',E,'constructive (divergent) boundaries')]),
'5.2':(1,[L(P+'3.5.1',E,'subduction zones')]),
'6.b':(1,[]),
'6.0':(1,[]),
'6.1':(2,[]),
'6.2':(1,[]),
'6.3':(1,[]),
'6.4':(1,[]),
'7.b':(1,[]),
'7.0':(1,[]),
'7.1':(1,[]),
'7.2':(1,[L('7.1',H,'cracks cut through layers','low')]),
'7.3':(1,[]),
'8.b':(1,[]),
'8.0':(1,[L('6.0',H,'sediment from rock fragments')]),
'8.1':(1,[L('6.0',H,'sediment from plant and animal remains')]),
'8.2':(1,[L('6.0',H,'minerals precipitated from water')]),
'9.b':(1,[]),
'9.0':(2,[L('8.1',H,'limestone is organic rock')]),
'9.1':(2,[L('8.0',H,'sandstone from sand and pebbles')]),
'9.2':(1,[L('9.1',H,'Old Red Sandstone')]),
'9.3':(1,[L('8.0',H,'shale and sandstone are clastic')]),
'9.4':(1,[L('13.4',H,'Antrim basalt lava flows')]),
'9.5':(1,[L('8.1',H,'coal from plant remains')]),
'9.6':(1,[L('8.2',H,'rock salt is an evaporite')]),
'10.b':(1,[]),
'10.0':(1,[]),
'10.1':(1,[]),
'10.2':(1,[]),
'11.b':(1,[]),
'11.0':(1,[L('4.b',H,'igneous intrusion heats rock')]),
'11.1':(1,[L(P+'3.0.1',H,'plate collision')]),
'12.b':(1,[]),
'12.0':(1,[L('8.1',H,'limestone parent rock')]),
'12.1':(1,[L('8.0',H,'sandstone parent rock')]),
'12.2':(2,[L('8.0',H,'shale parent rock')]),
'12.3':(1,[L('4.0',H,'granite is igneous')]),
'12.4':(2,[L('12.1',E,'quartzite from sandstone')]),
'12.5':(2,[L('11.0',H,'metamorphic aureole')]),
'12.6':(1,[L('12.3',H,'gneiss from granite')]),
'13.b':(1,[]),
'13.0':(1,[L('9.0',H,'Carboniferous limestone lowland')]),
'13.1':(2,[L('4.0',H,'granite','low')]),
'13.2':(2,[L('4.1',H,'batholith')]),
'13.3':(1,[L('13.2',H,'compares with Leinster granite')]),
'13.4':(2,[L('5.1',H,'basalt from runny lava')]),
'13.5':(2,[L(P+'3.11.2',H,'Iapetus closed, Atlantic opened')]),
'14.b':(1,[]),
'14.0':(1,[L(P+'3.5.1',H,'subduction')]),
'14.1':(1,[L('5.2',H,'volcanoes above subduction zones')]),
'14.2':(1,[L('4.1',H,'batholith')]),
'14.3':(1,[L('11.1',H,'regional metamorphism')]),
'14.4':(1,[L(P+'3.0.2',H,'transform boundary')]),
'14.5':(1,[]),
'14.6':(1,[L('6.1',H,'sediment on continental shelves')]),
'14.7':(1,[]),
'15.b':(1,[]),
'15.0':(1,[L('3.1',H,'plutonic slow cooling')]),
'15.1':(1,[L('3.2',H,'volcanic fast cooling')]),
'15.2':(1,[L('8.0',H,'sandstone is clastic')]),
'15.3':(1,[L('8.1',H,'limestone from shells')]),
'15.4':(1,[L('12.0',H,'marble from limestone')]),
'15.5':(1,[L('12.1',H,'quartzite from sandstone')]),
'15.6':(1,[L('10.2',H,'cleavage in metamorphism')]),
}
txt=open('packs/geo-rocks-weathering-s1.t1g1.txt').read()
ids=[]
t=txt.split('CANDIDATES')[0]
ids=re.findall(r'^\[(geo-rocks-weathering-s1\.[^\]]+)\]',t,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
out={}
for i in ids:
    k=i[len(S):]
    c,n=D[k]
    out[i]={"cost":c,"needs":n}
assert len(D)==len(ids)==len(out)
for v in out.values():
    for n in v['needs']: assert n['id'] in allids,n
json.dump(out,open('point-links/geo-rocks-weathering-s1.t1g1.json','w'),indent=1)
l=sum(len(v['needs']) for v in out.values())
print(len(out),l,sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
