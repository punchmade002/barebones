import json,re
H,E,h,l='high','essential','helpful','low'
def n(i,s,w,c=H): return {"id":i,"strength":s,"why":w,"confidence":c}
T={
"0.b":(1,[]),
"0.0":(1,[n("bio9-s1.0.b",E,"transfer molecule definition")]),
"0.1":(1,[n("bio9-s1.0.b",E,"transfer molecule definition")]),
"0.2":(1,[]),
"0.3":(1,[n("bio9-s1.0.2",E,"catabolic reaction type")]),
"0.4":(1,[n("bio9-s1.0.2",E,"anabolic reaction type")]),
"0.5":(2,[n("bio9-s1.0.3",E,"catabolic reactions"),n("bio9-s1.0.4",E,"anabolic reactions"),n("bio9-s1.0.1",h,"ATP as energy carrier")]),
"1.b":(1,[]),
"1.0":(2,[n("bio9-s1.1.b",h,"three-part ATP structure")]),
"1.1":(1,[n("bio9-s1.1.0",E,"adenine, ribose, phosphates")]),
"1.2":(1,[n("bio9-s1.1.0",E,"base, sugar, phosphate parts")]),
"1.3":(1,[n("bio9-s1.1.0",E,"ATP's three phosphates")]),
"1.4":(1,[n("bio9-s1.1.0",h,"phosphate group in ATP")]),
"1.5":(2,[n("bio9-s1.1.0",E,"parts of ATP"),n("bio9-s1.1.3",h,"ADP structure"),n("bio9-s1.2.2",h,"end bond broken for energy",l)]),
"2.b":(1,[n("bio9-s1.1.0",h,"end phosphate of ATP")]),
"2.0":(2,[n("bio9-s1.1.3",E,"ADP as product"),n("bio9-s1.1.4",E,"Pi as product")]),
"2.1":(1,[n("bio9-s1.2.0",E,"ATP breakdown reaction")]),
"2.2":(2,[n("bio9-s1.2.0",h,"end phosphate removal")]),
"2.3":(1,[n("bio9-s1.2.0",h,"energy release from ATP")]),
"2.4":(2,[n("bio9-s1.2.0",E,"released phosphate"),n("bio9-s1.1.4",h,"Pi as free phosphate",l)]),
"3.b":(1,[n("bio9-s1.2.0",h,"ATP breakdown to ADP"),n("bio9-s1.1.3",h,"ADP structure",l)]),
"3.0":(1,[n("bio9-s1.2.0",E,"reverse of ATP breakdown"),n("bio9-s1.1.3",h,"ADP structure")]),
"3.1":(1,[n("bio9-s1.3.0",E,"phosphate added to ADP")]),
"3.2":(2,[n("bio9-s1.3.0",E,"energy needed to make ATP")]),
"3.3":(2,[n("bio9-s1.3.0",E,"ATP made from ADP + Pi"),n("bio9-s1.3.2",h,"ATP made in respiration",l)]),
"4.b":(1,[n("bio9-s1.2.0",h,"ATP breakdown half"),n("bio9-s1.3.0",h,"ATP remaking half")]),
"4.0":(2,[n("bio9-s1.2.0",E,"ATP breakdown"),n("bio9-s1.3.0",E,"ATP remaking")]),
"4.1":(1,[n("bio9-s1.4.0",E,"ATP/ADP cycle")]),
"4.2":(1,[n("bio9-s1.4.1",h,"small ATP store"),n("bio9-s1.3.2",h,"ATP made by respiration")]),
"4.3":(2,[n("bio9-s1.4.0",E,"ATP/ADP cycle"),n("bio9-s1.5.b",h,"cell work uses ATP",l)]),
"5.b":(1,[n("bio9-s1.2.0",h,"ATP energy release")]),
"5.0":(2,[n("bio9-s1.2.0",h,"ATP releases energy"),n("bio9-s1.3.2",h,"mitochondria make ATP")]),
"5.1":(2,[n("bio9-s1.2.0",h,"ATP releases energy")]),
"5.2":(1,[n("bio9-s1.5.1",E,"active transport by pumps")]),
"5.3":(2,[n("bio9-s1.0.4",E,"anabolic reactions need energy")]),
"5.4":(1,[n("bio9-s1.0.4",h,"photosynthesis is anabolic"),n("bio9-s1.3.3",h,"light stage makes ATP")]),
"5.5":(1,[n("bio9-s1.2.0",h,"ATP releases energy")]),
"6.b":(1,[n("bio9-s1.3.2",h,"glucose makes ATP in respiration")]),
"6.0":(1,[]),
"6.1":(1,[n("bio9-s1.2.3",E,"small single-step packet"),n("bio9-s1.6.0",h,"glucose releases too much")]),
"6.2":(1,[n("bio9-s1.4.0",h,"ATP recycled in cycle")]),
"6.3":(2,[n("bio9-s1.3.2",h,"respiration makes ATP")]),
"7.b":(1,[n("bio9-s1.5.5",h,"firefly bioluminescence uses ATP")]),
"7.0":(2,[n("bio9-s1.5.5",E,"luciferase uses ATP for light")]),
"7.1":(1,[n("bio9-s1.7.0",E,"luciferase light shows ATP")]),
}
out={"bio9-s1."+k:{"cost":c,"needs":v} for k,(c,v) in T.items()}
open('/Users/gabrielwhelan/barebones/drafts/crunch/biology/point-links/bio9-s1.json','w').write(json.dumps(out,indent=1))
pk=open('/Users/gabrielwhelan/barebones/drafts/crunch/biology/points/bio9-s1.txt').read()
ids=re.findall(r'^\[([^\]]+)\]',pk,re.M)
tg=[i for i in ids if i.startswith('bio9-s1.')]
assert list(out)==tg,(set(tg)^set(out))
for k,v in out.items():
    for x in v['needs']: assert x['id'] in ids and x['id']!=k,(k,x)
nl=sum(len(v['needs']) for v in out.values())
print(len(out),nl,sum(v['cost']==2 for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
