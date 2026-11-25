import json,re,sys
H,E='h','e'
def L(i,s,w,c='h'): return {"id":i,"strength":"essential" if s=='e' else "helpful","why":w,"confidence":"high" if c=='h' else "low"}
def run(pack,out,P,costs=True):
    txt=open(pack).read()
    tgt=txt.split('\nCANDIDATES')[0]
    tids=re.findall(r'^\[([^\]]+)\]',tgt,re.M)
    allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    assert set(tids)==set(P) and len(tids)==len(P),(set(tids)^set(P))
    res={i:{"cost":P[i][0],"needs":[L(*n) for n in P[i][1]]} for i in tids}
    for i in tids:
        for n in res[i]["needs"]: assert n["id"] in allids and n["id"]!=i
    json.dump(res,open(out,'w'),indent=1)
    d=json.load(open(out)); assert list(d)==tids
    print(len(d),sum(len(v["needs"]) for v in d.values()),sum(v["cost"]==2 for v in d.values()),sum(n["confidence"]=="low" for v in d.values() for n in v["needs"]))
p='hist-eur6-s9.'
def n(*a): return a
P={}
def A(k,c,*needs): P[p+k]=(c,[(p+x[0] if x[0][0].isdigit() else x[0],)+x[1:] for x in needs])
A('0.b',1);A('0.0',2);A('0.1',1,('0.0','h','uses segregation'))
A('0.2',1);A('0.3',1,('0.1','h','overturns separate but equal'))
A('0.4',1,('0.3','e','responds to Brown ruling'))
A('0.5',1,('0.3','h','school desegregation ordered'))
A('0.6',1);A('0.7',1)
A('1.b',1);A('1.0',1,('0.0','h','uses segregation'))
A('1.1',1);A('1.2',1);A('1.3',2,('3.2','h','Southern Christian Leadership Conference'))
A('1.4',1,('1.3','e','Birmingham violence'))
A('1.5',1);A('1.6',2,('1.3','h','Birmingham campaign'))
A('1.7',2,('1.3','e','Birmingham campaign'))
A('1.8',1,('0.2','h','NAACP'))
A('1.9',1,('1.5','h','March on Washington'))
A('2.b',1);A('2.0',1);A('2.1',1,('0.0','h','poll taxes, literacy tests'))
A('2.2',1,('2.7','h','Selma campaign'))
A('2.3',1,('2.1','e','Voting Rights Act'))
A('2.4',1,('2.0','e','the Civil Rights Act'))
A('2.5',1,('2.0','e','the Civil Rights Act'))
A('2.6',1);A('2.7',2,('2.1','e','Voting Rights Act'))
A('3.b',1);A('3.0',1);A('3.1',1);A('3.2',1)
A('3.3',1,('1.3','e','Birmingham protests'))
A('3.4',1);A('3.5',1);A('3.6',1);A('3.7',1)
A('3.8',2,('4.5','h','Malcolm X'))
A('3.9',1);A('3.10',1)
A('3.11',2,('3.1','h','Gandhi shaped his non-violence'))
A('3.12',2,('1.6','h','Albany Movement'))
A('3.13',2,('3.6','h','Vietnam and poverty turn'))
A('4.b',1);A('4.0',1);A('4.1',1);A('4.2',1)
A('4.3',2,('4.2','e','uses the 1967 riots'))
A('4.4',1,('3.7','h','King\'s death'))
A('4.5',2,('4.0','h','Malcolm X leaving Nation, death'))
A('4.6',1,('4.1','h','Black Power self-defence','l'))
A('4.7',2,('4.2','h','Watts and Detroit riots'))
A('4.8',1,('4.3','e','Kerner Commission'))
A('5.b',1);A('5.0',1);A('5.1',1);A('5.2',1,('5.1','e','War on Poverty programmes'))
A('5.3',1);A('5.4',1);A('5.5',1)
A('5.6',2,('5.1','e','Economic Opportunity Act programmes'))
A('6.b',1);A('6.0',1);A('6.1',1)
A('6.2',1,('6.1','e','crack cocaine'))
A('6.3',1);A('6.4',1);A('6.5',1);A('6.6',1);A('6.7',1)
A('6.8',1,('6.2','h','mandatory sentences','l'))
A('6.9',2)
A('7.b',1);A('7.0',1,('2.0','h','Civil Rights Act'))
A('7.1',1,('5.3','h','poverty persistence'))
A('7.2',1,('6.9','h','busing'))
A('7.3',2)
d='/Users/gabrielwhelan/barebones/drafts/crunch/history/'
run(d+'packs/hist-eur6-s9.t1g1.txt',d+'point-links/hist-eur6-s9.t1g1.json',P)
