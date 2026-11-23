import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/biology/'
txt=open(P+'points/bio12-s3.txt').read()
ids=re.findall(r'^\[([^\]]+)\]',txt,re.M)
tgt=[i for i in ids if i.startswith('bio12-s3.')]
S='bio12-s3.'
E,H='essential','helpful'
# id suffix: (cost, [(need, strength, why, conf)])
d={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(2,[]),'0.2':(1,[]),
'0.3':(1,[('0.1',H,'sedimentary rock layers forming','high')]),
'0.4':(1,[]),'0.5':(1,[]),
'0.6':(1,[('0.3',H,'deeper layers are older','high')]),
'1.b':(1,[('bio12-s2.0.6',H,'natural selection prediction','low')]),
'1.0':(1,[('0.3',H,'rock age order','high')]),
'1.1':(1,[('0.3',H,'younger rocks higher up','high')]),
'1.2':(1,[]),
'1.3':(1,[('bio12-s2.0.6',H,'gradual change by selection','low')]),
'2.b':(1,[('0.0',H,'what a fossil is','high')]),
'2.0':(1,[('2.b',H,'transitional fossil meaning','high')]),
'2.1':(1,[('2.b',E,'transitional fossil meaning','high')]),
'2.2':(1,[]),
'2.3':(1,[('2.2',H,'Tiktaalik as fish','high')]),
'2.4':(1,[('bio12-s2.0.6',H,'theory predicts intermediate forms','low')]),
'3.b':(1,[('1.3',H,'gradual change in fossils','high')]),
'3.0':(2,[]),
'3.1':(1,[('3.0',H,'horse series traits','high')]),
'3.2':(1,[('0.1',H,'fossil formation conditions','high')]),
'3.3':(1,[('3.2',H,'incomplete fossil record','high')]),
'3.4':(1,[('3.2',H,'gaps in fossil record','high')]),
'4.b':(1,[]),'4.0':(1,[]),
'4.1':(2,[('4.0',E,'homologous structures','high')]),
'4.2':(2,[('4.1',E,'pentadactyl limb','high')]),
'4.3':(1,[('4.0',E,'common ancestor, different function','high')]),
'4.4':(1,[('4.2',E,'limb bone names','high')]),
'5.b':(1,[('4.0',H,'homologous structures contrast','high')]),
'5.0':(1,[('4.0',H,'contrast with homologous','low')]),
'5.1':(1,[('5.0',E,'analogous structures','high')]),
'5.2':(1,[]),
'5.3':(2,[('5.2',E,'vestigial structure meaning','high')]),
'5.4':(1,[('5.2',E,'vestigial structures','high')]),
'6.b':(1,[]),'6.0':(1,[]),
'6.1':(1,[('6.0',E,'pharyngeal pouches and tail','high')]),
'6.2':(1,[('6.0',E,'shared early embryo features','high')]),
'6.3':(1,[('6.0',E,'embryo similarity','high')]),
'6.4':(1,[('6.0',H,'embryo similarity','high')]),
'6.5':(1,[('6.0',E,'embryo features','high')]),
'7.b':(1,[('bio6-s3.6.0',H,'phylogeny and relatedness','low')]),
'7.0':(1,[('bio6-s3.6.1',H,'phylogenetic tree reading','high')]),
'7.1':(1,[('7.0',H,'common ancestor relatedness','high')]),
'7.2':(2,[('bio10-s1.0.4',H,'DNA bases','high')]),
'7.3':(1,[('7.1',H,'DNA similarity and relatedness','high')]),
'7.4':(1,[('7.1',H,'molecule similarity and relatedness','high')]),
'7.5':(1,[('7.4',E,'cytochrome c sequences','high')]),
'7.6':(1,[('7.1',E,'molecular trees match anatomy','high')]),
'7.7':(1,[('bio6-s3.2.1',H,'domains of life','low')]),
'8.b':(1,[('bio12-s2.0.6',H,'natural selection','high')]),
'8.0':(1,[]),
'8.1':(2,[('8.0',E,'antibiotic resistance meaning','high')]),
'8.2':(1,[('8.1',E,'resistant vs non-resistant bacteria','high')]),
'8.3':(1,[('8.2',E,'survivors after antibiotic','high')]),
'8.4':(1,[('8.3',E,'resistant bacteria reproduce','high')]),
'8.5':(1,[('8.4',E,'resistance spreads','high')]),
'8.6':(1,[('8.5',H,'resistance steps','high')]),
'9.b':(1,[('8.5',H,'resistance spread','high')]),
'9.0':(1,[('8.1',E,'pre-existing resistance mutations','high')]),
'9.1':(1,[('9.0',E,'resistance pre-exists','high')]),
'9.2':(1,[('8.0',H,'antibiotic resistance','high')]),
'9.3':(1,[('8.3',H,'rapid bacterial reproduction','high')]),
'9.4':(1,[('8.5',E,'selection producing resistance','high')]),
'10.b':(1,[('bio12-s2.0.6',H,'natural selection','high')]),
'10.0':(1,[]),
'10.1':(1,[('10.0',E,'drought seed shortage','high')]),
'10.2':(1,[('10.1',H,'beak depth selection','high')]),
'10.3':(2,[('bio12-s2.1.1',H,'island species resemble mainland','high')]),
'10.4':(1,[('10.3',E,'island resemblance pattern','high')]),
'11.b':(1,[('bio12-s2.3.5',H,'speciation from isolation','high')]),
'11.0':(1,[('bio6-s3.1.0',E,'species definition','high')]),
'11.1':(1,[('11.0',H,'reproductive isolation','high')]),
'11.2':(1,[('11.1',E,'separated populations','high')]),
'11.3':(1,[('11.2',E,'different mutations in groups','high')]),
'11.4':(1,[('11.3',E,'different selection pressures','high')]),
'11.5':(1,[('11.4',H,'speciation steps','high')]),
'12.b':(1,[('11.b',H,'geographical speciation','high')]),
'12.0':(1,[('10.3',H,'Galapagos mainland origin','low')]),
'12.1':(1,[('12.0',H,'finch species from ancestor','high')]),
'12.2':(1,[('11.4',H,'new species formation','high')]),
'13.b':(1,[('11.b',H,'speciation contrast','high')]),
'13.0':(2,[('11.0',H,'species and interbreeding','high')]),
'13.1':(2,[('13.0',H,'polyploidy speciation','high')]),
'13.2':(1,[('13.1',E,'Spartina hybrid origin','high')]),
'14.b':(1,[]),
'14.0':(1,[('3.2',H,'incomplete fossil record','low')]),
'14.1':(1,[]),
'14.2':(1,[('8.5',H,'antibiotic resistance example','high')]),
}
out={}
for t in tgt:
    k=t[len(S):]
    c,n=d[k]
    out[t]={'cost':c,'needs':[{'id':(x if x.startswith('bio') else S+x),'strength':s,'why':w,'confidence':cf} for x,s,w,cf in n]}
assert set(d)=={t[len(S):] for t in tgt}
json.dump(out,open(P+'point-links/bio12-s3.json','w'),indent=1)
o=json.load(open(P+'point-links/bio12-s3.json'))
assert list(o)==tgt
for t,v in o.items():
    for n in v['needs']: assert n['id'] in ids and n['id']!=t,(t,n)
L=sum(len(v['needs']) for v in o.values())
print(len(o),L,sum(v['cost']==2 for v in o.values()),sum(n['confidence']=='low' for v in o.values() for n in v['needs']))
