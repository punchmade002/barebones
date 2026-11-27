import json,re,sys
D='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/chemistry/'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
E,H='essential','helpful'
P='chem21-s2.'
R={
'0.b':(1,[]),
'0.0':(1,[L('chem21-s1.1.1',H,'enthalpy change ΔH definition')]),
'0.1':(1,[L('chem21-s1.1.1',H,'heat change at constant pressure'),L('chem8-s1.0.0',H,'the mole')]),
'0.2':(1,[L('chem10-s2.11.0',H,'ionic equations and spectator ions')]),
'0.3':(1,[L('chem21-s1.1.1',E,'ΔH defined at constant pressure')]),
'0.4':(1,[L(P+'8.6',H,'specific heat capacity c')]),
'1.b':(1,[]),
'1.0':(1,[L('chem8-s2.2.0',H,'molar concentration notation')]),
'1.1':(1,[]),'1.2':(1,[]),'1.3':(1,[]),'1.4':(1,[]),
'1.5':(1,[L(P+'0.4',H,'heat worked out from temperature rise')]),
'1.6':(1,[]),
'1.7':(1,[]),
'2.b':(1,[]),
'2.0':(1,[L('chem21-s1.0.3',H,'system and surroundings heat loss','low')]),
'2.1':(1,[]),'2.2':(1,[]),
'2.3':(1,[L(P+'0.1',H,'moles of water formed')]),
'2.4':(1,[]),'2.5':(1,[]),'2.6':(1,[]),
'2.7':(1,[L(P+'1.0',H,'burette step in the method','low')]),
'3.b':(1,[]),'3.0':(1,[]),'3.1':(1,[]),'3.2':(1,[]),
'3.3':(2,[L(P+'3.1',H,'uses the recorded temperature data')]),
'3.4':(1,[L(P+'3.3',H,'graph illustrates the extrapolation method')]),
'4.b':(1,[]),'4.0':(1,[]),
'4.1':(1,[L(P+'4.0',E,'uses the initial and maximum temperatures')]),
'4.2':(1,[L('chem8-s1.1.6',H,'mass from density and volume')]),
'4.3':(1,[L(P+'0.4',E,'Q = m × c × ΔT')]),
'4.4':(1,[L('chem8-s2.2.1',E,'moles from concentration and volume')]),
'4.5':(1,[L(P+'0.1',E,'ΔH is per mole of water')]),
'4.6':(1,[L('chem21-s1.1.3',E,'negative ΔH for exothermic')]),
'4.7':(1,[L(P+'5.0',H,'accepted value for strong acid-base')]),
'5.b':(1,[]),
'5.0':(2,[L('chem10-s2.11.3',E,'ionic equation of strong acid-base neutralisation')]),
'5.1':(1,[L(P+'5.0',H,'contrast with strong acid-base value')]),
'5.2':(1,[L('chem10-s2.12.0',H,'mole ratios from balanced equation')]),
'5.3':(1,[]),
'5.4':(2,[L(P+'4.3',H,'same heat calculation method')]),
'5.5':(1,[L(P+'5.2',E,'count moles of water from diprotic acid')]),
'5.6':(1,[L(P+'0.4',H,'Q depends on mass heated','low')]),
'6.b':(1,[]),'6.0':(1,[]),'6.1':(1,[]),
'6.2':(2,[]),
'6.3':(1,[L(P+'4.2',E,'mass of solution assumed as water')]),
'6.4':(2,[L(P+'3.3',H,'temperature-time graph correction')]),
'7.b':(1,[]),
'7.0':(1,[L('chem21-s1.1.1',H,'enthalpy change ΔH')]),
'7.1':(1,[]),
'7.2':(1,[L('chem8-s2.2.0',H,'concentration in mol L⁻¹')]),
'7.3':(1,[L(P+'7.1',H,'standard conditions')]),
'7.4':(1,[L(P+'7.1',E,'standard pressure definition')]),
'7.5':(1,[L('chem8-s1.9.0',E,'STP conditions')]),
'8.b':(1,[]),
'8.0':(1,[]),
'8.1':(1,[L(P+'0.4',H,'same Q = m × c × ΔT')]),
'8.2':(1,[L(P+'8.6',H,'specific heat capacity of water')]),
'8.3':(2,[L('chem8-s1.2.0',E,'n = m ÷ M for solids'),L('chem8-s2.2.1',E,'n = c × V for solutions')]),
'8.4':(1,[L(P+'8.3',E,'uses moles of limiting reactant')]),
'8.5':(1,[L('chem21-s1.1.3',E,'sign of ΔH exo/endothermic')]),
'8.6':(1,[]),
'8.7':(1,[L('chem8-s1.1.6',H,'density links volume and mass')]),
'8.8':(1,[L(P+'8.6',H,'heat capacity replaces c and m')]),
'9.b':(1,[]),'9.0':(1,[]),
'9.1':(1,[L('chem10-s2.11.0',H,'ionic equation')]),
'9.2':(1,[L(P+'8.3',E,'limiting reactant')]),
'9.3':(1,[L(P+'8.1',E,'Q = m × c × ΔT')]),
'9.4':(1,[L('chem8-s2.2.1',E,'moles from concentration and volume')]),
'9.5':(1,[L(P+'8.4',E,'heat per mole'),L(P+'8.5',E,'sign of ΔH from temperature rise')]),
'9.6':(1,[L(P+'6.2',H,'heat loss error')]),
'10.b':(1,[]),
'10.0':(1,[L('chem21-s1.6.7',H,'ΔH proportional to moles')]),
'10.1':(1,[L('chem8-s1.2.0',E,'moles from mass')]),
'10.2':(1,[L(P+'10.0',E,'heat by proportion of moles')]),
'10.3':(1,[L(P+'10.0',H,'ΔH per mole by proportion')]),
'11.b':(1,[]),
'11.0':(1,[L('chem21-s1.1.0',H,'enthalpy as heat content')]),
'11.1':(1,[L('chem21-s1.9.0',E,'enthalpy level diagram')]),
'11.2':(1,[L('chem21-s1.4.0',H,'activation energy')]),
'11.3':(1,[L('chem21-s1.1.1',H,'ΔH = H(products) − H(reactants)')]),
'11.4':(1,[L('chem21-s1.3.3',E,'bond making exceeds bond breaking')]),
'11.5':(1,[L('chem21-s1.3.4',E,'bond breaking exceeds bond making')]),
'11.6':(2,[L('chem21-s1.3.1',E,'bond breaking needs energy')]),
'11.7':(2,[L(P+'11.4',E,'exothermic profile'),L(P+'11.5',E,'endothermic profile')]),
}
R={P+k:v for k,v in R.items()}
txt=open(D+'packs/chem21-s2.t1g1.txt').read()
tg=txt.split('CANDIDATES')[0]
tids=re.findall(r'^\[(\S+?)\]',tg,re.M)
allids=set(re.findall(r'^\[(\S+?)\]',txt,re.M))
assert set(tids)==set(R) and len(tids)==len(R),(set(tids)^set(R))
out={}
for i in tids:
    c,n=R[i]
    for l in n: assert l['id'] in allids and l['id']!=i,(i,l)
    out[i]={"cost":c,"needs":n}
json.dump(out,open(D+'point-links/chem21-s2.t1g1.json','w'),ensure_ascii=False,indent=1)
o=json.load(open(D+'point-links/chem21-s2.t1g1.json'))
print(len(o),sum(len(v['needs']) for v in o.values()),sum(v['cost']==2 for v in o.values()),sum(l['confidence']=='low' for v in o.values() for l in v['needs']))
