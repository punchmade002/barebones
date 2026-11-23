import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/biology/'
E,H='essential','helpful'
def n(i,s,w,c='high'):return {"id":i,"strength":s,"why":w,"confidence":c}
p='bio16-s2.'
d={
'0.b':(1,[]),
'0.0':(1,[n('bio11-s1.0.0',H,'chromosome definition')]),
'0.1':(1,[n('bio16-s1.0.3',E,'diploid definition'),n('bio16-s1.0.4',E,'haploid definition')]),
'0.2':(1,[n('bio16-s1.1.2',E,'chromosome copying in DNA synthesis'),n('bio11-s1.2.1',H,'sister chromatids as copies','low')]),
'0.3':(1,[n('bio16-s1.0.2',E,'homologous chromosomes')]),
'0.4':(1,[n(p+'0.0',H,'genetically identical nuclei')]),
'0.5':(1,[n(p+'0.2',H,'exact copying of chromosomes'),n('bio12-s1.3.0',H,'mutation as DNA change')]),
'1.b':(1,[]),
'1.0':(2,[n('bio16-s1.0.3',E,'diploid to haploid'),n('bio16-s1.1.2',H,'DNA copied once')]),
'1.1':(2,[n(p+'1.0',E,'two divisions of meiosis'),n('bio16-s1.0.2',E,'homologous pairs'),n('bio11-s1.2.1',H,'copies of each chromosome','low')]),
'1.2':(2,[n(p+'1.1',E,'homologous pairs separate in first division'),n('bio12-s1.2.1',H,'independent assortment explained')]),
'1.3':(1,[n(p+'1.2',E,'independent assortment of pairs')]),
'1.4':(1,[n(p+'1.1',E,'first division pairing of homologues'),n('bio11-s1.3.5',H,'alleles on homologues')]),
'1.5':(1,[n(p+'1.2',H,'varied gametes'),n('bio12-s1.2.2',H,'random fertilisation')]),
'1.6':(1,[n(p+'1.0',E,'gametes haploid from meiosis'),n('bio16-s1.0.5',H,'zygote diploid at fertilisation')]),
'2.b':(1,[]),
'2.0':(1,[n(p+'0.0',E,'mitosis gives identical nuclei')]),
'2.1':(1,[n(p+'2.0',E,'asexual reproduction by mitosis')]),
'2.2':(1,[n(p+'2.1',H,'offspring identical'),n('bio12-s1.2.5',H,'clones share vulnerability')]),
'2.3':(2,[n(p+'1.0',E,'meiosis gives haploid cells'),n(p+'2.0',H,'unicellular eukaryotes')]),
'2.4':(1,[n(p+'1.2',H,'meiosis varies offspring')]),
'2.5':(1,[]),
'3.b':(1,[]),
'3.0':(1,[n(p+'0.0',E,'mitosis gives identical cells')]),
'3.1':(1,[n('bio16-s1.2.1',H,'meristems dividing regions','low')]),
'3.2':(1,[n(p+'0.0',H,'mitosis replaces cells')]),
'3.3':(1,[n(p+'0.4',E,'clone')]),
'3.4':(1,[n(p+'1.0',E,'meiosis makes gametes')]),
'3.5':(2,[n(p+'3.4',E,'gametes made by meiosis'),n('bio12-s1.6.1',H,'somatic mutations not inherited')]),
'3.6':(1,[]),
'4.b':(1,[]),
'4.0':(2,[n('bio16-s1.1.4',H,'interphase'),n('bio16-s1.6.0',H,'cytokinesis')]),
'4.1':(1,[n(p+'0.2',H,'one division mitosis'),n(p+'1.0',H,'two divisions meiosis')]),
'4.2':(1,[n(p+'0.1',H,'2n to 2n'),n(p+'1.0',H,'2n to n')]),
'4.3':(1,[n(p+'1.2',H,'meiosis cells differ'),n(p+'0.3',H,'no pairing in mitosis'),n(p+'1.1',H,'pairing in meiosis')]),
'4.4':(1,[n(p+'3.4',H,'meiosis in reproductive organs')]),
'4.5':(1,[n(p+'1.6',H,'constant chromosome number')]),
'4.6':(1,[n(p+'3.0',H,'mitosis for growth'),n(p+'2.0',H,'asexual reproduction')]),
'4.7':(2,[n(p+'4.2',H,'chromosome numbers compared'),n(p+'1.1',H,'homologous pair separation')]),
}
out={p+k:{"cost":c,"needs":ns} for k,(c,ns) in d.items()}
op=P+'point-links/bio16-s2.json'
json.dump(out,open(op,'w'),indent=1)
# validate
pk=open(P+'points/bio16-s2.txt').read()
ids=set(re.findall(r'^\[([^\]]+)\]',pk,re.M))
tg=[]; cur=None
for l in pk.splitlines():
    if l.startswith('TARGET'):cur='t'
    elif l.startswith('CANDIDATES'):cur='c'
    m=re.match(r'\[([^\]]+)\]',l)
    if m and cur=='t':tg.append(m.group(1))
o=json.load(open(op))
assert list(o)==tg,(set(tg)^set(o))
for k,v in o.items():
    for x in v['needs']:assert x['id'] in ids and x['id']!=k,(k,x)
L=[x for v in o.values() for x in v['needs']]
print(len(o),len(L),sum(v['cost']==2 for v in o.values()),sum(x['confidence']=='low' for x in L))
