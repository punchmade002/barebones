import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/biology/'
txt=open(P+'points/bio11-s6.txt').read()
tgt,cand=txt.split('\nCANDIDATES',1)
tids=re.findall(r'^\[([^\]]+)\]',tgt,re.M)
allids=set(tids)|set(re.findall(r'^\[([^\]]+)\]',cand,re.M))
def L(i,s,w,c='high'):return {"id":i,"strength":s,"why":w,"confidence":c}
E,H='essential','helpful'
d={
"bio11-s6.0.b":(2,[L("bio11-s2.2.5",E,"heterozygote definition"),L("bio11-s2.4.0",E,"dominant allele masking")]),
"bio11-s6.0.0":(1,[L("bio11-s2.6.2",H,"intermediate heterozygote phenotype"),L("bio11-s2.2.4",H,"homozygote definition")]),
"bio11-s6.0.1":(1,[L("bio11-s2.3.0",E,"genotype versus phenotype"),L("bio11-s6.0.0",H,"intermediate phenotype","low")]),
"bio11-s6.0.2":(1,[L("bio11-s2.4.0",E,"complete dominance masking"),L("bio11-s2.3.6",H,"phenotype not revealing genotype")]),
"bio11-s6.0.3":(1,[L("bio11-s6.0.0",E,"in-between result defines incomplete dominance"),L("bio11-s2.2.3",H,"ABO has A, B alleles","low")]),
"bio11-s6.1.b":(1,[]),
"bio11-s6.1.0":(2,[L("bio11-s2.4.3",H,"allele codes for working protein"),L("bio11-s2.2.0",H,"allele definition")]),
"bio11-s6.1.1":(1,[L("bio11-s6.1.0",E,"red allele codes for enzyme")]),
"bio11-s6.1.2":(1,[L("bio11-s6.1.1",E,"working copies make pigment"),L("bio11-s2.2.5",H,"heterozygote definition")]),
"bio11-s6.1.3":(1,[L("bio11-s6.0.0",H,"pink heterozygote from red and white")]),
"bio11-s6.2.b":(1,[L("bio11-s5.3.0",H,"capital/lower-case allele symbols")]),
"bio11-s6.2.0":(1,[L("bio11-s5.3.0",E,"capital/lower-case dominance symbols")]),
"bio11-s6.2.1":(1,[L("bio11-s5.3.1",H,"use question's letters")]),
"bio11-s6.2.2":(2,[L("bio11-s5.3.3",H,"state a key first"),L("bio11-s5.3.2",H,"avoid look-alike letters","low")]),
"bio11-s6.2.3":(1,[L("bio11-s5.3.1",E,"follow question's letters")]),
"bio11-s6.3.b":(1,[L("bio11-s5.9.b",H,"true-breeding cross parallel","low")]),
"bio11-s6.3.0":(1,[L("bio11-s5.4.0",E,"step 1: the key")]),
"bio11-s6.3.1":(1,[L("bio11-s5.4.1",E,"step 2: parents' phenotypes")]),
"bio11-s6.3.2":(1,[L("bio11-s5.4.2",E,"step 3: parents' genotypes")]),
"bio11-s6.3.3":(1,[L("bio11-s5.4.3",E,"step 4: gametes"),L("bio11-s5.1.0",H,"homozygous makes one gamete")]),
"bio11-s6.3.4":(1,[L("bio11-s5.4.5",E,"step 6: offspring genotypes")]),
"bio11-s6.3.5":(1,[L("bio11-s5.4.6",E,"step 7: offspring phenotypes"),L("bio11-s6.0.0",E,"heterozygote is pink")]),
"bio11-s6.4.b":(2,[L("bio11-s5.4.b",E,"standard cross layout"),L("bio11-s6.3.5",H,"pink plants from first cross","low")]),
"bio11-s6.4.0":(1,[L("bio11-s5.4.1",E,"step 2: parents' phenotypes")]),
"bio11-s6.4.1":(1,[L("bio11-s5.4.2",E,"step 3: parents' genotypes")]),
"bio11-s6.4.2":(1,[L("bio11-s5.1.1",E,"heterozygote makes two gametes")]),
"bio11-s6.4.3":(2,[L("bio11-s5.5.b",E,"Punnett square method"),L("bio11-s5.5.0",H,"gamete placement in grid")]),
"bio11-s6.4.4":(1,[L("bio11-s5.7.5",H,"1:2:1 genotype ratio from square")]),
"bio11-s6.4.5":(1,[L("bio11-s5.4.6",E,"step 7: offspring phenotypes"),L("bio11-s6.0.1",H,"genotype shown by phenotype")]),
"bio11-s6.4.6":(2,[L("bio11-s5.5.3",E,"drawing Punnett square diagram")]),
"bio11-s6.5.b":(1,[L("bio11-s2.6.2",H,"incomplete dominance definition","low")]),
"bio11-s6.5.0":(1,[L("bio11-s5.8.0",H,"genotype versus phenotype ratio"),L("bio11-s6.4.5",H,"1 red:2 pink:1 white")]),
"bio11-s6.5.1":(2,[L("bio11-s5.8.0",E,"3:1 ratio from dominance masking"),L("bio11-s2.4.0",H,"dominant masks other allele")]),
"bio11-s6.5.2":(2,[L("bio11-s6.5.0",E,"1:2:1 phenotype ratio"),L("bio11-s5.12.0",H,"working back from ratio","low")]),
"bio11-s6.6.b":(1,[L("bio11-s5.10.b",H,"1:1 ratio from one heterozygote parent","low")]),
"bio11-s6.6.0":(1,[L("bio11-s5.4.2",E,"step 3: parents' genotypes")]),
"bio11-s6.6.1":(1,[L("bio11-s5.10.2",E,"homozygous parent gives one gamete")]),
"bio11-s6.6.2":(1,[L("bio11-s5.10.4",H,"1:1 genotype ratio")]),
"bio11-s6.6.3":(1,[L("bio11-s6.0.0",E,"RW is pink")]),
"bio11-s6.6.4":(2,[L("bio11-s6.6.0",H,"worked pink × white pattern"),L("bio11-s5.10.5",H,"1:1 ratio outcome","low")]),
"bio11-s6.7.b":(1,[]),
"bio11-s6.7.0":(1,[L("bio11-s2.6.2",E,"incomplete dominance definition")]),
"bio11-s6.7.1":(1,[L("bio11-s6.0.0",E,"heterozygote intermediate phenotype"),L("bio11-s6.3.4",H,"all heterozygous offspring")]),
"bio11-s6.7.2":(1,[L("bio11-s6.4.5",E,"1:2:1 cross of heterozygotes")]),
"bio11-s6.7.3":(1,[L("bio11-s6.5.1",E,"3:1 ratio for complete dominance")]),
"bio11-s6.7.4":(2,[L("bio11-s2.2.4",E,"pure-breeding means homozygous"),L("bio11-s6.7.2",E,"blue × blue gives black and white")]),
"bio11-s6.7.5":(1,[L("bio11-s6.7.1",E,"black × white gives all blue")]),
"bio11-s6.8.b":(1,[]),
"bio11-s6.8.0":(1,[L("bio11-s2.6.2",E,"incomplete dominance definition"),L("bio11-s2.4.0",H,"complete dominance")]),
"bio11-s6.8.1":(1,[L("bio11-s6.8.0",H,"two-gene cross")]),
}
assert list(d)==tids,(set(tids)^set(d))
out={}
n=0
for k,(c,ns) in d.items():
    for x in ns:
        assert x['id'] in allids and x['id']!=k,(k,x['id'])
        assert len(x['why'].split())<=8
    out[k]={"cost":c,"needs":ns}
json.dump(out,open(P+'point-links/bio11-s6.json','w'),indent=1)
o=json.load(open(P+'point-links/bio11-s6.json'))
ls=[x for v in o.values() for x in v['needs']]
print(len(o),len(ls),sum(v['cost']==2 for v in o.values()),sum(x['confidence']=='low' for x in ls))
