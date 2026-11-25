import json,re
P='geo-plate-tectonics-s1.'
def L(i,s,w,c='high'): return {"id":P+i,"strength":s,"why":w,"confidence":c}
E,H='essential','helpful'
d={
"0.b":(1,[]),
"0.0":(1,[]),
"0.1":(1,[L("0.0",H,"uses the layers of the earth")]),
"0.2":(1,[L("0.1",E,"density and temperature increase inward")]),
"0.3":(1,[]),
"0.4":(2,[L("0.0",E,"the layers to label"),L("2.1",E,"Moho boundary"),L("2.3",E,"Gutenberg boundary")]),
"1.b":(1,[]),
"1.0":(1,[]),
"1.1":(1,[]),
"1.2":(2,[]),
"1.3":(1,[]),
"1.4":(2,[]),
"1.5":(1,[L("1.0",E,"continental crust thickness"),L("1.3",E,"oceanic crust thickness and density"),L("1.1",H,"continental density 2.7")]),
"1.6":(2,[L("1.3",H,"oceanic crust","low")]),
"2.b":(1,[]),
"2.0":(1,[]),
"2.1":(1,[L("2.0",E,"discontinuity defined"),L("7.0","helpful".replace("helpful",H),"earthquake waves reveal boundaries","low")]),
"2.2":(2,[L("2.1",E,"the Moho")]),
"2.3":(1,[L("2.0",E,"discontinuity defined")]),
"3.b":(1,[]),
"3.0":(1,[]),
"3.1":(1,[L("3.2",H,"asthenosphere"),L("3.4",H,"lithosphere")]),
"3.2":(2,[L("3.4",H,"lies beneath the lithosphere")]),
"3.3":(1,[]),
"3.4":(2,[L("0.0",H,"crust and mantle layers")]),
"3.5":(2,[L("3.4",E,"lithosphere"),L("3.2",E,"plastic asthenosphere")]),
"4.b":(1,[]),
"4.0":(1,[]),
"4.1":(2,[L("0.0",H,"outer core layer")]),
"4.2":(2,[L("0.0",H,"inner core layer")]),
"4.3":(2,[L("4.2",E,"inner core is solid and hot")]),
"5.b":(1,[]),
"5.0":(1,[]),
"5.1":(2,[L("3.2",H,"semi-molten rock in mantle")]),
"5.2":(1,[L("5.1",E,"convection currents"),L("0.1",H,"density and heat")]),
"5.3":(1,[L("5.1",E,"convection currents")]),
"5.4":(1,[L("5.1",E,"convection currents")]),
"6.b":(1,[]),
"6.0":(1,[L("5.0",H,"internal heat","low")]),
"6.1":(2,[L("6.0",E,"endogenic forces")]),
"6.2":(1,[L("6.0",H,"contrasts with endogenic forces")]),
"7.b":(1,[]),
"7.0":(2,[L("2.0",E,"discontinuities found")]),
"7.1":(1,[L("4.1",H,"outer core is liquid","low")]),
"7.2":(1,[]),
"7.3":(2,[L("7.2",E,"S-waves stopped by liquid"),L("4.1",H,"outer core liquid")]),
"7.4":(2,[L("7.3",E,"S-waves blocked by outer core")]),
}
out={P+k:{"cost":c,"needs":n} for k,(c,n) in d.items()}
txt=open('packs/geo-plate-tectonics-s1.t1g1.txt').read()
ids=re.findall(r'^\[([^\]]+)\]',txt,re.M)
assert list(out)==ids,(set(ids)^set(out))
for v in out.values():
    for n in v['needs']: assert n['id'] in ids
json.dump(out,open('point-links/geo-plate-tectonics-s1.t1g1.json','w'),indent=1)
json.load(open('point-links/geo-plate-tectonics-s1.t1g1.json'))
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
