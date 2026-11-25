import json,re
P='bio27-s5.'
D={}
def n(i,c,*l):
    D[P+i]=(c,[(x if '-' in x else P+x,s,w,f) for x,s,w,f in l])
H,E,h,l='high','essential','helpful','low'
for i in range(18): n(f'{i}.b',1)
n('0.0',2); n('0.1',1,('0.0',h,'balanced diet definition',H))
n('0.2',2,('0.0',h,'balanced diet needs',H),('bio8-s4.2.6',h,'iron-deficiency anaemia',H),('bio8-s5.3.3',h,'rickets from low vitamin D',H))
n('0.3',1,('0.2',h,'malnutrition definition',H)); n('0.4',1)
n('0.5',2,('0.4',E,'energy balance',H),('bio8-s3.0.4',h,'glycogen as store',H),('bio8-s3.3.5',h,'protein respired last',l))
n('1.0',1,('0.0',E,'balanced diet',H)); n('1.1',2,('1.0',E,'Food Pyramid shelves',H))
n('1.2',2,('1.0',E,'Food Pyramid shelves',H)); n('1.3',1,('1.0',E,'Food Pyramid shelves',H))
n('2.0',1); n('2.1',2,('2.0',E,'BMI formula',H)); n('2.2',1,('2.0',h,'what BMI measures',H))
n('2.3',1,('2.1',h,'adult BMI categories',H)); n('2.4',1,('2.0',E,'BMI formula',H))
n('3.0',2,('bio8-s3.3.1',h,'insulin hormone',l)); n('3.1',2,('bio8-s4.3.2',h,'salt and blood pressure',H),('bio8-s4.2.6',h,'iron and anaemia',H))
n('3.2',2,('bio8-s3.3.7',h,'protein for growth',H),('bio8-s5.3.1',h,'vitamin D and calcium',H))
n('3.3',1,('3.2',h,'growing needs',H),('1.2',E,'5 dairy servings',H))
n('3.4',2,('bio8-s5.3.4',h,'osteoporosis',H)); n('3.5',2,('bio8-s4.2.7',h,'iron loss in menstruation',H))
n('3.6',1,('bio8-s5.5.4',h,'folic acid in pregnancy',H),('bio8-s5.1.6',h,'vitamin A toxicity',H))
n('3.7',2,('0.4',h,'energy balance',H),('bio8-s3.0.4',h,'glycogen stores',H))
n('4.0',2,('bio8-s3.6.6',h,'essential amino acids',H)); n('4.1',1,('4.0',h,'varied diet',H))
n('4.2',2,('bio8-s3.6.6',E,'essential amino acids, combining proteins',H))
n('5.0',1); n('5.1',2); n('5.2',1,('5.1',h,'dehydration signs',H)); n('5.3',1,('11.0',E,'free sugars defined',H))
n('6.0',1,('bio8-s3.0.6',h,'cellulose in cell walls',H)); n('6.1',1,('6.0',h,'what fibre is',H))
n('6.2',2,('6.0',E,'fibre definition',H)); n('6.3',1,('6.0',h,'fibre',H)); n('6.4',1,('6.0',h,'fibre',H)); n('6.5',1,('6.0',h,'fibre',H)); n('6.6',1,('6.0',h,'fibre',H))
n('7.0',1); n('7.1',1,('7.0',h,'research question',H)); n('7.2',1,('7.1',h,'finding sources',H))
n('7.3',2,('7.1',h,'sources',l)); n('7.4',1,('7.3',E,'observational vs trial evidence',H))
n('7.5',1); n('7.6',1,('7.3',h,'evidence type',l)); n('7.7',2,('7.2',E,'funding bias',H))
n('8.0',2); n('8.1',2,('8.0',E,'vegetarian and vegan definitions',H)); n('8.2',1,('8.0',h,'diet types',H))
n('8.3',1); n('8.4',1)
n('9.0',1,('bio8-s5.5.3',h,'B12 only in animal food',H)); n('9.1',1,('bio8-s5.2.1',h,'vitamin C aids iron absorption',H))
n('9.2',1,('bio8-s4.2.0',h,'calcium roles',l)); n('9.3',1,('bio8-s4.4.0',h,'iodine and thyroxine',l)); n('9.4',1)
n('9.5',1,('bio8-s3.6.6',h,'essential amino acids',H)); n('9.6',1,('3.3',h,'teenage needs',l))
n('10.0',2,('8.0',h,'vegetarian and vegan',H)); n('10.1',1,('7.3',E,'observational study limits',H)); n('10.2',1,('8.0',h,'diet types',l))
n('11.0',2); n('11.1',1,('11.0',E,'free sugars',H))
n('12.0',1); n('12.1',2,('0.5',E,'excess energy stored as fat',H)); n('12.2',1); n('12.3',1)
n('12.4',1,('bio8-s3.0.1',h,'brain uses glucose',H)); n('12.5',1,('11.0',E,'free sugars',H)); n('12.6',1); n('12.7',1)
n('13.0',2); n('13.1',1,('13.0',h,'saturated fats',H)); n('13.2',1,('13.0',E,'saturated fat risk',H))
n('13.3',2,('bio8-s5.1.1',h,'fat-soluble vitamin absorption',H)); n('13.4',1,('bio8-s3.1.1',h,'fat energy per gram',H))
n('14.0',2,('bio8-s3.3.6',E,'deamination and urea',H)); n('14.1',1); n('14.2',1,('13.0',h,'saturated fat',H))
n('15.0',1); n('15.1',2,('15.0',E,'poor nutrient profile',H)); n('15.2',1,('15.0',h,'processed foods',H))
n('16.0',1,('3.0',h,'coeliac disease',H)); n('16.1',1,('16.0',h,'who needs these diets',H))
n('17.0',1,('bio8-s3.0.5',h,'glycogen store use',l)); n('17.1',1,('17.0',h,'crash diets',H))
out={k:{"cost":c,"needs":[{"id":i,"strength":s,"why":w,"confidence":f} for i,s,w,f in L]} for k,(c,L) in D.items()}
txt=open('/Users/gabrielwhelan/barebones/drafts/crunch/biology/points/bio27-s5.txt').read()
ids=re.findall(r'^\[([^\]]+)\]',txt,re.M)
tg=[i for i in ids if i.startswith(P)]
miss=[i for i in tg if i not in out]; extra=[k for k in out if k not in tg]
bad=[x['id'] for v in out.values() for x in v['needs'] if x['id'] not in ids or x['id']==0]
selfl=[k for k,v in out.items() if any(x['id']==k for x in v['needs'])]
print(miss,extra,bad,selfl)
ordered={k:out[k] for k in tg}
json.dump(ordered,open('/Users/gabrielwhelan/barebones/drafts/crunch/biology/point-links/bio27-s5.json','w'),indent=0)
v=list(ordered.values())
print(len(v),sum(len(x['needs']) for x in v),sum(x['cost']==2 for x in v),sum(n['confidence']=='low' for x in v for n in x['needs']))
