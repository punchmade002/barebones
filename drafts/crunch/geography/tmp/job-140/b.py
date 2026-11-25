import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
def ids(name):
    t=open(P+'packs/'+name+'.txt').read().split('CANDIDATES')[0]
    return re.findall(r'^\[(geo-urban-s7[^\]]*)\]',t,re.M)
T=ids('geo-urban-s7.t1g1')
c2={'0.4','1.1','16.0','16.2','17.2','21.3','21.5','23.2','27.0','28.0','32.2','32.3','37.0'}
m6='geo-population-migration-s6.'; s3='geo-urban-s3.'; s7='geo-urban-s7.'
n1={
'0.5':[L(m6+'0.4','helpful','megacities forming in Asia and Africa','low')],
'1.0':[L(m6+'0.1','helpful','natural increase as a driver','high')],
'1.1':[L(m6+'1.b','helpful','push factors idea','high')],
'1.2':[L(m6+'2.b','helpful','pull factors idea','high')],
'1.3':[L(s3+'5.b','helpful','primate city definition','high')],
'3.1':[L(s7+'3.0','helpful','waste near homes spreads disease','low')],
'4.0':[L(s7+'4.b','helpful','informal sector definition','high')],
'4.1':[L(s7+'4.b','helpful','informal sector definition','high')],
'9.1':[L(s7+'9.0','essential','slum clearance by eviction','high')],
'10.1':[L(s7+'10.0','essential','serviced plots','high')],
'11.1':[L(s7+'2.2','helpful','insecure tenure and eviction','high')],
'12.1':[L(s7+'27.0','helpful','Navi Mumbai new town','high'),L(s7+'21.3','helpful','Salt Lake new town','high')],
'13.1':[L(s7+'14.b','helpful','Curitiba bus system','high')],
'14.1':[L(s7+'13.0','helpful','bus rapid transit idea','high')],
'14.3':[L(s7+'13.0','helpful','bus rapid transit idea','high')],
'15.0':[L(s7+'1.1','essential','push factors in the countryside','high')],
'15.1':[L(s7+'21.6','helpful','Missionaries of Charity','high')],
'17.0':[L(s7+'1.2','helpful','pull factors of jobs','low')],
'17.3':[L(s7+'1.0','helpful','natural increase','high'),L(s7+'1.3','helpful','primacy','low')],
'18.0':[L(s7+'2.0','helpful','slums and bustees','high')],
'18.1':[L(s7+'2.3','helpful','pavement dwellers','high')],
'19.0':[L(s7+'17.2','essential','Partition of 1947','high')],
'19.1':[L(s7+'4.b','helpful','informal sector','high')],
'19.2':[L(s7+'4.0','helpful','informal work examples','high')],
'20.0':[L(s7+'3.b','helpful','sanitation definition','high')],
'20.1':[L(s7+'16.0','helpful','low-lying delta site','high')],
'21.1':[L(s7+'11.0','helpful','slum upgrading measures','high')],
'21.2':[L(s7+'13.0','helpful','metros ease congestion','high')],
'21.3':[L(s7+'12.0','helpful','planned new towns','high')],
'21.4':[L(s7+'12.0','helpful','planned new towns','high')],
'21.5':[L(s7+'6.1','helpful','untreated sewage','low')],
'21.6':[L(s7+'15.1','helpful','NGO work','high')],
'22.0':[L(s7+'21.1','essential','bustee improvement programme','high')],
'22.1':[L(s7+'21.3','essential','new towns Salt Lake, New Town','high')],
'23.5':[L(m6+'11.0','helpful','migrants from Bihar and UP','low')],
'24.0':[L(s7+'2.0','helpful','slums','high')],
'25.0':[L(s7+'5.1','helpful','overcrowded transport','high')],
'25.1':[L(s7+'5.0','helpful','congestion','high')],
'25.2':[L(s7+'7.0','helpful','monsoon flooding','high')],
'25.3':[L(s7+'3.0','helpful','services and sanitation','low')],
'26.1':[L(s7+'26.0','essential','mill closures','high')],
'27.0':[L(s7+'12.0','helpful','new town idea','high')],
'27.1':[L(s7+'27.0','essential','Navi Mumbai','high')],
'28.1':[L(s7+'24.0','essential','Dharavi slum','high'),L(s7+'28.0','helpful','rehabilitation scheme','low')],
'29.0':[L(s7+'25.0','helpful','overcrowded roads and trains','high')],
'29.2':[L(s7+'27.0','helpful','Navi Mumbai','high')],
'30.0':[L(s7+'28.0','essential','Slum Rehabilitation Authority','high')],
'30.1':[L(s7+'24.0','essential','Dharavi industries','high')],
'31.2':[L(s7+'31.0','helpful','Santos and the plateau','high')],
'32.0':[L(s7+'31.2','helpful','Santos port','high')],
'32.4':[L(m6+'13.0','helpful','nordestino migration','high')],
'34.0':[L(s7+'2.0','helpful','favelas','high')],
'34.1':[L(s7+'2.0','helpful','favelas','high')],
'34.2':[L(s7+'8.0','helpful','crime as social problem','high')],
'35.0':[L(s7+'5.0','helpful','congestion','high')],
'35.1':[L(s7+'6.0','helpful','air pollution','high')],
'35.2':[L(s7+'7.0','helpful','flooding in heavy rain','low')],
'36.1':[L(s7+'36.0','essential','Cantareira reservoirs','high')],
'37.0':[L(s7+'35.0','helpful','congestion it addresses','high')],
'37.1':[L(s7+'13.0','helpful','metros ease roads','high')],
'37.2':[L(s7+'35.0','helpful','congestion it addresses','high')],
'37.3':[L(s7+'2.0','helpful','favelas','high')],
'38.0':[L(s7+'11.0','helpful','slum upgrading','low'),L(s7+'37.1','helpful','transport improvement','low')],
'38.1':[L(s7+'35.0','helpful','congestion','low')],
}
def build(extra,cost):
    o={}
    for i in T:
        k=i[len(s7):]
        d={}
        if cost: d['cost']=2 if k in c2 else 1
        d['needs']=extra.get(k,[])
        o[i]=d
    return o
s5='geo-urban-s5.';s6='geo-urban-s6.';c1='geo-region-continental-s1.'
n2={
'5.0':[L(s5+'0.b','helpful','congestion definition','high')],
'7.0':[L(s5+'27.0','helpful','paving causes runoff and flooding','high')],
'12.0':[L(s6+'2.2','helpful','new towns planning','high')],
'13.0':[L(s5+'3.0','helpful','public transport measures','low')],
'14.1':[L(s5+'3.2','helpful','bus lanes give priority','high')],
'25.2':[L(s5+'27.0','helpful','paved surfaces and runoff','low')],
'28.1':[L(s6+'0.2','helpful','redevelopment clears and rebuilds','low')],
'35.0':[L(s5+'0.b','helpful','congestion definition','low')],
'35.1':[L(s5+'22.0','helpful','urban air pollution sources','low')],
'35.2':[L(s5+'27.0','helpful','urban flooding from runoff','high')],
'37.2':[L(s5+'3.6','helpful','orbital ring roads','high')],
}
n3={
'7.0':[L(c1+'2.0','helpful','monsoon as seasonal wind','high')],
'16.0':[L(c1+'27.7','helpful','Hooghly distributary at Kolkata','high')],
'16.2':[L(c1+'37.4','helpful','jute as cash crop','low')],
'19.0':[L(c1+'37.4','helpful','jute grown in Bengal','low')],
'20.1':[L(c1+'2.3','helpful','wet south-west monsoon','high')],
'25.2':[L(c1+'2.3','helpful','monsoon rain season','low')],
}
for name,ex,cost in [('geo-urban-s7.t1g1',n1,True),('geo-urban-s7.t1g2',n2,False),('geo-urban-s7.t1g3',n3,False)]:
    o=build(ex,cost)
    pk=open(P+'packs/'+name+'.txt').read()
    allids=set(re.findall(r'^\[([^\]]+)\]',pk,re.M))
    assert len(o)==len(T)
    ln=lo=c=0
    for v in o.values():
        for n in v['needs']:
            assert n['id'] in allids,n
            ln+=1; lo+= n['confidence']=='low'
        c+=v.get('cost',0)==2
    assert not any(k not in o for k in ex) if False else True
    for k in ex: assert s7+k in o,k
    json.dump(o,open(P+'point-links/'+name+'.json','w'),indent=0,ensure_ascii=False)
    json.load(open(P+'point-links/'+name+'.json'))
    print(name,len(o),ln,c,lo)
