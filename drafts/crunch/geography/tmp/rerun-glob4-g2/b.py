import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
txt=open(P+'packs/geo-economic-globalisation-s4.t1g2.txt').read()
ids=re.findall(r'^\[([^\]]+)\]',txt,re.M)
T='geo-economic-globalisation-s4.'
tg=[i for i in ids if i.startswith(T)]
D='geo-economic-development-'
H,E='helpful','essential'
L={ # id suffix -> list of (cand,strength,why,conf)
'4.1':[(D+'s2.2.2',H,'uses the Blue Banana','high')],
'5.1':[(D+'s2.12.1',H,'South Korea export-led industrialisation','low')],
'6.1':[(D+'s3.0.4',H,'colonies supplied raw materials','high')],
'6.2':[(D+'s2.11.2',H,'cumulative causation model','high')],
'6.3':[(D+'s2.11.2',H,'builds on cumulative causation','high')],
'6.4':[(D+'s2.2.2',H,'Blue Banana core belt','high')],
'7.0':[(D+'s3.0.4',H,'colonies exported raw materials','high')],
'7.1':[(D+'s3.1.0',H,'railways built for export','high')],
'7.2':[(D+'s3.1.4',H,'colonial borders drawn in Europe','high')],
'7.3':[(D+'s3.2.1',H,'neo-colonial dependence on raw materials','low')],
'8.0':[(D+'s2.11.3',H,'spread effects','high')],
'8.1':[(D+'s2.12.1',H,'export-led industrialisation','low')],
'8.2':[(D+'s2.15.1',H,'Ireland attracting foreign firms','high')],
'8.3':[(D+'s2.0.0',H,'the Brandt Line','high')],
'9.0':[(D+'s2.7.4',H,'Nigeria oil dependence','high')],
'9.2':[(D+'s2.7.5',H,'DR Congo cobalt','high')],
'9.3':[(D+'s3.27.2',H,'Sudan war since 2023','high')],
'9.4':[(D+'s3.23.3',H,'South Sudan independence 2011','high')],
'9.5':[(D+'s3.23.3',E,'South Sudan separate since 2011','high')],
'10.0':[(D+'s2.8.6',H,'infrastructure and development','low')],
'10.1':[(D+'s2.7.0',H,'landlocked countries','high')],
'10.2':[(D+'s2.10.2',H,'corruption deters investment','low')],
'10.3':[(D+'s2.8.2',H,'education and productivity','low')],
'10.5':[(D+'s2.10.5',H,'debt repayments cost development','high')],
'10.6':[(D+'s3.0.4',H,'colonial raw material export economies','high')],
'10.7':[(D+'s2.10.5',H,'tariffs disadvantage poor exporters','low')],
'11.0':[(D+'s2.10.5',H,'debt burden','low')],
'12.5':[(D+'s3.2.5',H,'WTO and trading blocs','low')],
'15.0':[(D+'s3.8.0',H,'Five-Year Plan','high')],
'15.1':[(D+'s3.8.1',H,'import substitution behind tariffs','high')],
'15.2':[(D+'s3.8.3',H,'Licence Raj','high')],
'15.3':[(D+'s3.10.0',H,'1991 reserves crisis','high')],
'15.4':[(D+'s3.10.2',H,'1991 reforms','high')],
'16.0':[(D+'s3.11.1',H,'Bengaluru IT industry','low')],
'16.1':[(D+'s3.11.1',H,'IT outsourcing in Bengaluru','high')],
'16.5':[(D+'s3.11.2',H,'Make in India','high')],
'16.6':[(D+'s3.11.0',H,'services over half of GDP','high')],
'17.0':[(D+'s3.12.2',H,'inequality between states','high')],
'17.3':[(D+'s3.12.0',H,'informal sector','high')],
'18.0':[(D+'s2.13.0',H,'Deng Xiaoping reforms','high')],
'18.1':[(D+'s2.13.1',H,'Shenzhen SEZ','high')],
'18.2':[(D+'s2.13.2',H,'China joining WTO','high')],
'18.4':[(D+'s2.13.3',H,'800 million out of poverty','high')],
'18.5':[(D+'s2.13.5',H,'coastal-interior gap','high')],
}
out={}
for i in tg:
    k=i[len(T):]
    out[i]={"needs":[{"id":c,"strength":s,"why":w,"confidence":f} for c,s,w,f in L.get(k,[])]}
assert all(T+k in out for k in L), [k for k in L if T+k not in out]
json.dump(out,open(P+'point-links/geo-economic-globalisation-s4.t1g2.json','w'),indent=1)
o=json.load(open(P+'point-links/geo-economic-globalisation-s4.t1g2.json'))
assert list(o)==tg and len(set(tg))==len(tg)
n=[x for v in o.values() for x in v['needs']]
assert all(x['id'] in ids for x in n)
print(len(o),len(n),sum(x['confidence']=='low' for x in n))
