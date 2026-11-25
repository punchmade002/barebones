import re,json
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/packs/geo-economic-environment-s1.t1g1.txt'
O='/Users/gabrielwhelan/barebones/drafts/crunch/geography/point-links/geo-economic-environment-s1.t1g1.json'
txt=open(P).read().split('\nCANDIDATES')[0]
tids=re.findall(r'^\[([^\]]+)\]',txt,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',open(P).read(),re.M))
E='geo-economic-environment-s1.'
c2={'0.3','2.1','3.1','3.2','5.0','5.1','6.1','7.1','8.0','8.1','8.2','9.4','11.3','12.1','16.2','18.1','18.2'}
H,S='helpful','essential'
L={
'1.0':[('0.1',H,'fossil fuels are non-renewable','high')],
'1.1':[('1.0',H,'peat as a fossil fuel','low')],
'1.2':[('0.1',H,'uranium as finite non-renewable','low')],
'2.1':[('2.0',S,'electricity versus primary energy','high'),('4.1',H,'oil used for transport and heating','high')],
'2.4':[('2.3',H,'price shocks and supply cuts','high')],
'3.0':[('2.4',H,'energy imports and import bill','low'),('5.1',H,'Corrib gas coming ashore 2015','high')],
'3.1':[('3.0',S,'import dependence measure','high'),('5.2',H,'Corrib output declining','high')],
'3.2':[('2.0',H,'primary energy','high')],
'3.3':[('3.2',S,'adds up the energy mix','high')],
'4.0':[('2.4',H,'import bill and price shocks','high')],
'5.2':[('5.1',S,'Corrib field','high'),('3.0',H,'import dependence','high')],
'5.3':[('13.b',H,'interconnectors','high')],
'5.4':[('2.0',H,'electricity made from gas','low')],
'6.2':[('6.1',H,'Moneypoint station','high')],
'6.3':[('6.1',H,'Moneypoint station','high')],
'7.2':[('10.4',H,'biomass as renewable fuel','high')],
'7.3':[('9.2',H,'Bellacorick wind farm','high')],
'7.4':[('7.b',H,'cutaway bogs','high')],
'8.2':[('8.b',H,'turbines and hydroelectric power','low')],
'9.0':[('2.0',H,'electricity versus total energy','low')],
'9.4':[('9.3',H,'onshore and offshore wind','low')],
'10.2':[('0.2',H,'geothermal heat','high')],
'11.0':[('0.2',H,'renewable energy','low')],
'11.1':[('11.0',S,'the 16% target','high')],
'12.0':[('4.1',H,'oil used for transport','high')],
'12.1':[('4.1',H,'oil used for home heating','high')],
'12.3':[('8.3',H,'no hydro potential left','high')],
'12.4':[('9.4',H,'offshore wind','high')],
'13.0':[('13.b',H,'interconnectors','high')],
'13.1':[('13.b',H,'interconnectors','high')],
'13.2':[('5.3',H,'gas from Britain by pipeline','high')],
'14.1':[('2.0',H,'electricity generation','low')],
'16.2':[('16.1',H,'the invasion of Ukraine','high')],
'16.3':[('16.0',S,'Russia share before 2022','high')],
'17.0':[('1.2',H,'nuclear energy from uranium','low')],
'18.0':[('0.2',H,'renewable energy','low')],
'18.1':[('1.2',H,'nuclear power','low')],
'21.0':[('8.b',H,'hydroelectric power','high')],
'21.1':[('0.2',H,'geothermal heat','high')],
'22.2':[('22.1',H,'the 2030 target','low')],
'24.2':[('3.0',H,'import dependence','low')],
}
out={}
for i in tids:
    k=i[len(E):]
    d={'cost':2 if k in c2 else 1,'needs':[{'id':E+t,'strength':s,'why':w,'confidence':c} for t,s,w,c in L.get(k,[])]}
    out[i]=d
json.dump(out,open(O,'w'),indent=1)
o=json.load(open(O))
assert list(o)==tids and len(set(tids))==len(tids)
n=[x for v in o.values() for x in v['needs']]
assert all(x['id'] in allids and x['id'] not in o or x['id'] in allids for x in n)
assert all(x['id']!=k for k,v in o.items() for x in v['needs'])
print(len(o),len(n),sum(v['cost']==2 for v in o.values()),sum(x['confidence']=='low' for x in n))
