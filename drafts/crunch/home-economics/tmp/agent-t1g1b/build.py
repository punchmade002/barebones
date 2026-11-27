import json,re,sys
D='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
def L(i,s,w,c='high'):return {"id":i,"strength":s,"why":w,"confidence":c}
def run(name,spec):
    txt=open(D+'packs/'+name+'.txt').read()
    ids=re.findall(r'^\[([^\]]+)\]',txt,re.M)
    tgt=[i for i in re.search(r'TARGET.*?(?=\nCANDIDATES)',txt,re.S).group(0).split('\n') for i in [re.match(r'\[([^\]]+)\]',i)] if i]
    tgt=[m.group(1) for m in tgt]
    out={}
    for t in tgt:
        c,n=spec[t]; out[t]={"cost":c,"needs":n}
    assert list(spec)==tgt,(set(tgt)^set(spec))
    for v in out.values():
        for n in v['needs']: assert n['id'] in ids
    json.dump(out,open(D+'point-links/'+name+'.json','w'),indent=1)
    nl=sum(len(v['needs']) for v in out.values())
    print(name,len(out),nl,sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
p='hom-food-preservation-s7.'
S={}
def a(k,c,*n):S[p+k]=(c,list(n))
a('0.b',1);a('0.0',1);a('0.1',2);a('0.2',1);a('0.3',1)
a('0.4',1,L(p+'0.3','helpful','no heat cold process'))
a('0.5',1)
a('1.b',1);a('1.0',1);a('1.1',1);a('1.2',1);a('1.3',1)
a('1.4',1,L('hom-food-preservation-s1.3.4','helpful','enzymes'))
a('1.5',2,L(p+'0.2','helpful','dose measured in grays'))
a('1.6',1,L('hom-food-preservation-s1.3.3','helpful','bacterial spores'))
a('2.b',1);a('2.0',1);a('2.1',1);a('2.2',1);a('2.3',1);a('2.4',1)
a('3.b',1);a('3.0',1);a('3.1',1);a('3.2',1)
a('3.3',1,L('hom-food-preservation-s1.1.3','helpful','oxidation causing rancidity'))
a('4.b',1);a('4.0',1);a('4.1',2);a('4.2',1);a('4.3',1);a('4.4',1);a('4.5',1)
a('4.6',1,L(p+'1.6','helpful','spores and viruses resist'))
a('4.7',1,L(p+'3.3','helpful','fats go rancid'))
a('5.b',1);a('5.0',2)
a('5.1',1,L(p+'0.2','helpful','kilogray dose unit'))
a('5.2',2)
a('5.3',1,L(p+'5.2','helpful','labelling words'))
a('5.4',1);a('5.5',1)
run('hom-food-preservation-s7.t1g1',S)

p='hom-work-leisure-s8.'
S={}
a('0.b',1);a('0.0',2);a('0.1',1);a('0.2',1);a('0.3',1);a('0.4',1);a('0.5',1);a('0.6',1)
a('1.b',1);a('1.0',2)
a('1.1',1,L(p+'4.1','helpful','value for money','high'))
a('1.2',1);a('1.3',2);a('1.4',1);a('1.5',2);a('1.6',1)
a('1.7',2,L('hom-work-leisure-s7.4.b','helpful','physical and social benefits','low'))
a('2.b',1);a('2.0',1);a('2.1',1);a('2.2',1);a('2.3',1);a('2.4',1);a('2.5',1);a('2.6',1)
a('3.b',1);a('3.0',1);a('3.1',1)
a('3.2',2,L(p+'3.0','helpful','membership fee'))
a('3.3',1,L(p+'3.0','helpful','membership fee'))
a('3.4',1);a('3.5',1);a('3.6',1)
a('3.7',1,L(p+'3.6','helpful','hidden costs included in total'))
a('4.b',1);a('4.0',1)
a('4.1',1,L(p+'4.0','helpful','value as benefit gained'))
a('4.2',1)
a('4.3',1)
a('4.4',1,L(p+'4.3','essential','cost per visit'))
a('4.5',1);a('4.6',1)
a('5.b',1);a('5.0',1);a('5.1',1)
a('5.2',1,L(p+'3.7','essential','total annual cost'))
a('5.3',1,L(p+'4.3','essential','cost per visit calculation'))
a('5.4',2)
a('5.5',1,L(p+'4.6','helpful','value depends on use'))
a('6.b',1)
a('6.0',1,L(p+'1.b','helpful','evaluation criteria'))
a('6.1',1);a('6.2',1);a('6.3',2)
a('6.4',1,L(p+'2.4','helpful','online booking systems'))
run('hom-work-leisure-s8.t1g1',S)

p='hom-consumer-rights-s3.'
q='hom-consumer-rights-s1.'
S={}
a('0.b',1);a('0.0',1);a('0.1',1);a('0.2',1);a('0.3',1)
a('0.4',1,L(p+'0.3','essential','manufacturer guarantee'))
a('0.5',1)
a('1.b',1)
a('1.0',1,L(q+'11.0','helpful','mandatory food label contents'))
a('1.1',1,L(q+'0.0','helpful','unit prices'))
a('1.2',1);a('1.3',1);a('1.4',1);a('1.5',1);a('1.6',1)
a('1.7',2,L(q+'11.6','helpful','Bord Bia Quality Mark'))
a('1.8',1)
a('2.b',1)
a('2.0',1,L(p+'5.b','helpful','consumer rights'))
a('2.1',1);a('2.2',1);a('2.3',1);a('2.4',1)
a('3.b',1)
a('3.0',1)
a('3.1',1,L(p+'5.4','helpful','right to redress'))
a('3.2',1);a('3.3',1,L(q+'1.6','helpful','impulse buying'))
a('3.4',1,L(q+'7.4','helpful','credit costs more'))
a('3.5',1)
a('4.b',1);a('4.0',1)
a('4.1',1,L(p+'4.0','essential','caveat emptor'))
a('4.2',1,L(q+'0.4','helpful','needs-based decision'))
a('4.3',1)
a('5.b',1)
for k in '012345':a('5.'+k,1)
a('5.6',1,L(p+'5.4','helpful','right to redress'))
a('5.7',1,L(p+'1.0','helpful','reading labels'))
run('hom-consumer-rights-s3.t1g1',S)
