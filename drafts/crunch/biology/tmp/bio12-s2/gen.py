import json,re
P='bio12-s2.'
E,H='essential','helpful'
# id: (cost, [(target, strength, why, conf)])
d={
'0.b':(1,[]),
'0.0':(1,[('bio11-s2.0.0',H,'species definition','high')]),
'0.1':(1,[('bio11-s2.2.0',H,'alleles as gene versions','high')]),
'0.2':(1,[]),
'0.3':(1,[(P+'0.2',E,'adaptation defined','high')]),
'0.4':(1,[(P+'0.2',E,'adaptation defined','high')]),
'0.5':(1,[(P+'0.2',E,'adaptation defined','high'),('bio12-s1.5.2',H,'lactase persistence mutation','low')]),
'0.6':(2,[(P+'0.2',E,'inherited favourable characteristics','high'),('bio12-s1.0.4',H,'only genetic variation selected','low')]),
'1.b':(1,[]),'1.0':(1,[]),
'1.1':(1,[('bio12-s1.0.0',H,'variation between individuals','low')]),
'1.2':(1,[]),
'1.3':(2,[(P+'1.1',E,'variation and island resemblance','high'),(P+'1.2',E,'fossils resembling living species','high')]),
'1.4':(1,[(P+'1.3',E,'observations needing explanation','high')]),
'2.b':(1,[]),'2.0':(1,[]),'2.1':(1,[]),
'2.2':(1,[(P+'0.6',H,'selection concept','low')]),
'2.3':(1,[]),
'2.4':(1,[(P+'2.3',H,'Wallace reached same idea','high')]),
'3.b':(1,[]),
'3.0':(1,[(P+'2.1',H,'Malthus on population growth','low')]),
'3.1':(1,[(P+'3.0',H,'overproduction creates competition','high')]),
'3.2':(2,[('bio12-s1.0.1',H,'genetic variation inherited','high')]),
'3.3':(2,[(P+'3.2',E,'inherited variation','high'),(P+'0.2',E,'adaptation to environment','high')]),
'3.4':(1,[(P+'3.3',E,'survivors are the fittest','high'),('bio11-s2.2.0',H,'alleles','high')]),
'3.5':(2,[(P+'3.4',E,'favourable alleles accumulate','high'),('bio11-s2.0.0',H,'species definition','low')]),
'3.6':(1,[(P+'0.0',H,'population evolves','high')]),
'3.7':(1,[(P+'4.0',H,'peppered moth example','low')]),
'4.b':(1,[]),
'4.0':(1,[('bio12-s1.3.0',H,'mutation as source of allele','high')]),
'4.1':(1,[(P+'4.0',E,'pale and dark forms','high')]),
'4.2':(1,[(P+'4.1',E,'prior pale camouflage','high')]),
'4.3':(2,[(P+'4.2',E,'dark moths camouflaged','high'),(P+'3.4',H,'inheritance of favourable allele','high')]),
'4.4':(1,[(P+'4.3',E,'dark form common earlier','high')]),
'5.b':(1,[]),
'5.0':(2,[('bio11-s2.0.2',H,'genes as DNA carrying traits','low')]),
'5.1':(2,[(P+'5.0',E,'common ancestors','high')]),
'5.2':(2,[(P+'0.2',E,'adaptation','high')]),
'5.3':(1,[(P+'5.2',E,'specialised organisms','high')]),
'6.b':(1,[]),
'6.0':(2,[(P+'0.6',E,'selection depends on environment','high')]),
'6.1':(2,[(P+'5.2',E,'specialised organisms','high'),(P+'6.0',H,'response to changed environment','high')]),
'6.2':(1,[(P+'6.1',H,'contrast with specialists','high')]),
'6.3':(2,[('bio12-s1.3.5',H,'fast reproducers accumulate mutations','low')]),
'6.4':(2,[(P+'6.3',E,'fast evolution of short-generation organisms','high'),('bio12-s1.3.5',H,'antibiotic resistance','low')]),
'7.b':(1,[(P+'2.2',H,'breeders selecting animals','low')]),
'7.0':(1,[(P+'7.b',E,'artificial selection','high')]),
'7.1':(1,[(P+'7.b',E,'artificial selection','high')]),
'7.2':(1,[(P+'7.b',E,'artificial selection','high')]),
'7.3':(2,[(P+'7.b',E,'artificial selection','high'),(P+'0.6',E,'natural selection','high')]),
'8.b':(1,[(P+'7.b',E,'artificial selection','high'),(P+'0.6',E,'natural selection','high')]),
'8.0':(1,[(P+'0.6',E,'natural selection','high'),(P+'7.b',E,'artificial selection','high')]),
'8.1':(1,[(P+'0.2',H,'adaptation increases survival','high')]),
'8.2':(1,[(P+'7.b',H,'strong human choice','low')]),
'8.3':(2,[(P+'3.5',E,'speciation','high'),(P+'0.2',H,'adaptation','low')]),
'8.4':(2,[('bio12-s1.2.6',H,'Irish potato example','high'),('bio12-s1.0.1',H,'genetic variation','low')]),
'8.5':(1,[('bio12-s1.0.1',H,'inherited variation','high')]),
'9.b':(1,[]),
'9.0':(1,[('bio11-s2.0.2',H,'heredity','low')]),
'9.1':(1,[('bio11-s2.1.2',H,'parents contribute chromosomes','low')]),
'9.2':(2,[(P+'9.1',E,'blending inheritance','high'),('bio11-s2.0.2',H,'genes as units','low')]),
'9.3':(1,[('bio12-s1.3.0',E,'mutation changes DNA','high')]),
'9.4':(2,[(P+'0.1',E,'allele frequency change','high'),('bio12-s1.7.4',H,'mutation and sexual variation','high')]),
'10.b':(1,[]),
'10.0':(1,[(P+'1.2',H,'fossils','low')]),
'10.1':(2,[(P+'10.0',E,'criticisms answered','high')]),
'10.2':(1,[(P+'1.4',H,'fixed separate creation idea','high')]),
'10.3':(1,[]),
}
txt=open('points/bio12-s2.txt').read()
ids=re.findall(r'^\[([^\]]+)\]',txt,re.M)
out={}
for i in ids:
    if not i.startswith(P): continue
    c,n=d[i[len(P):]]
    out[i]={'cost':c,'needs':[{'id':t,'strength':s,'why':w,'confidence':f} for t,s,w,f in n]}
allids=set(ids)
assert [k for k in d]==[k[len(P):] for k in out], 'order/coverage'
for k,v in out.items():
    for n in v['needs']: assert n['id'] in allids and n['id']!=k,(k,n)
json.dump(out,open('point-links/bio12-s2.json','w'),indent=1)
json.load(open('point-links/bio12-s2.json'))
nl=sum(len(v['needs']) for v in out.values())
print(len(out),nl,sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
