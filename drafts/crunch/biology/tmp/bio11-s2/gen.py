import json,re
E,H="essential","helpful"
d={
"0.b":(1,[]),"0.0":(1,[]),"0.1":(1,[("s2.0.0",E,"species definition",1)]),
"0.2":(1,[]),"0.3":(1,[("s2.0.2",H,"heredity",1)]),
"0.4":(1,[("bio11-s1.0.4",H,"homologous chromosomes",1)]),
"1.b":(1,[]),"1.0":(1,[]),
"1.1":(2,[("s2.0.4",E,"chromosome pairs, one set",1),("s2.1.4",H,"fertilisation adds sets",1)]),
"1.2":(1,[("s2.1.0",E,"gametes",1)]),"1.3":(1,[("s2.1.0",H,"gametes",1)]),
"1.4":(2,[("s2.1.1",E,"haploid gametes fuse",1)]),
"1.5":(1,[("s2.1.4",E,"zygote",1)]),"1.6":(2,[("s2.1.4",E,"life cycle stages",1)]),
"2.b":(1,[]),
"2.0":(2,[("bio11-s1.3.1",E,"locus",1),("s2.0.2",H,"gene",1)]),
"2.1":(1,[("s2.2.0",E,"alleles",1)]),"2.2":(1,[("s2.2.0",E,"alleles",1)]),
"2.3":(1,[("s2.2.2",E,"two alleles per gene",1)]),
"2.4":(1,[("s2.2.0",E,"alleles",1)]),"2.5":(1,[("s2.2.0",E,"alleles",1)]),
"2.6":(2,[("s2.2.0",E,"alleles and locus",1),("bio11-s1.3.1",H,"locus",1)]),
"3.b":(1,[]),"3.0":(1,[("s2.2.0",E,"alleles",1)]),
"3.1":(1,[("s2.3.0",E,"genotype",1)]),"3.2":(1,[("s2.3.1",E,"phenotype",1)]),
"3.3":(1,[("s2.3.2",E,"genotype and environment",1)]),
"3.4":(1,[("s2.3.2",E,"environment affects phenotype",1)]),
"3.5":(1,[("s2.3.2",E,"environment affects phenotype",1)]),
"3.6":(2,[("s2.4.0",E,"dominant allele masks",1)]),
"4.b":(1,[]),"4.0":(1,[("s2.2.5",E,"heterozygote",1)]),
"4.1":(1,[("s2.2.4",E,"homozygous condition",1),("s2.4.0",H,"dominant contrast",1)]),
"4.2":(1,[("s2.4.1",E,"recessive allele",1)]),
"4.3":(2,[("s2.4.0",E,"dominant allele",1),("bio10-s2.0.2",H,"protein",1)]),
"4.4":(2,[("s2.4.3",E,"working protein allele",1)]),
"4.5":(1,[("s2.4.0",E,"dominant allele",1)]),
"4.6":(1,[("s2.4.1",E,"recessive allele",1),("s2.4.7",H,"carrier",1)]),
"4.7":(1,[("s2.4.1",E,"recessive allele",1)]),
"5.b":(1,[]),"5.0":(2,[("s2.0.2",E,"gene",1),("bio10-s2.1.4",H,"gene to protein",0)]),
"5.1":(1,[("s2.5.0",E,"gene expression",1)]),"5.2":(1,[("s2.5.0",E,"gene expression",1)]),
"5.3":(2,[("s2.5.0",E,"gene expression",1),("bio11-s1.4.2",H,"regulatory sequences",1)]),
"5.4":(1,[]),
"6.b":(1,[]),
"6.0":(2,[("s2.5.0",E,"gene expression",1),("bio11-s1.1.0",H,"histones",1)]),
"6.1":(1,[("s2.6.0",E,"epigenetic tags",1)]),
"6.2":(2,[("s2.4.0",E,"complete dominance",1)]),
"6.3":(2,[("bio11-s1.0.0",E,"genes on chromosomes",1)]),
"6.4":(2,[("bio11-s1.0.3",E,"sex chromosomes",1)]),
}
txt=open("points/bio11-s2.txt").read()
ids=re.findall(r"^\[([^\]]+)\]",txt,re.M)
allids=set(ids)
tids=[i for i in ids if i.startswith("bio11-s2.")]
out={}
for i in tids:
    c,n=d[i[len("bio11-s2."):]]
    out[i]={"cost":c,"needs":[{"id":(x if x.startswith("bio") else "bio11-"+x),"strength":s,"why":w,"confidence":"high" if cf else "low"} for x,s,w,cf in n]}
assert len(out)==len(tids)
for k,v in out.items():
    for n in v["needs"]: assert n["id"] in allids and n["id"]!=k,(k,n)
json.dump(out,open("point-links/bio11-s2.json","w"),indent=1)
o=json.load(open("point-links/bio11-s2.json"))
print(len(o),sum(len(v["needs"]) for v in o.values()),sum(v["cost"]==2 for v in o.values()),sum(n["confidence"]=="low" for v in o.values() for n in v["needs"]))
