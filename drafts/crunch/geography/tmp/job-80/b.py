import json,re
P='geo-plate-tectonics-s3.'
E,H='essential','helpful'
# id: (cost, [(target, strength, why, conf)])
d={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),'0.2':(1,[]),
'1.b':(1,[]),'1.0':(1,[('geo-plate-tectonics-s1.5.1',H,'convection currents','high')]),'1.1':(1,[]),'1.2':(1,[]),
'2.b':(1,[]),'2.0':(1,[]),'2.1':(1,[(P+'0.2',H,'transform boundaries','high')]),'2.2':(1,[]),
'2.3':(1,[('geo-plate-tectonics-s2.5.1',H,'South American, African plates','high')]),
'2.4':(1,[(P+'2.2',H,'volcanic island on ridge','low')]),'2.5':(1,[]),'2.6':(1,[]),
'2.7':(2,[(P+'2.0',E,'rift valley on ridge','high'),(P+'1.0',H,'convection currents','high')]),
'3.b':(1,[]),'3.0':(1,[]),'3.1':(1,[(P+'3.0',H,'rift valley','high')]),
'3.2':(1,[('geo-plate-tectonics-s2.5.2',H,'Arabian plate','high')]),
'4.b':(1,[]),'4.0':(2,[(P+'2.b',H,'mid-ocean ridge','high')]),
'5.b':(1,[('geo-plate-tectonics-s1.1.5',H,'crust density','high')]),
'5.0':(1,[('geo-plate-tectonics-s1.1.5',E,'oceanic denser than continental','high')]),
'5.1':(1,[(P+'5.0',H,'oceanic plate forced down','high')]),
'5.2':(1,[(P+'5.1',H,'subducting plate','high')]),
'5.3':(1,[(P+'5.1',H,'subduction','low')]),
'6.b':(1,[(P+'5.0',H,'denser oceanic plate sinks','high')]),
'6.0':(1,[(P+'5.3',H,'ocean trench','high')]),
'6.1':(1,[(P+'5.1',H,'subducting plate','high')]),
'6.2':(1,[(P+'5.2',H,'melting of sinking plate','high')]),
'6.3':(2,[(P+'5.1',H,'subducting plate','high')]),
'6.4':(2,[('geo-plate-tectonics-s2.5.2',H,'Nazca plate','high')]),
'6.5':(2,[('geo-plate-tectonics-s2.5.2',H,'Juan de Fuca plate','high')]),
'6.6':(2,[(P+'6.0',H,'trench','high'),(P+'6.2',H,'melting and volcanoes','high'),(P+'6.3',H,'earthquake foci','high')]),
'7.b':(1,[(P+'5.1',H,'subduction','high')]),
'7.0':(1,[(P+'5.0',H,'denser crust sinks','high')]),
'7.1':(1,[(P+'5.3',H,'ocean trench','high')]),
'7.2':(2,[(P+'7.1',H,'island arc','high'),('geo-plate-tectonics-s2.5.2',H,'Philippine plate','high')]),
'7.3':(1,[(P+'7.1',H,'island arc','high')]),
'7.4':(1,[('geo-plate-tectonics-s2.5.2',H,'Philippine plate','low')]),
'8.b':(1,[('geo-plate-tectonics-s1.1.5',H,'continental crust light','high')]),
'8.0':(1,[('geo-plate-tectonics-s1.1.5',H,'continental crust light','high')]),
'8.1':(1,[(P+'6.2',H,'melting makes magma','high')]),
'8.2':(1,[]),
'8.3':(2,[('geo-plate-tectonics-s2.5.1',H,'Eurasian, Indo-Australian plates','high')]),
'8.4':(2,[('geo-plate-tectonics-s2.0.1',H,'Tethys Sea','high')]),
'8.5':(1,[('geo-plate-tectonics-s2.5.1',H,'African, Eurasian plates','high')]),
'9.b':(1,[]),'9.0':(1,[(P+'7.1',H,'island arcs','high')]),
'9.1':(2,[(P+'8.3',H,'Himalayan collision','high')]),
'9.2':(2,[]),
'9.3':(2,[(P+'5.1',H,'subduction','low')]),
'9.4':(1,[(P+'6.5',H,'Mount St Helens','high')]),
'10.b':(1,[(P+'0.2',H,'passive boundaries','high')]),
'10.0':(1,[]),'10.1':(1,[]),'10.2':(1,[]),
'10.3':(1,[(P+'10.b',H,'transform fault','high')]),
'10.4':(2,[(P+'10.3',H,'San Andreas Fault','high')]),
'10.5':(2,[(P+'10.b',H,'transform fault','high')]),
'10.6':(1,[(P+'10.b',H,'transform sliding','high')]),
'11.b':(1,[]),
'11.0':(1,[('geo-plate-tectonics-s2.3.5',H,'sea-floor recycling','high')]),
'11.1':(1,[('geo-plate-tectonics-s1.1.6',H,'oceanic crust age','high')]),
'11.2':(1,[('geo-plate-tectonics-s2.9.1',H,'Iapetus Ocean closing','high')]),
'12.b':(1,[]),
'12.0':(1,[(P+'0.0',H,'constructive boundary','high')]),
'12.1':(1,[(P+'0.1',H,'destructive boundary','high')]),
'12.2':(1,[(P+'0.2',H,'transform boundary','high')]),
'13.b':(1,[]),
'13.0':(1,[(P+'0.1',H,'destructive boundaries','high')]),
'13.1':(1,[(P+'13.0',E,'Ring of Fire','high')]),
'13.2':(1,[(P+'0.b',H,'boundary types','low')]),
'13.3':(1,[(P+'0.1',H,'convergent boundaries','high')]),
}
txt=open('packs/geo-plate-tectonics-s3.t1g1.txt').read()
ids=re.findall(r'^\[(\S+)\]',txt,re.M)
allids=set(ids)
tg=[i for i in ids if i.startswith(P)]
assert [P+k for k in d]==tg,(set(tg)^set(P+k for k in d))
out={};n=0;low=0;c2=0
for k,(c,l) in d.items():
    for t in l: assert t[0] in allids and t[0]!=P+k
    out[P+k]={'cost':c,'needs':[{'id':a,'strength':b,'why':w,'confidence':f} for a,b,w,f in l]}
    n+=len(l);low+=sum(1 for t in l if t[3]=='low');c2+=c==2
json.dump(out,open('point-links/geo-plate-tectonics-s3.t1g1.json','w'),indent=1)
print(len(out),n,c2,low)
