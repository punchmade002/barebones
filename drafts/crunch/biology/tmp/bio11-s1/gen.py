import json,re
P='bio11-s1.'
E,H='essential','helpful'
def n(i,s,w,c='high'): return (i if '-' in i else P[:-1]+'.'+i if False else i,s,w,c)
d={
'0.b':(1,[]),
'0.0':(1,[('bio10-s2.0.0',H,'gene as coded instruction','low')]),
'0.1':(1,[('bio11-s1.0.0',E,'chromosome as DNA plus protein','high')]),
'0.2':(1,[('bio11-s1.0.1',E,'chromatin state being condensed','high')]),
'0.3':(2,[('bio11-s1.0.0',E,'chromosome definition','high')]),
'0.4':(2,[('bio11-s1.0.3',E,'chromosomes in pairs','high'),('bio11-s1.3.0',H,'genes at same positions','low')]),
'0.5':(1,[('bio11-s1.0.3',H,'human chromosome number','high')]),
'0.6':(2,[('bio10-s1.2.1',H,'base pairs','low'),('bio11-s1.0.3',H,'23 chromosomes in a set','high')]),
'0.7':(2,[('bio10-s1.4.3',H,'bacterial DNA loop and plasmids','high'),('bio11-s1.1.0',H,'histones','low')]),
'1.b':(1,[('bio11-s1.0.6',H,'DNA length versus nucleus size','high')]),
'1.0':(1,[('bio10-s1.1.1',E,'negative phosphate backbone','high')]),
'1.1':(2,[('bio11-s1.1.0',E,'histones bind DNA','high')]),
'1.2':(1,[('bio11-s1.1.1',E,'nucleosome string','high')]),
'1.3':(2,[('bio11-s1.0.6',H,'need to pack long DNA','high')]),
'1.4':(2,[('bio11-s1.1.1',E,'DNA wound on nucleosomes','high'),('bio10-s2.1.3',H,'reading gene into mRNA','low')]),
'1.5':(2,[('bio11-s1.1.4',E,'histones switching genes on or off','high')]),
'1.6':(2,[('bio11-s1.1.1',E,'nucleosome structure','high')]),
'2.b':(1,[]),
'2.0':(1,[('bio10-s1.4.1',H,'DNA copied before division','high')]),
'2.1':(1,[('bio11-s1.2.0',E,'chromatids from replication','high')]),
'2.2':(2,[('bio11-s1.2.1',E,'sister chromatids','high')]),
'2.3':(1,[('bio11-s1.2.2',H,'chromatids separate at centromere','high')]),
'2.4':(1,[('bio11-s1.2.2',E,'centromere','high')]),
'2.5':(2,[('bio11-s1.2.0',E,'replication gives chromatids','high')]),
'2.6':(2,[('bio11-s1.2.1',E,'sister chromatids identical','high'),('bio11-s1.0.4',H,'homologous chromosomes','high')]),
'2.7':(2,[('bio11-s1.2.5',E,'replicated chromosome shape','high'),('bio11-s1.3.1',H,'locus','high')]),
'3.b':(1,[]),
'3.0':(1,[('bio10-s2.0.0',H,'gene codes for protein','low')]),
'3.1':(1,[('bio11-s1.3.0',E,'gene on chromosome','high')]),
'3.2':(2,[('bio11-s1.3.0',E,'gene codes for protein','high'),('bio10-s1.6.5',H,'tRNA and rRNA','high')]),
'3.3':(1,[('bio11-s1.3.0',E,'gene as protein code','high')]),
'3.4':(1,[('bio11-s1.3.0',H,'protein-coding genes','high')]),
'3.5':(2,[('bio11-s1.0.4',E,'homologous chromosomes carry same genes','high')]),
'4.b':(1,[]),
'4.0':(1,[('bio11-s1.3.0',E,'gene codes for protein','high')]),
'4.1':(1,[('bio11-s1.4.0',E,'coding versus non-coding DNA','high')]),
'4.2':(1,[('bio11-s1.3.0',H,'genes and expression','high')]),
'4.3':(2,[('bio10-s1.6.5',H,'rRNA and tRNA','high'),('bio11-s1.4.1',E,'non-coding DNA','high')]),
'4.4':(2,[('bio11-s1.2.2',H,'centromere','high')]),
'4.5':(1,[('bio11-s1.4.2',H,'regulating genes','high')]),
'4.6':(1,[('bio11-s1.4.4',H,'repeated sequences','high')]),
'4.7':(2,[('bio11-s1.4.3',H,'introns and gene structure','low')]),
}
out={}
for k,(c,ns) in d.items():
    out['bio11-s1.'+k]={'cost':c,'needs':[{'id':i,'strength':s,'why':w,'confidence':f} for i,s,w,f in ns]}
json.dump(out,open('point-links/bio11-s1.json','w'),indent=1)
pk=open('points/bio11-s1.txt').read()
ids=set(re.findall(r'^\[([^\]]+)\]',pk,re.M))
tg=re.findall(r'^\[(bio11-s1\.[^\]]+)\]',pk,re.M)
assert list(out)==tg,(set(tg)^set(out))
for k,v in out.items():
    for x in v['needs']: assert x['id'] in ids and x['id']!=k,(k,x)
L=[x for v in out.values() for x in v['needs']]
print(len(out),len(L),sum(v['cost']==2 for v in out.values()),sum(x['confidence']=='low' for x in L))
