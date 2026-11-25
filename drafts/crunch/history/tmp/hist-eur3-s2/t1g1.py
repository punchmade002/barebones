import json,re
H='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
P='hist-eur3-s2.'
E,h='essential','helpful'
# id: (cost, [(target,strength,why,conf)])
d={
"0.b":(1,[]),"0.0":(1,[]),"0.1":(1,[]),"0.2":(1,[]),"0.3":(2,[]),"0.4":(1,[]),"0.5":(1,[]),"0.6":(1,[]),
"1.b":(1,[]),"1.0":(1,[]),"1.1":(1,[("0.2",h,"President and Chancellor roles","high")]),
"1.2":(1,[("0.2",h,"Reichstag and coalitions","high")]),
"1.3":(1,[("0.2",h,"President and Reichstag powers","high")]),
"1.4":(1,[]),"1.5":(1,[("0.0",h,"defeat and armistice of 1918","high")]),
"2.b":(1,[]),"2.0":(1,[]),"2.1":(1,[]),"2.2":(2,[("0.4",h,"reparations","high")]),
"2.3":(1,[("2.2",h,"Treaty of Versailles","high")]),"2.4":(1,[("0.4",E,"reparations","high")]),
"3.b":(1,[]),"3.0":(2,[]),"3.1":(2,[("3.0",h,"Freikorps units","high")]),
"3.2":(1,[("3.1",E,"the Kapp Putsch","high")]),"3.3":(2,[]),"3.4":(1,[]),
"4.b":(1,[]),"4.0":(1,[("0.4",E,"reparations deliveries","high")]),
"4.1":(1,[("4.0",E,"the Ruhr occupation","high")]),
"4.2":(1,[("4.1",E,"printing money to fund resistance","high")]),
"4.3":(1,[("4.2",E,"hyperinflation","high")]),"4.4":(1,[("4.2",h,"hyperinflation","high")]),
"4.5":(2,[("4.2",h,"hyperinflation","high")]),
"5.b":(1,[]),"5.0":(1,[("4.1",E,"passive resistance in the Ruhr","high")]),
"5.1":(1,[("4.2",E,"hyperinflation","high")]),"5.2":(1,[("5.1",E,"the Rentenmark","high")]),
"5.3":(2,[("0.4",E,"reparations","high")]),
"5.4":(1,[("4.0",E,"the Ruhr occupation","high")]),
"5.5":(2,[("5.3",E,"American loans under Dawes Plan","high"),("0.6",E,"Wall Street Crash","high")]),
"6.b":(1,[]),"6.0":(2,[]),"6.1":(1,[("6.0",h,"the early Nazi party","high")]),
"6.2":(1,[("6.0",h,"the Nazi party","low")]),"6.3":(1,[("0.5",h,"what a putsch is","high")]),
"6.4":(1,[("6.3",E,"the Munich Putsch","high")]),
"7.b":(1,[]),"7.0":(1,[("6.4",E,"the failed putsch","high")]),"7.1":(1,[]),
"7.2":(1,[("6.4",h,"the party banned after putsch","high")]),
"7.3":(1,[("7.2",h,"legal strategy through elections","high")]),
"7.4":(1,[("8.3",E,"the Young Plan","high")]),
"8.b":(1,[]),"8.0":(1,[("2.2",h,"the Treaty of Versailles","high")]),
"8.1":(1,[("8.0",h,"Stresemann's policy","high")]),"8.2":(1,[("8.1",h,"improved relations with France","low")]),
"8.3":(1,[("0.4",h,"reparations","high")]),
"9.b":(1,[]),"9.0":(1,[]),"9.1":(1,[]),"9.2":(1,[("5.3",E,"American loans under Dawes Plan","high")]),
"9.3":(1,[]),"9.4":(1,[("8.0",h,"Stresemann's policies","high")]),
"10.b":(1,[]),"10.0":(1,[("9.2",h,"dependence on American loans","high")]),
"10.1":(1,[("9.1",E,"unemployment insurance","high")]),
"10.2":(1,[("1.3",E,"Article 48 emergency decrees","high"),("10.1",h,"collapse of the grand coalition","high")]),
"10.3":(1,[("10.2",E,"Brüning's policies","high")]),"10.4":(1,[]),
"10.5":(2,[("0.4",h,"reparations","high")]),"10.6":(1,[]),
"10.7":(2,[("10.2",E,"Brüning's emergency rule","high"),("1.3",h,"Article 48 decrees","high")]),
"11.b":(1,[]),"11.0":(1,[("7.3",h,"1928 result of 12 seats","high")]),
"11.1":(1,[("2.2",h,"attacks on the Versailles settlement","low")]),"11.2":(1,[]),
"11.3":(1,[("6.2",E,"the SA","high")]),"11.4":(1,[]),"11.5":(1,[("0.3",h,"the Centre, SPD and KPD","high")]),
"12.b":(1,[]),"12.0":(1,[("2.1",h,"Hindenburg as President","high")]),
"12.1":(1,[("12.0",E,"the first-round presidential result","high")]),
"12.2":(1,[("11.0",h,"Nazi electoral rise","high")]),
"12.3":(1,[("12.2",h,"Nazis as largest party","high")]),"12.4":(1,[("12.2",h,"July 1932 result","high")]),
"13.b":(1,[]),"13.0":(1,[("6.2",E,"the SA","high"),("10.2",h,"Brüning as Chancellor","high")]),
"13.1":(1,[("13.0",h,"Papen as Chancellor","high")]),"13.2":(2,[]),
"13.3":(1,[("13.2",E,"Schleicher's chancellorship","high")]),
"14.b":(1,[]),"14.0":(1,[("13.0",h,"Papen's earlier chancellorship","high")]),
"14.1":(1,[("14.0",h,"Papen's deal with Hitler","high")]),
"14.2":(1,[("7.4",h,"Hugenberg and the DNVP","low")]),
"15.b":(1,[]),"15.0":(1,[]),"15.1":(1,[("6.0",h,"German Workers' Party","high")]),
"15.2":(1,[("6.2",h,"the SA","high")]),
"15.3":(1,[("6.4",E,"the Munich Putsch","high"),("7.2",h,"legal road to power","high")]),
"15.4":(1,[("14.1",h,"Papen's belief he could control Hitler","high")]),
"15.5":(1,[("14.1",h,"Hitler's appointment","low")]),"15.6":(1,[("14.0",h,"January 1933 intrigues","high")]),
"16.b":(1,[]),"16.0":(1,[("9.0",h,"Weimar welfare measures","low")]),"16.1":(1,[]),
"16.2":(1,[("5.1",E,"the Rentenmark","high")]),
"16.3":(1,[("9.1",h,"1927 unemployment insurance","high")]),
"16.4":(1,[("10.2",E,"Brüning's emergency decrees","high")]),
"16.5":(1,[("10.2",h,"Brüning's cuts","low")]),"16.6":(1,[("13.0",h,"Papen's chancellorship","high")]),
"16.7":(1,[("6.2",h,"the SA","high")]),
"17.b":(1,[]),"17.0":(2,[("1.2",E,"proportional representation","high"),("1.3",E,"Article 48","high")]),
"17.1":(2,[("2.2",h,"Treaty of Versailles","high"),("8.0",h,"Stresemann's revision of reparations","high")]),
"17.2":(1,[("8.1",h,"League entry via Locarno","high")]),
"17.3":(1,[("5.5",E,"dependence on American loans","high")]),
"17.4":(2,[("11.0",h,"1930 Nazi breakthrough","high"),("7.3",h,"12 seats in 1928","high")]),
"17.5":(2,[("12.4",h,"falling Nazi vote late 1932","high"),("14.0",h,"conservatives' decisions in appointment","high")]),
"17.6":(1,[]),
}
txt=open(H+'packs/hist-eur3-s2.t1g1.txt').read()
ids=re.findall(r'^\[([^\]]+)\]',txt,re.M)
assert set(ids)=={P+k for k in d} and len(ids)==len(d),set(ids)^{P+k for k in d}
out={}
for i in ids:
    c,n=d[i[len(P):]]
    for t,*_ in n: assert P+t in ids and P+t!=i
    out[i]={"cost":c,"needs":[{"id":P+t,"strength":s,"why":w,"confidence":cf} for t,s,w,cf in n]}
json.dump(out,open(H+'point-links/hist-eur3-s2.t1g1.json','w'),indent=0)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
