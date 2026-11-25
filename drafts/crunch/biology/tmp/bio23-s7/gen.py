import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/biology/'
txt=open(P+'points/bio23-s7.txt').read()
tgt_part=txt.split('CANDIDATES')[0]
tids=re.findall(r'^\[([^\]]+)\]',tgt_part,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
E,H='essential','helpful'
def s(x): return 'bio23-s7.'+x
# id suffix -> (cost, [(id,strength,why,conf)])
D={
'1.3':(1,[(s('1.0'),E,'screening test definition','high'),(s('1.2'),H,'diagnostic test definition','high')]),
'2.0':(2,[('bio29-s4.9.0',E,'Rhesus positive and negative','high'),('bio29-s4.10.5',H,'anti-D injection','high')]),
'2.1':(1,[('bio29-s4.3.3',H,'anaemia and iron','high')]),
'2.2':(1,[('bio23-s5.6.3',H,'rubella harms foetus','high')]),
'2.3':(1,[('bio23-s5.6.3',H,'viruses crossing placenta','low')]),
'3.1':(2,[(s('3.0'),H,'blood pressure and urine tests','high')]),
'3.3':(1,[(s('3.2'),E,'gestational diabetes','high')]),
'4.1':(1,[('bio23-s5.6.b',H,'substances crossing placenta','high')]),
'5.1':(2,[('bio23-s5.5.2',E,'antibodies cross placenta','high')]),
'7.0':(2,[('bio23-s5.1.3',H,'ectopic pregnancy','high')]),
'7.1':(1,[('bio23-s5.2.1',H,'placenta position','low')]),
'7.3':(1,[(s('7.1'),H,'problem found at anomaly scan','low')]),
'8.1':(1,[(s('8.0'),E,'monitoring signs','high'),('bio23-s5.16.2',H,'Caesarean section','high')]),
'9.0':(1,[('bio11-s2.4.7',E,'carrier definition','high')]),
'9.1':(1,[(s('9.0'),H,'carrier testing','high')]),
'9.3':(2,[(s('6.0'),H,'ultrasound scanning','high'),(s('9.2'),H,'screening for Down syndrome','high')]),
'9.4':(1,[(s('9.3'),E,'combined test','high')]),
'9.5':(2,[('bio23-s5.2.1',H,'placenta','high')]),
'9.6':(1,[(s('1.3'),E,'positive screen needs diagnosis','high'),(s('9.2'),H,'trisomy conditions','low')]),
'9.7':(1,[(s('9.3'),E,'combined test components','high'),(s('9.5'),E,'NIPT blood sample','high')]),
'10.0':(2,[]),
'10.1':(1,[('bio23-s5.2.1',H,'placenta tissue','high')]),
'10.2':(1,[('bio23-s5.7.0',H,'amniotic fluid and sac','high')]),
'10.3':(1,[(s('10.1'),E,'CVS','high'),(s('10.2'),E,'amniocentesis','high')]),
'10.4':(2,[]),
'11.0':(2,[]),
'11.1':(1,[(s('11.0'),E,'Apgar score','high')]),
'13.0':(1,[(s('1.0'),H,'screening test','high')]),
'13.4':(1,[(s('13.0'),H,'heel-prick test','high'),(s('1.3'),E,'positive screen needs diagnosis','high')]),
'13.5':(2,[(s('14.1'),H,'phenylalanine in PKU','high')]),
'13.6':(1,[(s('13.5'),E,'why 3-5 days','high')]),
'14.1':(2,[]),
'14.2':(1,[('bio11-s2.4.1',E,'recessive allele','high')]),
'14.3':(1,[(s('14.1'),E,'phenylalanine and PKU','high')]),
'14.4':(1,[(s('14.1'),H,'phenylalanine','high')]),
'14.5':(1,[(s('14.1'),H,'phenylalanine build-up','high')]),
'14.6':(1,[(s('14.5'),H,'high phenylalanine harmful','high'),('bio23-s5.6.b',H,'substances reaching foetus','low')]),
'15.0':(1,[(s('13.0'),H,'heel-prick test','high')]),
'15.1':(2,[(s('15.0'),E,'CF screening','high')]),
'15.2':(1,[(s('15.0'),E,'cystic fibrosis','high')]),
'15.4':(1,[(s('15.3'),E,'congenital hypothyroidism','high')]),
'15.5':(2,[]),
'15.6':(1,[(s('15.5'),E,'galactosaemia','high')]),
'16.0':(1,[(s('2.1'),H,'anaemia','high'),(s('3.1'),H,'pre-eclampsia','high'),(s('3.2'),H,'gestational diabetes','high')]),
'16.1':(1,[(s('7.1'),H,'anomaly scan findings','high')]),
'16.3':(1,[(s('14.5'),H,'untreated PKU harm','high'),(s('15.6'),H,'galactosaemia treatment','low')]),
'16.4':(1,[(s('15.2'),H,'CF early treatment','high')]),
'16.5':(1,[(s('7.3'),H,'planning hospital birth','high')]),
'17.3':(1,[('bio23-s5.9.6',E,'lungs mature late','high')]),
'17.5':(1,[('bio23-s5.9.6',E,'late lung maturation','high')]),
'18.0':(1,[(s('1.1'),H,'screening not certain','high')]),
'18.1':(1,[(s('1.1'),H,'screening gives likelihood','high')]),
'18.2':(1,[(s('10.3'),E,'miscarriage risk of CVS','high')]),
'18.5':(1,[(s('17.0'),H,'premature baby care','low')]),
'19.1':(1,[(s('9.0'),H,'genetic screening','low')]),
'19.2':(1,[(s('9.2'),H,'Down syndrome screening','high')]),
'19.4':(1,[(s('13.0'),H,'blood-spot card','high')]),
}
out={}
for i in tids:
    c,n=D.get(i[len('bio23-s7.'):],(1,[]))
    out[i]={'cost':c,'needs':[{'id':a,'strength':b,'why':w,'confidence':f} for a,b,w,f in n]}
for k in D:
    assert s(k) in out,k
for k,v in out.items():
    for n in v['needs']: assert n['id'] in allids and n['id']!=k,(k,n['id'])
json.dump(out,open(P+'point-links/bio23-s7.json','w'),indent=1)
r=json.load(open(P+'point-links/bio23-s7.json'))
assert list(r)==tids and len(set(tids))==len(tids)
print(len(r),sum(len(v['needs']) for v in r.values()),sum(v['cost']==2 for v in r.values()),sum(n['confidence']=='low' for v in r.values() for n in v['needs']))
