import json,re,sys
B='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
H,E='h','e'
S={'h':('essential','helpful')}
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
def h(i,w,c='high'): return L(i,'helpful',w,c)
def e(i,w,c='high'): return L(i,'essential',w,c)

P={}
# ---- environmental s4
p='hom-environmental-issues-s4.'
a='hom-appliances-equipment-s2.'; r='hom-environmental-issues-s2.'; r1='hom-environmental-issues-s1.'
P['hom-environmental-issues-s4.t1g1']=(p,[
('0.b',1,[]),('0.0',1,[]),('0.1',1,[]),('0.2',1,[]),
('0.3',1,[h(r+'0.4','landfill or recovery of waste','low')]),
('1.b',1,[]),('1.0',1,[]),('1.1',1,[]),('1.2',1,[]),('1.3',1,[]),('1.4',1,[]),('1.5',1,[]),('1.6',1,[]),
('2.b',1,[]),('2.0',2,[]),('2.1',1,[]),
('2.2',1,[h(r1+'1.6','renewable heat sources')]),
('2.3',2,[h(r1+'4.0','effects of carbon dioxide emissions','low')]),
('2.4',1,[h(p+'2.3','emissions being reduced')]),
('3.b',1,[]),('3.0',1,[]),
('3.1',1,[h(p+'3.0','heating water uses energy')]),
('3.2',1,[]),('3.3',1,[]),('3.4',1,[]),('3.5',1,[]),('3.6',1,[]),('3.7',1,[]),
('4.b',1,[]),
('4.0',1,[h(r+'0.5','anaerobic decomposition releasing methane')]),
('4.1',1,[]),('4.2',2,[]),('4.3',1,[]),
('4.4',1,[h(r+'1.0','composting of food and garden waste')]),
('5.b',1,[]),('5.0',1,[]),('5.1',1,[]),('5.2',1,[]),('5.3',1,[]),
('5.4',1,[h(r+'4.3','EU Ecolabel')]),
('5.5',1,[]),
('6.b',1,[]),
('6.0',2,[h(a+'4.0','EU energy label A to G scale')]),
('6.1',1,[h(a+'4.3','energy consumption shown on label')]),
('6.2',1,[h(a+'4.4','water use shown on label')]),
('6.3',1,[h(p+'6.0','high energy rating')]),
('6.4',2,[]),
('7.b',1,[]),('7.0',1,[]),('7.1',1,[]),('7.2',2,[]),('7.3',1,[]),('7.4',2,[]),('7.5',2,[]),
('7.6',1,[h(p+'3.2','full loads save energy')]),
('8.b',1,[]),('8.0',1,[]),('8.1',1,[]),
('8.2',1,[h(r+'7.3','retailer take-back route')]),
('9.b',1,[]),('9.0',1,[]),('9.1',1,[]),('9.2',1,[]),('9.3',1,[]),
('9.4',1,[h(p+'1.4','lagging cylinder and pipes')]),
])
# ---- energy nutrition s5
p='hom-energy-nutrition-s5.'; s4='hom-energy-nutrition-s4.'; c5='hom-carbohydrates-s5.'; l5='hom-lipids-s5.'; v4='hom-vitamins-minerals-s4.'
P['hom-energy-nutrition-s5.t1g1']=(p,[
('0.b',1,[]),('0.0',1,[]),('0.1',1,[]),('0.2',1,[]),('0.3',1,[]),('0.4',1,[]),('0.5',1,[]),('0.6',1,[]),('0.7',1,[]),
('1.b',1,[]),
('1.0',1,[h(c5+'1.0','fibre value in the diet','low')]),
('1.1',1,[]),('1.2',1,[]),('1.3',1,[]),('1.4',1,[]),('1.5',1,[]),('1.6',1,[]),('1.7',1,[]),('1.8',1,[]),
('2.b',1,[]),('2.0',1,[]),('2.1',1,[]),('2.2',1,[]),('2.3',1,[]),('2.4',1,[]),('2.5',1,[]),('2.6',1,[]),('2.7',1,[]),
('3.b',2,[h(s4+'6.b','Food Pyramid as the benchmark')]),
('3.0',1,[h(s4+'1.1','guideline on wholegrain starchy foods')]),
('3.1',1,[h(s4+'1.0','five to seven portions guideline')]),
('3.2',1,[h(s4+'2.2','saturated fat raises cholesterol')]),
('3.3',1,[h(s4+'1.5','limit fat, sugar and salt')]),
('3.4',1,[h(s4+'6.2','top shelf of Food Pyramid')]),
('3.5',1,[h(s4+'3.4','nutrients often low in Irish diets','low')]),
('3.6',1,[h(p+'1.2','empty kilocalories')]),
('3.7',1,[]),
('4.b',1,[]),
('4.0',2,[h(p+'1.0','refined flour lowers fibre')]),
('4.1',2,[h(c5+'1.3','low fibre disease risks')]),
('4.2',2,[h(c5+'1.4','fibre gives fullness')]),
('4.3',2,[]),('4.4',1,[]),('4.5',1,[]),
('5.b',1,[]),('5.0',2,[]),('5.1',1,[]),
('5.2',2,[h(l5+'3.1','LDL cholesterol and heart disease')]),
('5.3',2,[]),('5.4',1,[]),('5.5',1,[]),
('6.b',1,[]),
('6.0',1,[h(v4+'2.2','iron in haemoglobin')]),
('6.1',2,[]),
('6.2',2,[h(v4+'2.4','iron deficiency anaemia')]),
('6.3',2,[h(v4+'2.5','causes of iron deficiency')]),
('6.4',1,[]),
('6.5',2,[h(v4+'2.6','vitamin C and iron absorption')]),
('6.6',1,[h(p+'6.4','tea reduces iron absorption')]),
('7.b',1,[]),
('7.0',2,[h(v4+'1.3','calcium functions')]),
('7.1',2,[]),
('7.2',2,[h(v4+'1.5','osteoporosis and low calcium')]),
('7.3',2,[h(v4+'1.0','dairy calcium sources','low')]),
('7.4',2,[h(p+'7.1','calcium-rich foods')]),
('7.5',1,[]),
('8.b',1,[]),('8.0',1,[]),
('8.1',1,[h(s4+'4.0','nutrient content from food tables','low')]),
('8.2',1,[h(s4+'1.b','healthy eating guidelines')]),
('8.3',1,[]),('8.4',1,[]),
('9.b',1,[h(s4+'6.b','Food Pyramid')]),
('9.0',1,[]),('9.1',1,[]),('9.2',1,[]),
('9.3',1,[h(s4+'1.b','healthy eating guidelines')]),
('9.4',1,[]),
])
# ---- microwave s6
p='hom-appliances-equipment-s6.'; a='hom-appliances-equipment-s2.'; c2='hom-cooking-methods-s2.'
P['hom-appliances-equipment-s6.t1g1']=(p,[
('0.b',1,[]),('0.0',1,[]),('0.1',1,[]),('0.2',1,[]),('0.3',1,[]),
('1.b',1,[]),('1.0',1,[]),
('1.1',1,[h(p+'1.0','transformer supplies magnetron voltage')]),
('1.2',1,[h(p+'1.1','microwaves from the magnetron')]),
('1.3',1,[h(p+'1.2','microwaves in the cavity')]),
('1.4',1,[]),('1.5',1,[]),('1.6',2,[]),
('1.7',2,[h(p+'1.1','timer stops the magnetron')]),
('1.8',2,[]),
('2.b',1,[]),
('2.0',1,[h(p+'1.1','magnetron makes microwaves')]),
('2.1',1,[h(p+'1.2','waveguide directs microwaves')]),
('2.2',1,[]),('2.3',1,[]),('2.4',2,[]),
('2.5',1,[h(c2+'2.b','heat conduction','high')]),
('2.6',1,[]),('2.7',1,[]),
('3.b',1,[]),('3.0',1,[]),
('3.1',1,[h(p+'2.2','metal reflects microwaves')]),
('3.2',1,[]),
('3.3',1,[h(p+'2.3','outer layers heat first')]),
('3.4',1,[]),('3.5',1,[]),
('3.6',1,[h(p+'2.5','heat conducts to the centre')]),
('3.7',1,[]),
('3.8',1,[h(c2+'2.0.0','heating destroys bacteria'.replace('2.0.0','')) if False else h(c2+'0.0','heat destroys bacteria')]),
('4.b',1,[]),('4.0',2,[]),('4.1',2,[]),
('4.2',2,[h(a+'0.b','buying criteria cost and capacity')]),
('5.b',1,[]),('5.0',1,[]),('5.1',1,[]),('5.2',1,[]),('5.3',1,[]),('5.4',1,[]),
('5.5',1,[h(p+'0.2','combination oven type')]),
('5.6',1,[]),('5.7',1,[]),('5.8',1,[]),
('6.b',1,[]),('6.0',1,[]),('6.1',1,[]),('6.2',1,[]),('6.3',1,[]),('6.4',1,[]),
('6.5',1,[h(a+'4.0','energy label rating','low')]),
('6.6',1,[]),('6.7',1,[]),
('6.8',1,[h(p+'2.7','no browning explained')]),
('7.b',1,[]),
('7.0',2,[h(p+'1.1','microwave frequency of magnetron')]),
('7.1',2,[h(p+'1.0','transformer raises voltage')]),
('7.2',2,[e(p+'7.1','step-up ratio uses induction')]),
('7.3',2,[h(p+'1.1','magnetron produces microwaves')]),
('7.4',2,[h(p+'2.4','water molecules polar heating')]),
('7.5',1,[h(p+'1.6','door metal screen')]),
('7.6',1,[h(p+'1.6','door interlock')]),
('7.7',2,[h(p+'7.4','polar molecules in a field')]),
])
for name,(p,items) in P.items():
    txt=open(B+'packs/'+name+'.txt').read()
    tgt=[]; ids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    sec=txt.split('CANDIDATES')[0]
    tgt=re.findall(r'^\[([^\]]+)\]',sec,re.M)
    out={}
    for k,c,n in items:
        assert p+k not in out; out[p+k]={"cost":c,"needs":n}
    assert list(out)==tgt,(name,set(tgt)^set(out))
    for k,v in out.items():
        for n in v['needs']: assert n['id'] in ids and n['id']!=k,(k,n['id'])
    json.dump(out,open(B+'point-links/'+name+'.json','w'),indent=1)
    json.dump(json.load(open(B+'point-links/'+name+'.json')),open('/dev/null','w'))
    nl=sum(len(v['needs']) for v in out.values())
    print(name,len(out),nl,sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
