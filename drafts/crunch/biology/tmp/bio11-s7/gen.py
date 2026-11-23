import json,re
H,L='high','low'
def n(i,s,w,c=H):return {"id":i,"strength":s,"why":w,"confidence":c}
e,h='essential','helpful'
P='bio11-s7.'
d={
"0.b":(1,[]),"0.0":(1,[]),"0.1":(1,[]),"0.2":(1,[]),"0.3":(1,[]),
"1.b":(1,[]),"1.0":(1,[]),"1.1":(1,[]),"1.2":(1,[]),"1.3":(1,[]),
"2.b":(1,[]),"2.0":(2,[]),"2.1":(1,[n(P+"1.1",h,"true-breeding lines")]),"2.2":(1,[]),"2.3":(1,[]),"2.4":(1,[]),
"3.b":(1,[]),"3.0":(1,[n(P+"2.3",h,"P and F1 generations"),n(P+"1.1",h,"true-breeding parents")]),
"3.1":(1,[n(P+"3.0",h,"F1 plants being selfed")]),"3.2":(2,[n(P+"3.1",h,"3 : 1 ratio in F2")]),
"3.3":(2,[n(P+"3.1",e,"dwarf reappears in F2")]),"3.4":(2,[n(P+"3.3",e,"hidden factor inference")]),
"4.b":(1,[n(P+"3.4",h,"factors, dominant and recessive")]),
"4.0":(2,[n(P+"3.4",e,"pairs of factors"),n("bio16-s2.1.0",h,"meiosis makes gametes",L)]),
"4.1":(1,[n(P+"4.0",h,"law restated")]),
"4.2":(2,[n("bio11-s5.1.1",e,"heterozygous gamete types")]),
"4.3":(2,[n(P+"4.2",e,"gamete types T and t"),n("bio11-s5.7.5",h,"Tt x Tt offspring ratio",L)]),
"4.4":(2,[n("bio11-s5.0.0",e,"alleles on homologous pair")]),
"4.5":(2,[n(P+"4.4",e,"alleles on homologous chromosomes"),n("bio16-s2.1.1",h,"homologues separate in meiosis I",L)]),
"4.6":(2,[n(P+"4.5",e,"segregation in meiosis")]),
"5.b":(1,[n(P+"4.0",h,"first law contrast")]),
"5.0":(2,[n(P+"4.0",e,"alleles of one gene segregate")]),
"5.1":(1,[n(P+"5.0",e,"law restated")]),
"5.2":(2,[n("bio11-s5.2.1",h,"unlinked genes",L)]),
"5.3":(2,[n(P+"4.2",e,"heterozygous gamete types")]),
"5.4":(1,[n(P+"5.3",e,"independent allele sorting")]),
"5.5":(2,[n("bio16-s2.1.2",e,"independent assortment of pairs")]),
"5.6":(2,[n(P+"5.5",e,"independent pair arrangement")]),
"5.7":(2,[n(P+"5.6",e,"two arrangements give four gametes")]),
"6.b":(1,[n(P+"5.0",h,"independent inheritance law")]),
"6.0":(1,[n(P+"3.0",h,"P to F1 cross")]),
"6.1":(2,[n(P+"6.0",e,"F1 round yellow parents")]),
"6.2":(2,[n(P+"6.1",e,"new combinations in F2")]),
"7.b":(1,[]),"7.0":(2,[n(P+"3.4",h,"factors masked, then reappear")]),
"7.1":(2,[n(P+"7.0",e,"particulate versus blending")]),"7.2":(1,[]),
}
out={P+k:{"cost":c,"needs":v} for k,(c,v) in d.items()}
json.dump(out,open("point-links/bio11-s7.json","w"),indent=1)
txt=open("points/bio11-s7.txt").read()
t=re.findall(r'^\[(bio11-s7\.[^\]]+)\]',txt,re.M)
allid=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
o=json.load(open("point-links/bio11-s7.json"))
assert list(o)==t,(set(t)^set(o))
assert all(x["id"] in allid and x["id"]!=k for k,v in o.items() for x in v["needs"])
nl=[x for v in o.values() for x in v["needs"]]
print(len(o),len(nl),sum(v["cost"]==2 for v in o.values()),sum(x["confidence"]=="low" for x in nl))
