import json,re,sys
D='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
E,H='essential','helpful'
P={}
a='hom-food-additives-s2.'
P['hom-food-additives-s2.t1g1']=[
(a+'0.b',1,[]),(a+'0.0',2,[]),(a+'0.1',2,[]),(a+'0.2',2,[]),(a+'0.3',2,[]),(a+'0.4',2,[]),(a+'0.5',1,[]),
(a+'1.b',1,[]),(a+'1.0',1,[]),(a+'1.1',1,[]),(a+'1.2',1,[]),(a+'1.3',1,[]),(a+'1.4',1,[]),(a+'1.5',1,[]),(a+'1.6',1,[]),
(a+'2.b',1,[]),(a+'2.0',1,[]),(a+'2.1',1,[]),(a+'2.2',2,[]),(a+'2.3',1,[]),(a+'2.4',1,[]),
(a+'3.b',1,[]),(a+'3.0',1,[]),(a+'3.1',1,[]),(a+'3.2',1,[]),
(a+'3.3',1,[L(a+'0.3',H,'uses polystyrene properties')]),
(a+'3.4',1,[L('hom-environmental-issues-s2.0.0',H,'uses reduce, reuse, recycle hierarchy')]),
(a+'3.5',2,[L('hom-environmental-issues-s2.5.4',H,'Re-turn deposit return scheme','low')]),
(a+'3.6',2,[L(a+'3.5',H,'same Re-turn scheme details')]),
(a+'4.b',1,[]),(a+'4.0',2,[]),
(a+'4.1',1,[L(a+'4.0',E,'uses MAP gas mixture')]),
(a+'4.2',1,[L(a+'4.0',H,'uses MAP method')]),
(a+'4.3',1,[]),
(a+'4.4',1,[L(a+'4.3',E,'gives examples of biodegradable packaging')]),
(a+'4.5',1,[L(a+'4.0',E,'shows MAP gas mixture and seal')]),
(a+'5.b',1,[]),(a+'5.0',2,[]),(a+'5.1',1,[]),(a+'5.2',2,[]),(a+'5.3',1,[]),(a+'5.4',2,[]),(a+'5.5',1,[]),(a+'5.6',1,[]),(a+'5.7',1,[]),(a+'5.8',1,[]),
(a+'6.b',1,[]),(a+'6.0',2,[]),
(a+'6.1',1,[L(a+'6.0',H,'uses declaration items per 100 g')]),
(a+'6.2',1,[]),
(a+'6.3',1,[L(a+'6.0',H,'uses full nutrition declaration items')]),
(a+'7.b',1,[]),
(a+'7.0',1,[L(a+'6.0',H,'uses energy, fat, sugar, salt declaration')]),
(a+'7.1',1,[L(a+'6.0',H,'uses declared nutrient values')]),
(a+'7.2',1,[L(a+'5.2',E,'uses allergen emphasis rule')]),
(a+'7.3',1,[L(a+'5.4',E,'uses use-by and best-before dates')]),
(a+'7.4',1,[L(a+'5.6',E,'uses country of origin labelling')]),
(a+'7.5',1,[L(a+'5.8',H,'uses lot or batch code')]),
(a+'7.6',2,[]),
]
b='hom-vitamins-minerals-s5.'
P['hom-vitamins-minerals-s5.t1g1']=[
(b+'0.b',1,[]),(b+'0.0',1,[]),(b+'0.1',1,[]),(b+'0.2',2,[]),(b+'0.3',1,[]),
(b+'1.b',1,[]),(b+'1.0',2,[]),
(b+'1.1',1,[L(b+'1.0',E,'uses haem iron')]),
(b+'1.2',1,[]),(b+'1.3',2,[]),
(b+'1.4',1,[L(b+'1.3',H,'uses poorly absorbed non-haem iron')]),
(b+'1.5',1,[L(b+'1.3',H,'uses non-haem iron poor absorption'),L('hom-vitamins-minerals-s2.2.2',H,'uses vitamin C aiding iron absorption')]),
(b+'2.b',1,[]),
(b+'2.0',1,[L(b+'1.3',E,'converts ferric to ferrous iron')]),
(b+'2.1',1,[L(b+'1.3',H,'uses ferric to ferrous conversion')]),
(b+'2.2',1,[L(b+'2.0',E,'uses vitamin C raising iron absorption')]),
(b+'2.3',1,[L(b+'1.4',E,'uses the meat factor')]),
(b+'3.b',1,[]),(b+'3.0',1,[]),(b+'3.1',2,[]),(b+'3.2',1,[]),(b+'3.3',1,[]),(b+'3.4',1,[]),
(b+'3.5',2,[L(b+'2.1',H,'uses stomach acid and iron absorption')]),
(b+'4.b',1,[]),
(b+'4.0',1,[L(b+'1.3',H,'uses ferric to ferrous iron')]),
(b+'4.1',1,[]),
(b+'4.2',1,[L('hom-vitamins-minerals-s1.4.3',H,'uses vitamin D calcium absorption')]),
(b+'4.3',1,[L('hom-vitamins-minerals-s1.4.3',H,'uses vitamin D absorbing phosphorus')]),
(b+'4.4',1,[L(b+'4.2',E,'uses vitamin D aiding calcium absorption')]),
(b+'5.b',1,[]),
(b+'5.0',1,[]),(b+'5.1',1,[]),
(b+'5.2',1,[L(b+'4.1',H,'uses vitamin C aiding calcium')]),
(b+'5.3',1,[]),
(b+'5.4',1,[L('hom-vitamins-minerals-s4.0.4',H,'uses phosphorus working with calcium')]),
(b+'5.5',1,[L('hom-vitamins-minerals-s1.4.4',H,'uses parathormone and vitamin D')]),
(b+'5.6',1,[L('hom-vitamins-minerals-s4.1.5',H,'uses osteoporosis')]),
(b+'5.7',1,[]),
(b+'6.b',1,[]),(b+'6.0',1,[]),(b+'6.1',1,[]),(b+'6.2',1,[]),(b+'6.3',1,[]),(b+'6.4',1,[]),(b+'6.5',1,[]),
(b+'6.6',1,[L('hom-vitamins-minerals-s4.0.4',H,'uses phosphorus working with calcium','low')]),
(b+'6.7',2,[L(b+'5.6',H,'uses oestrogen and calcium retention')]),
(b+'7.b',1,[]),
(b+'7.0',2,[L(b+'3.1',H,'uses phytates binding minerals')]),
(b+'7.1',1,[L(b+'7.0',E,'uses phytate breakdown')]),
(b+'7.2',1,[L(b+'3.2',H,'uses oxalates binding minerals')]),
(b+'7.3',1,[L(b+'7.2',E,'uses calcium oxalate in spinach')]),
(b+'7.4',1,[L(b+'7.0',H,'uses phytates and oxalates')]),
(b+'7.5',2,[L(b+'7.1',H,'uses leavening and soaking reducing phytate')]),
(b+'7.6',1,[L(b+'7.0',H,'uses phytates binding minerals')]),
]
c='hom-housing-s4.'
P['hom-housing-s4.t1g1']=[
(c+'0.b',1,[]),(c+'0.0',2,[]),(c+'0.1',1,[]),(c+'0.2',2,[]),(c+'0.3',1,[]),(c+'0.4',1,[]),
(c+'1.b',1,[]),(c+'1.0',2,[]),(c+'1.1',2,[]),(c+'1.2',2,[]),(c+'1.3',1,[]),
(c+'2.b',1,[]),(c+'2.0',2,[]),
(c+'2.1',1,[L(c+'2.0',H,'builds on emergency shelter step')]),
(c+'2.2',1,[]),
(c+'3.b',1,[]),(c+'3.0',1,[]),
(c+'3.1',1,[L(c+'3.0',E,'uses social housing allocation and priority')]),
(c+'3.2',1,[]),(c+'3.3',1,[]),
(c+'3.4',2,[L('hom-housing-s1.6.0',H,'uses private rented housing')]),
(c+'3.5',1,[L(c+'3.0',H,'contrasts with social housing')]),
(c+'3.6',1,[L('hom-housing-s2.1.5',H,'First Home shared equity scheme')]),
(c+'3.7',1,[L(c+'3.0',H,'uses social housing waiting lists')]),
(c+'4.b',1,[]),
(c+'4.0',1,[L(c+'3.0',H,'uses local authority social housing')]),
(c+'4.1',1,[L(c+'4.0',H,'uses social rented tenure')]),
(c+'4.2',1,[]),
(c+'4.3',1,[L(c+'4.2',E,'uses urban and rural location differences')]),
(c+'5.b',1,[]),(c+'5.0',1,[]),(c+'5.1',1,[]),(c+'5.2',1,[]),
(c+'5.3',1,[L('hom-housing-s1.6.2',H,'rented housing minimum standards')]),
(c+'6.b',1,[]),
(c+'6.0',2,[L('hom-housing-s2.0.1',H,'costs of buying, stamp duty, fees')]),
(c+'6.1',2,[L('hom-housing-s2.0.4',H,'uses mortgage repayments')]),
(c+'6.2',2,[]),
(c+'6.3',1,[L(c+'6.2',H,'uses renting costs')]),
(c+'6.4',1,[L(c+'6.1',H,'uses mortgage repayments')]),
(c+'6.5',1,[]),
(c+'7.b',1,[]),(c+'7.0',1,[]),
(c+'7.1',2,[L(c+'7.0',H,'uses adequacy idea'),L(c+'3.4',H,'uses HAP and RAS'),L(c+'3.5',H,'uses cost rental')]),
(c+'7.2',2,[L(c+'7.0',H,'uses adequacy idea'),L(c+'4.3',H,'uses urban and rural distribution')]),
(c+'7.3',1,[L(c+'2.0',H,'uses emergency accommodation')]),
(c+'7.4',2,[L(c+'3.1',H,'single people lower priority')]),
(c+'7.5',1,[L(c+'3.2',H,'uses voluntary housing'),L(c+'3.3',H,'uses co-operative housing')]),
(c+'7.6',1,[L('hom-housing-s1.2.2',H,'uses refurbishing vacant property','low')]),
(c+'8.b',1,[]),(c+'8.0',1,[]),(c+'8.1',1,[]),(c+'8.2',1,[]),(c+'8.3',1,[]),(c+'8.4',1,[]),(c+'8.5',1,[]),(c+'8.6',1,[]),
]
for name,rows in P.items():
    txt=open(D+'packs/'+name+'.txt').read()
    ids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    tgt=re.findall(r'^\[([^\]]+)\]',txt.split('CANDIDATES')[0],re.M)
    out={}
    for i,cost,n in rows:
        assert i not in out,i
        for x in n: assert x['id'] in ids and x['id']!=i,(i,x)
        out[i]={"cost":cost,"needs":n}
    assert list(out)==tgt,(name,set(tgt)^set(out))
    json.dump(out,open(D+'point-links/'+name+'.json','w'),indent=1)
    nl=sum(len(v['needs']) for v in out.values())
    print(name,len(out),nl,sum(v['cost']==2 for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
