import json,re
D='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
def run(name,pref,costs,links):
    ids=[]
    for tok in costs.split():
        k,c=tok.split(':'); ids.append((pref+'.'+k,int(c)))
    out={}
    for i,c in ids:
        out[i]={"cost":c,"needs":[{"id":n[0],"strength":n[1],"why":n[2],"confidence":n[3]} for n in links.get(i,[])]}
    txt=open(D+'packs/'+name+'.txt').read()
    pk=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    tg=[m for m in re.findall(r'^\[([^\]]+)\]',txt.split('\nCANDIDATES')[0],re.M)]
    assert [i for i,_ in ids]==tg,(set(tg)^set(i for i,_ in ids))
    for v in out.values():
        for n in v['needs']: assert n['id'] in pk and n['id'] not in out or n['id'] in out, n
        for n in v['needs']: assert n['id'] in pk
    for i,v in out.items():
        for n in v['needs']: assert n['id']!=i
    json.dump(out,open(D+'point-links/'+name+'.json','w'),indent=1)
    L=sum(len(v['needs']) for v in out.values())
    print(name,len(out),L,sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
H,L_='helpful','low'
def a(i,s,w,c='high'): return (i,s,w,c)
# package 1
c1="0.b:1 0.0:2 0.1:1 0.2:1 0.3:1 0.4:2 0.5:1 1.b:1 1.0:1 1.1:1 1.2:1 1.3:1 2.b:1 2.0:1 2.1:1 3.b:1 3.0:1 3.1:1 3.2:2 3.3:1 3.4:1 3.5:1 4.b:1 4.0:1 4.1:1 4.2:1 4.3:1 4.4:1 4.5:2 5.b:1 5.0:1 5.1:1 5.2:1 6.b:1 6.0:1 6.1:1 6.2:1 6.3:1 6.4:1 7.b:2 7.0:1 7.1:1 7.2:1 7.3:1 8.b:1 8.0:2 8.1:2 8.2:1 8.3:1 9.b:1 9.0:2 9.1:1 9.2:1 9.3:1 9.4:1 9.5:2 9.6:1 9.7:1 10.b:1 10.0:1 10.1:1 10.2:1 10.3:1 11.b:1 11.0:2 11.1:1 11.2:2 11.3:1 11.4:1 12.b:1 12.0:1 12.1:1 12.2:1 12.3:1 12.4:1 13.b:1 13.0:2 13.1:2 13.2:1 13.3:2"
p='hom-food-preservation-s9.'
l1={p+'0.5':[a('hom-food-preservation-s2.1.b',H,'slow vs quick ice crystals')],
p+'1.1':[a(p+'1.b',H,'blanching defined')],
p+'1.2':[a(p+'1.1',H,'cooling after blanching')],
p+'3.3':[a('hom-food-preservation-s2.0.4',H,'water expands on freezing','low')],
p+'4.5':[a('hom-food-preservation-s2.4.3',H,'no refreezing thawed food')],
p+'5.1':[a(p+'1.b',H,'blanching destroys vitamins')],
p+'5.2':[a(p+'0.5',H,'slow freezing ice crystals')],
p+'7.1':[a('hom-food-preservation-s5.1.0',H,'sugar preserves by osmosis')],
p+'7.2':[a('hom-food-preservation-s3.5.2',H,'pectin gel with sugar, acid')],
p+'8.b':[a('hom-food-preservation-s3.5.2',H,'pectin sets jam')],
p+'8.1':[a('hom-food-preservation-s3.5.2',H,'pectin definition','low')],
p+'8.2':[a(p+'8.1',H,'strawberries low pectin')],
p+'11.0':[a(p+'8.1',H,'pectin and acid for set')],
p+'13.1':[a(p+'13.0',H,'chutney ingredients and preservation')],
p+'13.2':[a(p+'7.2',H,'jam needs pectin')]}
# fix key naming (prefix has trailing dot)
l1={k.replace('s9.s9.','s9.'):v for k,v in l1.items()}
run('hom-food-preservation-s9.t1g1','hom-food-preservation-s9',c1,{k:v for k,v in l1.items()})
# package 2
c2="0.b:1 0.0:1 0.1:2 0.2:2 0.3:1 0.4:1 0.5:1 0.6:1 1.b:1 1.0:1 1.1:1 1.2:1 1.3:1 1.4:1 1.5:1 2.b:1 2.0:2 2.1:2 2.2:1 2.3:2 3.b:1 3.0:1 3.1:1 3.2:2 3.3:1 3.4:1 4.b:1 4.0:1 4.1:1 4.2:1 4.3:1 4.4:1 5.b:1 5.0:1 5.1:1 5.2:1 5.3:1 5.4:1 5.5:2 6.b:1 6.0:1 6.1:1 6.2:1 6.3:1 6.4:1 6.5:1 6.6:1 6.7:1 7.b:1 7.0:2 7.1:2 7.2:2 7.3:1 7.4:2 7.5:1 7.6:1"
q='hom-cooking-methods-s6.'
E='hom-energy-nutrition-s4.'; M='hom-meal-planning-s4.'
l2={q+'0.b':[a(E+'0.2',H,'Food Pyramid and guidelines')],
q+'0.0':[a(E+'4.1.b'.replace('4.','',1) if False else E+'1.b',H,'healthy eating guideline principles','low')],
q+'0.1':[a(E+'6.0',H,'Food Pyramid shelves')],
q+'0.2':[a(E+'6.1',H,'upper Food Pyramid shelves')],
q+'0.3':[a(E+'2.1',H,'fibre from wholegrain foods','low')],
q+'0.4':[a(E+'2.2',H,'saturated fat risks','low')],
q+'1.0':[a(E+'0.b',H,'healthy-eating guidelines')],
q+'1.1':[a(M+'5.b',H,'coeliac and gluten')],
q+'2.0':[a('hom-cooking-methods-s3.0.4',H,'low-fat cooking methods')],
q+'2.1':[a(E+'2.3',H,'excess salt and blood pressure','low')],
q+'2.3':[a('hom-carbohydrates-s6.2.3',H,'wholegrain swaps for fibre')],
q+'3.0':[a(M+'5.2',H,'gluten-free staples')],
q+'3.1':[a(M+'3.0',H,'vegetarian protein and iron sources','low')],
q+'7.0':[a(M+'5.b',H,'coeliac and gluten')],
q+'7.1':[a(M+'6.b',H,'diabetic diet aims')],
q+'7.2':[a(M+'0.b',H,'low-fat heart-healthy diet')],
q+'7.3':[a(M+'0.4',H,'reducing salt','low')],
q+'7.4':[a(M+'4.b',H,'vegan diet exclusions')],
q+'7.6':[a('hom-carbohydrates-s6.2.3',H,'fibre-rich foods','low')]}
run('hom-cooking-methods-s6.t1g1','hom-cooking-methods-s6',c2,l2)
# package 3
c3="0.b:1 0.0:1 0.1:1 0.2:1 0.3:1 0.4:1 0.5:1 0.6:1 0.7:1 1.b:1 1.0:2 1.1:2 1.2:2 1.3:1 1.4:1 2.b:1 2.0:1 2.1:1 2.2:1 2.3:1 3.b:1 3.0:1 3.1:1 3.2:1 3.3:1 4.b:1 4.0:2 4.1:1 4.2:1 4.3:1 4.4:1 4.5:1 4.6:1 4.7:1 5.b:1 5.0:1 5.1:1 5.2:1 6.b:1 6.0:1 6.1:1 6.2:1 6.3:1 6.4:1 6.5:1 6.6:2 7.b:1 7.0:1 7.1:1 8.b:1 8.0:1 8.1:1 8.2:1 8.3:1 8.4:1 9.b:1 9.0:1 9.1:1 9.2:1 9.3:1 9.4:1 10.b:1 10.0:1 10.1:2 10.2:2 10.3:1 11.b:1 11.0:1 11.1:1 11.2:1 11.3:1 12.b:1 12.0:1 12.1:1 12.2:1 12.3:1 12.4:1"
r='hom-home-interior-s3.'
l3={r+'0.6':[a('hom-home-interior-s1.18.0',H,'environmental impact of materials')],
r+'1.1':[a(r+'1.0',H,'solid hardwoods named')],
r+'2.2':[a(r+'0.5',H,'insulation, poor conductors')],
r+'4.1':[a(r+'0.5',H,'good conductors feel cold')],
r+'4.3':[a(r+'4.2',H,'stainless steel resists corrosion')],
r+'6.3':[a(r+'5.2',H,'double glazing reduces heat loss')],
r+'9.1':[a(r+'8.1',H,'thermoplastics damaged by solvents')],
r+'10.1':[a('hom-textiles-fibres-s1.2.b',H,'fabric choice criteria')],
r+'10.2':[a('hom-textiles-fibres-s1.3.b',H,'fabric property meanings','low')]}
run('hom-home-interior-s3.t1g1','hom-home-interior-s3',c3,l3)
