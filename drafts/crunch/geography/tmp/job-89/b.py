import json,re
P='geo-region-concept-s1.'
R='geo-rocks-weathering-s4.'; V='geo-volcanoes-earthquakes-s5.'
H,E='helpful','essential'
def n(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
d={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),'0.2':(1,[]),'0.3':(1,[]),'0.4':(1,[]),'0.5':(1,[]),
'1.b':(1,[]),'1.0':(1,[]),'1.1':(1,[]),'1.2':(1,[]),'1.3':(1,[]),'1.4':(1,[]),'1.5':(1,[]),
'2.b':(1,[]),'2.0':(1,[]),'2.1':(1,[]),'2.2':(1,[]),'2.3':(1,[]),
'3.b':(1,[]),'3.0':(1,[]),'3.1':(1,[]),'3.2':(1,[]),'3.3':(1,[]),'3.4':(1,[]),
'4.b':(1,[]),'4.0':(1,[]),'4.1':(1,[]),'4.2':(1,[]),'4.3':(1,[]),'4.4':(1,[]),'4.5':(1,[]),
'5.b':(1,[]),
'5.0':(2,[n(P+'4.3',H,'winds bring Atlantic rain')]),
'5.1':(1,[n(P+'4.5',H,'relief rainfall over mountains')]),
'5.2':(1,[n(P+'4.5',H,'forced uplift on western slopes','low')]),
'5.3':(1,[]),'5.4':(1,[]),'5.5':(1,[]),
'6.b':(1,[]),'6.0':(2,[]),
'6.1':(1,[n(P+'4.1',H,'North Atlantic Drift')]),
'6.2':(2,[n(P+'4.2',H,'maritime influence on range')]),
'6.3':(1,[n(P+'1.3',H,'transition zones')]),
'7.b':(1,[]),'7.0':(1,[]),'7.1':(1,[]),'7.2':(1,[]),
'8.b':(1,[]),'8.0':(1,[]),
'9.b':(1,[n(R+'0.b',H,'karst on limestone')]),
'9.0':(1,[]),
'9.1':(1,[n(R+'1.b',H,'limestone pavement formation')]),
'9.2':(1,[n(R+'4.0',H,'turlough seasonal lake')]),
'9.3':(2,[n(R+'5.0',H,'caves in limestone')]),
'9.4':(1,[n(R+'1.4',H,'folded terraced limestone hill')]),
'9.5':(1,[n(R+'0.2',H,'limestone permeable via cracks')]),
'9.6':(2,[n(R+'1.0',H,'ice removed soil exposing rock')]),
'10.b':(1,[]),'10.0':(1,[]),'10.1':(1,[]),'10.2':(1,[]),'10.3':(1,[]),'10.4':(1,[]),
'11.b':(1,[]),
'11.0':(1,[n(V+'1.1',H,'anticlines and synclines')]),
'11.1':(1,[n(V+'5.b',H,'differential erosion')]),
'11.2':(2,[n(P+'11.1',H,'ridges are resistant sandstone')]),
'11.3':(1,[n(P+'11.1',H,'valleys are weak limestone')]),
'11.4':(2,[n(V+'6.1',H,'trellised drainage pattern')]),
'11.5':(1,[n(V+'7.4',H,'drowned valleys form rias')]),
'11.6':(1,[n(P+'11.3',H,'valleys versus ridges')]),
'12.b':(1,[]),'12.0':(1,[]),'12.1':(1,[]),'12.2':(1,[]),
'12.3':(1,[n(P+'12.2',E,'uses loess soils')]),
'12.4':(2,[]),'12.5':(1,[]),'12.6':(2,[]),
'13.b':(1,[]),
'13.0':(1,[n(P+'9.b',H,'Burren limestone karst')]),
'13.1':(1,[n(P+'11.b',H,'folded ridges and valleys')]),
'13.2':(1,[n(P+'12.1',H,'glacial deposits')]),
'13.3':(1,[n(R+'10.3',H,'Leinster batholith granite')]),
}
txt=open('packs/geo-region-concept-s1.t1g1.txt').read()
tg=re.findall(r'^\[(geo-region-concept-s1\.[^\]]+)\]',txt,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
assert sorted(tg)==sorted(P+k for k in d),(set(tg)^set(P+k for k in d))
out={t:{"cost":d[t[len(P):]][0],"needs":d[t[len(P):]][1]} for t in tg}
for v in out.values():
  for x in v['needs']: assert x['id'] in allids,x
json.dump(out,open('point-links/geo-region-concept-s1.t1g1.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
