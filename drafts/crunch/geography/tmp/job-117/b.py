import json
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
N=[(20,5),(21,5),(22,4),(23,4),(24,8),(25,7),(26,6),(27,5),(28,5),(29,7),(30,7),(31,5),(32,5),(33,6),(34,6),(35,5),(36,7),(37,7),(38,6),(39,7),(40,6),(41,6)]
C={20:"11111",21:"11111",22:"1111",23:"1111",24:"11111111",25:"1111111",26:"111111",27:"11111",28:"11111",29:"1111111",30:"1111111",31:"11111",32:"11211",33:"111111",34:"111111",35:"11111",36:"1111112",37:"1111112",38:"111111",39:"1111111",40:"112111",41:"111111"}
ids=[];cost={}
for g,n in N:
    assert len(C[g])==n
    for i in range(n):
        k=f"geo-region-ireland-s1.{g}."+("b" if i==0 else str(i-1))
        ids.append(k);cost[k]=int(C[g][i])
S='geo-region-ireland-s1.'
def L(i,s,w,c='high'):return {"id":i,"strength":s,"why":w,"confidence":c}
p1={
'20.1':[L(S+'16.2','helpful','M50 orbital motorway')],
'21.2':[L(S+'21.1','essential','uses corporation tax')],
'23.1':[L(S+'1.4','helpful','cumulative causation')],
'24.5':[L(S+'21.1','helpful','corporation tax advantage')],
'24.6':[L(S+'15.5','helpful','data centres use electricity')],
'30.0':[L(S+'29.0','helpful','radial roads and M50')],
'30.2':[L(S+'11.0','helpful','urban sprawl defined')],
'30.3':[L(S+'29.2','helpful','DART as public transport')],
'33.1':[L(S+'5.2','helpful','Wicklow upland relief')],
'33.3':[L(S+'5.0','helpful','lowland relief of Meath, Kildare')],
'36.0':[L(S+'8.0','helpful','River Liffey')],
'36.5':[L(S+'35.2','helpful','Wide Streets Commissioners'),L(S+'37.1','helpful','Wright Report'),L(S+'31.2','helpful','Docklands Development Authority')],
'37.4':[L(S+'31.0','helpful','IFSC')],
'38.0':[L(S+'11.0','helpful','urban sprawl defined')],
'41.1':[L(S+'41.0','essential','national Catholic and no-religion figures')],
}
p2={
'22.1':[L('geo-economic-activities-s2.3.4','helpful','air freight of light high-value goods')],
'22.2':[L('geo-economic-activities-s2.0.0','helpful','bulk-reducing food processing')],
'23.0':[L('geo-economic-activities-s2.6.0','helpful','agglomeration')],
'24.4':[L('geo-economic-activities-s2.17.1','helpful','branch plants vulnerable to HQ decisions')],
'24.5':[L('geo-economic-activities-s2.4.2','helpful','corporation tax rates')],
'24.6':[L('geo-economic-activities-s2.15.1','helpful','grid limits data centres')],
'36.4':[L('geo-economic-activities-s2.14.5','helpful','brewing is bulk-gaining')],
}
p3={
'30.0':[L('geo-urban-s5.0.2','helpful','radial roads converge on centre')],
'30.2':[L('geo-urban-s5.11.0','helpful','sprawl causes car dependence')],
'30.3':[L('geo-urban-s5.3.0','helpful','public transport as congestion response')],
'30.4':[L('geo-urban-s5.3.4','helpful','cycle lanes as response')],
'30.1':[L('geo-urban-s5.2.0','helpful','commuters by car cause congestion')],
'38.3':[L('geo-urban-s5.0.3','helpful','peak-time commuting')],
'38.0':[L('geo-urban-s5.12.0','helpful','Dublin sprawl')],
'37.2':[L('geo-urban-s5.16.0','helpful','Ballymun tower blocks')],
'29.1':[L('geo-urban-s5.2.3','helpful','Port Tunnel removes port traffic')],
'24.1':[L('geo-urban-s5.1.0','helpful','congestion raises business costs')],
'37.3':[L('geo-urban-s5.19.3','helpful','Temple Bar regeneration','low')],
}
def out(name,links,withcost):
    d={}
    for k in ids:
        s=k.replace(S,'')
        e={}
        if withcost:e['cost']=cost[k]
        e['needs']=links.get(s,[])
        d[k]=e
    json.dump(d,open(P+'point-links/'+name+'.json','w'),indent=1)
    print(name,len(d),sum(len(v['needs']) for v in d.values()),sum(v.get('cost',0)==2 for v in d.values()),sum(n['confidence']=='low' for v in d.values() for n in v['needs']))
out('geo-region-ireland-s1.t2g1',p1,True)
out('geo-region-ireland-s1.t2g2',p2,False)
out('geo-region-ireland-s1.t2g3',p3,False)
# check ids exist in packs
import re
for n in ('t2g1','t2g2','t2g3'):
    txt=open(P+f'packs/geo-region-ireland-s1.{n}.txt').read()
    pk=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    d=json.load(open(P+f'point-links/geo-region-ireland-s1.{n}.json'))
    assert all(i in pk for i in d)
    for v in d.values():
        for x in v['needs']: assert x['id'] in pk,(n,x['id'])
