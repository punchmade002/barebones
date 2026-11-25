import json,re
H=lambda i,s,w,c='high':{"id":i,"strength":s,"why":w,"confidence":c}
def ids(p):
    t=open(p).read().split('\nCANDIDATES')[0]
    return re.findall(r'^\[([^\]]+)\]',t,re.M),set(re.findall(r'^\[([^\]]+)\]',open(p).read().split('\nCANDIDATES',1)[1],re.M)),open(p).read()
# package 1: links only
p='packs/hist-eur3-s9.t1g3.txt'
tg,cand,txt=ids(p)
L={
"hist-eur3-s9.3.5":[H("hist-eur3-s1.13.5","helpful","Italy's entry into war in 1940")],
"hist-eur3-s9.5.b":[H("hist-eur3-s1.13.5","helpful","Italy's failures in Greece and Africa")],
"hist-eur3-s9.5.0":[H("hist-eur3-s1.13.5","helpful","Italian invasion of Greece 1940")],
"hist-eur3-s9.13.0":[H("hist-eur3-s1.13.1","helpful","Rome-Berlin Axis"),H("hist-eur3-s1.13.4","helpful","Pact of Steel")],
"hist-eur3-s9.13.3":[H("hist-eur3-s1.13.5","helpful","Italian defeats in Greece and North Africa")],
"hist-eur3-s9.10.4":[H("hist-eur3-s1.14.2","helpful","Italy's armistice of 1943"),H("hist-eur3-s1.14.0","helpful","Allied invasion of Sicily")],
}
out={i:{"needs":L.get(i,[])} for i in tg}
for v in out.values():
    for n in v["needs"]: assert n["id"] in cand
json.dump(out,open('point-links/hist-eur3-s9.t1g3.json','w'),indent=1)
chk=json.load(open('point-links/hist-eur3-s9.t1g3.json'))
print(len(tg),len(chk),sum(len(v["needs"]) for v in chk.values()),0)
# package 2
p='packs/hist-ire2-s9.t1g1.txt'
tg,cand,txt=ids(p)
allid=set(tg)|cand
P="hist-ire2-s9."
C2={"0.3","1.1","2.5","6.3","6.4","9.b","9.3","9.4","10.6","11.1","11.2","11.3"}
N={
"0.3":[("hist-ire2-s4.0.0","helpful","Parnell and the Irish Party")],
"2.1":[(P+"7.2","helpful","Cusack's 1886 quarrel","high")],
"2.5":[(P+"2.0","helpful","Cusack's background"),(P+"2.3","helpful","Davin's background")],
"3.0":[(P+"3.1","helpful","United Ireland newspaper")],
"4.0":[(P+"0.3","helpful","Land War")],
"4.1":[(P+"0.1","helpful","anglicisation")],
"4.2":[(P+"0.3","helpful","Land and Home Rule movements")],
"4.3":[(P+"0.1","helpful","de-anglicisation")],
"4.4":[(P+"3.1","helpful","United Ireland")],
"5.1":[(P+"1.0","helpful","English amateur definition")],
"5.3":[(P+"0.1","helpful","de-anglicisation")],
"5.6":[(P+"5.5","helpful","parish club structure")],
"7.0":[(P+"0.4","essential","the IRB")],
"7.1":[(P+"7.0","helpful","IRB membership in clubs","low")],
"7.3":[(P+"7.0","helpful","IRB-linked delegates")],
"7.4":[(P+"0.5","helpful","Church's constitutional outlook")],
"7.6":[(P+"7.0","helpful","IRB influence in the GAA")],
"8.1":[(P+"6.2","helpful","1888 championship")],
"8.2":[("hist-ire2-s4.2.2","helpful","Committee Room 15 split")],
"8.3":[("hist-ire2-s4.2.2","helpful","the Irish Party split"),(P+"4.2","helpful","Parnell as GAA patron")],
"9.0":[(P+"5.5","helpful","parish club system")],
"9.1":[(P+"4.5","helpful","Croke's patronage")],
"9.3":[(P+"7.2","helpful","Cusack's removal"),(P+"7.5","helpful","Davin's resignation")],
"9.4":[(P+"4.2","helpful","Parnell and Davitt as patrons"),(P+"8.3","helpful","Parnell split effect on GAA")],
"9.5":[(P+"5.3","helpful","foreign games ban")],
"10.0":[(P+"3.0","helpful","Cusack's 1884 article")],
"10.1":[(P+"4.1","helpful","Croke's 1884 letter")],
"10.2":[(P+"7.4","helpful","Croke's complaint on drinking")],
"10.3":[(P+"4.3","helpful","Davitt's support")],
"10.4":[(P+"7.1","helpful","Dublin Castle view of GAA")],
"10.5":[(P+"7.3","helpful","1887 convention dispute")],
"11.1":[(P+"8.5","helpful","collapse by 1891")],
"11.3":[(P+"0.6","helpful","Irish Ireland")],
}
out={}
for i in tg:
    k=i[len(P):]
    needs=[]
    for t in N.get(k,[]):
        needs.append(H(t[0],t[1],t[2],t[3] if len(t)>3 else "high"))
        assert t[0] in allid and t[0]!=i
    out[i]={"cost":2 if k in C2 else 1,"needs":needs}
assert all(P+k in tg for k in C2)
json.dump(out,open('point-links/hist-ire2-s9.t1g1.json','w'),indent=1)
chk=json.load(open('point-links/hist-ire2-s9.t1g1.json'))
assert set(chk)==set(tg) and len(chk)==len(tg)
print(len(tg),sum(len(v["needs"]) for v in chk.values()),sum(v["cost"]==2 for v in chk.values()),sum(n["confidence"]=="low" for v in chk.values() for n in v["needs"]))
