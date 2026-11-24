import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
S='geo-rocks-weathering-s'
H,E='helpful','essential'
# id: (cost, [(target, strength, why, conf)])
d={
'7.0.b':(1,[]),
'7.0.0':(2,[('5.0.2',H,'friction, cohesion, roots resist gravity','high')]),
'7.0.1':(1,[('7.0.0',E,'reverses the three factors','high')]),
'7.0.2':(2,[('7.0.0',H,'vegetation removal','low')]),
'7.0.3':(1,[('5.0.0',H,'mass movement definition','high')]),
'7.1.b':(1,[]),
'7.1.0':(1,[]),
'7.1.1':(1,[]),
'7.1.2':(1,[('5.0.2',H,'cohesion resists downslope force','high')]),
'7.1.3':(2,[('5.2.b',H,'soil creep and terracettes','high')]),
'7.1.4':(1,[]),
'7.2.b':(1,[]),
'7.2.0':(2,[('7.1.b',H,'overgrazing','high')]),
'7.2.1':(1,[('7.1.0',H,'overgrazing strips vegetation','high')]),
'7.2.2':(1,[('7.2.0',E,'headage payments being replaced','high')]),
'7.2.3':(1,[('7.1.0',H,'carrying capacity, stocking rate','low')]),
'7.2.4':(1,[]),
'7.3.b':(1,[('7.1.0',H,'overgrazing causes','low')]),
'7.3.0':(1,[('7.1.0',E,'carrying capacity','high')]),
'7.3.1':(1,[('7.1.0',H,'animals staying too long','low')]),
'7.3.2':(1,[('5.9.0',H,'roots bind soil','high')]),
'7.4.b':(1,[]),
'7.4.0':(1,[]),
'7.4.1':(1,[]),
'7.4.2':(1,[]),
'7.4.3':(1,[]),
'7.5.b':(1,[]),
'7.5.0':(1,[]),
'7.5.1':(1,[('7.5.0',E,'ploughed grassland','high')]),
'7.5.2':(1,[('7.5.1',H,'soil loss effects','high')]),
'7.5.3':(2,[('7.5.1',H,'wind erosion problem','low')]),
'7.6.b':(1,[]),
'7.6.0':(1,[]),
'7.6.1':(1,[('7.1.0',H,'overgrazing','high')]),
'7.6.2':(1,[('7.4.0',H,'fallow, overcropping','high')]),
'7.6.3':(2,[('7.6.1',H,'bare soil from grazing','high')]),
'7.7.b':(1,[]),
'7.7.0':(1,[('7.4.0',H,'fallow, nutrient depletion','high')]),
'7.7.1':(1,[('7.4.3',E,'furrows channel water downhill','high')]),
'7.7.2':(2,[]),
'7.7.3':(1,[]),
'7.7.4':(1,[('7.7.2',H,'terracing','high')]),
'7.8.b':(1,[]),
'7.8.0':(1,[]),
'7.8.1':(2,[('5.9.0',H,'roots bind soil','high')]),
'7.8.2':(1,[('7.8.1',E,'tree functions lost','high')]),
'7.8.3':(1,[('5.6.0',H,'mudflow','high')]),
'7.9.b':(1,[]),
'7.9.0':(1,[]),
'7.9.1':(2,[('7.9.0',E,'Haiti deforestation','high')]),
'7.9.2':(2,[('7.8.3',H,'deforestation worsens landslides','high')]),
'7.9.3':(1,[('7.9.2',E,'Hurricane Mitch','high')]),
'7.10.b':(1,[]),
'7.10.0':(1,[]),
'7.10.1':(1,[('7.10.0',H,'1900 forest cover comparison','high')]),
'7.10.2':(2,[('5.7.b',H,'peat slides','high')]),
'7.11.b':(1,[]),
'7.11.0':(1,[('7.8.1',H,'roots bind soil','high')]),
'7.11.1':(1,[('7.8.1',H,'roots hold soil','low')]),
'7.11.2':(1,[('7.10.2',E,'clear-felling','high')]),
'7.12.b':(1,[('5.7.b',H,'peat slides on bogs','high')]),
'7.12.0':(1,[('5.7.0',H,'blanket bog','high')]),
'7.12.1':(2,[('7.12.0',H,'construction on blanket bog','high')]),
'7.12.2':(2,[('7.12.1',E,'Derrybrien slide','high')]),
'7.12.3':(2,[('7.12.1',H,'similar wind farm peat slide','low')]),
'7.13.b':(1,[('5.0.2',H,'downslope force versus resistance','high')]),
'7.13.0':(1,[('5.9.2',H,'removing support at base','high')]),
'7.13.1':(1,[('5.9.3',E,'loading','high')]),
'7.13.2':(1,[('5.8.1',H,'water adds weight, reduces friction','high')]),
'7.13.3':(1,[('5.12.1',E,'Vajont case','high')]),
'7.13.4':(1,[('5.9.3',H,'spoil loading','low')]),
'7.14.b':(1,[]),
'7.14.0':(1,[]),
'7.14.1':(1,[('5.8.0',H,'slope angle','high')]),
'7.14.2':(1,[('7.12.2',H,'environmental impact assessment','low')]),
'7.14.3':(1,[]),
}
txt=open(P+'packs/geo-rocks-weathering-s7.t1g1.txt').read()
tg=re.findall(r'^\[(geo-rocks-weathering-s7\.[^\]]+)\]',txt,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
assert [S+k for k in d]==tg,(set(tg)^set(S+k for k in d))
out={};n=l=c2=lo=0
for k,(c,ns) in d.items():
    out[S+k]={'cost':c,'needs':[{'id':S+t,'strength':s,'why':w,'confidence':f} for t,s,w,f in ns]}
    assert all(S+t in allids and S+t!=S+k for t,*_ in ns)
    n+=1;l+=len(ns);c2+=c==2;lo+=sum(f=='low' for *_,f in ns)
json.dump(out,open(P+'point-links/geo-rocks-weathering-s7.t1g1.json','w'),indent=1)
json.load(open(P+'point-links/geo-rocks-weathering-s7.t1g1.json'))
print(n,l,c2,lo)
