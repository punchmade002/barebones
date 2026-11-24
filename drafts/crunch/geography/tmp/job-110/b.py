import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
C2={'0.1','2.2','4.2','6.0','6.6','9.2','12.0','13.1','20.2','20.3','21.3','30.3','30.4','31.2','33.1'}
# explicit per-section suffix lists (every target id)
S={0:'b 0 1 2 3',1:'b 0 1 2 3 4 5',2:'b 0 1 2 3 4 5 6',3:'b 0 1 2 3',4:'b 0 1 2 3 4',5:'b 0 1 2 3 4',
6:'b 0 1 2 3 4 5 6 7',7:'b 0 1 2 3 4',8:'b 0 1 2 3',9:'b 0 1 2 3 4',10:'b 0 1 2 3',11:'b 0 1 2 3 4',
12:'b 0 1 2',13:'b 0 1 2 3',14:'b 0 1 2 3',15:'b 0 1',16:'b 0 1 2 3',17:'b 0 1 2',18:'b 0 1 2 3',19:'b 0 1 2',
20:'b 0 1 2 3 4',21:'b 0 1 2 3 4 5',22:'b 0 1 2',23:'b 0 1 2 3 4 5 6',24:'b 0 1 2 3 4 5 6',25:'b 0 1 2 3',
26:'b 0 1 2',27:'b 0 1 2 3',28:'b 0 1 2 3 4 5',29:'b 0 1 2 3 4 5 6',30:'b 0 1 2 3 4 5',31:'b 0 1 2 3 4',
32:'b 0 1 2 3',33:'b 0 1 2 3',34:'b 0 1 2 3 4'}
ids=[f'{s}.{x}' for s,v in S.items() for x in v.split()]
txt=open(P+'packs/geo-region-european-s1.t1g1.txt').read()
tg=re.findall(r'^\[(geo-region-european-s1\.[^\]]+)\]',txt,re.M)
assert tg==['geo-region-european-s1.'+i for i in ids],(len(tg),len(ids))
def L(i,s,w,c='high'): return (i,{"id":i if False else None})
def mk(src,strength,why,conf='high'): return {"id":src,"strength":strength,"why":why,"confidence":conf}
E='geo-region-european-s1.';CO='geo-region-concept-s4.';V='geo-volcanoes-earthquakes-s4.'
G='geo-economic-activities-s2.';U='geo-urban-s4.';A='geo-region-concept-s2.'
l1={'1.b':[mk(CO+'1.b','helpful','what a core region is')],
'1.5':[mk(CO+'0.3','helpful','cumulative causation')],
'4.0':[mk(V+'2.0','helpful','dip of strata')],
'4.2':[mk(V+'12.b','helpful','escarpment and dip slope')],
'4.3':[mk(V+'12.3','helpful','vale between cuestas')],
'4.4':[mk(V+'12.b','helpful','how cuestas form','low')],
'5.3':[mk(E+'5.2','helpful','dry chalk plain')],
'5.4':[mk(E+'4.3','helpful','clay vales','low')],
'6.5':[mk(V+'5.0','helpful','permeable rock')],
'7.1':[mk(E+'4.1','helpful','low relief')],
'7.2':[mk(E+'5.1','helpful','limon fertility')],
'9.1':[mk(E+'5.2','helpful','thin chalk soils')],
'9.4':[mk(E+'9.2','helpful','protected AOC name')],
'10.0':[mk(E+'5.4','helpful','wet clay suits grass')],
'20.4':[mk(E+'20.0','helpful','decentralisation steering industry')],
'21.5':[mk(CO+'0.3','helpful','cumulative causation')],
'22.2':[mk(CO+'0.1','helpful','primary and tertiary activity')],
'29.1':[mk(E+'6.1','helpful','tributaries of the Seine')],
'29.2':[mk(E+'24.0','helpful','radial transport network')],
'29.4':[mk(E+'5.1','helpful','limon fertility')],
'29.6':[mk(E+'30.0','helpful','Haussmann rebuilding')],
'32.0':[mk(E+'11.1','helpful','mechanisation cuts workers')],
'2.2':[mk(E+'2.0','helpful','Seine drawn earlier','low')],
'2.4':[mk(E+'0.1','helpful','edging uplands')]}
l2={'14.0':[mk(G+'3.0','helpful','market location factor')],
'14.1':[mk(G+'2.2','helpful','labour location factor')],
'14.2':[mk(G+'4.0','helpful','capital as location factor','low')],
'14.3':[mk(G+'1.2','helpful','research and development')],
'15.1':[mk(G+'0.0','essential','bulk-reducing processing near source')],
'16.b':[mk(G+'1.7','helpful','infrastructure')],
'16.1':[mk(G+'3.6','helpful','freight modes')],
'16.2':[mk(G+'3.6','helpful','water suits bulk goods')],
'19.0':[mk(G+'1.5','helpful','cluster')],
'20.0':[mk(G+'4.4','helpful','regional policy steers firms','low')],
'21.5':[mk(G+'6.0','helpful','agglomeration')]}
l3={'0.2':[mk(A+'9.0','helpful','French regions as administrative units')],
'0.3':[mk(A+'9.1','helpful','2016 regional merger')],
'17.2':[mk(U+'8.1','helpful','industry moving to suburbs')],
'20.3':[mk(U+'17.1','helpful','new towns')],
'21.2':[mk(U+'0.0','helpful','CBD')],
'28.0':[mk(A+'10.0','helpful','centralised France','low')],
'30.4':[mk(A+'9.0','helpful','communes as local units')],
'31.2':[mk(U+'13.b','helpful','social segregation'),mk(A+'8.2','helpful','what a département is','low')],
'31.4':[mk(U+'15.b','helpful','urban sprawl on rural fringe')],
'32.2':[mk(U+'15.3','helpful','commuter villages','low')]}
def fix(d):
    return {E+k:v for k,v in d.items()}
def pk(name):
    return open(P+'packs/'+name+'.txt').read()
def check(name,out,cost):
    t=pk(name);have=set(re.findall(r'^\[([^\]]+)\]',t,re.M))
    assert list(out)==[E+i for i in ids]
    for k,v in out.items():
        assert ('cost' in v)==cost
        for n in v['needs']: assert n['id'] in have and n['id']!=k,(k,n)
def w(name,out,cost):
    check(name,out,cost); json.dump(out,open(P+'point-links/'+name+'.json','w'),indent=1,ensure_ascii=False)
    nl=sum(len(v['needs']) for v in out.values()); lo=sum(n['confidence']=='low' for v in out.values() for n in v['needs'])
    print(name,len(out),nl,sum(v.get('cost')==2 for v in out.values()),lo)
a,b,c=fix(l1),fix(l2),fix(l3)
w('geo-region-european-s1.t1g1',{E+i:{"cost":2 if i in C2 else 1,"needs":a.get(E+i,[])} for i in ids},True)
w('geo-region-european-s1.t1g2',{E+i:{"needs":b.get(E+i,[])} for i in ids},False)
w('geo-region-european-s1.t1g3',{E+i:{"needs":c.get(E+i,[])} for i in ids},False)
