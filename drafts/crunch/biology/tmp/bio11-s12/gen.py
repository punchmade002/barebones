import json,re
P='bio11-s12.'
E,H='essential','helpful'
d={ # id: (cost, [(need,strength,why,conf)])
'0.b':(1,[]),'0.0':(1,[]),'0.1':(2,[]),
'0.2':(1,[('0.1',H,'alleles of a gene','high')]),
'0.3':(1,[('0.1',H,'alleles of a gene','high')]),
'0.4':(1,[('bio11-s5.2.0',H,'monohybrid cross prediction','high')]),
'0.5':(1,[('0.1',H,'alleles as gene versions','low')]),
'0.6':(1,[('0.5',E,'single-gene trait','high')]),
'1.b':(1,[]),
'1.0':(2,[('bio11-s5.14.7',H,'carrier cross gives 1 in 4','high')]),
'1.1':(1,[('1.0',H,'predicting risk from genotypes','high')]),
'1.2':(1,[('bio11-s5.14.2',H,'carriers of recessive allele','high')]),
'1.3':(1,[('bio11-s5.14.0',H,'cystic fibrosis is recessive','high')]),
'1.4':(1,[('0.2',H,'recessive vs dominant alleles','high')]),
'1.5':(1,[('0.2',E,'dominant allele','high')]),
'1.6':(2,[('6.2',H,'sex-linked genes','high')]),
'2.b':(1,[]),
'2.0':(2,[('bio11-s5.13.0',E,'test cross method','high')]),
'2.1':(1,[('bio11-s5.1.2',H,'true-breeding means homozygous','high')]),
'2.2':(1,[('2.1',H,'true-breeding varieties','low')]),
'2.3':(1,[('0.3',E,'independent assortment principle','high')]),
'3.b':(1,[]),
'3.0':(2,[('0.1',E,'segregation of alleles in gametes','high')]),
'3.1':(2,[('0.2',E,'recessive alleles hidden by dominant','high')]),
'3.2':(1,[('0.0',H,'single-gene disorders','low')]),
'3.3':(1,[('3.2',E,'test result identifies allele','high')]),
'4.b':(1,[]),
'4.0':(1,[('0.5',H,'contrast with single-gene traits','low')]),
'4.1':(2,[('4.0',E,'polygenic traits','high'),('0.6',H,'discontinuous variation contrast','high')]),
'4.2':(2,[('4.0',H,'multiple genes affecting a trait','low')]),
'4.3':(1,[('4.2',E,'gene interaction','high'),('0.4',H,'simple Mendelian ratios','low')]),
'4.4':(1,[]),
'4.5':(1,[('4.4',E,'genotype plus environment','high')]),
'4.6':(1,[('4.4',E,'genotype plus environment','high')]),
'4.7':(1,[('4.4',H,'environment affects phenotype','high'),('0.4',H,'Mendelian ratios','high')]),
'5.b':(1,[]),
'5.0':(1,[('4.0',H,'many genes affect traits','high')]),
'5.1':(1,[('5.0',E,'multifactorial risk','high')]),
'5.2':(2,[('bio11-s4.1.0',E,'epigenetics and gene expression','high')]),
'6.b':(1,[]),
'6.0':(1,[('0.3',E,'independent assortment','high')]),
'6.1':(2,[('0.2',E,'dominance','high'),('bio11-s5.2.4',H,'F2 generation','high')]),
'6.2':(1,[('1.6',H,'sex-linked genes','low')]),
'6.3':(1,[('0.1',H,'alleles','high'),('4.0',H,'polygenic contrast','high')]),
'7.b':(1,[]),
'7.0':(2,[('0.1',H,'alleles passed in gametes','low')]),
'7.1':(1,[('bio11-s5.6.0',H,'ratio as prediction','high')]),
'7.2':(1,[('7.1',E,'predictions are probabilities','high'),('bio11-s5.6.4',H,'small samples vary','high')]),
'7.3':(1,[('7.1',H,'probability not certainty','high')]),
'8.b':(1,[]),
'8.0':(1,[('0.0',H,'Mendelian genetics scope','high')]),
'8.1':(1,[('4.0',H,'complex traits','high'),('5.0',H,'common diseases multifactorial','high')]),
'8.2':(2,[('4.0',H,'polygenic risk','high'),('4.4',H,'gene-environment interaction','high'),('5.2',H,'epigenetics','high')]),
}
f=lambda i:i if i.startswith('bio') else P+i
out={P+k:{'cost':c,'needs':[{'id':f(i),'strength':s,'why':w,'confidence':q} for i,s,w,q in n]} for k,(c,n) in d.items()}
json.dump(out,open('../../point-links/bio11-s12.json','w'),indent=1)
txt=open('../../points/bio11-s12.txt').read()
tg=re.findall(r'^\[(bio11-s12\.[^\]]+)\]',txt.split('CANDIDATES')[0],re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
assert list(out)==tg,(set(tg)^set(out))
assert all(n['id'] in allids and n['id']!=k for k,v in out.items() for n in v['needs'])
L=[n for v in out.values() for n in v['needs']]
print(len(out),len(L),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for n in L))
