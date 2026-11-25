import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
U='geo-urban-s2.'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
# id: (cost, links)
d={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),'0.2':(1,[]),'0.3':(1,[]),'0.4':(1,[]),
'1.b':(1,[]),'1.0':(1,[]),'1.1':(2,[]),'1.2':(1,[L(U+'1.1','helpful','Land Acts and holdings')]),'1.3':(1,[]),'1.4':(1,[]),
'2.b':(1,[]),'2.0':(1,[]),'2.1':(1,[L('geo-urban-s1.0.0','helpful','bridging point as a site')]),'2.2':(1,[]),'2.3':(1,[]),
'2.4':(1,[L('geo-urban-s1.0.0','helpful','wet point as a site')]),'2.5':(1,[L('geo-urban-s1.0.0','helpful','dry point as a site')]),
'2.6':(1,[]),'2.7':(1,[]),'2.8':(2,[L(U+'2.2','helpful','estates as a settlement focus')]),
'3.b':(1,[]),'3.0':(1,[L(U+'0.1','helpful','clustered settlement pattern')]),
'3.1':(2,[L(U+'3.0','helpful','clachan it explains')]),
'3.2':(1,[L(U+'3.0','essential','what a clachan is')]),
'3.3':(1,[L(U+'3.2','helpful','clachan districts of the west')]),
'3.4':(2,[L(U+'3.0','essential','clachans being broken up'),L(U+'1.1','helpful','consolidation of holdings')]),
'3.5':(1,[L(U+'1.1','essential','Land Commission and consolidation'),L(U+'0.0','helpful','dispersed settlement')]),
'3.6':(1,[L(U+'3.0','essential','what a clachan is')]),
'4.b':(1,[]),'4.0':(2,[L(U+'0.2','essential','linear settlement pattern')]),
'4.1':(1,[L(U+'0.2','helpful','linear settlement pattern')]),
'5.b':(1,[L('geo-mapwork-s1.25.b','helpful','map evidence for absence of settlement')]),
'5.0':(1,[]),'5.1':(1,[]),'5.2':(1,[]),'5.3':(1,[]),'5.4':(1,[]),
'6.b':(1,[]),'6.0':(2,[]),'6.1':(2,[L(U+'0.1','helpful','clustered pattern'),L(U+'0.0','helpful','dispersed pattern')]),
'7.b':(1,[L(U+'0.2','essential','linear (ribbon) pattern'),L('geo-mapwork-s1.24.4','helpful','ribbon development on approach roads','low')]),
'7.0':(1,[]),'7.1':(1,[]),'7.2':(1,[]),'7.3':(1,[]),'7.4':(1,[]),
'7.5':(1,[L(U+'10.b','helpful','planning control by the State','low')]),'7.6':(1,[]),
'8.b':(1,[L(U+'7.b','essential','ribbon housing')]),
'8.0':(1,[]),'8.1':(1,[]),'8.2':(1,[]),'8.3':(1,[]),'8.4':(1,[]),'8.5':(1,[]),'8.6':(1,[]),
'9.b':(1,[]),'9.0':(1,[]),'9.1':(1,[]),'9.2':(1,[]),
'10.b':(1,[]),'10.0':(1,[]),'10.1':(2,[L(U+'10.0','helpful','planning permission decisions')]),
'10.2':(1,[]),'10.3':(2,[L(U+'10.2','essential','County Development Plan')]),
'10.4':(1,[L(U+'10.3','helpful','County Development Plan')]),
'11.b':(1,[]),'11.0':(2,[]),'11.1':(1,[]),
'11.2':(1,[L(U+'11.1','helpful','Rural Housing Guidelines area types','low')]),
'11.3':(1,[L(U+'11.1','helpful','Rural Housing Guidelines area types','low')]),
'12.b':(1,[]),'12.0':(1,[]),'12.1':(1,[L(U+'8.0','helpful','entrances as traffic hazard')]),
'12.2':(1,[]),'12.3':(1,[]),'12.4':(1,[L(U+'8.2','helpful','septic tank pollution')]),
'12.5':(1,[]),'12.6':(1,[L(U+'10.3','helpful','zoning')]),
'13.b':(1,[L(U+'8.2','helpful','septic tank pollution')]),'13.0':(1,[]),'13.1':(1,[]),
'14.b':(1,[]),'14.0':(1,[]),'14.1':(1,[]),'14.2':(1,[]),'14.3':(1,[]),
'15.b':(1,[]),'15.0':(2,[L(U+'9.0','helpful','communities kept alive by housing'),L(U+'7.b','helpful','ribbon sprawl','low')]),
'15.1':(2,[L(U+'12.0','essential','local-needs criteria')]),
'15.2':(1,[L(U+'7.b','essential','ribbon development')]),
'15.3':(1,[L(U+'12.2','essential','housing directed into villages')]),
}
g1={U+k:{"cost":c,"needs":l} for k,(c,l) in d.items()}
g2={U+k:{"needs":[]} for k in d}
g2[U+'3.4']['needs']=[L('geo-region-ireland-s2.9.1','helpful','Congested Districts Board work','low')]
g2[U+'14.b']['needs']=[L('geo-region-ireland-s2.37.2','helpful','rural depopulation and service decline','low')]
for name,g in(('geo-urban-s2.t1g1',g1),('geo-urban-s2.t1g2',g2)):
    txt=open(P+'packs/%s.txt'%name).read()
    ids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    tg=[i for i in re.findall(r'^\[([^\]]+)\]',txt.split('CANDIDATES')[0],re.M)]
    assert tg==list(g),(set(tg)^set(g))
    for v in g.values():
        for n in v['needs']: assert n['id'] in ids,n
    json.dump(g,open(P+'point-links/%s.json'%name,'w'),indent=1)
    print(name,len(g),sum(len(v['needs']) for v in g.values()),sum(v.get('cost',0)==2 for v in g.values()),sum(n['confidence']=='low' for v in g.values() for n in v['needs']))
