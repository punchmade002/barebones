import json,re,sys
D='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
H,E='helpful','essential'
P={}
# package 1
p='hom-cooking-methods-s4.'
P['hom-cooking-methods-s4.t1g1']=[
('0.b',1,[]),
('0.0',1,[L(p+'0.5',H,'uses stock')]),
('0.1',1,[]),('0.2',1,[]),
('0.3',2,[L(p+'3.b',H,'uses roux as thickener','low')]),
('0.4',1,[]),('0.5',1,[]),
('0.6',1,[L(p+'0.5',H,'uses stock')]),
('1.b',1,[]),('1.0',1,[]),('1.1',1,[]),
('1.2',1,[L(p+'0.5',H,'uses stock as liquid')]),
('1.3',1,[L(p+'0.2',H,'uses purée soups')]),
('1.4',1,[]),
('1.5',1,[L(p+'0.3',H,'uses liaison','low')]),
('1.6',1,[]),('2.b',1,[]),
('2.0',2,[L(p+'0.2',H,'thick soups','low')]),
('2.1',1,[L(p+'0.0',H,'uses clear soups')]),
('2.2',1,[L(p+'0.4',H,'uses cold soups')]),
('2.3',1,[]),('3.b',1,[]),
('3.0',2,[L(p+'3.b',H,'uses roux')]),
('3.1',1,[L(p+'3.0',E,'continues roux steps')]),
('3.2',1,[L('hom-carbohydrates-s4.1.0',H,'gelatinisation of starch')]),
('3.3',1,[L(p+'3.b',H,'uses roux')]),
('3.4',1,[L(p+'3.3',H,'contrasts white roux','low'),L('hom-carbohydrates-s4.7.6',H,'browned flour thickens less','low')]),
('3.5',2,[L(p+'3.b',E,'liquid amount sets thickness')]),
('3.6',1,[L(p+'3.5',H,'uses panada binding sauce'),L(p+'3.3',H,'uses white sauce','low')]),
('3.7',2,[]),
('4.b',1,[]),
('4.0',1,[L(p+'3.7',H,'roux-based sauce examples')]),
('4.1',2,[]),('4.2',1,[]),('4.3',1,[]),('4.4',1,[]),('4.5',1,[]),('4.6',2,[]),
('5.b',1,[]),('5.0',1,[]),('5.1',1,[]),('5.2',1,[]),('5.3',1,[]),('5.4',1,[]),
('6.b',1,[]),('6.0',2,[]),('6.1',1,[]),('6.2',1,[]),('6.3',1,[]),
('7.b',1,[]),('7.0',1,[]),('7.1',1,[]),('7.2',1,[]),('7.3',2,[]),('7.4',1,[]),('7.5',1,[]),
('7.6',1,[L(p+'7.3',H,'uses salt in declaration'),L(p+'7.2',H,'uses allergen emphasis')]),
]
p='hom-food-safety-s9.'
P['hom-food-safety-s9.t1g1']=[
('0.b',1,[]),('0.0',1,[]),
('0.1',1,[L(p+'0.0',H,'uses EU regulation')]),
('0.2',1,[]),('0.3',1,[]),('1.b',1,[]),('1.0',1,[]),('1.1',2,[]),('1.2',1,[]),('1.3',1,[]),('1.4',1,[]),
('1.5',1,[L('hom-food-safety-s8.4.0',H,'environmental health officers inspect')]),
('1.6',1,[L(p+'1.2',H,'uses HACCP system'),L(p+'1.5',H,'uses closing premises','low')]),
('2.b',1,[]),('2.0',1,[]),
('2.1',1,[L(p+'3.0',H,'the 14 allergens')]),
('2.2',1,[]),('2.3',1,[]),('2.4',1,[]),('2.5',1,[]),('2.6',2,[]),('2.7',1,[]),
('3.b',1,[]),('3.0',2,[]),('3.1',1,[]),
('3.2',1,[L(p+'3.1',H,'contrasts use-by date')]),
('4.b',1,[]),
('4.0',1,[L('hom-food-safety-s8.1.0',H,'FSAI established by the Act','low')]),
('4.1',1,[L('hom-food-safety-s8.3.0',H,'official agencies')]),
('4.2',1,[]),('4.3',1,[]),
('4.4',1,[L('hom-food-safety-s8.7.1',H,'traceability one step back/forward')]),
('4.5',1,[L('hom-food-safety-s8.7.3',H,'rapid alerts','low')]),
('4.6',2,[]),('4.7',1,[]),
('5.b',1,[]),('5.0',1,[]),('5.1',1,[]),('5.2',1,[]),('5.3',1,[]),
('5.4',1,[L('hom-food-safety-s8.1.2',H,'FSAI coordinates agencies'),L('hom-food-safety-s8.3.0',H,'official agencies list','low')]),
('5.5',1,[L('hom-food-safety-s8.4.3',H,'closure orders and enforcement notices')]),
]
p='hom-consumer-rights-s5.'
P['hom-consumer-rights-s5.t1g1']=[
('0.b',1,[]),('0.0',1,[]),('0.1',1,[]),('0.2',1,[]),('0.3',1,[]),
('1.b',1,[]),
('1.0',1,[L('hom-consumer-rights-s4.5.b',H,'Consumer Protection Act 2007')]),
('1.1',1,[L('hom-consumer-rights-s4.6.1',H,'misleading price claims')]),
('1.2',1,[L(p+'0.1',H,'voluntary bodies lack legal powers','low')]),
('1.3',1,[]),('1.4',1,[]),('1.5',1,[]),
('1.6',1,[L('hom-consumer-rights-s4.5.4',H,'CCPC enforces, not disputes','low')]),
('2.b',1,[]),
('2.0',1,[L(p+'0.0',H,'statutory body')]),
('2.1',1,[]),('2.2',1,[]),('2.3',1,[]),
('3.b',1,[]),('3.0',1,[]),('3.1',1,[]),('3.2',1,[]),
('3.3',1,[L(p+'0.3',H,'complain to the trader first','low')]),
('3.4',1,[]),
('4.b',1,[]),
('4.0',1,[L(p+'0.0',H,'statutory body')]),
('4.1',1,[L('hom-food-safety-s8.1.3',H,'FSAI protects consumers','low')]),
('4.2',1,[L('hom-food-safety-s8.3.0',H,'official agencies')]),
('5.b',1,[]),('5.0',1,[]),('5.1',1,[]),
('5.2',1,[L(p+'1.b',H,'CCPC runs it')]),
('5.3',1,[]),
('6.b',1,[]),
('6.0',1,[L('hom-consumer-rights-s3.1.3',H,'Consumer Choice publication')]),
('6.1',1,[]),('6.2',1,[]),('6.3',1,[]),
('7.b',1,[L(p+'0.2',H,'self-regulation')]),
('7.0',1,[]),('7.1',1,[]),
('7.2',1,[L(p+'0.1',H,'voluntary bodies have no legal powers')]),
('8.b',1,[]),('8.0',1,[]),
('8.1',1,[L(p+'2.1',H,'Citizens Information Centres')]),
('9.b',1,[]),
('9.0',1,[L(p+'1.1',H,'CCPC investigates misleading pricing'),L(p+'7.0',H,'ASA advertising code')]),
('9.1',1,[L(p+'3.1',E,'FSPO handles financial complaints'),L(p+'3.3',H,'provider first, ombudsman last','low')]),
('9.2',1,[L(p+'3.0',E,'Ombudsman handles public bodies')]),
('9.3',2,[L(p+'2.b',H,'Citizens Information'),L(p+'1.3',H,'CCPC informs consumers'),L(p+'6.0',H,'CAI publishes findings')]),
('9.4',1,[L(p+'5.2',E,'European Consumer Centre Ireland')]),
('9.5',1,[L(p+'4.b',E,'FSAI handles unsafe food')]),
]
for name,items in P.items():
    pk=open(D+'packs/'+name.replace('.t1g1','')+'.t1g1.txt').read()
    pre=name.split('.t1g1')[0]
    ids=re.findall(r'^\[([^\]]+)\]',pk,re.M)
    tgt_sec=pk.split('\nCANDIDATES')[0]
    targets=re.findall(r'^\[([^\]]+)\]',tgt_sec,re.M)
    out={}
    for k,c,n in items:
        i=pre+'.'+k
        assert i not in out,i
        out[i]={"cost":c,"needs":n}
        for x in n: assert x['id'] in ids and x['id']!=i,(i,x)
    assert list(out)==targets,(set(targets)^set(out))
    json.dump(out,open(D+'point-links/'+name+'.json','w'),indent=1,ensure_ascii=False)
    links=sum(len(v['needs']) for v in out.values())
    print(name,len(out),links,sum(v['cost']==2 for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
