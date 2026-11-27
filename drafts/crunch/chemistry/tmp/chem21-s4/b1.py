import json,re
base='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/chemistry/'
E,H='essential','helpful'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
D={
"chem21-s4.0.b":(1,[]),
"chem21-s4.0.0":(1,[L("chem21-s1.1.1",H,"enthalpy change definition")]),
"chem21-s4.0.1":(1,[L("chem21-s4.0.0",E,"Hess's law statement")]),
"chem21-s4.0.2":(1,[L("chem21-s1.0.0",E,"conservation of energy"),L("chem21-s4.0.1",H,"path independence of ΔH")]),
"chem21-s4.0.3":(1,[L("chem21-s4.0.0",E,"using Hess's law to find ΔH")]),
"chem21-s4.0.4":(1,[L("chem21-s5.0.2",H,"incomplete combustion gives CO and CO₂")]),
"chem21-s4.0.5":(1,[]),
"chem21-s4.1.b":(1,[L("chem21-s4.0.0",H,"Hess's law")]),
"chem21-s4.1.0":(1,[L("chem21-s4.0.0",E,"Hess's law routes")]),
"chem21-s4.1.1":(1,[L("chem21-s4.1.0",E,"direct and indirect routes"),L("chem21-s4.0.1",H,"ΔH independent of route","low")]),
"chem21-s4.1.2":(1,[L("chem21-s1.6.6",E,"reversing reaction reverses ΔH sign")]),
"chem21-s4.1.3":(2,[L("chem21-s4.1.0",E,"structure of an energy cycle"),L("chem21-s5.0.3",H,"combustion products and heat of combustion","low")]),
"chem21-s4.1.4":(2,[L("chem21-s4.1.1",E,"sum ΔH along routes"),L("chem21-s4.1.3",E,"methane cycle set-up"),L("chem21-s5.0.3",H,"heat of combustion")]),
"chem21-s4.1.5":(1,[L("chem21-s4.1.4",E,"combustion routes from cycle"),L("chem21-s4.1.2",H,"change sign going backwards")]),
"chem21-s4.1.6":(1,[L("chem21-s1.9.0",E,"enthalpy level diagram")]),
"chem21-s4.1.7":(2,[L("chem21-s4.1.3",E,"methane cycle"),L("chem21-s4.1.6",H,"enthalpy level diagram of cycle")]),
"chem21-s4.2.b":(1,[L("chem21-s4.0.0",H,"Hess's law")]),
"chem21-s4.2.0":(1,[]),
"chem21-s4.2.1":(1,[L("chem21-s4.2.0",E,"target equation")]),
"chem21-s4.2.2":(1,[L("chem21-s1.6.6",E,"reverse equation changes ΔH sign")]),
"chem21-s4.2.3":(1,[L("chem21-s1.6.7",E,"ΔH proportional to coefficients")]),
"chem21-s4.2.4":(1,[L("chem21-s4.0.0",E,"stage ΔH values add up")]),
"chem21-s4.2.5":(1,[L("chem21-s4.2.4",E,"added equations to cancel")]),
"chem21-s4.3.b":(1,[L("chem21-s4.0.0",H,"Hess's law")]),
"chem21-s4.3.0":(1,[L("chem21-s2.7.2",H,"standard states and conditions")]),
"chem21-s4.3.1":(1,[L("chem21-s4.3.0",E,"one mole of compound formed")]),
"chem21-s4.3.2":(2,[L("chem21-s4.3.1",E,"writing formation equations")]),
"chem21-s4.3.3":(1,[L("chem21-s4.3.0",E,"formation from elements")]),
"chem21-s4.3.4":(1,[L("chem21-s5.0.3",E,"heat of combustion"),L("chem21-s4.3.0",E,"heat of formation")]),
"chem21-s4.3.5":(1,[L("chem21-s4.0.0",E,"finding ΔH by Hess's law"),L("chem21-s5.0.3",H,"heats of combustion")]),
"chem21-s4.3.6":(2,[L("chem21-s4.3.0",E,"heats of formation"),L("chem21-s4.0.0",H,"Hess's law")]),
"chem21-s4.3.7":(1,[L("chem21-s4.3.6",E,"products minus reactants formula"),L("chem21-s4.0.1",H,"route-independent ΔH")]),
"chem21-s4.4.b":(1,[L("chem21-s4.2.b",H,"combining equations")]),
"chem21-s4.4.0":(1,[L("chem21-s4.2.0",H,"target and given equations")]),
"chem21-s4.4.1":(1,[L("chem21-s4.2.1",E,"rearranging given equations")]),
"chem21-s4.4.2":(1,[L("chem21-s4.2.3",E,"multiplying equation and ΔH")]),
"chem21-s4.4.3":(1,[L("chem21-s4.2.2",E,"reversing equation and ΔH sign")]),
"chem21-s4.4.4":(1,[L("chem21-s4.2.5",E,"adding and cancelling equations")]),
"chem21-s4.4.5":(1,[L("chem21-s4.2.4",E,"adding ΔH values")]),
"chem21-s4.5.b":(1,[L("chem21-s4.3.6",E,"products minus reactants")]),
"chem21-s4.5.0":(1,[L("chem21-s4.3.6",E,"ΔHf sum formula"),L("chem21-s4.3.3",E,"element ΔHf is zero")]),
"chem21-s4.5.1":(1,[L("chem21-s4.3.6",E,"sum of products times coefficients")]),
"chem21-s4.5.2":(1,[L("chem21-s4.3.3",H,"zero ΔHf for O₂")]),
"chem21-s4.5.3":(1,[L("chem21-s4.3.6",E,"products minus reactants")]),
"chem21-s4.6.b":(1,[L("chem21-s4.3.6",E,"products minus reactants")]),
"chem21-s4.6.0":(1,[L("chem21-s4.3.3",H,"zero ΔHf for O₂")]),
"chem21-s4.6.1":(2,[L("chem21-s4.3.6",E,"products minus reactants with coefficients")]),
"chem21-s4.7.b":(1,[L("chem21-s4.1.5",E,"ΔHf from ΔHc cycle result")]),
"chem21-s4.7.0":(1,[L("chem21-s4.1.5",H,"formula using ΔHc values")]),
"chem21-s4.7.1":(1,[L("chem21-s4.1.5",E,"ΔHf from ΔHc formula")]),
"chem21-s4.7.2":(1,[L("chem21-s1.6.1",E,"endothermic means products higher enthalpy")]),
"chem21-s4.8.b":(1,[L("chem21-s4.2.b",E,"combining given equations")]),
"chem21-s4.8.0":(1,[L("chem21-s4.2.0",H,"target equation first")]),
"chem21-s4.8.1":(1,[L("chem21-s4.2.2",E,"reverse equation, flip ΔH"),L("chem21-s4.2.3",E,"multiply equation and ΔH")]),
"chem21-s4.8.2":(1,[L("chem21-s4.2.2",E,"reverse equation, flip ΔH")]),
"chem21-s4.8.3":(1,[L("chem21-s4.2.3",E,"multiply equation and ΔH")]),
"chem21-s4.8.4":(1,[L("chem21-s4.2.5",E,"add and cancel equations")]),
}
txt=open(base+'packs/chem21-s4.t1g1.txt').read()
ids=re.findall(r'^\[(\S+?)\]',txt,re.M)
tg=txt.split('CANDIDATES')[0]
targets=re.findall(r'^\[(\S+?)\]',tg,re.M)
assert set(targets)==set(D) and len(targets)==len(D),(set(targets)^set(D))
for t,(c,ns) in D.items():
    for n in ns: assert n['id'] in ids and n['id']!=t,(t,n['id'])
json.dump({t:{"cost":D[t][0],"needs":D[t][1]} for t in targets},open(base+'point-links/chem21-s4.t1g1.json','w'),ensure_ascii=False,indent=0)
print(len(targets),sum(len(v[1]) for v in D.values()),sum(v[0]==2 for v in D.values()),sum(n['confidence']=='low' for v in D.values() for n in v[1]))
