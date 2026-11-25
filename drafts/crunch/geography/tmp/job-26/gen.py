import json,re
G='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
P='geo-economic-globalisation-s4'
H,E,hi,lo='helpful','essential','high','low'
def L(i,s,w,c=hi): return {"id":i,"strength":s,"why":w,"confidence":c}
S4=P+'.'
# package 1: (id, cost, links)
p1=[
('0.b',1,[L('geo-economic-globalisation-s1.0.3',H,'production split into stages')]),
('0.0',1,[L('geo-economic-globalisation-s1.8.b',H,'Intel chain stages spread across continents')]),
('0.1',1,[]),('0.2',1,[]),
('0.3',1,[L('geo-economic-globalisation-s3.4.2',H,'trade blocs remove internal barriers')]),
('0.4',1,[]),('0.5',1,[]),('0.6',1,[]),
('1.b',1,[L('geo-economic-globalisation-s1.14.0',H,'outsourcing production to contract makers')]),
('1.0',1,[]),
('1.1',1,[L('geo-economic-globalisation-s1.0.1',H,'headquarters and design stay in home country')]),
('1.2',1,[L('geo-economic-globalisation-s1.14.0',H,'contract manufacturers make the product',lo)]),
('1.3',1,[]),('1.4',1,[]),
('2.b',2,[]),('2.0',1,[L(S4+'2.b',H,'export processing zone idea')]),
('2.1',1,[L('geo-economic-globalisation-s3.12.1',H,'Special Economic Zones in China')]),
('2.2',1,[L(S4+'2.b',H,'export processing zone idea')]),
('2.3',1,[L(S4+'2.b',E,'export processing zone rules')]),
('3.b',1,[]),
('3.0',2,[L('geo-economic-globalisation-s3.6.b',H,'disruption spreads through linked trade')]),
('3.1',1,[L('geo-economic-globalisation-s1.0.2',H,'branch plants compete for investment',lo)]),
('3.2',1,[]),('3.3',1,[]),('3.4',1,[]),
('4.b',1,[]),('4.0',2,[]),
('4.1',1,[L(S4+'4.b',E,'core meaning')]),
('4.2',1,[L(S4+'4.b',E,'periphery meaning')]),
('4.3',1,[L(S4+'4.2',H,'periphery features')]),
('5.b',1,[]),
('5.0',1,[L(S4+'4.b',H,'core and periphery')]),
('5.1',1,[L(S4+'5.0',E,'NICs and semi-periphery')]),
('6.b',1,[L(S4+'4.b',H,'core and periphery')]),
('6.0',1,[]),('6.1',2,[]),('6.2',2,[]),
('6.3',1,[L(S4+'4.b',E,'core and periphery')]),
('6.4',2,[L(S4+'4.1',H,'Blue Banana as core')]),
('7.b',1,[]),('7.0',1,[]),
('7.1',1,[L(S4+'7.0',H,'export economies built for raw materials')]),
('7.2',1,[]),
('7.3',2,[L(S4+'7.0',H,'raw material export economies')]),
('8.b',1,[]),
('8.0',1,[L(S4+'6.3',H,'backwash contrasts with spread effects')]),
('8.1',1,[L(S4+'5.0',E,'semi-periphery')]),
('8.2',1,[L(S4+'4.b',H,'core economy meaning')]),
('8.3',1,[L(S4+'4.b',H,'North-South pattern like core-periphery')]),
('9.b',1,[L(S4+'4.2',H,'periphery supplies raw materials')]),
('9.0',1,[]),('9.1',1,[]),('9.2',2,[]),('9.3',1,[]),('9.4',1,[]),
('9.5',1,[L(S4+'9.4',E,'South Sudan independence in 2011')]),
('10.b',1,[]),('10.0',1,[]),('10.1',2,[]),('10.2',1,[]),('10.3',1,[]),('10.4',1,[]),('10.5',1,[]),
('10.6',1,[L(S4+'7.0',E,'colonial raw-material export economies')]),
('10.7',2,[L('geo-economic-globalisation-s3.4.1',H,'tariffs as trade barriers')]),
('11.b',1,[]),
('11.0',1,[L(S4+'10.5',H,'heavy debt problem')]),
('11.1',1,[L('geo-economic-globalisation-s3.4.2',H,'trade blocs remove barriers')]),
('11.2',1,[L(S4+'10.0',H,'poor infrastructure problem')]),
('11.3',1,[L('geo-economic-globalisation-s3.4.6',E,'fair trade guaranteed price')]),
('12.b',2,[]),
('12.0',1,[L('geo-economic-globalisation-s1.0.b',H,'MNC meaning')]),
('12.1',2,[L(S4+'12.0',H,'MNC production networks')]),
('12.2',1,[L(S4+'12.1',H,'stages across countries')]),
('12.3',1,[]),
('12.4',1,[L('geo-economic-globalisation-s3.12.4',H,'China as largest exporter')]),
('12.5',1,[L('geo-economic-globalisation-s3.4.4',H,'WTO role')]),
('12.6',1,[L('geo-economic-globalisation-s3.5.1',H,'containerisation made shipping cheaper')]),
('12.7',1,[]),
('13.b',1,[]),
('13.0',1,[L(S4+'0.1',H,'production moves to low-wage countries')]),
('13.1',1,[L(S4+'5.0',H,'NICs')]),
('13.2',1,[]),
('13.3',1,[L(S4+'9.b',H,'regions excluded from manufacturing')]),
('13.4',1,[L(S4+'19.2',E,'Rana Plaza collapse')]),
('13.5',1,[L(S4+'3.3',H,'environmental cost of transport',lo)]),
('14.b',1,[]),
('14.0',1,[L('geo-economic-globalisation-s3.8.5',H,'US-China trade war tariffs')]),
('14.1',1,[L(S4+'3.4',E,'reshoring meaning')]),
('14.2',1,[L('geo-economic-globalisation-s3.6.5',H,'COVID supply chain disruption')]),
('15.b',1,[]),('15.0',1,[]),
('15.1',1,[L('geo-economic-globalisation-s3.4.1',H,'tariffs as trade barriers')]),
('15.2',1,[]),('15.3',1,[L('geo-economic-globalisation-s3.1.0',H,'balance of payments',lo)]),
('15.4',1,[L(S4+'15.2',H,'Licence Raj removed')]),
('16.b',1,[]),('16.0',1,[]),
('16.1',2,[L('geo-economic-globalisation-s3.17.0',H,'Bengaluru IT services hub')]),
('16.2',1,[]),('16.3',1,[]),('16.4',1,[]),
('16.5',1,[L('geo-economic-globalisation-s1.16.1',H,'iPhone assembly in India')]),
('16.6',2,[]),('16.7',1,[]),
('17.b',1,[]),('17.0',1,[]),('17.1',1,[]),('17.2',1,[]),('17.3',1,[]),
('17.4',1,[L('geo-economic-globalisation-s1.0.b',H,'MNC meaning')]),
('18.b',1,[]),
('18.0',1,[L('geo-economic-globalisation-s3.12.0',H,'Deng Xiaoping reforms')]),
('18.1',1,[L(S4+'2.1',H,'Shenzhen Special Economic Zone')]),
('18.2',1,[L('geo-economic-globalisation-s3.12.3',H,'China joining WTO')]),
('18.3',1,[]),('18.4',1,[]),('18.5',1,[]),('18.6',2,[]),
('19.b',1,[]),('19.0',1,[]),('19.1',1,[]),('19.2',1,[]),
('19.3',1,[L(S4+'19.2',H,'Rana Plaza collapse')]),
]
# links-only packages: id -> links (every id listed explicitly)
ids=[i for i,_,_ in p1]
D2='geo-economic-development-s2.'; D3='geo-economic-development-s3.'; D4='geo-economic-development-s4.'
l2={i:[] for i in ids}
l2.update({
'4.b':[L(D2+'2.2',H,'core and periphery in EU')],
'4.1':[L(D2+'2.2',H,'Blue Banana core')],
'6.4':[L(D2+'2.2',H,'Blue Banana core')],
'5.1':[L(D2+'12.b',H,'South Korea as industrialising economy')],
'6.1':[L(D3+'0.4',H,'colonies supplied raw materials')],
'6.2':[L(D2+'11.2',H,'cumulative causation',hi)],
'6.3':[L(D2+'11.2',H,'cumulative core growth',lo)],
'7.b':[L(D3+'0.b',H,'colonialism meaning')],
'7.0':[L(D3+'0.4',H,'colonies exporting raw materials')],
'7.1':[L(D3+'1.0',H,'colonial railways to ports')],
'7.2':[L(D3+'1.4',H,'artificial colonial borders')],
'7.3':[L(D3+'2.2',H,'debt crises after independence',lo)],
'8.0':[L(D2+'11.3',H,'spread effects')],
'8.1':[L(D2+'12.b',H,'Asian Tigers growth',lo)],
'8.2':[L(D2+'15.b',H,'Ireland moved up through FDI')],
'8.3':[L(D2+'0.0',H,'Brandt Line')],
'9.0':[L(D2+'7.4',H,'Nigeria oil dependence')],
'9.2':[L(D2+'7.5',H,'DR Congo cobalt')],
'9.3':[L(D3+'27.2',H,'Sudan war SAF and RSF')],
'9.4':[L(D3+'23.3',H,'South Sudan independence')],
'9.5':[L(D3+'23.3',H,'South Sudan independence 2011')],
'10.0':[L(D2+'8.6',H,'infrastructure and development',lo)],
'10.1':[L(D2+'7.0',H,'landlocked countries')],
'10.2':[L(D2+'10.2',H,'corruption and instability')],
'10.3':[L(D2+'8.2',H,'education and workforce')],
'10.5':[L(D3+'2.2',H,'debt crises',lo)],
'10.6':[L(D3+'0.4',H,'colonial raw-material exports')],
'11.0':[L(D3+'2.2',H,'IMF and debt',lo)],
'15.0':[L(D3+'8.0',H,'Five-Year Plans')],
'15.1':[L(D3+'8.1',H,'import substitution protection')],
'15.2':[L(D3+'8.3',H,'Licence Raj')],
'15.3':[L(D3+'10.0',H,'1991 foreign-exchange crisis')],
'15.4':[L(D3+'10.2',H,'1991 reforms')],
'16.1':[L(D3+'11.1',H,'Bengaluru IT industry')],
'16.6':[L(D3+'11.0',H,'services over half of GDP')],
'17.3':[L(D3+'12.0',H,'informal sector')],
'17.0':[L(D3+'12.2',H,'inequality between Indian states')],
'18.0':[L(D2+'13.0',H,'Deng reforms')],
'18.1':[L(D2+'13.1',H,'Special Economic Zones')],
'18.2':[L(D2+'13.2',H,'China joining WTO')],
'18.4':[L(D2+'13.3',H,'poverty reduction in China')],
'18.5':[L(D2+'13.5',H,'coast and interior inequality')],
})
l3={i:[] for i in ids}
l3.update({
'0.1':[L(D4+'17.0',H,'labour-intensive work in low-wage countries')],
'1.4':[L(D4+'17.2',H,'exploitation in factories',lo)],
'3.2':[L(D4+'17.2',H,'low wages and poor conditions')],
'7.3':[L(D4+'3.0',H,'commodity price instability')],
'9.b':[L(D4+'3.0',H,'dependence on raw material exports')],
'10.5':[L(D4+'9.0',H,'debt repayments crowd out spending')],
'10.7':[L(D4+'3.3',H,'tariff escalation')],
'11.0':[L(D4+'11.1',H,'HIPC initiative')],
'11.3':[L(D4+'6.b',H,'fair trade model')],
'13.4':[L(D4+'18.0',H,'Rana Plaza collapse')],
'17.1':[L(D4+'3.0',H,'price instability for commodities',lo)],
'19.2':[L(D4+'18.0',H,'Rana Plaza collapse')],
'19.3':[L(D4+'18.3',H,'Accord on Fire and Building Safety')],
})
out={}
out[1]={P+'.'+i:{"cost":c,"needs":n} for i,c,n in p1}
out[2]={P+'.'+i:{"needs":l2[i]} for i in ids}
out[3]={P+'.'+i:{"needs":l3[i]} for i in ids}
for k,name in ((1,'t1g1'),(2,'t1g2'),(3,'t1g3')):
    pk=G+f'packs/{P}.{name}.txt'; txt=open(pk).read()
    allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    tgt=[]; sec=None
    for ln in txt.splitlines():
        if ln.startswith('TARGET'): sec='t'
        elif ln.startswith('CANDIDATES'): sec='c'
        m=re.match(r'\[([^\]]+)\]',ln)
        if m and sec=='t': tgt.append(m.group(1))
    d=out[k]
    assert list(d)==tgt,(k,set(tgt)^set(d))
    for t,v in d.items():
        for n in v['needs']:
            assert n['id'] in allids and n['id']!=t,(k,t,n['id'])
    json.dump(d,open(G+f'point-links/{P}.{name}.json','w'),indent=1)
    links=sum(len(v['needs']) for v in d.values())
    low=sum(n['confidence']=='low' for v in d.values() for n in v['needs'])
    c2=sum(v.get('cost')==2 for v in d.values())
    print(k,len(d),links,c2 if k==1 else '-',low)
