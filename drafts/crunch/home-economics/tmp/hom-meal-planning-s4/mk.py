import json,re,sys
D='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
def N(i,w,s='helpful',c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
M='hom-meal-planning-s'; F='hom-food-preservation-s'
g1={
'0.b':(1,[N(M+'4.1.2','uses LDL cholesterol')]),
'0.0':(1,[N(M+'4.1.2','uses LDL cholesterol')]),
'0.1':(1,[]),'0.2':(1,[]),'0.3':(1,[]),
'0.4':(1,[N(M+'3.1.3','salt raises blood pressure')]),
'0.5':(1,[N(M+'3.1.2','refined carbohydrate harms heart')]),
'0.6':(1,[]),'0.7':(1,[]),
'1.b':(1,[]),'1.0':(1,[]),'1.1':(2,[]),
'1.2':(1,[]),'1.3':(1,[]),'1.4':(2,[]),
'2.b':(1,[]),'2.0':(1,[]),
'2.1':(1,[N(M+'4.1.2','lowers LDL cholesterol')]),
'2.2':(1,[]),'2.3':(1,[]),'2.4':(1,[]),
'3.b':(1,[]),
'3.0':(2,[N('hom-proteins-s7.0.0','uses high biological value protein'),N('hom-proteins-s7.1.0','combining plant proteins (complementation)')]),
'3.1':(2,[N('hom-vitamins-minerals-s2.2.3','vitamin C aids calcium absorption','helpful','low')]),
'3.2':(2,[N('hom-vitamins-minerals-s2.2.2','vitamin C improves iron absorption')]),
'3.3':(2,[]),'3.4':(1,[]),'3.5':(1,[]),'3.6':(2,[]),'3.7':(2,[]),
'4.b':(1,[]),
'4.0':(2,[N('hom-proteins-s7.1.0','pulses with grains complement amino acids')]),
'4.1':(1,[N('hom-vitamins-minerals-s2.6.1','vegans rely on fortified B12')]),
'4.2':(2,[]),
'4.3':(2,[N('hom-vitamins-minerals-s2.2.2','vitamin C improves iron absorption')]),
'4.4':(1,[]),
'4.5':(2,[N('hom-proteins-s4.3.2','gelatine is animal-derived')]),
'4.6':(1,[]),
'5.b':(1,[]),
'5.0':(1,[N('hom-proteins-s4.4.0','gluten is the wheat protein')]),
'5.1':(2,[N('hom-proteins-s4.4.3','foods depending on wheat gluten')]),
'5.2':(2,[N('hom-cereals-grains-s3.2.6','gluten-free flours for coeliacs','helpful','low')]),
'5.3':(1,[]),'5.4':(1,[]),'5.5':(1,[]),'5.6':(1,[]),'5.7':(1,[]),
'6.b':(1,[]),'6.0':(1,[]),'6.1':(2,[]),
'6.2':(1,[N('hom-carbohydrates-s6.5.0','low-calorie sweeteners replace sugar')]),
'6.3':(1,[]),'6.4':(1,[]),
'6.5':(1,[N(M+'3.2.b','insulin controls blood glucose')]),
'7.b':(1,[]),'7.0':(1,[]),'7.1':(1,[]),'7.2':(1,[]),'7.3':(1,[]),
'8.b':(1,[]),'8.0':(1,[]),
'8.1':(1,[N('hom-cereals-grains-s3.4.3','allergens emphasised in ingredients')]),
'8.2':(1,[]),'8.3':(2,[]),'8.4':(2,[]),'8.5':(1,[]),
}
g1={M+'4.'+k:{"cost":v[0],"needs":v[1]} for k,v in g1.items()}
g2={'0.b':[],'0.0':[],'0.1':[],'0.2':[],'0.3':[],
'0.4':[N('hom-vitamins-minerals-s4.7.4','excess sodium raises blood pressure')],
'0.5':[],'0.6':[],'0.7':[],'1.b':[],'1.0':[],'1.1':[],'1.2':[],'1.3':[],'1.4':[],
'2.b':[],'2.0':[],'2.1':[],'2.2':[],'2.3':[],'2.4':[],'3.b':[],
'3.0':[N('hom-proteins-s9.0.0','soya products tofu and TVP')],
'3.1':[],
'3.2':[N('hom-vitamins-minerals-s4.2.1','non-haem iron from plants')],
'3.3':[],
'3.4':[N('hom-proteins-s9.3.2','egg albumen binder in mycoprotein')],
'3.5':[],'3.6':[],'3.7':[],'4.b':[],
'4.0':[N('hom-proteins-s9.0.1','seitan and plant protein products','helpful','low')],
'4.1':[],
'4.2':[N('hom-vitamins-minerals-s4.1.1','calcium-set tofu and fortified sources')],
'4.3':[N('hom-vitamins-minerals-s4.2.1','non-haem iron from plants')],
'4.4':[],'4.5':[],
'4.6':[N('hom-proteins-s9.0.3','mycoprotein mince')],
'5.b':[],
'5.0':[N('hom-vitamins-minerals-s4.2.4','iron deficiency effects','helpful','low')],
'5.1':[N('hom-proteins-s9.0.1','seitan is made from wheat gluten')],
'5.2':[],
'5.3':[N('hom-consumer-rights-s1.11.0','ingredient lists on labels')],
'5.4':[N('hom-consumer-rights-s1.11.5','claims need defined criteria')],
'5.5':[],'5.6':[],'5.7':[],'6.b':[],'6.0':[],'6.1':[],'6.2':[],'6.3':[],'6.4':[],'6.5':[],
'7.b':[],'7.0':[],'7.1':[],'7.2':[],
'7.3':[N('hom-consumer-rights-s1.4.6','sampling and demonstrations','helpful','low')],
'8.b':[],
'8.0':[N('hom-consumer-rights-s1.11.0','mandatory ingredient listing')],
'8.1':[N('hom-consumer-rights-s1.11.2','allergens emphasised in ingredients')],
'8.2':[N('hom-consumer-rights-s1.11.3','nutrition declaration')],
'8.3':[N('hom-consumer-rights-s1.11.6','quality marks and symbols')],
'8.4':[N('hom-consumer-rights-s1.11.1','use-by and best-before dates')],
'8.5':[N('hom-consumer-rights-s1.11.5','claims need defined criteria','helpful','low')],
}
g2={M+'4.'+k:{"needs":v} for k,v in g2.items()}
S=lambda x:F+'3.'+x
g3={
'0.b':(1,[]),'0.0':(1,[N('hom-food-preservation-s1.2.5','heat denatures enzymes')]),
'0.1':(1,[N('hom-food-preservation-s1.5.6','prevent re-contamination')]),
'0.2':(2,[N('hom-food-preservation-s1.3.3','spores resist heat')]),
'0.3':(1,[N('hom-food-preservation-s1.2.0','pH acidity affects growth','helpful','low')]),
'0.4':(1,[]),'0.5':(1,[]),
'1.b':(1,[]),'1.0':(2,[N(S('0.2'),'spores survive moderate heat')]),'1.1':(1,[]),
'1.2':(1,[N(S('0.2'),'heat-resistant spores')]),
'1.3':(1,[N(S('1.2'),'sterilisation vs pasteurisation')]),
'1.4':(1,[N(S('1.2'),'sterilisation','helpful','low')]),
'1.5':(1,[N(S('1.4'),'UHT milk process')]),'1.6':(1,[]),
'2.b':(1,[N(S('1.2'),'sterilisation')]),'2.0':(2,[]),
'2.1':(2,[N(S('0.1'),'sealing prevents re-contamination')]),
'2.2':(1,[]),'2.3':(1,[]),'2.4':(1,[]),
'2.5':(2,[N(S('0.2'),'botulinum spores resist boiling','essential')]),
'2.6':(1,[N('hom-food-preservation-s1.1.1','micro-organisms produce gas','helpful','low')]),
'3.b':(1,[]),'3.0':(1,[N(S('0.5'),'vitamin C is heat-sensitive')]),
'3.1':(1,[N(S('0.5'),'B vitamins reduced by heat','helpful','low')]),
'3.2':(1,[]),'3.3':(1,[]),'3.4':(1,[]),'3.5':(1,[]),
'3.6':(2,[N(S('3.0'),'vitamin C loss in canning'),N(S('3.3'),'salt added in canning')]),
'4.b':(1,[]),'4.0':(2,[]),
'4.1':(1,[N(S('0.1'),'sealing prevents re-contamination','helpful','low')]),
'4.2':(1,[N(S('4.1'),'vacuum forms as jar cools')]),
'4.3':(1,[]),'4.4':(1,[]),
'4.5':(2,[N(S('0.2'),'botulinum spores resist boiling','essential')]),
'4.6':(1,[N(S('0.3'),'acid foods easier to heat-preserve')]),
'5.b':(1,[]),'5.0':(1,[N(S('0.0'),'heat destroys organisms and enzymes')]),
'5.1':(1,[N('hom-food-preservation-s1.4.2','osmosis draws water from cells')]),
'5.2':(2,[N('hom-carbohydrates-s4.8.3','gel from pectin, sugar, acid','helpful','low')]),
'5.3':(2,[N(S('5.2'),'pectin gelling')]),
'5.4':(1,[N(S('5.2'),'pectin released and set')]),
'5.5':(1,[N(S('5.2'),'pectin content')]),
'5.6':(1,[N(S('0.1'),'sealing prevents re-contamination')]),
'5.7':(1,[N(S('0.5'),'vitamin C lost by heat')]),
'6.b':(1,[]),'6.0':(1,[]),
'6.1':(2,[N(S('5.1'),'sugar proportion preserves and sets')]),
'6.2':(1,[N(S('6.1'),'boiling to setting point')]),
'6.3':(1,[]),
'6.4':(2,[N(S('5.1'),'sugar preserves by osmosis'),N(S('0.1'),'sealing prevents re-contamination')]),
'6.5':(1,[N('hom-food-preservation-s1.2.1','warmth speeds microbial growth','helpful','low')]),
}
g3={S(k):{"cost":v[0],"needs":v[1]} for k,v in g3.items()}
for name,g in [('hom-meal-planning-s4.t1g1',g1),('hom-meal-planning-s4.t1g2',g2),('hom-food-preservation-s3.t1g1',g3)]:
    txt=open(D+'packs/'+name+'.txt').read()
    tgt=re.findall(r'^\[([^\]]+)\]',txt.split('\nCANDIDATES')[0],re.M)
    allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    assert set(tgt)==set(g) and len(tgt)==len(g),(name,set(tgt)^set(g))
    out={k:g[k] for k in tgt}
    links=low=c2=0
    for k,v in out.items():
        for n in v['needs']:
            assert n['id'] in allids and n['id']!=k,(name,k,n['id']); links+=1; low+=n['confidence']=='low'
        c2+=v.get('cost')==2
    json.dump(out,open(D+'point-links/'+name+'.json','w'),indent=1)
    print(name,len(out),links,c2,low)
