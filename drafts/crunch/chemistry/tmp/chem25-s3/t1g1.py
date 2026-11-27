import json,re
H,E='helpful','essential'
def n(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
P='chem25-s3.'
d={
"0.b":(1,[n('chem25-s5.0.0',H,'oxidation as gaining oxygen/losing hydrogen')]),
"0.0":(1,[n('chem26-s2.0.3',H,'percentage yield definition'),n('chem9-s2.8.4',H,'recrystallisation purifies crystals','low')]),
"0.1":(1,[n('chem24-s1.7.0',E,'primary alcohol definition'),n('chem25-s5.0.2',H,'primary alcohol to acid ladder')]),
"0.2":(2,[n('chem25-s5.3.0',H,'permanganate reduction in basic solution')]),
"0.3":(1,[n(P+'0.2',E,'same equation with potassium shown')]),
"0.4":(1,[n('chem25-s5.3.0',E,'permanganate reduced to MnO2 in base')]),
"0.5":(1,[n(P+'0.2',E,'mole ratios from balanced equation')]),
"0.6":(1,[]),
"0.7":(1,[]),
"1.b":(1,[]),
"1.0":(1,[]),
"1.1":(1,[]),
"1.2":(1,[n(P+'0.2',H,'excess permanganate and base in equation','low')]),
"1.3":(2,[n('chem25-s5.2.0',E,'heating under reflux'),n(P+'0.4',H,'purple to brown MnO2 change')]),
"1.4":(1,[n(P+'1.3',H,'reflux or water bath set-up')]),
"2.b":(1,[]),
"2.0":(1,[]),
"2.1":(2,[n(P+'3.2',H,'sulfite reduces MnO2 in acid'),n(P+'3.3',H,'why fume cupboard is needed','low')]),
"2.2":(1,[n(P+'3.0',H,'acid converts benzoate to benzoic acid')]),
"2.3":(1,[n(P+'3.0',H,'benzoic acid less soluble in cold water','low')]),
"2.4":(1,[n('chem9-s2.7.2',H,'filtration to collect solid')]),
"2.5":(1,[n(P+'2.4',H,'suction filtration apparatus')]),
"3.b":(1,[]),
"3.0":(1,[n(P+'0.1',E,'benzoate ion formed in base')]),
"3.1":(1,[n(P+'1.2',H,'sodium carbonate added as the base')]),
"3.2":(2,[n(P+'0.4',E,'brown MnO2 formed in oxidation'),n('chem25-s5.0.0',H,'reduction and oxidation ideas','low')]),
"3.3":(1,[n(P+'3.0',H,'HCl fumes from concentrated acid','low')]),
"4.b":(1,[]),
"4.0":(1,[n(P+'3.2',H,'MnCl2 and salts present as impurities','low')]),
"4.1":(1,[n(P+'4.0',H,'impurities to be removed')]),
"4.2":(1,[n(P+'4.1',E,'solubility hot versus cold water')]),
"4.3":(2,[n('chem9-s2.7.2',H,'filtration and filtrate'),n(P+'4.1',H,'benzoic acid crystallises when cooled')]),
"4.4":(1,[n(P+'4.1',E,'solubility differs with temperature')]),
"4.5":(1,[n(P+'4.4',H,'cooling stage before filtering')]),
"4.6":(1,[n(P+'2.4',H,'suction filtration and cold wash')]),
"4.7":(1,[]),
"5.b":(1,[]),
"5.0":(1,[]),
"5.1":(1,[n(P+'5.3',H,'melting point above 100 degrees')]),
"5.2":(1,[n(P+'5.0',H,'sample loaded in capillary tube')]),
"5.3":(1,[]),
"5.4":(1,[n(P+'5.3',E,'pure melting point value')]),
"5.5":(1,[n(P+'5.4',E,'impurities change melting range')]),
"5.6":(1,[n(P+'5.0',H,'capillary tube set-up')]),
"6.b":(1,[n('chem26-s2.0.3',H,'percentage yield definition')]),
"6.0":(1,[]),
"6.1":(2,[n('chem26-s2.1.1',E,'moles from mass and molar mass'),n(P+'6.0',H,'uses the sample data')]),
"6.2":(2,[n(P+'0.5',E,'1:1 mole ratio'),n('chem26-s2.1.2',H,'theoretical yield from mole ratio')]),
"6.3":(1,[n('chem26-s2.0.3',E,'percentage yield formula')]),
"6.4":(2,[n('chem26-s2.6.2',H,'product lost in transfer and purification')]),
"7.b":(1,[n('chem26-s2.0.1',H,'limiting reactant idea')]),
"7.0":(2,[n(P+'0.2',E,'3:4 ratio from equation'),n(P+'6.1',H,'moles of phenylmethanol')]),
"7.1":(1,[n(P+'7.0',E,'moles of KMnO4 needed')]),
"7.2":(2,[n(P+'7.1',E,'mass of KMnO4 needed'),n('chem26-s2.0.1',H,'limiting reactant')]),
"8.b":(1,[]),
"8.0":(1,[]),
"8.1":(1,[]),
}
out={P+k:{"cost":c,"needs":nd} for k,(c,nd) in d.items()}
base='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/chemistry/'
json.dump(out,open(base+'point-links/chem25-s3.t1g1.json','w'),ensure_ascii=False)
txt=open(base+'packs/chem25-s3.t1g1.txt').read()
tg=[]
sec=None
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
for l in txt.split('\n'):
    if l.startswith('TARGET'): sec=1
    elif l.startswith('CANDIDATES'): sec=0
    m=re.match(r'\[([^\]]+)\]',l)
    if m and sec: tg.append(m.group(1))
assert sorted(tg)==sorted(out) and len(tg)==len(out),(set(tg)^set(out))
for k,v in out.items():
    for x in v['needs']: assert x['id'] in allids and x['id']!=k,(k,x)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
