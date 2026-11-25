import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/biology/'
pk=open(P+'points/bio11-s8.txt').read()
tg=re.findall(r'^\[(bio11-s8\.[^\]]+)\]',pk.split('CANDIDATES')[0],re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',pk,re.M))
E,H='essential','helpful'
T='bio11-s8.'
d={ # id:(cost,[(need,strength,why,conf)])
'0.b':(1,[('bio11-s5.2.0',H,'monohybrid cross','high')]),
'0.0':(1,[('bio11-s5.2.0',H,'monohybrid cross, one trait','high')]),
'0.1':(2,[('bio11-s7.5.0',H,'independent assortment of genes','high')]),
'0.2':(1,[('bio11-s5.3.0',H,'dominant capital, recessive lower case','high')]),
'0.3':(1,[('bio11-s5.4.2',H,'writing genotypes','low')]),
'1.b':(1,[('bio11-s5.1.b',H,'gametes from homozygous/heterozygous parents','high')]),
'1.0':(1,[('bio11-s5.0.1',E,'gamete carries one allele per gene','high')]),
'1.1':(1,[(T+'1.0',E,'one allele of each gene per gamete','high')]),
'1.2':(2,[(T+'1.1',E,'pairing method for gametes','high'),('bio11-s7.5.0',H,'independent assortment statement','high')]),
'1.3':(2,[(T+'1.1',E,'gamete pairing method','high'),('bio11-s5.1.b',H,'heterozygous vs homozygous','high')]),
'1.4':(1,[(T+'1.3',E,'gamete count from heterozygous genes','high')]),
'2.b':(1,[('bio11-s5.9.b',H,'pure lines cross','low')]),
'2.0':(1,[('bio11-s5.1.2',E,'true-breeding means homozygous','high')]),
'2.1':(1,[('bio11-s5.1.2',H,'true-breeding homozygous','low')]),
'2.2':(1,[(T+'1.1',E,'gamete method','high')]),
'2.3':(1,[(T+'2.2',E,'gametes combine at fertilisation','high')]),
'2.4':(1,[('bio11-s5.9.4',H,'dominant masks recessive','high')]),
'3.b':(1,[(T+'1.4',E,'four gamete types','high'),('bio11-s5.5.b',H,'Punnett square','high')]),
'3.0':(1,[(T+'2.3',H,'F1 genotype RrYy','high')]),
'3.1':(1,[(T+'1.4',E,'gametes of double heterozygote','high')]),
'3.2':(1,[('bio11-s5.5.2',E,'each box equally likely','high')]),
'3.3':(2,[(T+'3.1',E,'gametes along top and side','high'),('bio11-s5.5.1',H,'filling Punnett square boxes','high')]),
'3.4':(2,[(T+'3.1',E,'gametes along top and side','high')]),
'3.5':(2,[(T+'3.4',E,'completed square to count','high')]),
'4.b':(1,[(T+'3.5',H,'F2 genotypes','low')]),
'4.0':(2,[(T+'3.5',E,'F2 genotype list','high'),('bio11-s5.8.0',H,'dominance masks genotype difference','low')]),
'4.1':(2,[(T+'4.0',E,'F2 phenotype counts','high')]),
'5.b':(1,[(T+'4.0',H,'F2 phenotypes','low')]),
'5.0':(1,[(T+'4.0',E,'F2 phenotypes','high')]),
'5.1':(1,[('bio11-s7.5.0',E,'independent assortment','high')]),
'5.2':(1,[(T+'4.0',E,'phenotype counts to mark','high'),(T+'3.3',H,'square contents','low')]),
'6.b':(1,[]),
'6.0':(2,[('bio11-s7.5.0',E,'genes independent','high'),('bio11-s5.7.6',H,'monohybrid 3:1','high')]),
'6.1':(1,[('bio11-s5.7.6',E,'monohybrid 3:1 ratio','high')]),
'6.2':(2,[(T+'6.1',E,'monohybrid fractions to multiply','high')]),
'6.3':(1,[(T+'6.0',H,'multiplication check','high')]),
'7.b':(1,[('bio11-s5.13.0',E,'test cross','high')]),
'7.0':(1,[('bio11-s5.13.0',E,'test cross','high')]),
'7.1':(1,[(T+'1.3',H,'rryy makes one gamete','high')]),
'7.2':(1,[(T+'7.1',E,'test cross gametes','high')]),
'7.3':(1,[(T+'7.2',E,'offspring genotypes','high')]),
'7.4':(2,[(T+'7.3',E,'1:1:1:1 test cross result','high')]),
'7.5':(1,[(T+'7.3',H,'same test cross pattern','high')]),
'8.b':(1,[(T+'1.3',H,'one heterozygous gene gives two gametes','low')]),
'8.0':(1,[(T+'1.3',H,'homozygous vs heterozygous gametes','low')]),
'8.1':(1,[(T+'1.1',E,'gamete method','high')]),
'8.2':(1,[(T+'3.2',H,'counting boxes as chances','low')]),
'8.3':(2,[(T+'8.2',E,'4x2 square','high')]),
'8.4':(1,[(T+'6.2',E,'multiply gene fractions','high')]),
'9.b':(1,[]),
'9.0':(1,[('bio11-s5.3.0',H,'dominant/recessive key','low')]),
'9.1':(1,[(T+'9.0',E,'snapdragon key','high')]),
'9.2':(1,[(T+'1.1',E,'gamete method','high')]),
'9.3':(1,[(T+'9.2',E,'gametes combined','high')]),
'9.4':(1,[(T+'9.3',E,'offspring list','high')]),
'9.5':(1,[(T+'9.1',H,'parent genotypes','low')]),
'9.6':(2,[(T+'9.5',E,'F1 parent genotype','high')]),
'9.7':(2,[(T+'6.0',E,'multiply independent genes','high')]),
}
out={}
for t in tg:
    c,n=d[t.replace(T,'')]
    out[t]={"cost":c,"needs":[{"id":i,"strength":s,"why":w,"confidence":f} for i,s,w,f in n]}
json.dump(out,open(P+'point-links/bio11-s8.json','w'),indent=1)
o=json.load(open(P+'point-links/bio11-s8.json'))
assert list(o)==tg and len(set(tg))==len(tg)
L=[n for v in o.values() for n in v['needs']]
assert all(n['id'] in allids for n in L)
assert all(n['id']!=k for k,v in o.items() for n in v['needs'])
print(len(o),len(L),sum(v['cost']==2 for v in o.values()),sum(n['confidence']=='low' for n in L))
