import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
E='geo-region-european-s2.'
C='geo-region-concept-s4.'
X='geo-economic-activities-s2.'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
# pkg1: id -> (cost, links)
p1={
'15.2':(1,[]),'15.3':(1,[]),
'15.4':(1,[L(E+'1.3','helpful','organised crime drains investment')]),
'15.5':(1,[]),
'16.b':(1,[L(E+'9.1','essential','Cassa state investment')]),
'16.0':(2,[L(E+'16.b','helpful','growth pole policy')]),
'16.1':(2,[L(E+'16.b','helpful','growth pole policy')]),
'16.2':(1,[L(E+'2.4','helpful','Bari-Brindisi-Taranto industrial triangle')]),
'16.3':(1,[L(E+'16.b','essential','state growth poles')]),
'17.b':(1,[]),'17.0':(2,[]),'17.1':(1,[]),'17.2':(1,[]),
'18.b':(1,[]),
'18.0':(1,[L(E+'16.0','essential','Taranto steelworks')]),
'18.1':(1,[]),'19.b':(1,[]),
'19.0':(2,[L(C+'6.1','essential','less-developed region 75% definition')]),
'19.1':(1,[]),'19.2':(1,[]),'19.3':(1,[]),
'19.4':(1,[L(E+'10.6','helpful','specialised produce, agri-food processing')]),
'20.b':(1,[]),
'20.0':(1,[L(E+'1.5','helpful','southern unemployment')]),
'20.1':(1,[L(E+'14.1','helpful','gas pipelines landing in Sicily')]),
'20.2':(1,[L(E+'15.2','helpful','small local market')]),
'20.3':(1,[L(E+'15.1','helpful','poor infrastructure')]),
'20.4':(1,[L(E+'16.b','essential','Cassa growth poles'),L(E+'19.1','helpful','ZES Unica')]),
'21.b':(1,[]),'21.0':(1,[]),'21.1':(2,[]),'21.2':(1,[]),'21.3':(1,[]),'21.4':(1,[]),
'22.b':(1,[]),'22.0':(1,[]),'22.1':(1,[]),
'22.2':(1,[L(E+'1.3','helpful','organised crime')]),
'22.3':(1,[L(E+'23.b','helpful','transport links problem')]),
'23.b':(1,[]),'23.0':(1,[]),'23.1':(1,[]),'23.2':(1,[]),'23.3':(1,[]),'23.4':(1,[]),'23.5':(1,[]),
'23.6':(1,[L(E+'23.4','helpful','Strait of Messina ferries')]),
'24.b':(1,[]),'24.0':(1,[]),
'24.1':(1,[L(E+'18.1','essential','lavoro nero defined')]),
'24.2':(1,[]),'25.b':(1,[]),
'25.0':(1,[L(E+'6.2','helpful','fertile volcanic soils')]),
'25.1':(1,[L(E+'4.b','helpful','mountainous relief')]),
'25.2':(1,[]),
'25.3':(1,[L(E+'6.2','helpful','fertile volcanic soils')]),
'25.4':(1,[]),'26.b':(1,[]),'26.0':(1,[]),'26.1':(1,[]),'26.2':(1,[]),
'27.b':(1,[]),'27.0':(1,[]),
'27.1':(1,[L(E+'27.0','helpful','fertility rate')]),
'27.2':(1,[]),'27.3':(1,[]),'27.4':(1,[]),
'28.b':(1,[]),'28.0':(1,[]),'28.1':(1,[]),'28.2':(1,[]),'28.3':(1,[]),'28.4':(1,[]),'28.5':(1,[]),
'29.b':(1,[]),'29.0':(1,[]),'29.1':(1,[]),
'30.b':(1,[]),'30.0':(1,[]),'30.1':(1,[]),'30.2':(1,[]),'30.3':(1,[]),
'30.4':(1,[L(E+'0.4','helpful','autonomous regions special statute')]),
'30.5':(1,[]),
'31.b':(1,[]),'31.0':(1,[]),'31.1':(1,[]),'31.2':(1,[]),'31.3':(1,[]),'31.4':(1,[]),
'31.5':(1,[L(E+'31.3','helpful','Camorra defined')]),
'31.6':(1,[]),
'32.b':(1,[]),'32.0':(1,[]),'32.1':(1,[]),'32.2':(1,[]),
'32.3':(1,[L(E+'6.2','helpful','fertile volcanic soils')]),
'32.4':(1,[]),
'33.b':(1,[]),
'33.0':(1,[L(E+'9.4','helpful','malaria in coastal lowlands','low')]),
'33.1':(1,[]),
'33.2':(1,[L(E+'33.1','helpful','Matera sassi evacuated')]),
'33.3':(1,[]),
}
p2={k:[] for k in p1}
def S(k,i,s,w,c='high'): p2[k].append(L(X+i,s,w,c))
S('15.2','3.0','helpful','market size')
S('15.3','4.0','helpful','capital as location factor')
S('15.5','2.0','helpful','raw materials factor')
S('19.0','4.6','helpful','EU funds regional development')
S('19.1','4.4','helpful','regional policy incentives')
S('20.b','2.b','helpful','location factor')
S('20.0','2.2','helpful','labour factor')
S('20.1','2.0','helpful','raw materials factor')
S('20.2','3.0','helpful','market factor')
S('20.3','1.7','helpful','infrastructure defined')
S('20.4','4.4','helpful','regional policy incentives')
S('22.3','3.7','helpful','motorways and rail links','low')
S('23.b','3.7','helpful','motorways and rail links','low')
S('23.3','3.1','helpful','ports as transport factor','low')
def pk(name):
    t=open(P+'packs/'+name+'.txt').read()
    tg=t.split('CANDIDATES')[0]
    return re.findall(r'^\[(\S+?)\]',tg,re.M), set(re.findall(r'^\[(\S+?)\]',t,re.M))
for name,fn in(('geo-region-european-s2.t2g1',lambda k:{"cost":p1[k][0],"needs":p1[k][1]}),('geo-region-european-s2.t2g2',lambda k:{"needs":p2[k]})):
    ids,allids=pk(name)
    out={}
    for i in ids:
        k=i.split('s2.',1)[1]
        out[i]=fn(k)
    assert len(out)==len(ids)==len(p1),(len(out),len(p1))
    for v in out.values():
        for n in v['needs']: assert n['id'] in allids,n
    json.dump(out,open(P+'point-links/'+name+'.json','w'),indent=1)
    nl=sum(len(v['needs']) for v in out.values())
    print(name,len(out),nl,sum(v.get('cost')==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
