import json,re
P="geo-economic-development-s3."
pack="/Users/gabrielwhelan/barebones/drafts/crunch/geography/packs/geo-economic-development-s3.t1g5.txt"
out="/Users/gabrielwhelan/barebones/drafts/crunch/geography/point-links/geo-economic-development-s3.t1g5.json"
C="geo-region-continental-s2."
# id: [(target,S,why,conf)]  target w/o prefix => s3 ; "c:" => candidate
L={
"13.4":[(C+"15.3","H","massape soil for sugar","l")],
"13.6":[(C+"15.1","H","terra roxa coffee soil","l")],
"15.0":[(C+"2.1","H","Northeast poorest region","h")],
"15.1":[(C+"2.3","E","Southeast economic core","h")],
"19.6":[(C+"2.1","H","Northeast poorest region","h")],
"18.4":[(C+"37.0","E","soya and coffee leading producer","h")],
"18.2":[(C+"37.0","H","Brazil's main commodity exports","l")],
"19.4":[(C+"38.2","H","extensive cattle ranching","h")],
"14.2":[(C+"28.3","H","favelas on steep hills","l")],
"13.7":[(C+"30.2","H","Manaus on the Amazon","l")],
"13.5":[(C+"2.3","H","Minas Gerais in Southeast","l")],

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
