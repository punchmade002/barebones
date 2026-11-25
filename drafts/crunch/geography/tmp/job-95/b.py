import json,re,sys

L = {
 "t1g4": {
  "geo-region-continental-s1.11.0": [("geo-rocks-weathering-s1.5.0","helpful","basalt lava weathers to black soil","high")],
  "geo-region-continental-s1.12.0": [("geo-rocks-weathering-s1.12.3","helpful","granite and gneiss crystalline rock","low")],
  "geo-region-continental-s1.16.0": [("geo-rocks-weathering-s1.5.0","helpful","basalt is the parent rock","high")],
  "geo-region-continental-s1.18.0": [("geo-plate-tectonics-s3.8.0","helpful","continental collision forms fold mountains","high")],
  "geo-region-continental-s1.19.4": [("geo-plate-tectonics-s3.8.1","helpful","earthquakes at collision zones","low")],
  "geo-region-continental-s1.21.4": [("geo-volcanoes-earthquakes-s3.2.0","helpful","fissure eruptions of runny lava","high")]},
 "t1g5": {
  "geo-region-continental-s1.8.1": [("geo-rivers-s4.12.0","helpful","heavy rain overwhelms river channels","low")],
  "geo-region-continental-s1.15.1": [("geo-rivers-s4.7.4","helpful","irrigation causes waterlogging and salinisation","high")],
  "geo-region-continental-s1.19.3": [("geo-rivers-s4.1.1","helpful","drop in height gives hydro power","high")],
  "geo-region-continental-s1.25.1": [("geo-economic-activities-s2.2.0","helpful","raw materials draw industry","low")],
  "geo-region-continental-s1.25.2": [("geo-rivers-s4.1.0","helpful","falling water drives turbines","low")]},
 "t1g6": {
  "geo-region-continental-s1.27.7": [("geo-urban-s7.16.2","helpful","Kolkata as port on the Hooghly","low")]}
}

for k,links in L.items():
    name="geo-region-continental-s1."+k
    txt=open(f"packs/{name}.txt").read()
    ids=re.findall(r"^\[(geo-region-continental-s1\.[^\]]+)\]",txt,re.M)
    allids=set(re.findall(r"^\[([^\]]+)\]",txt,re.M))
    out={}
    for i in ids:
        out[i]={"needs":[dict(id=a,strength=b,why=c,confidence=d) for a,b,c,d in links.get(i,[])]}
    assert set(links)<=set(ids)
    for v in out.values():
        for n in v["needs"]: assert n["id"] in allids,n
    json.dump(out,open(f"point-links/{name}.json","w"),indent=0)
    print(k,len(out),sum(len(v["needs"]) for v in out.values()),sum(n["confidence"]=="low" for v in out.values() for n in v["needs"]))
