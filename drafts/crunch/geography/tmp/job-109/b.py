import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
H,E='helpful','essential'
ids="""93.2 93.3 94.b 94.0 94.1 94.2 94.3 95.b 95.0 95.1 95.2 95.3 95.4 96.b 96.0 96.1 96.2 96.3 97.b 97.0 97.1 97.2 97.3 98.b 98.0 98.1 98.2 98.3 99.b 99.0 99.1 99.2 100.b 100.0 100.1 100.2 100.3 101.b 101.0 101.1 101.2 102.b 102.0 102.1 102.2 103.b 103.0 103.1 103.2 104.b 104.0 104.1 104.2 105.b 105.0 105.1 105.2 105.3 106.b 106.0 106.1 106.2 107.b 107.0 107.1 107.2 107.3 108.b 108.0 108.1 108.2 108.3 109.b 109.0 109.1 109.2 109.3 110.b 110.0 110.1 110.2 111.b 111.0 111.1 111.2 111.3 112.b 112.0 112.1 112.2 112.3 112.4 112.5 113.b 113.0 113.1 113.2 113.3 113.4 114.b 114.0 114.1 114.2 114.3 115.b 115.0 115.1 115.2 115.3 115.4 116.b 116.0 116.1 116.2 116.3 117.b 117.0 117.1 117.2 117.3 118.b 118.0 118.1 118.2 118.3 119.b 119.0 119.1 119.2 119.3 120.b 120.0 120.1 120.2 121.b 121.0 121.1 121.2 121.3 121.4 122.b 122.0 122.1 122.2 123.b 123.0 123.1 123.2 123.3 123.4 124.b 124.0 124.1 124.2 124.3""".split()
R='geo-rivers-s4.';A='geo-economic-activities-s2.';U='geo-urban-s7.';M='geo-population-migration-s6.'
p1={'113.2':[L(R+'1.0',H,'reservoir behind a dam')],
'113.3':[L(R+'12.1',H,'urban surfaces speed runoff, flooding','low')],
'98.3':[L(R+'1.b',H,'what a hydro-electric dam is','low')],
'124.2':[L(R+'1.b',H,'water turned into electricity by dams')],
'112.4':[L(A+'2.2',H,'labour as location factor','low')],
'123.3':[L(A+'4.4',H,'regional policy steering firms','low')],
'117.1':[L(A+'4.4',H,'incentives like free trade zones','low')]}
p2={'94.b':[L(M+'0.b',H,'donor and receiver regions')],
'94.0':[L(M+'13.0',H,'nordestinos moving to São Paulo')],
'94.1':[L(M+'1.b',E,'push factors')],
'94.2':[L(M+'2.b',E,'pull factors')],
'95.3':[L(U+'32.2',H,'Japanese immigration to São Paulo')],
'99.0':[L(U+'2.0',H,'favelas as informal settlements')],
'105.2':[L(U+'31.1',H,'São Paulo founded by Jesuits')],
'109.0':[L(M+'0.0',H,'urbanisation as share living in towns')],
'109.1':[L(M+'0.b',E,'rural-to-urban migration')],
'109.2':[L(M+'1.1',H,'mechanisation as push factor')],
'109.3':[L(M+'1.b',H,'push factors','high'),L(M+'2.b',H,'pull factors')],
'110.0':[L(U+'0.5',H,'megacities over 10 million')],
'111.2':[L(U+'31.1',H,'Jesuit mission founding in 1554')],
'112.0':[L(U+'32.0',H,'coffee exported via Santos')],
'112.1':[L(U+'32.0',H,'railway carried coffee to Santos')],
'112.2':[L(U+'32.2',H,'Japanese immigration, Liberdade')],
'112.3':[L(U+'32.3',H,'ABC car plants')],
'112.4':[L(U+'32.4',H,'nordestino migrants')],
'113.0':[L(U+'2.0',H,'favelas as informal settlements')],
'113.1':[L(U+'35.1',H,'traffic and air pollution')],
'113.2':[L(U+'36.1',H,'2014-15 Cantareira drought')],
'113.3':[L(U+'35.2',H,'Tietê flooding')],
'113.4':[L(U+'34.2',H,'inequality and crime')],
'114.0':[L(U+'37.0',H,'rodízio scheme')],
'114.1':[L(U+'13.0',H,'metro and bus rapid transit','low')],
'114.2':[L(U+'11.b',H,'upgrading improves slums in place')],
'114.3':[L(U+'37.4',H,'Minha Casa Minha Vida')],
'115.3':[L(U+'7.1',H,'hillside slums landslide risk')],
'117.3':[L(U+'14.0',H,'Curitiba bus rapid transit')],
'118.0':[L(U+'2.0',H,'favelas as informal settlements')],
'118.1':[L(U+'4.b',H,'informal sector')],
'118.2':[L(U+'3.b',H,'sanitation')],
'118.3':[L(U+'8.0',H,'crime and violence in cities','low')],
'119.1':[L(M+'1.4',H,'drought pushes people out','low')],
'119.3':[L(M+'1.3',H,'poor rural services push people out')],
'120.0':[L(U+'15.0',H,'land reform','low')],
'124.0':[L(M+'13.0',H,'sertão migrants to São Paulo','low')]}
def build(p,links,name):
    txt=open(P+'packs/'+name+'.txt').read()
    pk=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    out={}
    for i in ids:
        k='geo-region-continental-s2.'+('9'+i[1:] if False else i)
        assert k in pk,k
        out[k]={"needs":links.get(i,[])}
    for ls in links.values():
        for l in ls: assert l['id'] in pk,l['id']
    assert set(links)<=set(ids)
    json.dump(out,open(P+'point-links/'+name+'.json','w'),ensure_ascii=False)
    d=json.load(open(P+'point-links/'+name+'.json'))
    n=sum(len(v['needs']) for v in d.values()); lo=sum(l['confidence']=='low' for v in d.values() for l in v['needs'])
    print(name,len(d),n,lo)
build(p1,p1,'geo-region-continental-s2.t4g4')
build(p2,p2,'geo-region-continental-s2.t4g5')
