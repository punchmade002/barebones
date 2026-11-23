import json,re
P='bio35-s2.'
H,E='helpful','essential'
d={}
def a(i,c,*n):
    d[P+i]={"cost":c,"needs":[{"id":(x[0] if '-' in x[0] else P+x[0]),"strength":x[1],"why":x[2],"confidence":x[3] if len(x)>3 else "high"} for x in n]}
a('0.b',1);a('0.0',1)
a('0.1',1,('0.0',H,'what a profile is'))
a('0.2',1);
a('0.3',2,('bio35-s3.4.0',H,'PCR copying repeat regions'),('1.1',H,'repeat regions'))
a('0.4',2,('4.b',H,'gel electrophoresis separation'))
a('1.b',1,('bio11-s1.4.1',H,'non-coding DNA'))
a('1.0',1,('bio11-s1.4.1',E,'non-coding DNA'))
a('1.1',2,('1.0',H,'non-coding DNA'),('bio10-s1.0.4',H,'DNA bases'))
a('1.2',2,('bio11-s1.3.1',E,'locus'),('1.1',E,'repeat sequences'))
a('1.3',1,('1.0',H,'non-coding DNA basis'))
a('2.b',1,('bio11-s1.0.4',H,'homologous chromosome pairs'))
a('2.0',1,('bio11-s1.3.1',E,'locus'),('bio11-s1.0.4',H,'chromosome from each parent'))
a('2.1',2,('2.0',E,'two copies of locus'),('bio11-s1.3.5',H,'alleles'))
a('2.2',1,('2.1',E,'two bands per locus'))
a('3.b',1);
a('3.0',1,('1.2',H,'locus'))
a('3.1',1,('3.0',E,'many loci tested'))
a('3.2',1,('0.2',H,'identical twins same DNA'))
a('4.b',1);a('4.0',1)
a('4.1',2,('bio10-s1.1.1',H,'phosphate backbone','low'))
a('4.2',2,('4.1',H,'movement in electric field'),('1.2',H,'repeats set length'))
a('4.3',1,('bio35-s3.9.4',H,'DNA ladder'))
a('4.4',2,('4.2',H,'size separation'))
a('4.5',2,('4.2',E,'shorter fragments travel further'))
a('5.b',1)
a('5.0',1,('4.0',H,'bands as fragments'))
a('5.1',1,('5.0',E,'match rule'))
a('5.2',2,('2.2',E,'child bands from each parent'),('5.1',H,'exclusion logic'))
for k in ['6.b','6.0','6.1','6.2','7.b','7.2','7.3']: a(k,1)
a('7.0',1,('0.0',H,'profile comparison'))
a('7.1',1,('5.1',E,'exclusion'))
a('7.4',1,('5.2',H,'paternity matching'))
a('8.b',1);a('8.0',1)
a('8.1',2);a('8.2',2,('8.1',E,'mitochondrial DNA female line'))
a('8.3',1)
for k in ['9.b','9.0','9.1','9.2','9.3','9.4','10.b']: a(k,1)
a('10.0',1,('1.0',H,'non-coding DNA'))
a('10.1',1,('bio11-s1.3.0',H,'gene and allele','low'))
a('11.b',1);a('11.0',1);a('11.1',1)
a('11.2',2,('3.2',H,'identical twin exception','low'))
a('11.3',1);a('11.4',1)
t=open('points/bio35-s2.txt').read()
tg=re.findall(r'^\[(bio35-s2\.[^\]]+)\]',t.split('CANDIDATES')[0],re.M)
allid=set(re.findall(r'^\[([^\]]+)\]',t,re.M))
assert list(d)==tg,(set(tg)^set(d))
for v in d.values():
    for n in v['needs']: assert n['id'] in allid,n
json.dump(d,open('point-links/bio35-s2.json','w'),indent=1)
n=[x for v in d.values() for x in v['needs']]
print(len(d),len(n),sum(v['cost']==2 for v in d.values()),sum(x['confidence']=='low' for x in n))
