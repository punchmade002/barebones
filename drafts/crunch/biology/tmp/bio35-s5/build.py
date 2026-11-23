import json,re
B='/Users/gabrielwhelan/barebones/drafts/crunch/biology/'
txt=open(B+'points/bio35-s5.txt').read()
ids=re.findall(r'^\[([^\]]+)\]',txt,re.M)
tgt=[i for i in ids if i.startswith('bio35-s5.')]
P='bio35-s5.'
E,H='essential','helpful'
# id suffix -> (cost, [(full-or-short id, strength, why, conf)])
S={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),
'0.2':(2,[('bio35-s4.0.0',H,'what sequencing reads','high')]),
'0.3':(1,[]),
'0.4':(1,[('bio35-s4.0.3',H,'Human Genome Project','high')]),
'1.b':(1,[]),
'1.0':(1,[('bio35-s4.0.0',H,'DNA sequence as string of bases','low')]),
'1.1':(2,[('1.0',E,'aligned matching sequences','high')]),
'1.2':(1,[('1.0',H,'similar sequences found by alignment','high')]),
'1.3':(1,[('1.0',H,'finding similar sequences','high')]),
'2.b':(1,[]),
'2.0':(1,[('bio35-s4.0.3',H,'reference sequence','high')]),
'2.1':(1,[('2.0',E,'variant defined','high')]),
'2.2':(2,[('2.0',E,'variant flagged against reference','high'),('bio17-s3.5.1',H,'GAG to GUG sickle-cell change','high')]),
'2.3':(1,[('bio17-s3.5.1',H,'sickle-cell amino acid change','high')]),
'2.4':(2,[('2.2',H,'GTG example codon','high')]),
'3.b':(1,[]),
'3.0':(1,[('2.0',H,'comparing genome with reference','high')]),
'3.1':(1,[('bio11-s5.14.2',H,'carrier defined','low')]),
'3.2':(1,[('bio17-s3.0.0',H,'mutation defined','low')]),
'3.3':(1,[]),'3.4':(1,[]),
'4.b':(1,[]),'4.0':(1,[]),'4.1':(1,[]),'4.2':(1,[]),
'4.3':(2,[]),'4.4':(1,[]),'4.5':(1,[]),'4.6':(1,[]),
'5.b':(1,[]),
'5.0':(1,[('4.0',E,'OMIM website','high')]),
'5.1':(2,[('5.0',E,'search step before results','high')]),
'5.2':(1,[('5.1',E,'entry symbols and MIM numbers','high')]),
'5.3':(2,[('5.2',E,'disease entry opened','high'),('6.5',H,'reading cytogenetic band','high')]),
'5.4':(1,[('5.3',E,'same phenotype-gene table','high'),('5.1',H,'* means gene entry','high')]),
'6.b':(1,[]),'6.0':(1,[('5.2',E,'disease entry opened','high')]),
'6.1':(2,[('5.4',E,'link to gene entry','high')]),
'6.2':(1,[('5.3',H,'location and inheritance columns','high')]),
'6.3':(1,[('5.0',H,'repeat search steps','low')]),
'6.4':(2,[('8.0',H,'NCBI Gene lookup','high')]),
'6.5':(2,[('5.3',H,'cytogenetic band location','high')]),
'7.b':(1,[]),
'7.0':(1,[('bio11-s5.14.0',H,'autosomal recessive inheritance','low')]),
'7.1':(2,[('bio17-s3.6.1',H,'F508del deletion','high')]),
'7.2':(1,[('bio17-s3.6.0',H,'CFTR chloride channel','high')]),
'7.3':(1,[]),'7.4':(2,[]),
'7.5':(2,[('7.4',E,'CAG repeat expansion','high')]),
'7.6':(1,[('bio17-s3.5.0',H,'beta-globin sickle-cell gene','high')]),
'7.7':(1,[('bio17-s3.5.1',H,'glutamic acid to valine','high')]),
'8.b':(1,[]),
'8.0':(1,[('4.3',E,'NCBI Gene database','high')]),
'8.1':(1,[('8.0',H,'Gene record opened','high')]),
'8.2':(2,[('4.3',E,'ClinVar database','high')]),
'8.3':(1,[('8.2',E,'pathogenic classification','high')]),
'8.4':(1,[('4.5',H,'Ensembl genome browser','high')]),
'8.5':(2,[('8.4',E,'Ensembl gene page','high')]),
'8.6':(1,[('4.6',H,'cross-species comparison in Ensembl','high')]),
'9.b':(1,[]),'9.0':(1,[]),
'9.1':(2,[('5.3',H,'AR and AD inheritance','low')]),
'9.2':(1,[('7.1',H,'many alleles of one gene','low')]),
'9.3':(1,[('8.2',H,'ClinVar uncertain significance','high')]),
'9.4':(2,[('9.0',H,'contrast with single-gene disease','low')]),
'9.5':(1,[]),'9.6':(1,[]),
}
def full(x): return x if x.startswith('bio') else P+x
out={}
for t in tgt:
    c,n=S[t[len(P):]]
    out[t]={"cost":c,"needs":[{"id":full(i),"strength":s,"why":w,"confidence":cf} for i,s,w,cf in n]}
json.dump(out,open(B+'point-links/bio35-s5.json','w'),indent=1)
d=json.load(open(B+'point-links/bio35-s5.json'))
assert list(d)==tgt and len(tgt)==len(S)
for k,v in d.items():
    for n in v['needs']: assert n['id'] in ids and n['id']!=k,(k,n)
L=[n for v in d.values() for n in v['needs']]
print(len(d),len(L),sum(v['cost']==2 for v in d.values()),sum(n['confidence']=='low' for n in L))
