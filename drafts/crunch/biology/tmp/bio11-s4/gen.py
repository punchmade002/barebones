import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/biology/'
E,H='essential','helpful'
d={
'b':{}, }
raw={
'0.b':(1,[]),
'0.0':(1,[('bio10-s1.0.6',E,'base sequence as information','high'),('bio11-s2.1.0',H,'gametes pass DNA on','high')]),
'0.1':(1,[('bio10-s1.4.1',H,'DNA copied before division','high')]),
'0.2':(1,[('bio10-s1.0.6',H,'base sequence carries information','low')]),
'0.3':(1,[('bio11-s4.0.2',E,'mutation defined','high'),('bio11-s2.1.0',H,'gamete passes mutation on','low')]),
'0.4':(2,[('bio11-s2.5.2',E,'same genes, different expression','high'),('bio11-s2.6.0',H,'epigenetic expression defined','low')]),
'1.b':(1,[]),
'1.0':(1,[('bio11-s2.5.0',E,'gene expression','high')]),
'1.1':(1,[('bio11-s4.1.0',H,'epigenetics defined','high')]),
'1.2':(1,[('bio11-s4.1.1',H,'epigenetic marks','high')]),
'1.3':(1,[('bio11-s2.5.2',H,'specialised cells express some genes','high')]),
'1.4':(1,[('bio11-s4.1.1',H,'epigenetic marks added/removed','high')]),
'1.5':(2,[('bio11-s4.1.4',H,'reversible epigenetic marks','high')]),
'2.b':(1,[]),
'2.0':(2,[('bio11-s2.1.0',E,'gametes carry inheritance','high'),('bio11-s4.1.1',H,'epigenetic marks','high')]),
'2.1':(1,[('bio11-s4.2.0',H,'marks passed on in mammals','high')]),
'2.2':(2,[('bio11-s2.3.3',H,'identical twins, same genotype','high'),('bio11-s4.1.1',H,'epigenetic marks','high')]),
'2.3':(1,[('bio11-s4.2.2',H,'twins epigenetic differences','high')]),
'3.b':(1,[]),
'3.0':(2,[('bio10-s1.0.4',E,'cytosine base','high')]),
'3.1':(1,[('bio11-s4.3.0',E,'DNA methylation','high')]),
'3.2':(1,[('bio10-s1.2.1',E,'C pairs with G','high'),('bio11-s4.3.0',E,'methylated cytosine','high')]),
'3.3':(2,[('bio11-s2.6.0',H,'histones defined','high')]),
'3.4':(2,[('bio11-s4.3.3',E,'histone modification','high')]),
'3.5':(2,[('bio11-s4.3.1',E,'methylation silences genes','high'),('bio11-s4.3.4',E,'histone packing','high')]),
'3.6':(2,[('bio11-s4.3.5',E,'loose vs tight packing','high')]),
'4.b':(1,[]),
'4.0':(1,[('bio11-s4.1.0',E,'epigenetic change definition','high')]),
'4.1':(2,[('bio11-s4.0.2',H,'mutation as cause','high'),('bio11-s4.1.2',H,'epigenetic triggers','high')]),
'4.2':(1,[('bio11-s4.0.3',H,'mutations permanent','high'),('bio11-s4.1.4',H,'epigenetic reversibility','high')]),
'4.3':(1,[('bio11-s4.0.3',H,'mutation spreads slowly','low')]),
'4.4':(2,[('bio11-s4.2.0',E,'erasure of marks in mammals','high')]),
'4.5':(1,[('bio11-s4.1.3',H,'marks differ by cell type','low')]),
'4.6':(1,[('bio11-s4.1.3',H,'marks copied in mitosis','high')]),
'4.7':(1,[('bio11-s4.3.1',H,'methylation silences genes','high')]),
'5.b':(1,[]),
'5.0':(1,[]),
'5.1':(1,[('bio11-s4.1.2',H,'diet as epigenetic trigger','low')]),
'5.2':(1,[('bio11-s4.5.1',E,'royal jelly feeding','high')]),
'5.3':(2,[('bio11-s4.3.1',E,'methylation switches genes','high'),('bio11-s4.5.2',H,'diets produce castes','high')]),
'5.4':(2,[('bio11-s4.5.3',E,'methylation mechanism','high')]),
'5.5':(1,[('bio11-s2.3.2',H,'phenotype = genotype + environment','high')]),
'5.6':(2,[('bio11-s4.1.3',H,'marks copied in mitosis','high'),('bio11-s4.5.2',H,'diet decides caste','high')]),
'6.b':(1,[]),
'6.0':(2,[('bio11-s2.5.1',H,'gene switched on','low')]),
'6.1':(1,[('bio11-s4.3.1',E,'methylation silences','high'),('bio11-s4.6.0',E,'agouti gene always on','high')]),
'6.2':(1,[('bio11-s4.6.1',H,'unmethylated yellow case','high')]),
'6.3':(2,[('bio11-s4.3.0',E,'methyl groups added to DNA','high'),('bio11-s4.6.2',H,'methylation gives brown mice','high')]),
'6.4':(1,[('bio11-s4.6.3',H,'methyl donors raise methylation','high')]),
'6.5':(2,[('bio11-s4.2.0',E,'marks escaping erasure','high')]),
'6.6':(1,[('bio11-s4.6.3',H,'diet changes methylation','high')]),
'7.b':(1,[]),
'7.0':(1,[]),
'7.1':(1,[]),
'7.2':(2,[('bio11-s4.7.0',H,'famine background','high')]),
'7.3':(2,[('bio11-s4.3.1',E,'less methylation, expression change','high'),('bio11-s4.7.2',H,'exposed people studied','high')]),
'7.4':(1,[('bio11-s4.7.3',E,'methylation difference found','high')]),
'7.5':(1,[('bio11-s4.2.0',H,'inheritance of marks','low')]),
'7.6':(1,[('bio11-s4.7.4',H,'lasting epigenetic effect','high'),('bio11-s4.7.5',H,'weak inheritance evidence','high')]),
'8.b':(1,[]),
'8.0':(2,[]),
'8.1':(1,[('bio11-s4.8.0',H,'vernalisation context','low')]),
'8.2':(2,[('bio11-s4.3.3',E,'histone modification','high'),('bio11-s4.8.1',E,'FLC gene','high')]),
'8.3':(1,[('bio11-s4.8.2',E,'FLC switched off','high'),('bio11-s4.1.3',H,'marks copied in mitosis','high')]),
'8.4':(1,[('bio11-s4.1.0',E,'epigenetic: sequence unchanged','high')]),
'8.5':(1,[('bio11-s4.8.3',H,'FLC off in plant','high'),('bio11-s4.2.0',H,'reset vs inheritance','low')]),
'8.6':(1,[('bio11-s4.8.0',E,'vernalisation','high')]),
'9.b':(1,[]),
'9.0':(1,[]),
'9.1':(1,[('bio11-s4.9.0',H,'normal toadflax flowers','high')]),
'9.2':(2,[('bio11-s4.3.1',E,'methylation silences gene','high'),('bio11-s4.9.1',H,'peloric form','high')]),
'9.3':(1,[('bio11-s4.9.2',E,'same sequence, methylated','high'),('bio11-s4.0.2',H,'mutation defined','high')]),
'9.4':(1,[('bio11-s4.2.1',E,'plant epigenetic inheritance','high')]),
'9.5':(1,[('bio11-s4.1.4',H,'reversible marks','high')]),
'9.6':(1,[('bio11-s4.9.3',H,'epimutation','high')]),
'10.b':(1,[]),
'10.0':(1,[]),
'10.1':(1,[]),
'10.2':(1,[]),
'10.3':(1,[('bio11-s4.3.0',H,'methylation','high'),('bio11-s4.3.3',H,'histone modification','high')]),
'10.4':(1,[]),
'10.5':(1,[('bio11-s4.3.2',H,'sequence unchanged, marks differ','high')]),
'10.6':(1,[('bio11-s4.1.4',H,'reversibility','high'),('bio11-s4.2.0',H,'inheritance of marks','high')]),
'10.7':(1,[]),
'10.8':(2,[('bio11-s4.6.3',H,'agouti diet and methylation','low')]),
}
out={}
for k,(c,n) in raw.items():
    out['bio11-s4.'+k]={'cost':c,'needs':[{'id':i,'strength':s,'why':w,'confidence':f} for i,s,w,f in n]}
txt=open(P+'points/bio11-s4.txt').read()
tgt=re.findall(r'^\[(bio11-s4\.[^\]]+)\]',txt,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
# order per package
out={t:out[t] for t in tgt}
assert list(out)==tgt and len(set(tgt))==len(tgt)
for t,v in out.items():
    for n in v['needs']: assert n['id'] in allids and n['id']!=t,(t,n['id'])
json.dump(out,open(P+'point-links/bio11-s4.json','w'),indent=0)
json.load(open(P+'point-links/bio11-s4.json'))
nl=sum(len(v['needs']) for v in out.values())
print(len(out),nl,sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
