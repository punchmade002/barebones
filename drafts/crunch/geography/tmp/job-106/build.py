import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
S='geo-region-continental-s2.'
def full(x):
    for k,v in (('r1.','geo-rivers-s1.'),('r4.','geo-rivers-s4.'),('p1.','geo-population-migration-s1.'),('s2.',S)):
        if x.startswith(k): return v+x[len(k):]
    raise Exception(x)
def L(i,st,why,c='high'): return {"id":full(i),"strength":st,"why":why,"confidence":c}
h=lambda i,w,c='high':L(i,'helpful',w,c)
e=lambda i,w,c='high':L(i,'essential',w,c)
# id: (cost, pkg1 links, pkg2 links, pkg3 links) -- every target listed explicitly
T=[
('62.2',1,[h('s2.48.1','Mercosur trade bloc')],[],[]),
('63.b',1,[],[],[]),
('63.0',2,[h('s2.54.0','Carajás iron ore')],[],[]),
('63.1',1,[h('s2.42.2','sugar cane ethanol fuel','low')],[],[]),
('63.2',1,[],[],[]),
('63.3',1,[h('s2.52.0','eucalyptus plantations')],[],[]),
('63.4',1,[h('s2.57.0','Petrobras oil','low')],[],[]),
('64.b',1,[],[],[]),
('64.0',1,[h('s2.32.2','Itaipu Dam')],[],[h('r4.1.0','dam stores water, turbines','low')]),
('64.1',1,[h('s2.34.1','Tucuruí Dam')],[],[]),
('64.2',1,[h('s2.56.0','rain-fed hydroelectricity')],[],[]),
('65.b',1,[],[],[]),
('65.0',1,[],[],[]),
('65.1',1,[],[h('s2.95.2','Italian German immigrants')],[]),
('65.2',1,[h('s2.60.2','ABC region')],[h('s2.94.0','Northeast to Southeast migration')],[]),
('65.3',1,[h('s2.61.2','Embraer São José dos Campos')],[],[]),
('66.b',1,[],[],[]),
('66.0',1,[],[],[]),
('66.1',1,[],[],[]),
('66.2',1,[],[],[]),
('67.b',1,[],[],[]),
('67.0',1,[h('s2.59.1','coffee profits financed industry')],[],[]),
('67.1',1,[],[],[]),
('67.2',1,[],[],[]),
('67.3',1,[],[],[]),
('68.b',1,[],[],[]),
('68.0',1,[e('s2.60.0','import substitution industrialisation')],[],[]),
('68.1',2,[],[],[]),
('68.2',2,[],[],[]),
('68.3',1,[e('s2.68.2','SUDENE incentives, "the same"')],[],[]),
('69.b',1,[],[],[]),
('69.0',1,[h('s2.3.5','industrial triangle on map')],[],[]),
('69.1',2,[],[],[]),
('69.2',1,[],[],[]),
('70.b',1,[],[],[]),
('70.0',1,[h('s2.60.2','ABC region car makers')],[],[]),
('70.1',1,[h('s2.61.2','Embraer')],[],[]),
('70.2',1,[h('s2.60.1','CSN Volta Redonda')],[],[]),
('70.3',1,[h('s2.57.0','Petrobras')],[],[]),
('70.4',1,[],[],[]),
('70.5',1,[],[],[]),
('71.b',1,[],[],[]),
('71.0',1,[],[],[]),
('71.1',1,[],[],[]),
('71.2',1,[],[],[]),
('71.3',1,[h('s2.69.0','Southeast industrial concentration')],[],[]),
('72.b',1,[],[],[]),
('72.0',1,[],[],[]),
('72.1',1,[],[h('s2.112.5','São Paulo financial capital','low')],[]),
('73.b',1,[],[],[]),
('73.0',1,[],[],[]),
('73.1',1,[h('s2.27.0','Sugarloaf granite dome')],[],[]),
('73.2',1,[],[],[]),
('73.3',1,[],[h('s2.108.0','Carnival festival')],[]),
('74.b',1,[],[],[]),
('74.0',1,[h('s2.24.2','Iguaçu Falls')],[h('r1.8.0','waterfall formation','low')],[]),
('74.1',1,[h('s2.50.2','rubber boom Teatro Amazonas')],[h('s2.117.1','Manaus rubber wealth')],[]),
('74.2',1,[h('s2.26.0','Pantanal wetland','low')],[],[]),
('74.3',1,[],[],[]),
('74.4',1,[],[h('s2.116.0','Brasília inauguration')],[]),
('74.5',1,[h('s2.27.1','Lençóis Maranhenses dunes')],[],[]),
('75.b',1,[],[],[]),
('75.0',1,[],[],[]),
('75.1',1,[],[h('s2.108.0','Carnival')],[]),
('75.2',1,[h('s2.26.0','Pantanal','low')],[],[]),
('75.3',1,[],[],[]),
('75.4',1,[],[],[]),
('76.b',1,[],[],[]),
('76.0',1,[],[],[]),
('76.1',1,[],[],[]),
('76.2',1,[],[],[]),
('76.3',1,[],[],[]),
('76.4',1,[h('s2.75.4','2014 World Cup 2016 Olympics')],[],[]),
('77.b',1,[],[],[]),
('77.0',1,[],[],[]),
('77.1',1,[],[],[]),
('77.2',1,[h('s2.76.4','mega-events investment')],[],[]),
('77.3',1,[],[],[]),
('77.4',1,[],[h('s2.108.0','Carnival heritage','low')],[]),
('78.b',1,[],[],[]),
('78.0',1,[],[],[]),
('78.1',1,[h('s2.75.4','2016 Olympics Rio')],[],[]),
('78.2',1,[],[],[]),
('78.3',1,[h('s2.75.4','2014 World Cup')],[],[]),
('78.4',1,[h('s2.75.4','2016 Olympics Rio')],[],[]),
('78.5',1,[],[h('s2.108.0','Carnival peak')],[]),
('79.b',1,[],[],[]),
('79.0',1,[],[],[]),
('79.1',1,[],[],[]),
('79.2',1,[],[],[]),
('79.3',1,[h('s2.41.3','soya Mato Grosso','low')],[],[]),
('79.4',1,[],[h('s2.93.2','Rondônia BR-364 settlement')],[]),
('80.b',1,[],[],[]),
('80.0',1,[h('s2.54.0','Carajás ore railway')],[],[]),
('80.1',1,[h('s2.36.0','Amazon as highway')],[],[]),
('80.2',2,[],[],[]),
('80.3',1,[h('s2.41.3','soya harvest','low')],[],[]),
('81.b',1,[],[],[]),
('81.0',1,[],[],[]),
('81.1',1,[],[h('s2.117.3','Curitiba BRT planning')],[]),
('81.2',2,[],[h('s2.114.0','rodízio scheme')],[]),
('82.b',1,[],[],[]),
('82.0',1,[],[],[]),
('82.1',1,[],[],[]),
('82.2',1,[],[h('s2.116.2','Brasília opens interior')],[]),
('82.3',1,[h('s2.79.4','roads open Amazon to clearance')],[],[]),
('83.b',1,[],[],[]),
('83.0',1,[],[],[h('p1.1.1','census count','low')]),
('83.1',1,[],[],[]),
('83.2',1,[],[],[h('p1.1.1','census held at intervals')]),
('84.b',2,[],[],[h('p1.15.b','Demographic Transition Model')]),
('84.0',1,[],[],[h('p1.16.1','causes of falling death rate')]),
('84.1',2,[],[],[e('p1.0.5','replacement level')]),
('84.2',1,[],[h('s2.109.1','rural-urban migration','low')],[h('p1.22.3','urbanisation lowers fertility')]),
('84.3',1,[],[],[h('p1.22.0','female education and work')]),
('85.b',1,[],[],[e('p1.25.b','population pyramid')]),
('85.0',1,[h('s2.84.1','fertility collapse')],[],[h('p1.34.0','falling fertility narrows base')]),
('85.1',1,[],[],[h('p1.34.1','life expectancy widens top')]),
('85.2',1,[],[],[e('p1.28.1','old-age dependency ratio')]),
('85.3',1,[h('s2.85.2','old-age dependency')],[],[h('p1.30.3','raising pension age')]),
('86.b',1,[h('s2.2.b','five macro-regions')],[],[h('p1.4.b','distribution')]),
('86.0',2,[e('s2.2.b','macro-region names')],[],[]),
('86.1',1,[h('s2.2.0','North region Amazon')],[],[]),
('86.2',1,[],[],[e('p1.4.1','density formula')]),
('86.3',1,[],[],[h('p1.4.0','distribution of people')]),
('87.b',1,[],[],[]),
('87.0',1,[],[],[]),
('87.1',1,[h('s2.9.1','São Paulo cooler than Rio')],[],[]),
('87.2',1,[h('s2.15.1','terra roxa coffee soil')],[],[]),
('87.3',1,[],[h('s2.94.0','migrants to cities','low')],[]),
('87.4',1,[],[],[]),
('88.b',1,[],[],[]),
('88.0',1,[],[],[]),
('88.1',1,[h('s2.15.2','massapê soil')],[],[]),
('88.2',1,[],[h('s2.95.1','enslaved Africans')],[]),
('88.3',1,[h('s2.8.0','south-east trade winds')],[],[]),
('89.b',1,[],[],[]),
('89.0',1,[],[],[]),
('89.1',1,[],[],[]),
('89.2',1,[h('s2.13.0','latosol soils')],[],[]),
('89.3',1,[],[],[h('p1.4.1','density meaning','low')]),
('90.b',1,[],[],[]),
('90.0',1,[],[],[]),
('90.1',1,[h('s2.7.0','sertão rainfall')],[],[]),
('90.2',1,[h('s2.7.4','2012-2017 drought')],[h('s2.94.1','drought push factor')],[]),
('90.3',1,[h('s2.17.0','sertão thin stony soils')],[],[]),
('91.b',1,[],[],[]),
('91.0',1,[],[],[h('p1.4.1','density formula','low')]),
('91.1',1,[e('s2.91.0','São Paulo state density figure')],[],[]),
('91.2',2,[h('s2.91.1','density contrast')],[],[]),
('92.b',1,[],[],[]),
('92.0',1,[],[h('s2.116.2','Brasília opens interior','low')],[]),
('92.1',1,[h('s2.92.0','Brasília new capital')],[],[]),
('92.2',1,[h('s2.92.1','March to the West')],[],[]),
('93.b',1,[],[],[]),
('93.0',1,[h('s2.79.2','Trans-Amazonian Highway')],[],[]),
('93.1',1,[],[],[]),
]
ids=[S+t[0] for t in T]
assert len(set(ids))==len(ids)
# check against pack target lists
for n,k in ((1,'t3g1'),(2,'t3g2'),(3,'t3g3')):
    txt=open(P+f'packs/geo-region-continental-s2.{k}.txt').read()
    tgt=[]; sec=None
    for ln in txt.split('\n'):
        if ln.startswith('TARGET'): sec='T'
        elif ln.startswith('CANDIDATES'): sec='C'
        m=re.match(r'\[([^\]]+)\]',ln)
        if m:
            (tgt if sec=='T' else []).append(m.group(1))
    allids={m for m in re.findall(r'^\[([^\]]+)\]',txt,re.M)}
    assert tgt==ids,(k,set(tgt)^set(ids))
    out={}
    nl=nc2=nlow=0
    for t,i in zip(T,ids):
        links=t[1+n]
        for l in links:
            assert l['id'] in allids,(k,l['id'])
            assert l['id']!=i
            if n>1: assert not l['id'] in [x['id'] for x in t[2]] or n==1
        if n==1:
            d={"cost":t[1],"needs":links}; nc2+=t[1]==2
        else: d={"needs":links}
        nl+=len(links); nlow+=sum(l['confidence']=='low' for l in links)
        out[i]=d
    json.dump(out,open(P+f'point-links/geo-region-continental-s2.{k}.json','w'),ensure_ascii=False,indent=1)
    json.loads(open(P+f'point-links/geo-region-continental-s2.{k}.json').read())
    print(k,len(out),nl,nc2 if n==1 else '-',nlow)
