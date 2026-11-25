import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
S='geo-option-culture-identity-s6.'
def L(i,s,w,c='high'):return (i if '.' in i and i.startswith('geo') else None,s,w,c)
# (id, cost, [(link,strength,why,conf)])
E,H='essential','helpful'
T=[
('30.3',1,[('30.2',E,'ICTY tried the leaders'),('24.0',H,'Milošević rise to power','low')]),
('31.b',1,[]),('31.0',1,[('24.0',H,'Milošević as target of protest')]),('31.1',1,[]),
('31.2',1,[('29.2',E,'the siege of Sarajevo')]),('31.3',2,[]),
('32.b',1,[]),('32.0',1,[('29.3',E,'Mostar Old Bridge destroyed, rebuilt')]),
('32.1',1,[('28.b',H,'the coming war in Croatia','low')]),('32.2',2,[]),
('33.b',1,[]),('33.0',1,[]),('33.1',1,[]),
('34.b',1,[]),('34.0',1,[('29.1',H,'ethnic cleansing makes areas uniform')]),
('34.1',1,[]),('34.2',1,[('34.1',E,'the Western Balkans route')]),
('35.b',1,[]),('35.0',2,[('23.2',H,'the republics of Yugoslavia')]),
('35.1',2,[('23.2',H,'Serbia and Montenegro republics','low')]),
('36.b',1,[]),('36.0',1,[('24.1',H,'Kosovo autonomy removed')]),
('36.1',2,[('36.0',E,'Kosovo independence being recognised')]),
('36.2',2,[('29.5',E,'the Dayton Agreement'),('26.2',H,'Bosniak, Croat, Serb groups','low')]),
('36.3',1,[('36.2',H,'Bosnia divided under Dayton','low')]),
('37.b',1,[]),('37.0',2,[]),('37.1',1,[('37.0',H,'EU membership process','low')]),
('38.b',1,[]),('38.0',1,[('23.2',H,'old republic lines')]),
('38.1',1,[('29.5',E,'Dayton Agreement'),('36.2',H,'Dayton structure of Bosnia')]),
('38.2',1,[('37.1',H,'EU candidates and accession')]),
('39.b',1,[]),('39.0',1,[]),('39.1',2,[('39.0',H,'Celtic regions listed')]),
('39.2',1,[]),('39.3',1,[('39.2',H,'Anglo-Saxons pushed Celts west')]),('39.4',1,[]),('39.5',1,[]),
('40.b',1,[]),('40.0',1,[]),('40.1',1,[]),('40.2',2,[('40.1',H,'Edward I conquest of Wales')]),('40.3',1,[]),
('41.b',1,[]),('41.0',1,[('41.b',H,'meaning of devolution')]),
('41.1',1,[('41.b',H,'devolution to Welsh body')]),('41.2',1,[('40.3',H,'border with England unchanged since','low')]),
('42.b',1,[]),('42.0',1,[]),('42.1',1,[]),('42.2',1,[('42.1',H,'Gwynedd and Anglesey heartland')]),('42.3',2,[]),
('43.b',1,[]),('43.0',1,[]),('43.1',1,[]),('43.2',1,[('43.0',H,'Anglican versus Nonconformist church')]),
('44.b',1,[]),('44.0',1,[]),('44.1',1,[('44.0',E,'the Eisteddfod')]),('44.2',1,[('44.0',H,'Eisteddfod festival')]),('44.3',1,[]),
('45.b',1,[]),('45.0',1,[]),('45.1',1,[]),('45.2',1,[]),('45.3',1,[]),('45.4',1,[]),
('46.b',1,[]),('46.0',1,[]),('46.1',1,[]),('46.2',1,[('46.3',H,'second-home ownership grievance')]),
('46.3',1,[]),('46.4',1,[('46.3',E,'second-home ownership')]),('46.5',1,[]),
('47.b',1,[]),('47.0',1,[]),('47.1',1,[]),('47.2',1,[('47.1',H,'central French state')]),('47.3',1,[]),
('48.b',1,[]),('48.0',1,[]),('48.1',1,[('48.0',E,'Nantes separated in 1941')]),('48.2',1,[('48.1',H,'Brittany boundary and Nantes')]),
('49.b',1,[]),('49.0',1,[]),('49.1',2,[]),('49.2',1,[]),('49.3',1,[]),('49.4',1,[]),
('50.b',1,[]),('50.0',1,[]),('50.1',1,[]),('50.2',1,[]),
('51.b',1,[]),('51.0',1,[('49.4',E,'the Lorient festival')]),('51.1',1,[]),
('52.b',1,[]),('52.0',1,[]),('52.1',1,[]),('52.2',1,[]),('52.3',1,[('52.0',H,'the language border','low')]),
('53.b',1,[]),('53.0',1,[('53.b',H,'federalisation meaning')]),('53.1',2,[('53.b',H,'federalisation, regions and communities')]),('53.2',1,[]),
('54.b',1,[]),('54.0',2,[]),('54.1',1,[]),('54.2',1,[]),
('55.b',1,[]),('55.0',1,[]),('55.1',1,[]),('55.2',1,[('55.1',H,'no nationwide parties','low')]),('55.3',1,[]),
('56.b',1,[]),('56.0',1,[]),('56.1',1,[]),('56.2',1,[]),
('57.b',1,[]),('57.0',1,[]),('57.1',1,[('57.0',E,'van Eyck altarpiece reference')]),('57.2',1,[]),('57.3',1,[]),('57.4',1,[]),('57.5',1,[]),
('58.b',1,[]),('58.0',1,[]),('58.1',1,[]),
('59.b',1,[]),('59.0',1,[]),('59.1',1,[('59.0',H,'migrants in Belgian coal mines')]),('59.2',1,[]),('59.3',1,[]),('59.4',1,[]),
('60.b',1,[]),('60.0',1,[]),('60.1',1,[]),('60.2',1,[('60.1',E,'Flanders economy grew'),('60.0',H,'Wallonia industry declined')]),
('61.b',1,[]),('61.0',1,[('53.1',H,'federal regions'),('54.2',H,'Brussels position')]),('61.1',1,[('53.1',H,'devolution to regions','low')]),
]
# extra links for packs 2,3 keyed by target
X2={'39.5':[('s2.17.0',H,'Manx and Cornish revival')],
'42.3':[('s2.25.2',H,'Welsh Language Measure 2011'),('s2.14.2',H,'S4C channel'),('s2.25.4',H,'Cymraeg 2050 target')],
'40.3':[('s2.23.0',H,'Laws in Wales Acts')],'44.2':[('s2.26.1',H,'Urdd and Eisteddfod')],
'46.0':[('s2.23.2',H,'coal and iron spread English')],'46.4':[('s2.27.3',H,'second-home council-tax premium')],
'46.3':[('s2.27.2',H,'second homes and in-migration')],'47.2':[('s2.29.1',H,'French as language of Republic')],
'47.3':[('s2.29.1',H,'Article 2 French Constitution'),('s2.29.4',H,'Diwan schools')],
'51.1':[('s2.31.0',H,'EU and Europe minority language support')],
'52.2':[('s2.2.b',H,'language of power spreads','low')],
'53.2':[('s2.0.2',H,'language defines cultural regions','low')],
'54.b':[('s2.9.0',H,'Flemish as Dutch','low')],
'61.1':[('s2.4.0',H,'Belgium language border divides state','low')]}
X3={'43.0':[('s3.6.1',H,'Protestant branches','low')],'43.2':[('s3.11.1',H,'established church')],
'49.0':[('s3.6.0',H,'Roman Catholic tradition','low')],'56.0':[('s3.6.0',H,'Catholic majority','low')],
'56.1':[('s3.2.b',H,'secularisation')],'56.2':[('s3.7.4',H,'Islam growing through migration')]}
def lk(t):return {"id":t[0],"strength":t[1],"why":t[2],"confidence":t[3] if len(t)>3 else "high"}
def build(pack,out,mode,extra=None):
    txt=open(P+'packs/'+pack).read()
    ids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    tg=[S+k for k,_,_ in T]
    top=txt.split('CANDIDATES')[0]
    assert set(re.findall(r'^\[([^\]]+)\]',top,re.M))==set(tg),'targets differ'
    d={};n=l=c2=low=0
    for k,c,ls in T:
        if mode=='full': arr=[(S+a if a.startswith(('3','4','5','6','2','1')) and not a.startswith('s') else a,*r) for a,*r in ls]
        else: arr=[]
        if extra: arr+= [(( S[:-3]+a if a.startswith('s') else a),*r) for a,*r in extra.get(k,[])]
        arr=[(a if a.startswith('geo') else a,)+tuple(r) for a,*r in arr]
        nd=[lk(a) for a in arr]
        for x in nd: assert x['id'] in ids and x['id']!=S+k,x
        e={"needs":nd}
        if mode=='full': e={"cost":c,"needs":nd}; c2+=c==2
        d[S+k]=e;l+=len(nd);low+=sum(x['confidence']=='low' for x in nd)
    json.dump(d,open(P+'point-links/'+out,'w'),ensure_ascii=False,indent=0)
    json.load(open(P+'point-links/'+out)); print(pack,len(d),l,c2,low)
base='geo-option-culture-identity-s6.t2g'
build(base+'1.txt',base[:-1]+'2g1.json'.replace('2g1','t2g1') if False else 'geo-option-culture-identity-s6.t2g1.json','full')
build(base+'2.txt','geo-option-culture-identity-s6.t2g2.json','links',X2)
build(base+'3.txt','geo-option-culture-identity-s6.t2g3.json','links',X3)
