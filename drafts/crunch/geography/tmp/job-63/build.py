import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
C={}
spec="""0:b1 0 1 1 1|1:b1 0 2 1|2:b1 0 1 2 2|3:b1 0 1 2 1|4:b1 0 1 2 1 1 1|5:b1 0 1 1 2|6:b1 0 1 1 2|7:b1 0 2 1 1 1|8:b1 0 1 2 1|9:b1 0 1 1 1 1|10:b1 0 2 2 1 1 1 2 1|11:b1 0 1 1 2 2 2 1 2|12:b1 0 1 1 1|13:b1 0 1 1 1 2 2 1|14:b1 0 1 1 1 1|15:b1 0 1 2|16:b1 0 1 1|17:b1 0 1 2 1 1 1|18:b1 0 1 1 1 2|19:b1 0 2 1 1|20:b1 0 1 1 1|21:b1 0 1 2 1 1 1 1 1|22:b1 0 1 2 1 1 2 1|23:b1 0 2 1 1 1|24:b1 0 1 2 2 1 1|25:b1 0 2 1 1|26:b1 0 1 1 1|27:b1 0 1 1 2|28:b1 0 2 1|29:b1 0 2 1"""
# format per block: "b<costb> then costs of bullets 0..n"; first token after colon is b+cost, rest are bullet costs (first '0' is a placeholder removed)
ids=[];cost={}
for blk in spec.split('|'):
    n,rest=blk.split(':');t=rest.split()
    ids.append(f"geo-option-geoecology-s5.{n}.b");cost[ids[-1]]=int(t[0][1:])
    for i,c in enumerate(t[2:]):
        ids.append(f"geo-option-geoecology-s5.{n}.{i}");cost[ids[-1]]=int(c)
def L(t,s,w,c='high'):return {"id":t,"strength":{'E':'essential','H':'helpful'}[s],"why":w,"confidence":c}
p='geo-option-geoecology-'
l1={'1.1':[L(p+'s4.0.3','H','biome belts','low')],
'8.b':[L(p+'s4.17.1','H','Amazon Basin location')],
'11.0':[L(p+'s4.24.b','H','high rainforest species diversity')],
'11.2':[L(p+'s4.20.3','E','closed rapid nutrient cycle')],
'11.3':[L(p+'s4.20.0','H','laterised latosol soils')],
'11.4':[L(p+'s4.19.6','H','forest recycles rain by evapotranspiration')],
'14.b':[L(p+'s4.17.3','H','South-East Asia rainforest location')],
'14.3':[L(p+'s4.25.3','H','orangutan found in Borneo/Sumatra canopy','low')],
'25.0':[L(p+'s4.0.3','H','boreal forest biome','low')]}
l2={'7.1':[L(p+'s3.14.0','H','deforestation exposes soil to erosion')],
'7.3':[L(p+'s3.24.1','H','Iceland birch loss after settlement')],
'11.3':[L(p+'s3.14.0','H','soil erosion after deforestation')],
'18.0':[L(p+'s3.14.2','H','fertiliser causes nitrate runoff')],
'18.1':[L(p+'s3.14.2','H','eutrophication from fertiliser')],
'18.3':[L(p+'s3.20.1','H','Nitrates Directive rules'),L(p+'s3.20.0','H','REPS, GLAS, ACRES schemes')],
'19.2':[L(p+'s3.20.0','H','agri-environment payment schemes','low')],
'20.1':[L(p+'s3.2.2','H','Dust Bowl drought and wind erosion')],
'21.5':[L(p+'s3.14.3','H','salinisation and waterlogging from irrigation')],
'22.b':[L(p+'s2.4.0'.replace(p,'geo-'),'H','acid rain definition')] ,
'22.0':[{"id":"geo-economic-environment-s2.4.1","strength":"helpful","why":"SO2 and NOx form acids","confidence":"high"}],
'22.1':[{"id":"geo-economic-environment-s2.4.b","strength":"helpful","why":"transboundary pollution","confidence":"high"}],
'23.1':[{"id":"geo-economic-environment-s2.2.1","strength":"helpful","why":"SO2 causes acid rain","confidence":"low"}],
'23.3':[{"id":"geo-economic-environment-s2.6.2","strength":"helpful","why":"scrubbers remove SO2","confidence":"high"}],
'28.0':[{"id":"geo-economic-environment-s2.3.0","strength":"helpful","why":"greenhouse effect and warming","confidence":"high"}],
'28.1':[L(p+'s3.14.5','H','sprawl seals soil')],
'29.0':[L(p+'s3.23.3','H','results-based payments on Burren')]}
l2['22.b']=[{"id":"geo-economic-environment-s2.4.0","strength":"helpful","why":"acid rain definition","confidence":"high"}]
l3={'7.1':[{"id":"geo-rocks-weathering-s7.8.1","strength":"helpful","why":"tree roots bind soil","confidence":"high"}],
'11.3':[{"id":"geo-rocks-weathering-s7.8.3","strength":"helpful","why":"sediment reaches rivers","confidence":"low"}],
'23.2':[{"id":"geo-economic-environment-s1.6.1","strength":"helpful","why":"Moneypoint power station","confidence":"high"}]}
def out(name,links,withcost):
    txt=open(P+'packs/'+name+'.txt').read()
    pk=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    tg=[i for i in ids]
    assert all(i in pk for i in tg) and len(pk&set(tg))==len(tg)
    d={}
    for i in tg:
        k=i.replace(p+'s5.','')
        e={}
        if withcost:e['cost']=cost[i]
        e['needs']=links.get(k,[])
        for n in e['needs']:assert n['id'] in pk and n['id']!=i,(i,n)
        d[i]=e
    json.dump(d,open(P+'point-links/'+name+'.json','w'),ensure_ascii=False)
    d=json.load(open(P+'point-links/'+name+'.json'))
    nl=sum(len(v['needs']) for v in d.values());lo=sum(n['confidence']=='low' for v in d.values() for n in v['needs'])
    print(name,len(d),nl,sum(v.get('cost')==2 for v in d.values()) if withcost else '-',lo)
out('geo-option-geoecology-s5.t1g1',l1,True)
out('geo-option-geoecology-s5.t1g2',l2,False)
out('geo-option-geoecology-s5.t1g3',l3,False)
