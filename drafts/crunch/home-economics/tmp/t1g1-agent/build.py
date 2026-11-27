import json,re,os
H='high';L='low';E='essential';P='helpful'
B='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
def n(i,s,w,c=H): return {"id":i,"strength":s,"why":w,"confidence":c}
def run(name,entries):
    txt=open(B+'packs/'+name+'.txt').read()
    ids=re.findall(r'^\[([^\]]+)\]',txt,re.M)
    tgt=[]
    for line in txt.split('\n'):
        if line.startswith('CANDIDATES'): break
        m=re.match(r'\[([^\]]+)\]',line)
        if m: tgt.append(m.group(1))
    out={}
    for k,c,ns in entries:
        assert k not in out,k
        out[k]={"cost":c,"needs":ns}
    assert list(out)==tgt,(set(tgt)^set(out))
    for v in out.values():
        for x in v['needs']: assert x['id'] in ids and x['id']!=k
    os.makedirs(B+'point-links',exist_ok=True)
    json.dump(out,open(B+'point-links/'+name+'.json','w'),indent=1)
    print(name,len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(x['confidence']==L for v in out.values() for x in v['needs']))

p='hom-energy-nutrition-s4.'
run('hom-energy-nutrition-s4.t1g1',[
(p+'0.b',1,[]),(p+'0.0',1,[]),(p+'0.1',1,[]),(p+'0.2',1,[]),(p+'0.3',1,[]),(p+'0.4',1,[]),(p+'0.5',2,[]),(p+'0.6',1,[]),
(p+'1.b',1,[]),(p+'1.0',1,[]),(p+'1.1',1,[]),(p+'1.2',1,[]),
(p+'1.3',1,[n('hom-vitamins-minerals-s4.1.b',P,'calcium as nutrient',L)]),
(p+'1.4',1,[]),(p+'1.5',1,[]),(p+'1.6',1,[]),(p+'1.7',1,[]),
(p+'2.b',1,[]),(p+'2.0',1,[]),
(p+'2.1',1,[n('hom-carbohydrates-s6.2.b',P,'fibre and its role')]),
(p+'2.2',1,[n('hom-lipids-s5.2.2',P,'saturated fat raises LDL cholesterol')]),
(p+'2.3',1,[n('hom-vitamins-minerals-s4.7.4',P,'excess sodium raises blood pressure')]),
(p+'2.4',1,[n('hom-carbohydrates-s6.4.b',P,'harm from high sugar diet',L)]),
(p+'3.b',1,[]),(p+'3.0',1,[]),(p+'3.1',1,[]),(p+'3.2',1,[]),(p+'3.3',1,[]),
(p+'3.4',1,[n('hom-vitamins-minerals-s4.2.b',P,'iron as a nutrient',L),n('hom-vitamins-minerals-s4.1.b',P,'calcium as a nutrient',L)]),
(p+'4.b',1,[n(p+'3.b',P,'RDA values to compare against')]),
(p+'4.0',1,[]),(p+'4.1',1,[]),
(p+'4.2',2,[n(p+'4.0',P,'per 100 g values in tables')]),
(p+'4.3',1,[n(p+'4.2',E,'per 100 g calculation method')]),
(p+'4.4',2,[n(p+'4.2',E,'per-food calculation method'),n(p+'3.1',P,'comparing totals with RDA')]),
(p+'5.b',1,[n(p+'4.b',P,'food composition table job')]),
(p+'5.0',1,[n(p+'4.0',P,'food composition database')]),
(p+'5.1',1,[n(p+'3.1',P,'comparing totals with RDA')]),
(p+'5.2',1,[]),(p+'5.3',1,[]),(p+'5.4',1,[]),
(p+'6.b',1,[n(p+'1.b',P,'guidelines turned into pyramid')]),
(p+'6.0',2,[]),(p+'6.1',2,[]),(p+'6.2',1,[]),
(p+'6.3',2,[n(p+'6.0',P,'shelves servings apply to')]),
(p+'6.4',1,[]),
(p+'6.5',1,[n(p+'6.0',E,'which shelves are lower and large')]),
(p+'6.6',1,[n(p+'6.b',P,'shelves and portions')]),
(p+'6.7',1,[]),
(p+'6.8',2,[n(p+'6.0',E,'lower shelves and foods'),n(p+'6.1',E,'middle shelves and foods'),n(p+'6.2',E,'top shelf foods')]),
(p+'7.b',1,[n(p+'6.b',P,'pyramid servings')]),
(p+'7.0',1,[]),(p+'7.1',1,[]),(p+'7.2',1,[]),
(p+'7.3',1,[n(p+'6.0',P,'starchy foods shelf')]),
(p+'7.4',1,[]),
(p+'8.b',1,[]),(p+'8.0',1,[]),(p+'8.1',1,[]),(p+'8.2',1,[]),
(p+'8.3',1,[n('hom-vitamins-minerals-s4.2.4',P,'anaemia from iron deficiency')]),
(p+'8.4',1,[]),(p+'8.5',2,[]),(p+'8.6',1,[]),(p+'8.7',1,[]),
(p+'9.b',1,[]),(p+'9.0',1,[]),(p+'9.1',2,[]),(p+'9.2',1,[]),(p+'9.3',1,[]),
(p+'9.4',1,[n('hom-energy-nutrition-s3.0.3',P,'alcohol empty kilocalories')]),
(p+'9.5',1,[]),(p+'9.6',1,[]),(p+'9.7',1,[]),
])

p='hom-work-leisure-s6.'
run('hom-work-leisure-s6.t1g1',[
(p+'0.b',1,[]),(p+'0.0',1,[]),(p+'0.1',1,[]),
(p+'0.2',1,[n(p+'4.4',P,'National Childcare Scheme subsidy')]),
(p+'0.3',1,[]),
(p+'1.b',1,[n(p+'0.b',P,'family situation to match')]),
(p+'1.0',1,[]),(p+'1.1',1,[n(p+'0.0',P,"parents' working pattern")]),
(p+'1.2',1,[]),(p+'1.3',1,[]),(p+'1.4',1,[]),(p+'1.5',2,[]),
(p+'2.b',1,[]),(p+'2.0',1,[]),(p+'2.1',1,[]),(p+'2.2',1,[]),(p+'2.3',1,[]),(p+'2.4',1,[]),(p+'2.5',1,[]),
(p+'3.b',1,[]),
(p+'3.0',1,[n(p+'0.3',P,'after-school cover gap')]),
(p+'3.1',1,[]),(p+'3.2',1,[]),(p+'3.3',1,[]),
(p+'3.4',1,[n('hom-education-s3.0.0',P,'ECCE free pre-school year')]),
(p+'4.b',1,[]),(p+'4.0',2,[]),
(p+'4.1',1,[n(p+'4.0',E,'Tusla registration and inspection')]),
(p+'4.2',2,[n(p+'4.0',P,'Tusla registration of services')]),
(p+'4.3',2,[n(p+'4.4',P,'National Childcare Scheme'),n(p+'4.2',P,'childminder registration')]),
(p+'4.4',1,[]),
(p+'5.b',1,[]),(p+'5.0',1,[]),(p+'5.1',1,[]),(p+'5.2',1,[]),(p+'5.3',1,[]),(p+'5.4',1,[]),(p+'5.5',1,[]),(p+'5.6',1,[]),
(p+'6.b',1,[n(p+'2.0',E,'creche as an option')]),
(p+'6.0',1,[]),(p+'6.1',1,[]),(p+'6.2',1,[]),
(p+'6.3',1,[n(p+'4.0',P,'registration and inspection')]),
(p+'6.4',1,[]),(p+'6.5',1,[]),(p+'6.6',1,[]),(p+'6.7',1,[]),
(p+'7.b',1,[n(p+'2.1',E,'childminder as an option')]),
(p+'7.0',1,[]),(p+'7.1',1,[]),(p+'7.2',1,[]),(p+'7.3',1,[]),(p+'7.4',1,[]),(p+'7.5',1,[]),
(p+'7.6',2,[n(p+'4.2',P,'childminder Tusla registration')]),
(p+'8.b',1,[n(p+'1.b',P,'requirements these criteria come from')]),
(p+'8.0',1,[]),(p+'8.1',1,[]),(p+'8.2',1,[]),(p+'8.3',1,[]),(p+'8.4',1,[]),(p+'8.5',1,[]),(p+'8.6',1,[]),(p+'8.7',1,[]),
(p+'9.b',1,[n(p+'6.b',P,'creche advantages and disadvantages'),n(p+'7.b',P,'childminder advantages and disadvantages')]),
(p+'9.0',1,[n(p+'0.b',P,'family requirements')]),
(p+'9.1',1,[]),
(p+'9.2',2,[n(p+'6.0',P,'creche fixed hours advantage'),n(p+'7.1',P,'childminder flexibility advantage')]),
(p+'9.3',1,[n(p+'9.2',P,'point-by-point comparison')]),
(p+'9.4',1,[n(p+'7.6',P,'what family must check',L)]),
(p+'9.5',1,[n(p+'2.3',P,'au pair role'),n(p+'3.0',P,'after-school group role')]),
(p+'9.6',1,[n(p+'3.1',P,'playschool sessional service')]),
])

p='hom-education-s4.'
run('hom-education-s4.t1g1',[
(p+'0.b',1,[]),(p+'0.0',1,[]),(p+'0.1',1,[]),(p+'0.2',1,[]),(p+'0.3',1,[]),
(p+'0.4',1,[n('hom-education-s3.4.4',P,'Free Fees Initiative')]),
(p+'0.5',1,[]),(p+'0.6',2,[]),(p+'0.7',1,[]),
(p+'1.b',1,[]),(p+'1.0',1,[]),
(p+'1.1',2,[n(p+'4.0',P,'early school leaving defined',L)]),
(p+'1.2',2,[]),
(p+'1.3',1,[n(p+'1.2',P,'gendered subject choice')]),
(p+'1.4',1,[n(p+'1.2',P,'gendered subject choice')]),
(p+'1.5',1,[]),(p+'1.6',1,[]),(p+'1.7',2,[]),
(p+'2.b',1,[]),(p+'2.0',1,[]),(p+'2.1',2,[]),
(p+'2.2',2,[n('hom-education-s3.4.3',P,'SUSI grants')]),
(p+'2.3',1,[n(p+'2.2',P,'supports that reduce costs')]),
(p+'2.4',2,[]),(p+'2.5',1,[]),(p+'2.6',1,[]),(p+'2.7',1,[]),
(p+'2.8',2,[n(p+'3.4',P,'DEIS programme'),n('hom-education-s3.4.5',P,'HEAR entry route')]),
(p+'3.b',1,[]),(p+'3.0',2,[]),(p+'3.1',1,[]),(p+'3.2',1,[]),(p+'3.3',1,[]),(p+'3.4',2,[]),
(p+'3.5',2,[n(p+'3.4',P,'DEIS supports'),n('hom-education-s3.6.2',P,'special needs assistants')]),
(p+'4.b',1,[]),(p+'4.0',1,[]),(p+'4.1',1,[]),(p+'4.2',1,[]),(p+'4.3',2,[]),
(p+'4.4',1,[n(p+'4.0',P,'early school leaver defined')]),
(p+'4.5',2,[n(p+'4.0',P,'early school leaver defined',L)]),
(p+'4.6',1,[]),
(p+'4.7',2,[n(p+'3.4',P,'DEIS programme'),n('hom-education-s3.5.1',P,'Youthreach second-chance route')]),
])
