import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/biology/'
txt=open(P+'points/bio11-s5.txt').read()
ids=re.findall(r'^\[([^\]]+)\]',txt,re.M)
tgt=txt.split('CANDIDATES')[0]
tids=re.findall(r'^\[([^\]]+)\]',tgt,re.M)
# item: cost, [(id,E/H,why,H/L)]
T="""
0.b|1
0.0|1|bio11-s2.2.2:H:two alleles on homologous pair:H
0.1|1|bio16-s2.1.1:E:homologues separate in meiosis:H
0.2|1|bio11-s2.1.4:H:fertilisation forms zygote:H
0.3|1
1.b|1
1.0|1|bio11-s2.2.4:E:homozygous means identical alleles:H
1.1|1|bio11-s5.0.1:E:one allele per gamete:H
1.2|1|bio11-s2.2.4:E:pure-breeding is homozygous:H
2.b|1
2.0|1|bio11-s2.2.0:H:alleles of one gene:H
2.1|1|bio11-s2.6.3:H:linkage:H
2.2|1
2.3|1|bio11-s5.2.2:E:P generation:H
2.4|1|bio11-s5.2.3:E:F1 generation:H
2.5|1|bio11-s5.2.3:H:offspring of a cross:L
3.b|1
3.0|1|bio11-s2.4.0:E:dominant and recessive alleles:H
3.1|1
3.2|1
3.3|1|bio11-s5.3.0:H:choosing allele symbols:H
4.b|1
4.0|1|bio11-s5.3.3:H:the key:H
4.1|1|bio11-s2.3.1:E:phenotype meaning:H
4.2|1|bio11-s2.3.0:E:genotype meaning:H
4.3|1|bio11-s5.1.1:E:gametes each parent makes:H
4.4|1|bio11-s5.4.3:E:gametes combined in grid:H
4.5|1|bio11-s5.4.4:E:square gives genotypes:H
4.6|1|bio11-s5.4.5:E:genotypes give phenotypes:H
5.b|1
5.0|1|bio11-s5.4.3:E:gametes placed on grid:H
5.1|1|bio11-s5.5.0:E:rows and columns of gametes:H
5.2|1|bio11-s5.1.1:H:two gametes per heterozygote:L
5.3|2|bio11-s5.5.1:E:filling boxes of square:H
6.b|1
6.0|1
6.1|1
6.2|1|bio11-s5.7.6:H:3 to 1 ratio example:L
6.3|1
6.4|1|bio11-s5.6.0:H:ratio is a prediction:H
7.b|1|bio11-s5.4.b:H:standard layout of steps:H
7.0|1|bio11-s5.3.3:H:writing a key:H
7.1|1
7.2|1|bio11-s5.1.1:E:heterozygote makes two gametes:H
7.3|1|bio11-s5.1.1:E:heterozygote makes both gametes:H
7.4|1|bio11-s5.5.1:E:filling the Punnett square:H
7.5|1|bio11-s5.7.4:E:counting boxes of square:H
7.6|1|bio11-s5.7.5:E:genotypes give phenotypes:H
7.7|2|bio11-s5.7.6:E:which offspring are tall:H
8.b|1
8.0|1|bio11-s2.4.0:E:dominant masks recessive:H
8.1|2|bio11-s2.4.1:E:recessive hidden in heterozygote:H
9.b|1|bio11-s5.1.2:H:true-breeding is homozygous:H
9.0|1|bio11-s5.1.2:E:true-breeding meaning:H
9.1|1|bio11-s2.2.4:H:homozygous genotypes:H
9.2|1|bio11-s5.1.0:E:homozygote makes one gamete:H
9.3|1|bio11-s5.9.2:E:one gamete from each parent:H
9.4|1|bio11-s2.4.0:E:dominant masks recessive:H
9.5|2|bio11-s5.2.3:E:F1 generation:H
9.6|1
10.b|1
10.0|1
10.1|1|bio11-s5.1.1:H:heterozygote makes two gametes:H
10.2|1|bio11-s5.1.0:E:homozygote makes one gamete:H
10.3|1|bio11-s5.5.0:E:Punnett square layout:H
10.4|1|bio11-s5.10.3:E:genotypes from square:H
10.5|1|bio11-s5.10.4:E:phenotypes from genotypes:H
11.b|1
11.0|1|bio11-s5.1.0:E:homozygote makes one gamete:H
11.1|1|bio11-s5.1.1:E:heterozygote gametes:H
11.2|1|bio11-s5.9.3:H:TT x tt result:H
11.3|1|bio11-s5.7.5:H:Tt x Tt result:H
11.4|1|bio11-s5.10.4:H:Tt x tt result:H
11.5|1|bio11-s5.1.0:E:homozygote makes one gamete:H
12.b|1
12.0|2|bio11-s5.11.3:E:Tt x Tt gives 3 to 1:H
12.1|2|bio11-s5.11.4:E:Tt x tt gives 1 to 1:H
12.2|2|bio11-s2.4.1:E:recessive shows only as homozygote:H
13.b|1|bio11-s2.3.6:H:genotype not seen from phenotype:H
13.0|2|bio11-s2.3.6:E:finding unknown genotype:H
13.1|2|bio11-s5.1.0:E:tt gives only t:H
13.2|1|bio11-s5.9.3:E:TT x tt gives all Tt:H
13.3|2|bio11-s5.10.5:E:Tt x tt gives 1 to 1:H
13.4|1|bio11-s5.6.4:H:chance in small samples:H
14.b|1|bio11-s2.4.7:H:carrier meaning:H
14.0|1|bio11-s2.4.1:H:recessive allele:H
14.1|1|bio11-s5.3.0:H:dominant capital, recessive lower:L
14.2|1|bio11-s2.4.7:E:carrier meaning:H
14.3|1|bio11-s5.14.1:E:key for F and f:H
14.4|1|bio11-s5.1.1:E:heterozygote makes both gametes:H
14.5|1|bio11-s5.14.4:E:combining gametes:H
14.6|1|bio11-s5.14.5:E:genotypes give phenotypes:H
14.7|2|bio11-s5.14.5:E:read chances from genotype ratio:H
14.8|1
"""
out={}
for l in T.strip().split('\n'):
    p=l.split('|'); k='bio11-s5.'+p[0]
    needs=[]
    for n in p[2:]:
        i,s,w,c=n.split(':')
        needs.append({"id":i,"strength":"essential" if s=='E' else "helpful","why":w,"confidence":"high" if c=='H' else "low"})
    out[k]={"cost":int(p[1]),"needs":needs}
assert list(out)==tids,(set(tids)^set(out))
for k,v in out.items():
    for n in v['needs']: assert n['id'] in ids and n['id']!=k,(k,n)
json.dump(out,open(P+'point-links/bio11-s5.json','w'),indent=1)
json.load(open(P+'point-links/bio11-s5.json'))
L=sum(len(v['needs']) for v in out.values())
print(len(out),L,sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
