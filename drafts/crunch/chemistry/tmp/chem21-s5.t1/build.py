import json,re
D='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/chemistry/'
E,H='essential','helpful'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
# (id, cost, links1) pack1
P1=[
("0.b",1,[]),
("0.0",1,[]),
("0.1",1,[L("chem21-s5.0.0",H,"combustion definition")]),
("0.2",1,[L("chem21-s5.0.1",H,"complete combustion contrast")]),
("0.3",2,[L("chem21-s1.1.1",E,"enthalpy change definition"),L("chem21-s2.7.1",H,"standard conditions values")]),
("0.4",1,[L("chem21-s5.0.3",E,"heat of combustion per mole")]),
("0.5",1,[L("chem21-s1.6.7",E,"ΔH scales with amounts"),L("chem21-s5.0.4",H,"C2H6 combustion equation")]),
("1.b",1,[]),
("1.0",1,[]),
("1.1",1,[]),
("1.2",1,[]),
("1.3",1,[L("chem21-s5.1.1",E,"CO2 count from carbon"),L("chem21-s5.1.2",E,"H2O count from hydrogen")]),
("1.4",1,[L("chem21-s5.1.3",H,"fractional O2 coefficient")]),
("1.5",1,[L("chem10-s2.7.2",H,"state symbols"),L("chem21-s5.0.3",H,"standard heats use liquid water","low")]),
("2.b",1,[]),
("2.0",2,[L("chem21-s5.1.3",H,"oxygen counting method","low")]),
("2.1",1,[]),
("2.2",2,[]),
("2.3",2,[]),
("3.b",1,[]),
("3.0",1,[]),
("3.1",1,[]),
("3.2",1,[L("chem21-s5.1.4",H,"doubling to whole numbers")]),
("3.3",1,[]),
("3.4",1,[]),
("3.5",1,[L("chem21-s5.1.4",H,"doubling to whole numbers")]),
("4.b",1,[L("chem21-s5.1.3",E,"subtract O in fuel")]),
("4.0",1,[L("chem21-s5.1.3",H,"subtract O in fuel")]),
("4.1",1,[L("chem21-s5.1.3",H,"subtract O in fuel")]),
("4.2",1,[L("chem21-s5.1.4",H,"doubling to whole numbers","low")]),
("4.3",1,[]),
("4.4",1,[L("chem21-s5.1.4",H,"doubling to whole numbers","low")]),
("4.5",1,[]),
("5.b",1,[]),
("5.0",2,[L("chem21-s5.0.3",H,"heat of combustion definition")]),
("5.1",2,[L("chem21-s5.0.3",H,"heat of combustion definition")]),
("5.2",2,[L("chem21-s5.0.3",H,"heat of combustion definition")]),
("5.3",1,[L("chem21-s5.0.3",H,"heat of combustion definition")]),
("6.b",1,[]),
("6.0",1,[L("chem21-s5.5.0",H,"alkane data values")]),
("6.1",1,[L("chem21-s5.5.0",E,"alkane ΔHc values")]),
("6.2",1,[L("chem21-s5.5.1",E,"alcohol ΔHc values")]),
("6.3",2,[L("chem21-s1.3.0",E,"bonds broken and made")]),
("6.4",1,[L("chem21-s5.6.3",E,"bonds per extra CH2"),L("chem21-s1.3.3",E,"net energy from bond balance")]),
("6.5",1,[L("chem21-s5.6.3",E,"same bonds per CH2"),L("chem21-s5.6.0",H,"constant increase")]),
("7.b",1,[]),
("7.0",2,[L("chem21-s1.2.0",E,"bond enthalpy definition"),L("chem21-s5.6.3",E,"bonds per extra CH2")]),
("7.1",1,[L("chem21-s5.7.0",E,"estimate uses gaseous water"),L("chem21-s1.5.4",H,"condensing releases heat")]),
("7.2",1,[L("chem21-s5.6.5",E,"linear trend"),L("chem21-s5.5.1",H,"hexanol data","low")]),
("8.b",1,[]),
("8.0",1,[L("chem21-s5.5.0",E,"alkane values"),L("chem21-s5.5.1",E,"alcohol values")]),
("8.1",1,[L("chem21-s5.4.b",H,"oxygen in alcohol OH","low")]),
("8.2",1,[L("chem21-s5.8.1",E,"alcohol already partly oxidised"),L("chem21-s5.4.1",H,"ethanol needs 3 O2")]),
("9.b",1,[]),
("9.0",1,[L("chem21-s5.5.2",E,"two-carbon data values")]),
("9.1",1,[L("chem21-s5.9.0",H,"alkane alkene alkyne order"),L("chem21-s5.6.3",H,"O–H bonds from water","low")]),
("9.2",1,[L("chem21-s5.9.1",E,"fewer O–H bonds formed")]),
("10.b",1,[]),
("10.0",1,[L("chem21-s5.0.3",H,"heat of combustion")]),
("10.1",1,[]),
("10.2",1,[L("chem21-s2.8.1",E,"Q = m c ΔT")]),
("10.3",1,[L("chem21-s2.8.6",E,"specific heat capacity")]),
("10.4",1,[L("chem21-s5.10.2",E,"Q from heating water"),L("chem21-s2.8.5",H,"sign of ΔH")]),
("10.5",1,[L("chem21-s5.6.0",E,"constant increase per CH2")]),
("11.b",1,[]),
("11.0",1,[]),
("11.1",1,[L("chem21-s5.10.4",H,"heat per mole calculation")]),
("11.2",1,[]),
("11.3",1,[]),
("11.4",1,[]),
("12.b",1,[]),
("12.0",1,[]),
("12.1",1,[]),
("12.2",1,[]),
("12.3",1,[]),
("12.4",1,[]),
("12.5",1,[]),
("12.6",1,[L("chem21-s5.12.2",E,"initial mass of burner")]),
("12.7",1,[]),
("13.b",1,[]),
("13.0",2,[]),
("14.b",1,[]),
("14.0",1,[L("chem21-s5.13.0",H,"copper can in apparatus")]),
("14.1",1,[L("chem21-s5.13.0",H,"draught shield in apparatus")]),
("14.2",1,[L("chem21-s5.12.6",H,"reweigh burner at once")]),
("14.3",1,[L("chem21-s5.12.4",H,"stirring step")]),
("14.4",1,[L("chem21-s5.11.4",H,"same temperature rise")]),
("14.5",1,[L("chem21-s5.12.5",H,"20 °C rise step")]),
("15.b",1,[]),
("15.0",1,[L("chem21-s5.10.2",E,"Q = m c ΔT")]),
("15.1",1,[]),
("15.2",2,[L("chem21-s5.15.0",E,"Q from water"),L("chem21-s5.15.1",E,"moles of ethanol burned")]),
("15.3",1,[L("chem21-s5.15.2",E,"experimental value used"),L("chem21-s5.5.1",H,"standard ethanol value")]),
("16.b",1,[]),
("16.0",1,[L("chem21-s5.15.2",H,"same calculation method")]),
("16.1",1,[L("chem21-s5.15.2",H,"same calculation method")]),
("16.2",1,[L("chem21-s5.15.2",H,"same calculation method")]),
("16.3",1,[L("chem21-s5.5.1",E,"standard alcohol values"),L("chem21-s5.16.2",H,"experimental values")]),
("16.4",1,[L("chem21-s5.6.5",H,"straight-line trend"),L("chem21-s5.16.3",H,"experimental below standard")]),
("17.b",1,[]),
("17.0",1,[]),
("17.1",1,[L("chem21-s5.10.2",E,"Q = m c ΔT")]),
("17.2",1,[L("chem21-s5.0.2",E,"incomplete combustion products")]),
("17.3",1,[L("chem21-s5.14.2",E,"capping prevents evaporation")]),
("17.4",1,[L("chem21-s5.7.1",H,"vapour condensation heat"),L("chem21-s5.0.3",H,"standard liquid water")]),
("17.5",1,[L("chem21-s5.17.0",E,"heat loss error"),L("chem21-s5.14.1",H,"draught shield")]),
("17.6",1,[L("chem21-s5.17.2",H,"incomplete combustion error"),L("chem21-s5.17.3",H,"evaporation error"),L("chem21-s5.17.1",H,"can absorbs heat")]),
("17.7",1,[]),
("18.b",1,[]),
("18.0",1,[]),
("18.1",1,[]),
("18.2",1,[]),
]
# pack2 links (explicit for every id)
P2={i:[] for i,_,_ in P1}
P2.update({
"0.3":[L("chem8-s1.0.0",H,"per mole amount")],
"0.4":[L("chem8-s1.0.0",H,"per mole amount")],
"2.0":[L("chem23-s3.1.0",H,"alkane general formula")],
"2.1":[L("chem23-s3.2.0",H,"alkene general formula")],
"2.2":[L("chem23-s3.3.0",H,"alkyne general formula")],
"3.0":[L("chem23-s3.1.0",H,"alkane formulae")],
"3.1":[L("chem23-s3.1.0",H,"alkane formulae")],
"3.2":[L("chem23-s3.1.0",H,"alkane formulae")],
"3.3":[L("chem23-s3.2.0",H,"alkene formulae")],
"3.4":[L("chem23-s3.2.0",H,"alkene formulae")],
"3.5":[L("chem23-s3.3.0",H,"alkyne formulae")],
"5.0":[L("chem23-s3.1.0",H,"alkane names and formulae","low")],
"6.b":[L("chem23-s3.0.5",E,"homologous series")],
"6.0":[L("chem23-s3.0.5",H,"homologous series")],
"9.1":[L("chem23-s3.2.0",H,"alkene has two fewer H","low")],
"10.4":[L("chem8-s1.2.0",H,"moles from mass")],
"15.1":[L("chem8-s1.2.0",E,"moles from mass and M")],
"16.0":[L("chem8-s1.2.0",H,"moles from mass")],
"16.1":[L("chem8-s1.2.0",H,"moles from mass")],
"16.2":[L("chem8-s1.2.0",H,"moles from mass")],
})
def pack_ids(f):
    ids=[]
    for l in open(D+'packs/'+f):
        if l.startswith('CANDIDATES'): break
        m=re.match(r'\[(chem21-s5\.[^\]]+)\]',l)
        if m: ids.append(m.group(1))
    return ids
def allids(f):
    return {m for l in open(D+'packs/'+f) for m in re.findall(r'^\[([^\]]+)\]',l)}
for f,out in (('chem21-s5.t1g1.txt',1),('chem21-s5.t1g2.txt',2)):
    ids=pack_ids(f); names=['chem21-s5.'+i for i,_,_ in P1]
    assert ids==names,(set(ids)^set(names))
    res={}
    for i,c,l in P1:
        k='chem21-s5.'+i
        if out==1: res[k]={"cost":c,"needs":l}
        else: res[k]={"needs":P2[i]}
    ok=allids(f)
    n=0
    for k,v in res.items():
        for x in v["needs"]:
            assert x["id"] in ok and x["id"]!=k,(k,x["id"]); n+=1
    json.dump(res,open(D+'point-links/'+f.replace('.txt','.json'),'w'),ensure_ascii=False,indent=0)
    low=sum(x["confidence"]=="low" for v in res.values() for x in v["needs"])
    print(f,len(res),n,sum(v.get("cost")==2 for v in res.values()),low)
