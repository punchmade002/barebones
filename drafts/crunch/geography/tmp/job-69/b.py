import json,re,sys
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
S='geo-option-global-interdependence-s2.'
def L(i,s,w,c): return {"id":i,"strength":s,"why":w,"confidence":c}
ids=[]
for n,subs in [(22,[2,3,4,5]),(23,['b',0,1,2,3]),(24,['b',0,1,2,3,4]),(25,['b',0,1,2,3,4,5,6]),(26,['b',0,1,2,3]),(27,['b',0,1,2,3,4,5,6]),(28,['b',0,1,2,3,4,5,6]),(29,['b',0,1,2]),(30,['b',0,1,2,3,4,5,6,7]),(31,['b',0,1,2,3,4,5,6]),(32,['b',0,1,2,3,4]),(33,['b',0,1,2,3,4,5]),(34,['b',0,1,2,3]),(35,['b',0,1,2,3,4,5,6]),(36,['b',0,1,2,3,4,5]),(37,['b',0,1,2,3]),(38,['b',0,1,2,3]),(39,['b',0,1,2,3,4,5,6]),(40,['b',0,1,2,3,4]),(41,['b',0,1,2,3]),(42,['b',0,1])]:
    for s in subs: ids.append(f'{S}{n}.{s}')
M='geo-population-migration-s4.';D='geo-economic-development-s4.'
a={
 '28.6':[L(M+'0.2','helpful','uses economic migrant definition','low')],
 '30.4':[L(M+'0.4','helpful','uses asylum seeker term','low')],
 '32.1':[L(M+'0.4','helpful','asylum decision wait','low')],
 '33.2':[L(M+'6.b','helpful','direct provision system','low')],
 '33.4':[L(M+'9.3','helpful','anti-immigration protests','low')],
 '36.3':[L(M+'12.3','helpful','labour shortages and ageing','low')],
 '36.4':[L(M+'16.4','helpful','anti-immigration party rise','high')],
 '36.5':[L(M+'15.3','helpful','Pact main ideas','low')],
 '38.0':[L(D+'0.0','helpful','Universal Declaration of Human Rights','high')],
 '38.1':[L(M+'0.5','helpful','1951 Refugee Convention','high')],
 '39.6':[L(D+'19.3','helpful','cobalt mining child labour','high')],
 '41.1':[L(M+'6.2','helpful','direct provision criticisms','high')],
 '42.1':[L(M+'0.6','helpful','UNHCR role','low'),L(M+'0.5','helpful','Refugee Convention','low')],
}
b={'39.b':[L('geo-economic-globalisation-s2.1.0','helpful','labour costs drive sourcing','low')]}
def out(name,links,pack):
    t=open(P+'packs/'+name+'.txt').read()
    pk=set(re.findall(r'^\[([^\]]+)\]',t,re.M))
    d={i:{"needs":links.get(i[len(S):],[])} for i in ids}
    for v in d.values():
        for l in v['needs']: assert l['id'] in pk,l
    tg=re.findall(r'^\[([^\]]+)\]',t.split('CANDIDATES')[0],re.M)
    assert tg==ids
    json.dump(d,open(P+'point-links/'+name+'.json','w'),indent=1)
    print(name,len(d),sum(len(v['needs']) for v in d.values()),sum(l['confidence']=='low' for v in d.values() for l in v['needs']))
out('geo-option-global-interdependence-s2.t2g4',a,0)
out('geo-option-global-interdependence-s2.t2g5',b,0)
