import json,re
P="geo-economic-development-s3."
pack="/Users/gabrielwhelan/barebones/drafts/crunch/geography/packs/geo-economic-development-s3.t1g6.txt"
out="/Users/gabrielwhelan/barebones/drafts/crunch/geography/point-links/geo-economic-development-s3.t1g6.json"
C="geo-region-continental-s2."
# id: [(target,S,why,conf)]  target w/o prefix => s3 ; "c:" => candidate
L={
"13.6":[(C+"40.0","H","coffee boom in Sao Paulo","h")],
"13.7":[(C+"50.3","H","rubber boom and collapse","h")],
"14.5":[(C+"47.0","H","latifundia and minifundia","h")],
"14.6":[(C+"47.0","H","unequal land ownership","h")],
"14.7":[(C+"47.1","H","MST landless movement","h")],
"15.3":[(C+"68.2","H","SUDENE incentives","h")],
"16.b":[(C+"60.0","H","import substitution industrialisation","h")],
"16.0":[(C+"60.1","H","Vargas state-built industry","h")],
"16.1":[(C+"57.0","H","Petrobras founded","h")],
"16.2":[(C+"60.2","H","Kubitschek car industry","h")],
"16.4":[(C+"68.1","H","Manaus Free Trade Zone","h")],
"16.5":[(C+"61.0","H","Brazilian miracle under military","h")],
"17.1":[(C+"61.3","H","1980s debt crisis","h")],
"17.2":[(C+"62.0","H","Real Plan","h")],
"18.0":[(C+"62.1","H","Vale privatisation","h")],
"18.1":[(C+"48.1","H","Mercosur founding","h")],
"18.2":[(C+"48.0","H","export markets such as China","h")],
"18.6":[(C+"61.2","H","Embraer","h")],
"19.4":[(C+"43.2","E","ranching causes Amazon clearance","h")],
"19.5":[(C+"49.3","H","dependence on commodity prices","h")],

}
txt=open(pack).read()
tsec=txt.split("CANDIDATES")[0]
tids=re.findall(r"^\[([^\]]+)\]",tsec,re.M)
allids=set(re.findall(r"^\[([^\]]+)\]",txt,re.M))
R={};n=lo=0
for i in tids:
    k=i[len(P):]
    ns=[]
    for t,s,w,c in L.get(k,[]):
        tid=t if t.startswith("geo-") else P+t
        assert tid in allids and tid!=i,(i,tid)
        ns.append({"id":tid,"strength":"essential" if s=="E" else "helpful","why":w,"confidence":"high" if c=="h" else "low"})
        lo+=c=="l"
    n+=len(ns);R[i]=({"needs":ns})
for k in L: assert P+k in R,k
json.dump(R,open(out,"w"),indent=0)
d=json.load(open(out));assert list(d)==tids
print(len(tids),n,lo)
