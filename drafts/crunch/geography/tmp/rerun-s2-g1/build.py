import json,re
P='geo-economic-activities-s2.'
def full(i): return 'geo-economic-activities-'+i if i.startswith('s1.') else P+i
two=set('0.0 0.1 2.1 3.0 3.1 3.6 4.1 6.0 9.1 12.0 12.3 14.3 15.1 16.0 18.1 19.0 20.0 20.1 21.1 22.0 22.2 24.1 25.1 27.1 28.1 29.0 11.7'.split())
# fix: item ids use section.index; 2.1 = energy is 2.1? no: energy is 2.1 only as id 2.1
S={}
def n(k,*a): S[k]=a
E,H='essential','helpful'
n('0.b'); n('0.0',('0.b',H,'Weber least-cost principle'))
n('0.1',('0.b',H,'Weber least-cost principle'))
n('0.2',('0.0',E,'bulk-reducing pull to raw material'),('0.1',E,'bulk-gaining pull to market'))
for k in '1.b 1.0 1.1 1.2 1.3 1.4 1.5 1.6 1.7 2.b 2.1 2.2 2.4'.split(): n(k)
S['2.0']=(('0.0',E,'weight-losing raw materials'),)
S['2.3']=(('1.0',H,'footloose high-tech firms'),)
S['2.4']=(('2.3',H,'high-tech graduates example','L'),)
n('3.b'); n('3.0',('0.1',H,'bulk-gaining goods near market')); n('3.1'); n('3.2',('s1.23.4',H,'Brexit effects on trade'))
for k in '3.3 3.4 3.5 3.6'.split(): n(k)
n('3.7',('3.6',H,'freight modes','L'))
n('4.b'); n('4.0'); n('4.1'); n('4.2',('s1.5.2',H,'12.5% corporation tax')); 
for k in '4.3 4.4 4.5 4.6'.split(): n(k)
n('4.7',('3.0',H,'access to markets','L'))
for k in '5.b 5.0 5.1 5.2 5.3'.split(): n(k)
n('6.b'); n('6.0',('1.5',E,'cluster definition')); n('6.1',('6.0',E,'clusters form by agglomeration'))
for k in '6.2 6.3 6.4 7.b 7.0'.split(): n(k)
n('7.1',('7.0',H,'Corrib project')); n('7.2',('7.1',H,'local opposition to Corrib'))
n('8.b'); n('8.0',('2.1',H,'energy and coalfields')); n('8.1',('3.0',H,'markets as factor','L')); n('8.2',('1.0',E,'footloose definition'))
n('9.b',('0.0',H,'bulk-reducing industry')); n('9.0'); n('9.1',('0.0',E,'bulk-reducing rule'))
n('9.2'); n('9.3',('3.1',H,'deep-water ports for bulk carriers')); n('9.4',('5.2',H,'hazardous industry away from homes','L'))
n('9.5',('4.4',H,'government support policy','L')); n('9.6'); n('9.7')
n('10.b',('3.1',H,'deep-water ports')); n('10.0',('2.1',H,'energy as location factor')); n('10.1',('10.0',E,'Moneypoint coal station'))
n('11.b',('1.0',E,'footloose definition')); n('11.0')
n('11.1',('2.3',H,'graduate labour factor')); n('11.2',('4.1',H,'IDA support'),('4.2',H,'low corporation tax'))
n('11.3',('3.0',H,'EU single market access')); n('11.4',('3.7',H,'motorway and airport links')); n('11.5',('1.3',E,'greenfield site definition'))
n('11.6',('1.0',H,'footloose meaning')); n('11.7',('1.1',E,'branch plant parent decisions'))
n('12.b',('6.0',E,'agglomeration clustering')); n('12.0'); n('12.1',('3.1',H,'deep-water ports')); n('12.2',('5.0',H,'large flat site'))
n('12.3',('2.3',H,'graduate labour')); n('12.4',('6.0',H,'clustering')); n('12.5'); n('12.6')
n('13.b',('6.0',H,'cluster formation')); n('13.0'); n('13.1',('21.3',E,'DEC Galway closure')); n('13.2'); n('13.3')
n('14.b',('0.0',E,'bulk-reducing processing'),('0.1',E,'bulk-gaining brewing'))
n('14.0'); n('14.1',('0.0',E,'bulk-reducing rule')); n('14.2'); n('14.3',('0.0',E,'bulk-reducing rule'),('14.2',H,'Killybegs fishing port'))
n('14.4'); n('14.5',('0.1',E,'bulk-gaining rule')); n('14.6',('6.3',E,'industrial inertia definition'))
n('15.b',('2.1',H,'energy as location factor')); n('15.0'); n('15.1',('2.1',H,'power demand of data centres')); n('15.2'); n('15.3',('6.0',H,'clusters of tech firms'))
n('16.b',('1.0',H,'footloose activities')); n('16.0',('3.6',H,'freight modes')); n('16.1'); n('16.2'); n('16.3',('3.0',H,'EU single market')); n('16.4')
n('17.b',('1.1',E,'branch plant definition')); n('17.0'); n('17.1',('1.2',E,'headquarters definition')); n('17.2',('4.2',H,'tax incentives'))
n('18.b',('1.1',E,'branch plant definition')); n('18.0',('3.0',H,'market access')); n('18.1',('3.0',E,'EU single market access'))
n('18.2'); n('18.3',('2.3',H,'skilled labour')); n('18.4',('6.0',E,'cluster sharing skills')); n('18.5',('4.2',H,'low corporation tax'))
n('19.b',('1.1',E,'branch plant definition')); 
for k in '19.0 19.1 19.2 19.3 19.4'.split(): n(k)
n('19.5',('22.3',H,'decline stage of life cycle'))
n('20.b',('19.b',H,'closure versus survival of branch plant')); n('20.0',('1.2',E,'R&D term'))
n('20.1',('20.0',E,'moving up value chain'),('11.0',H,'Intel Leixlip example'))
n('21.b',('1.1',H,'branch plant')); n('21.0'); n('21.1',('19.1',H,'relocation to lower-cost country'))
n('21.2',('18.1',H,'EU trade bloc access','L')); n('21.3'); n('21.4')
n('22.b'); n('22.0',('1.2',E,'HQ and R&D')); n('22.1',('1.1',E,'branch plants')); n('22.2',('16.2',H,'standardised low-skilled production')); n('22.3')
n('23.b',('20.0',H,'plant changing role')); n('23.0'); n('23.1',('19.2',H,'outsourcing to contract manufacturers')); n('23.2',('1.2',E,'headquarters definition'))
n('24.b'); n('24.0',('22.0',H,'early life-cycle stage')); n('24.1',('2.3',H,'graduate labour')); n('24.2',('2.3',H,'graduate labour'))
n('25.b'); n('25.0',('1.0',H,'footloose activities')); n('25.1'); n('25.2',('25.1',E,'teleservices definition'),('3.7',H,'broadband access'))
n('25.3',('25.1',E,'teleservices definition')); n('25.4')
n('26.b'); n('26.0'); n('26.1',('26.0',H,'e-commerce meaning')); n('26.2',('26.0',E,'e-commerce meaning')); n('26.3')
n('27.b'); n('27.0'); n('27.1',('3.7',H,'broadband and rural access')); n('27.2',('27.0',H,'remote working')); n('27.3'); n('27.4',('27.1',H,'broadband coverage'))
n('28.b'); n('28.0'); n('28.1',('2.2',E,'labour cost as location factor'))
n('29.b'); n('29.0'); n('29.1'); n('29.2'); n('29.3',('29.0',E,'answer structure'))
n('30.b'); n('30.0',('5.0',H,'flat site requirements')); n('30.1',('3.6',H,'freight transport modes')); n('30.2',('2.2',H,'labour factor')); n('30.3',('1.4',E,'industrial estate definition'))
n('31.b',('0.0',E,'bulk-reducing raw material')); n('31.0',('14.3',H,'fish processing at ports')); n('31.1'); n('31.2'); n('31.3',('5.0',H,'flat site'))
n('32.b'); n('32.0'); n('32.1'); n('32.2',('3.7',H,'road access')); n('32.3')
n('33.b',('29.3',E,'reason against structure')); n('33.0',('5.0',H,'flat site requirements')); n('33.1'); n('33.2',('4.5',H,'planning permission')); n('33.3')
n('34.b'); n('34.0',('29.0',E,'reason with evidence structure')); n('34.1',('29.1',E,'explain why factor matters')); n('34.2',('29.3',E,'reason against structure'))
n('35.b',('29.0',H,'map and photograph answer method')); n('35.0',('s2.35.1',H,'accepted notation for photographs'))
S['2.3']=(); S['2.4']=(('11.1',H,'Intel graduate labour example','L'),); S['35.0']=(('35.1',H,'accepted notation for photographs'),)
two.discard('11.7')
pack=open('packs/geo-economic-activities-s2.t1g1.txt').read()
tgt=[]
for l in pack.split('CANDIDATES')[0].splitlines():
    m=re.match(r'\[(geo-[^\]]+)\]',l)
    if m: tgt.append(m.group(1))
allids=set(re.findall(r'^\[(geo-[^\]]+)\]',pack,re.M))
out={};nl=lo=0
for t in tgt:
    k=t[len(P):]
    assert k in S,k
    needs=[]
    for a in S[k]:
        i=full(a[0]); assert i in allids and i!=t,(k,i)
        needs.append({'id':i,'strength':a[1],'why':a[2],'confidence':'low' if len(a)>3 else 'high'})
    nl+=len(needs); lo+=sum(x['confidence']=='low' for x in needs)
    out[t]={'cost':2 if k in two else 1,'needs':needs}
assert not set(S)-{t[len(P):] for t in tgt}
json.dump(out,open('point-links/geo-economic-activities-s2.t1g1.json','w'),indent=1)
chk=json.load(open('point-links/geo-economic-activities-s2.t1g1.json'))
print(len(chk),nl,sum(v['cost']==2 for v in chk.values()),lo)
