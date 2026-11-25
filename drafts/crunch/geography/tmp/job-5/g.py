import re,json
P='geo-economic-activities-s2.'
A='geo-aerial-photographs-s1.'
txt=open('packs/geo-economic-activities-s2.t1g4.txt').read()
ids=re.findall(r'^\[([^\]]+)\]',txt,re.M)
tg=[i for i in ids if i.startswith(P)]
E,H='essential','helpful'
L={ # id: [(target,strength,why,conf)]
'0.2':[('0.0',E,'bulk-reducing pulls to raw material','high'),('0.1',E,'bulk-gaining pulls to market','high')],
'1.1':[('1.2',H,'headquarters','high')],
'2.0':[('0.0',E,'weight-losing raw materials','high')],
'2.3':[('2.2',H,'labour skills and wages','high')],
'2.4':[('11.0',H,'Intel Leixlip example','high'),('13.0',H,'Galway cluster example','high')],
'3.0':[('0.1',H,'bulk-gaining goods near market','high')],
'3.7':[('1.7',H,'infrastructure','high')],
'4.1':[('1.4',H,'serviced sites, estates','low')],
'5.3':[('1.7',H,'infrastructure services','low')],
'6.0':[('1.5',H,'cluster/agglomeration term','high')],
'6.1':[('6.0',E,'clusters through agglomeration','high')],
'7.1':[('7.0',H,'Corrib project','high')],
'7.2':[('7.1',H,'local opposition campaign','high')],
'8.0':[('2.0',H,'raw materials factor','high')],
'8.1':[('3.0',H,'markets factor','high'),('2.2',H,'labour factor','low')],
'8.2':[('1.0',E,'footloose industry','high')],
'9.b':[('0.0',E,'bulk-reducing industry','high')],
'9.1':[('0.0',E,'bulk-reducing principle','high')],
'9.3':[('3.1',H,'deep-water ports, bulk carriers','high')],
'9.4':[('5.0',H,'flat site for plant','high'),('5.2',H,'hazardous industry away from homes','low')],
'9.5':[('4.4',H,'government support/regional policy','low')],
'10.b':[('9.3',H,'deep water serves estuary','low')],
'10.0':[('2.1',H,'energy as location factor','low')],
'10.1':[('10.0',E,'Moneypoint coal station','high')],
'11.b':[('1.0',E,'footloose industry','high')],
'11.1':[('2.3',E,'skilled graduates for high-tech','high')],
'11.2':[('4.1',E,'IDA support','high'),('4.2',E,'corporation tax','high')],
'11.3':[('3.0',E,'EU single market access','high')],
'11.4':[('3.7',H,'motorway connections','high'),('3.5',H,'Dublin Airport','low')],
'11.5':[('1.3',E,'greenfield site','high'),('5.0',H,'site requirements','low')],
'11.6':[('1.0',E,'footloose meaning','high')],
'11.7':[('1.1',E,'branch plant','high'),('17.1',H,'distant headquarters decisions','high')],
'12.b':[('6.0',H,'agglomeration clustering','high')],
'12.1':[('3.1',H,'deep-water ports','high')],
'12.2':[('5.0',H,'flat site needs','high')],
'12.3':[('2.3',H,'graduates for skilled labour','high')],
'12.4':[('4.1',E,'IDA support','high'),('6.0',E,'clustering','high')],
'13.1':[('21.3',E,'DEC Galway closure','high')],
'13.2':[('6.0',H,'cluster supplier network','low')],
'14.b':[('0.0',E,'bulk-reducing','high'),('0.1',E,'bulk-gaining','high')],
'14.1':[('0.0',E,'bulk-reducing dairy','high')],
'14.3':[('0.0',E,'bulk-reducing','high'),('14.2',H,'Killybegs port','high')],
'14.5':[('0.1',E,'bulk-gaining','high')],
'14.6':[('6.3',E,'industrial inertia','high')],
'15.b':[('2.1',E,'energy need','high'),('1.0',H,'footloose activity','low')],
'15.1':[('15.0',H,'data centre electricity use','low'),('2.1',H,'energy as factor','low')],
'15.3':[('3.7',H,'fibre links','low')],
'16.2':[('2.3',H,'low-wage assembly','low')],
'16.3':[('3.0',H,'EU single market','high')],
'17.b':[('1.1',H,'branch plant','high')],
'17.1':[('1.1',E,'branch plant','high'),('1.2',E,'headquarters','high')],
'17.2':[('4.2',H,'tax incentives','low')],
'18.b':[('1.1',H,'branch plant','high')],
'18.0':[('3.0',H,'markets','low')],
'18.1':[('3.0',H,'EU single market','high')],
'18.3':[('2.3',H,'skilled labour','high')],
'18.4':[('6.0',E,'cluster agglomeration','high')],
'18.5':[('4.2',H,'corporation tax','high')],
'19.1':[('18.2',H,'lower costs motive','low')],
'19.5':[('22.3',H,'decline stage','low')],
'20.0':[('1.2',E,'R&D','high')],
'20.1':[('20.0',E,'moving up value chain','high')],
'21.1':[('19.1',H,'relocation to lower costs','high')],
'21.2':[('21.1',H,'Dell move to Poland','high')],
'22.0':[('1.2',E,'HQ and R&D','high')],
'22.1':[('1.1',H,'branch plants','high')],
'22.2':[('2.3',H,'low-wage standardised work','low')],
'23.1':[('19.2',E,'outsourcing to contract makers','high')],
'23.2':[('1.2',E,'headquarters','high')],
'24.0':[('22.0',H,'product life cycle','low')],
'24.1':[('2.3',H,'skilled labour','low')],
'24.2':[('2.3',H,'graduates as labour','high')],
'25.1':[('25.0',H,'footloose services','low')],
'25.2':[('25.1',E,'teleservices','high'),('3.7',E,'broadband','high')],
'25.3':[('25.1',E,'teleservices','high'),('19.3',H,'automation','high')],
'26.1':[('26.0',H,'e-commerce','high'),('3.7',H,'motorways','low')],
'26.2':[('26.0',E,'e-commerce','high')],
'27.1':[('3.7',H,'broadband','high')],
'27.2':[('27.0',H,'remote working','high')],
'27.4':[('27.1',H,'broadband rollout','high')],
'28.1':[('19.3',E,'automation','high'),('2.2',H,'labour cost','high')],
'29.0':[(A+'3.2',E,'accepted notation','high'),(A+'10.0',H,'grid reference','high')],
'29.3':[('29.0',H,'same answer structure','high')],
'30.0':[('5.0',E,'flat land site','high')],
'30.1':[('3.6',H,'freight transport modes','low')],
'30.2':[('2.2',H,'labour force','high')],
'30.3':[('1.4',H,'industrial estate','high')],
'31.b':[('0.0',E,'bulk-reducing','high')],
'31.0':[('14.3',H,'fish processing at ports','high')],
'31.1':[('3.6',H,'road freight','low')],
'31.3':[('5.0',H,'flat site','high')],
'33.0':[('5.0',H,'flat site','high')],
'33.2':[('4.5',H,'planning permission','low')],
'34.0':[('29.0',E,'grid reference evidence','high'),('30.0',H,'flat land factor','high')],
'34.1':[('5.0',E,'site needs','high')],
'34.2':[('29.3',E,'reason against structure','high'),('33.1',E,'floodplain','high')],
'35.0':[(A+'3.2',E,'accepted notation','high')],
}
out={}
for i in tg:
    k=i[len(P):]
    k=k[:-2] if k.endswith('.b') and False else k
    key=k.replace('.b','.b')
    lk=L.get(k) or L.get(k)
    out[i]={"needs":[{"id":(t if t.startswith('geo-') else P+t),"strength":s,"why":w,"confidence":c} for t,s,w,c in (L.get(k,[]))]}
json.dump(out,open('point-links/geo-economic-activities-s2.t1g4.json','w'),indent=1)
d=json.load(open('point-links/geo-economic-activities-s2.t1g4.json'))
assert list(d)==tg and len(set(tg))==len(tg)
n=0;lo=0
for i,v in d.items():
    for x in v['needs']:
        assert x['id'] in ids and x['id']!=i,(i,x);n+=1;lo+=x['confidence']=='low'
assert all(P+k in tg for k in L),[k for k in L if P+k not in tg]
print(len(tg),n,lo)
