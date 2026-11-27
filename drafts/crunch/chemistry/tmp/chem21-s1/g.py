import json,re
D='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/chemistry/'
H,E='helpful','essential'
def L(i,s,w,c='high'):
    return {"id":i if ':' not in i else i,"strength":s,"why":w,"confidence":c}
S=lambda k:"chem21-s1."+k
R={
"0.b":(1,[]),"0.0":(1,[]),
"0.1":(1,[L("chem5-s1.0.0",H,"chemical bonds")]),
"0.2":(1,[]),"0.3":(1,[]),
"0.4":(1,[L(S("0.0"),E,"system and surroundings exchange conserved energy")]) if False else (1,[L(S("0.3"),E,"system and surroundings defined")]),
"0.5":(1,[L(S("0.4"),E,"energy lost by system gained by surroundings")]),
"1.b":(1,[]),
"1.0":(1,[L(S("0.1"),H,"energy stored in bonds")]),
"1.1":(1,[L(S("1.0"),E,"enthalpy as heat content")]),
"1.2":(1,[L(S("1.1"),E,"enthalpy change definition")]),
"1.3":(1,[L(S("1.1"),E,"ΔH = H products − H reactants")]),
"1.4":(1,[L(S("1.1"),E,"enthalpy change at constant pressure")]),
"2.b":(1,[]),
"2.0":(1,[L("chem5-s1.2.0",E,"covalent bond as shared pair")]),
"2.1":(1,[L(S("2.0"),E,"bond enthalpy definition")]),
"2.2":(1,[L(S("2.0"),E,"energy to break a bond")]),
"2.3":(1,[L(S("2.0"),E,"bond enthalpy definition")]),
"2.4":(1,[L(S("2.0"),E,"bond enthalpy measures bond strength")]),
"3.b":(1,[]),
"3.0":(1,[L(S("2.0"),H,"breaking bonds in reactants")]),
"3.1":(1,[L(S("1.3"),E,"endothermic and exothermic terms"),L(S("2.2"),H,"bond breaking needs energy")]),
"3.2":(1,[L(S("3.1"),E,"bond breaking is endothermic")]),
"3.3":(2,[L(S("3.1"),E,"breaking takes energy in"),L(S("3.2"),E,"making releases energy")]),
"3.4":(1,[L(S("3.3"),H,"mirror of the exothermic case")]),
"3.5":(2,[L(S("3.3"),E,"comparing energy of breaking and making")]),
"3.6":(2,[L(S("3.3"),E,"more energy released than needed"),L(S("2.4"),H,"strong bonds hold more energy")]),
"3.7":(2,[L(S("3.3"),E,"more energy released than needed")]),
"4.b":(1,[]),
"4.0":(1,[]),
"4.1":(1,[L(S("3.3"),H,"bond breaking and making balance")]),
"4.2":(2,[]),
"4.3":(1,[L(S("3.3"),E,"bond energy balance gives heat change")]),
"5.b":(1,[]),
"5.0":(2,[L("chem10-s1.1.2",H,"changes of state are physical changes")]),
"5.1":(1,[L(S("5.0"),E,"intermolecular forces overcome, bonds kept")]),
"5.2":(1,[L(S("5.0"),E,"overcoming forces takes energy")]),
"5.3":(2,[L(S("5.2"),H,"melting and boiling are endothermic")]),
"5.4":(1,[L(S("5.2"),E,"reverse of melting and boiling")]),
"5.5":(1,[L(S("1.3"),H,"exothermic and endothermic")]),
"5.6":(1,[L(S("5.5"),H,"dissolving can be endothermic")]),
"5.7":(1,[L(S("5.2"),E,"evaporation is endothermic")]),
"6.b":(1,[]),
"6.0":(1,[L(S("1.3"),E,"negative ΔH means heat given out")]),
"6.1":(1,[L(S("1.3"),E,"positive ΔH means heat taken in")]),
"6.2":(1,[L(S("6.0"),E,"exothermic reaction gives out heat")]),
"6.3":(1,[L(S("6.1"),E,"endothermic reaction takes in heat")]),
"6.4":(1,[L(S("1.1"),E,"ΔH value and units")]),
"6.5":(1,[L(S("6.4"),E,"state symbols in thermochemical equations")]),
"6.6":(1,[L(S("6.4"),E,"ΔH of an equation")]),
"6.7":(2,[L(S("6.4"),E,"ΔH goes with the equation as written")]),
"7.b":(1,[]),
"7.0":(1,[L(S("6.4"),E,"thermochemical equation with ΔH")]),
"7.1":(2,[L(S("6.4"),H,"thermochemical equation with ΔH")]),
"7.2":(2,[L(S("6.4"),H,"thermochemical equation with ΔH")]),
"7.3":(2,[L(S("6.4"),H,"thermochemical equation with ΔH")]),
"7.4":(1,[L(S("7.3"),E,"rusting equation and ΔH")]),
"7.5":(1,[L(S("6.0"),H,"exothermic reaction")]),
"8.b":(1,[]),
"8.0":(1,[L(S("6.1"),H,"endothermic reaction")]),
"8.1":(1,[L(S("8.0"),H,"thermal decomposition is endothermic")]),
"8.2":(2,[L(S("6.1"),H,"endothermic reaction")]),
"8.3":(1,[L(S("6.6"),E,"reversing flips sign of ΔH"),L(S("7.2"),H,"respiration equation")]),
"8.4":(1,[L(S("6.1"),H,"endothermic reaction")]),
"9.b":(1,[]),
"9.0":(2,[L(S("1.1"),E,"enthalpy and ΔH")]),
"9.1":(1,[L(S("9.0"),E,"enthalpy level diagram layout")]),
"9.2":(1,[L(S("9.0"),E,"enthalpy level diagram layout")]),
"9.3":(1,[L(S("6.0"),E,"heat flow in exothermic and endothermic")]),
"9.4":(2,[L(S("9.1"),E,"exothermic diagram"),L(S("9.2"),E,"endothermic diagram")]),
"9.5":(1,[L(S("4.0"),H,"activation energy")]),
}
pk=open(D+'packs/chem21-s1.t1g1.txt').read()
tg=[];sec=None
for ln in pk.split('\n'):
    if ln.startswith('TARGET'): sec='T'
    elif ln.startswith('CANDIDATES'): sec='C'
    m=re.match(r'\[(\S+?)\]',ln)
    if m and sec=='T': tg.append(m.group(1))
ids=set(re.findall(r'^\[(\S+?)\]',pk,re.M))
keys=[t.split('chem21-s1.')[1] for t in tg]
assert set(R)==set(keys) and len(keys)==len(set(keys)),set(R)^set(keys)
out={}
for t,k in zip(tg,keys):
    c,n=R[k]; out[t]={"cost":c,"needs":n}
    for x in n: assert x['id'] in ids and x['id']!=t,(t,x)
json.dump(out,open(D+'point-links/chem21-s1.t1g1.json','w'),indent=0)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
