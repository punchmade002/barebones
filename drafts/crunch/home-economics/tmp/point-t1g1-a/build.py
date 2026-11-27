import json,re
D='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
H,E='helpful','essential'
P={}
# name -> (ordered list of (id,cost,links))
P['hom-dairy-eggs-s2.t1g1']=[
('0.b',1,[]),('0.0',2,[L('hom-food-safety-s3.3.b',H,'conditions bacteria need to grow')]),
('0.1',1,[]),('0.2',1,[L('hom-food-safety-s3.3.2',H,'warmth and cold affect growth')]),
('0.3',2,[L('hom-food-preservation-s3.0.5',H,'heat-sensitive water-soluble vitamins')]),
('1.b',1,[]),('1.0',1,[]),('1.1',1,[]),('1.2',1,[]),
('1.3',1,[L('hom-dairy-eggs-s2.0.3',H,'heat-sensitive vitamins lost')]),
('1.4',1,[]),('1.5',1,[]),
('2.b',1,[]),('2.0',1,[]),('2.1',1,[]),('2.2',1,[]),('2.3',1,[]),
('3.b',1,[]),('3.0',1,[]),('3.1',1,[]),('3.2',1,[]),('3.3',1,[]),('3.4',1,[]),('3.5',1,[]),('3.6',2,[]),
('4.b',1,[]),('4.0',1,[]),('4.1',1,[]),('4.2',1,[]),('4.3',1,[]),('4.4',1,[]),
('5.b',1,[]),('5.0',1,[]),
('5.1',1,[L('hom-dairy-eggs-s1.8.3',H,'skimmed milk','low')]),
('5.2',1,[L('hom-dairy-eggs-s1.8.0',H,'whole, semi-skimmed, skimmed milk types')]),
('5.3',1,[L('hom-dairy-eggs-s1.8.4',H,'fortified milk')]),
('5.4',1,[]),('5.5',1,[]),('5.6',1,[]),('5.7',2,[]),
('6.b',1,[]),('6.0',2,[]),
('6.1',1,[L('hom-dairy-eggs-s1.0.7',H,'riboflavin and vitamin A in milk')]),
('6.2',2,[]),('6.3',2,[]),('6.4',2,[]),('6.5',1,[]),
('7.b',1,[]),('7.0',1,[]),('7.1',1,[]),('7.2',1,[]),('7.3',1,[]),('7.4',1,[]),('7.5',2,[]),
]
P['hom-cereals-grains-s4.t1g1']=[
('0.b',1,[]),
('0.0',1,[L('hom-carbohydrates-s4.1.0',H,'gelatinisation of starch')]),
('0.1',1,[L('hom-carbohydrates-s4.7.5',H,'dextrinisation of starch')]),
('0.2',1,[]),
('0.3',1,[L('hom-carbohydrates-s4.7.0',H,'caramelisation of sugar')]),
('0.4',1,[]),
('0.5',1,[L('hom-proteins-s5.0.3',H,'coagulation of protein')]),
('0.6',1,[]),('0.7',1,[]),
('1.b',1,[]),('1.0',1,[]),('1.1',1,[]),('1.2',1,[]),('1.3',1,[]),('1.4',1,[]),('1.5',2,[]),('1.6',1,[]),('1.7',1,[]),
('2.b',1,[]),('2.0',1,[]),('2.1',1,[]),('2.2',1,[]),
('2.3',1,[L('hom-carbohydrates-s4.1.0',H,'gelatinisation of starch')]),
('2.4',1,[]),('2.5',2,[]),('2.6',1,[]),('2.7',1,[]),
('3.b',1,[]),('3.0',2,[]),('3.1',1,[]),
('3.2',2,[L('hom-carbohydrates-s4.4.2',H,'yeast fermenting sugar'),L('hom-cereals-grains-s3.3.1',H,'gluten traps gas')]),
('3.3',1,[L('hom-cereals-grains-s4.3.2',H,'yeast fermentation and proving')]),
('3.4',1,[]),
('3.5',1,[L('hom-cereals-grains-s4.3.4',H,'bicarbonate releasing carbon dioxide')]),
('3.6',1,[L('hom-cereals-grains-s4.3.5',H,'baking powder as raising agent')]),
('3.7',2,[]),
('4.b',1,[]),('4.0',1,[]),('4.1',1,[]),('4.2',1,[]),
('4.3',1,[L('hom-cereals-grains-s4.3.0',H,'air trapped as raising agent')]),
]
P['hom-family-society-s5.t1g1']=[
('0.b',1,[]),('0.0',2,[]),
('0.1',1,[L('hom-sociological-concepts-s3.3.b',H,'socialisation defined')]),
('0.2',1,[]),
('0.3',1,[L('hom-family-society-s5.6.b',H,'adopt and supplement a function')]),
('0.4',1,[]),
('1.b',1,[]),('1.0',2,[]),('1.1',1,[]),('1.2',1,[]),('1.3',2,[]),('1.4',2,[]),
('2.b',1,[]),('2.0',1,[]),('2.1',1,[]),('2.2',1,[]),('2.3',1,[]),('2.4',1,[]),('2.5',1,[]),('2.6',2,[]),('2.7',2,[]),
('3.b',1,[]),('3.0',1,[]),('3.1',1,[]),('3.2',1,[]),('3.3',2,[]),('3.4',1,[]),
('4.b',1,[]),('4.0',1,[]),('4.1',1,[]),('4.2',1,[]),('4.3',1,[]),('4.4',2,[]),('4.5',2,[]),
('5.b',1,[L('hom-sociological-concepts-s3.3.1',H,'primary socialisation')]),
('5.0',1,[L('hom-sociological-concepts-s3.3.4',H,'learning by observation and imitation','low')]),
('5.1',1,[]),('5.2',1,[]),
('5.3',2,[L('hom-sociological-concepts-s3.3.2',H,'secondary socialisation'),L('hom-sociological-concepts-s4.2.1',H,'hidden curriculum')]),
('5.4',1,[]),
('6.b',1,[]),('6.0',1,[]),('6.1',1,[]),('6.2',1,[]),('6.3',2,[]),
('7.b',1,[]),('7.0',1,[]),('7.1',1,[]),('7.2',1,[]),('7.3',1,[]),('7.4',1,[]),
]
for n,items in P.items():
    pk=open(D+'packs/'+n+'.txt').read()
    pre=n.split('.')[0]
    tgt=re.findall(r'^\[('+re.escape(pre)+r'\.[^\]]+)\]',pk,re.M)
    allids=set(re.findall(r'^\[([^\]]+)\]',pk,re.M))
    out={}
    for k,c,l in items:
        out[pre+'.'+k]={"cost":c,"needs":l}
    assert list(out)==tgt,(n,set(tgt)^set(out))
    for v in out.values():
        for x in v['needs']: assert x['id'] in allids,x
    import os; os.makedirs(D+'point-links',exist_ok=True)
    json.dump(out,open(D+'point-links/'+n+'.json','w'),indent=1)
    print(n,len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
