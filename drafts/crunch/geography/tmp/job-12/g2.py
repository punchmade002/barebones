import json,re,sys
G="geo-economic-globalisation-s3.";N="geo-economic-environment-s3.";P="geo-economic-development-s4."
H="helpful"
d={
"3.0":[(G+"14.0",H,"raw material exports share","high")],
"3.1":[(G+"0.b",H,"exports and imports","low")],
"3.3":[(G+"4.1",H,"tariffs as trade barriers","high")],
"4.0":[(G+"4.1",H,"subsidies as trade barrier","high")],
"4.2":[(G+"4.5",H,"WTO settles disputes","high")],
"5.0":[(G+"4.4",H,"the WTO","high")],
"5.1":[(G+"4.1",H,"tariffs and quotas","high")],
"6.b":[(G+"4.6",H,"fair trade minimum price","high")],
"6.0":[(G+"4.6",H,"fair trade price and premium","high")],
"7.4":[(G+"4.0",H,"trade rules and protectionism","low")],
"17.0":[(G+"16.0",H,"MNCs move assembly to cheap labour","high")],
"18.4":[(G+"17.2",H,"assembly spreading to Bangladesh","low")],
"18.5":[(G+"16.0",H,"MNCs use low-cost factories","low")],
"22.b":[(N+"2.1",H,"enhanced greenhouse effect","high")],
"22.0":[(N+"2.1",H,"greenhouse emissions cause warming","high")],
"22.1":[(N+"5.0",H,"sea-level rise","high")],
"22.2":[(N+"5.0",H,"sea-level rise","high")],
"22.3":[(N+"5.1",H,"drought from warming","high")],
"22.4":[(N+"8.3",H,"COP climate conferences","high")],
}
pack=open(sys.argv[1]).read()
ids=set(re.findall(r'^\[(\S+?)\]',pack,re.M))
tg=re.findall(r'^\[(\S+?)\]',pack.split("CANDIDATES")[0],re.M)
out={k:{"needs":[]} for k in tg}
for k,v in d.items():
    out[P+k]["needs"]=[{"id":x[0],"strength":x[1],"why":x[2],"confidence":x[3]} for x in v]
for k,v in out.items():
    for n in v["needs"]: assert n["id"] in ids and n["id"]!=k,(k,n)
json.dump(out,open(sys.argv[2],"w"),indent=0)
json.load(open(sys.argv[2]))
L=[n for v in out.values() for n in v["needs"]]
print(len(out),len(L),sum(n["confidence"]=="low" for n in L))
