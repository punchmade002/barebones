import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
S='geo-option-global-interdependence-s3.'
def L(i,s,w,c='high'): return (i,s,w,c)
E,H='essential','helpful'
# id: cost  (explicit for every target)
cost={}
two={'1.0','1.1','3.1','4.2','4.4','4.6','5.1','10.3','12.1','13.2','14.2','15.1','16.1','18.5'}
counts={0:4,1:4,2:6,3:5,4:7,5:5,6:3,7:6,8:1,9:6,10:5,11:4,12:5,13:6,14:4,15:5,16:6,17:5,18:7,19:4,20:7,21:3}
ids=[]
for s in range(23):
    ids.append(f'{s}.b')
    for k in range(counts.get(s,0)): ids.append(f'{s}.{k}')
assert len(ids)==131
# links per package: g1 (own subsection), g2 (s1/ed-s1), g3 (ed-s4/ed-s3)
g1={
'0.1':[L('0.0',H,'growth captured by elites')],
'0.2':[L('0.1',H,'growth stays with elites')],
'0.3':[L('0.2',E,'empowerment means control and voice')],
'1.1':[L('1.0',H,'the loans being repaid')],
'1.2':[L('1.1',H,'why debts could not be repaid')],
'2.1':[L('2.0',E,'repayments take government revenue')],
'2.2':[L('2.1',E,'less spent on health, schools')],
'2.3':[L('2.2',H,'low productivity and incomes')],
'2.4':[L('2.3',E,'government borrows more')],
'2.5':[L('2.0',H,'repayments needing foreign currency')],
'3.1':[L('3.0',E,'structural adjustment conditions')],
'3.2':[L('3.0',H,'structural adjustment conditions')],
'3.3':[L('3.2',H,'cuts to services, subsidies')],
'3.4':[L('3.1',H,'privatisation as a condition')],
'4.2':[L('4.0',H,'debt cancellation campaign')],
'4.3':[L('4.1',H,'HIPC relief')],
'4.4':[L('4.1',E,'first HIPC relief recipient')],
'4.5':[L('4.1',H,'relief funding schools')],
'4.6':[L('4.1',E,'HIPC completion point')],
'5.2':[L('5.1',H,'Sri Lanka default')],
'5.4':[L('2.1',H,'debt cuts spending on services')],
'6.1':[L('6.0',H,'Chinese infrastructure loans')],
'6.2':[L('6.1',E,'Hambantota lease example')],
'7.1':[L('7.0',H,'Irish debt crisis')],
'7.2':[L('7.0',H,'Irish debt crisis')],
'7.3':[L('7.2',H,'austerity effects')],
'7.4':[L('7.2',H,'austerity and emigration')],
'7.5':[L('7.1',H,'the EU-IMF programme')],
'8.0':[L('1.3',H,'loans to dictators')],
'9.4':[L('1.b',H,'debt from loans','low')],
'10.1':[L('10.0',E,'the 0.7% target')],
'10.2':[L('10.0',E,'the 0.7% target')],
'10.3':[L('10.0',H,'USA as largest donor')],
'10.4':[L('10.2',H,'donor cuts example')],
'12.0':[L('9.5',E,'tied aid')],
'12.1':[L('12.0',H,'aid tied to donor interests')],
'12.3':[L('12.0',H,'tied aid returns money to donor')],
'13.0':[L('0.1',H,'elite capture of benefits')],
'13.3':[L('13.2',E,'the Haiti rice policy')],
'13.4':[L('9.4',H,'loans add to debt')],
'14.1':[L('13.0',H,'corruption'),L('13.1',H,'dependency')],
'14.2':[L('31.0',H,'top-down versus bottom-up')],
'14.3':[L('9.5',H,'untied aid')],
'15.1':[L('9.2',E,'bilateral aid')],
'15.2':[L('9.5',E,'untied aid')],
'15.4':[L('10.0',E,'the 0.7% target')],
'16.0':[L('9.2',H,'multilateral aid')],
'16.2':[L('9.0',H,'humanitarian aid')],
'16.5':[L('6.0',E,'Belt and Road Initiative')],
'17.0':[L('9.3',H,'NGO aid')],
'17.1':[L('9.0',H,'emergency relief'),L('9.1',H,'long-term development aid')],
'17.2':[L('28.b',H,'co-operatives')],
'17.3':[L('17.0',H,'NGO independence')],
'18.0':[L('9.0',H,'emergency relief')],
'18.6':[L('17.0',H,'what NGOs are')],
'20.0':[L('31.0',H,'bottom-up decisions')],
'20.1':[L('9.5',H,'tied aid')],
'20.2':[L('17.0',H,'NGO funding')],
'20.3':[L('17.0',H,'NGO scale')],
'21.2':[L('21.0',H,'land as main source of income')],
}
g2={
'0.0':[L('geo-economic-development-s1.1.0',H,'GDP defined'),L('geo-economic-development-s1.0.1',H,'development wider than income')],
'1.1':[L('geo-option-global-interdependence-s1.10.1',H,'commodity price dependence','low')],
'1.3':[L('geo-option-global-interdependence-s1.8.0',H,'prestige projects such as dams')],
'3.4':[L('geo-option-global-interdependence-s1.11.2',H,'Zambia copper dependence')],
'6.0':[L('geo-option-global-interdependence-s1.28.0',H,'Belt and Road Initiative')],
'7.3':[L('geo-economic-development-s1.15.2',H,'Irish unemployment 2012')],
'10.0':[L('geo-economic-development-s1.1.3',H,'GNI defined')],
'14.0':[L('geo-option-global-interdependence-s1.3.0',H,'Sachs and The End of Poverty')],
'20.6':[L('geo-option-global-interdependence-s1.18.0',E,'negative images of Africa')],
}
g3={
'2.5':[L('geo-economic-development-s4.3.0',H,'raw-material exports with low prices','low')],
'13.2':[L('geo-economic-development-s4.4.0',H,'subsidised rich-country exports dumped')],
'16.4':[L('geo-economic-development-s4.4.0',H,'farm subsidies undercut poor farmers')],
}
def need(l,pre=''):
    i,s,w,c=l
    return {'id':i if i.startswith('geo-') else S+i,'strength':s,'why':w,'confidence':c}
def build(links,withcost):
    out={}
    for i in ids:
        d={}
        if withcost: d['cost']=2 if i in two else 1
        d['needs']=[need(l) for l in links.get(i,[])]
        out[S+i]=d
    return out
paths=['geo-option-global-interdependence-s3.t1g1','geo-option-global-interdependence-s3.t1g2','geo-option-global-interdependence-s3.t1g3']
for p,l,wc in zip(paths,[g1,g2,g3],[True,False,False]):
    for k in l: assert k in ids,k
    o=build(l,wc)
    pk=open(P+'packs/'+p+'.txt').read()
    pids=set(re.findall(r'^\[([^\]]+)\]',pk,re.M))
    for t,d in o.items():
        assert t in pids
        for n in d['needs']:
            assert n['id'] in pids and n['id']!=t,(t,n['id'])
    json.dump(o,open(P+'point-links/'+p+'.json','w'),ensure_ascii=False,indent=1)
    nl=sum(len(d['needs']) for d in o.values())
    lo=sum(n['confidence']=='low' for d in o.values() for n in d['needs'])
    print(p,len(o),nl,sum(d.get('cost')==2 for d in o.values()),lo)
