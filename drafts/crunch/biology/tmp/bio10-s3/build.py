import json,re
P='bio10-s3.'
def n(i,s,w,c='high'):return {"id":i,"strength":s,"why":w,"confidence":c}
E,H='essential','helpful'
d={
"0.b":(1,[n("bio10-s2.0.0",H,"gene as DNA recipe")]),
"0.0":(1,[n("bio10-s1.6.4",H,"mRNA as copy of gene")]),
"0.1":(1,[n("bio10-s1.0.4",H,"the four bases")]),
"0.2":(2,[n("bio10-s1.0.4",E,"four bases in DNA/RNA"),n("bio10-s2.0.2",H,"about 20 amino acids","low")]),
"0.3":(1,[n(P+"0.2",E,"combination counting argument")]),
"0.4":(1,[n(P+"0.1",E,"codon definition")]),
"0.5":(2,[n(P+"0.1",E,"codon read in threes"),n("bio10-s1.6.5",H,"tRNA brings amino acids","low")]),
"1.b":(1,[]),
"1.0":(1,[n(P+"0.1",E,"codon definition")]),
"1.1":(1,[n(P+"0.4",H,"stop codons exist")]),
"1.2":(2,[n(P+"0.1",E,"codons of three bases"),n(P+"1.0",H,"start codon sets frame")]),
"1.3":(1,[n(P+"0.4",E,"61 codons, 20 amino acids")]),
"1.4":(1,[n(P+"1.3",E,"degenerate code")]),
"1.5":(1,[n(P+"1.3",E,"degenerate code")]),
"1.6":(2,[n(P+"1.1",H,"UGA as stop codon")]),
"1.7":(2,[n(P+"1.6",E,"universal code")]),
"2.b":(1,[]),
"2.0":(1,[n(P+"0.1",E,"codon definition"),n("bio10-s1.6.5",H,"tRNA molecule","low")]),
"2.1":(1,[n(P+"2.0",E,"anticodon definition"),n("bio10-s1.2.1",H,"complementary base pairing")]),
"2.2":(1,[n(P+"2.1",E,"anticodon-codon pairing"),n(P+"1.0",H,"AUG start codon","low")]),
"2.3":(1,[n(P+"0.4",E,"stop codons")]),
"2.4":(2,[n(P+"2.1",E,"anticodon pairs with codon")]),
"3.b":(1,[]),
"3.0":(2,[n("bio10-s1.6.1",E,"A-U pairing in RNA"),n("bio10-s1.2.1",H,"complementary base pairing")]),
"3.1":(1,[n(P+"3.0",E,"mRNA made first"),n(P+"1.0",E,"start codon AUG")]),
"3.2":(1,[n(P+"0.1",H,"codon codes amino acid")]),
"3.3":(1,[n(P+"0.4",E,"stop codons"),n(P+"2.0",E,"anticodons complementary")]),
"3.4":(1,[n(P+"1.0",H,"AUG start codon","low")]),
"3.5":(2,[n(P+"3.0",E,"transcribing DNA to mRNA"),n(P+"2.1",E,"anticodon pairing")]),
"3.6":(1,[n(P+"3.5",E,"worked example anticodons")]),
"3.7":(2,[n(P+"0.1",E,"three bases per codon"),n(P+"0.4",H,"stop codon adds three")]),
}
out={}
for k,(c,nn) in d.items(): out[P+k]={"cost":c,"needs":nn}
json.dump(out,open('point-links/bio10-s3.json','w'),indent=1)
t=open('points/bio10-s3.txt').read()
tgt=re.findall(r'^\[(bio10-s3\.[^\]]+)\]',t.split('CANDIDATES')[0],re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',t,re.M))
o=json.load(open('point-links/bio10-s3.json'))
assert list(o)==tgt,(set(tgt)^set(o))
bad=[x['id'] for v in o.values() for x in v['needs'] if x['id'] not in allids]
assert not bad,bad
assert all(x['id']!=k for k,v in o.items() for x in v['needs'])
L=[x for v in o.values() for x in v['needs']]
print(len(o),len(L),sum(v['cost']==2 for v in o.values()),sum(x['confidence']=='low' for x in L))
