import json,re
P='hom-proteins-s1.'
def L(i,s,w,c='high'): return {"id":P+i,"strength":s,"why":w,"confidence":c}
E,H='essential','helpful'
D={
"0.b":(1,[]),
"0.0":(2,[]),
"0.1":(1,[L("0.0",H,"elements in protein")]),
"0.2":(1,[L("0.0",H,"elements in protein")]),
"0.3":(1,[L("1.0",E,"amino group")]),
"0.4":(1,[L("0.2",H,"amino acids")]),
"1.b":(1,[]),
"1.0":(1,[L("0.2",H,"amino acids")]),
"1.1":(1,[L("0.2",H,"amino acids")]),
"1.2":(1,[]),
"1.3":(1,[L("1.b",H,"side group differs")]),
"1.4":(1,[L("1.3",H,"R side group varies")]),
"1.5":(2,[L("1.0",E,"amino group"),L("1.1",E,"carboxyl group"),L("1.3",E,"R side group")]),
"2.b":(1,[]),
"2.0":(1,[L("0.2",H,"amino acids")]),
"2.1":(2,[L("2.0",E,"essential amino acid definition")]),
"2.2":(2,[L("2.1",H,"eight essential for adults")]),
"2.3":(1,[L("2.0",H,"contrast with essential")]),
"2.4":(2,[L("2.3",E,"non-essential amino acid definition")]),
"2.5":(1,[L("2.3",E,"non-essential amino acids")]),
"2.6":(2,[L("2.0",E,"essential amino acids")]),
"3.b":(1,[]),
"3.0":(1,[L("1.0",E,"amino group"),L("1.1",E,"carboxyl group")]),
"3.1":(1,[L("3.0",E,"peptide bond reaction")]),
"3.2":(1,[L("3.0",H,"peptide bond")]),
"3.3":(1,[L("3.0",H,"peptide bond")]),
"3.4":(1,[L("3.3",E,"polypeptide chains")]),
"3.5":(2,[L("3.0",H,"peptide bond formation"),L("3.1",H,"water released")]),
"4.b":(1,[]),
"4.0":(1,[L("3.0",E,"peptide bond"),L("3.1",H,"condensation reversed")]),
"4.1":(1,[L("4.0",E,"hydrolysis of peptide bond"),L("3.3",H,"peptides and polypeptides")]),
"4.2":(1,[L("4.0",H,"hydrolysis")]),
}
txt=open('packs/hom-proteins-s1.t1g1.txt').read()
ids=re.findall(r'^\[(hom-[^\]]+)\]',txt,re.M)
assert [P+k for k in D]==ids,(len(ids),len(D))
out={P+k:{"cost":c,"needs":n} for k,(c,n) in D.items()}
assert all(l['id'] in ids and l['id']!=k for k,v in out.items() for l in v['needs'])
json.dump(out,open('point-links/hom-proteins-s1.t1g1.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(l['confidence']=='low' for v in out.values() for l in v['needs']))
