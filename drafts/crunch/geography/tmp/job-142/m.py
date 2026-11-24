import json,re
last={0:6,1:3,2:3,3:1,4:2,5:2,6:2,7:1,8:2,9:1,10:1,11:1,12:1,13:1,14:3,15:1,16:4,17:4,18:2,19:2,20:2,21:6,22:1,23:6,24:1,25:3,26:1,27:1,28:1,29:2,30:1,31:2,32:4,33:2,34:2,35:2,36:1,37:4,38:1}
L={
"geo-urban-s7.32.4":[("geo-region-continental-s2.94.0","helpful","nordestinos migration from sertao","low")],
"geo-urban-s7.33.0":[("geo-region-continental-s2.110.0","helpful","city versus Greater Sao Paulo size","low")],
"geo-urban-s7.33.2":[("geo-region-continental-s2.109.0","helpful","Brazil urbanisation share and shift","high")],
"geo-urban-s7.38.0":[("geo-region-continental-s2.114.2","helpful","favela upgrading idea","high")],
}
out={}
for s,n in last.items():
    for k in ["b"]+list(range(n+1)):
        i=f"geo-urban-s7.{s}.{k}"
        out[i]={"needs":[{"id":a,"strength":b,"why":c,"confidence":d} for a,b,c,d in L.get(i,[])]}
txt=open("packs/geo-urban-s7.t1g7.txt").read()
tg=re.findall(r"^\[(geo-urban-s7\.[^\]]+)\]",txt,re.M)
allid=set(re.findall(r"^\[([^\]]+)\]",txt,re.M))
assert list(out)==tg,(len(out),len(tg))
for v in out.values():
    for n in v["needs"]: assert n["id"] in allid
json.dump(out,open("point-links/geo-urban-s7.t1g7.json","w"),indent=0)
print(len(out),sum(len(v["needs"]) for v in out.values()),sum(n["confidence"]=="low" for v in out.values() for n in v["needs"]))
