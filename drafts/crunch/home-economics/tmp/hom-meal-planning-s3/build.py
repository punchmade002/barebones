import json,re,sys
B='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
def L(i,s,w,c): return {"id":i,"strength":s,"why":w,"confidence":c}
P='hom-meal-planning-s3.'
E='hom-energy-nutrition-s2.'
C5='hom-carbohydrates-s5.'
V4='hom-vitamins-minerals-s4.'
g1={
'0.b':(1,[]),
'0.0':(1,[]),
'0.1':(1,[]),
'0.2':(2,[L(E+'0.0','helpful','uses energy input','high')]),
'0.3':(1,[L(E+'4.1','helpful','sedentary lifestyle lowers output','high')]),
'0.4':(2,[]),
'0.5':(2,[L(E+'1.0','helpful','reducing energy intake','high')]),
'0.6':(2,[L(E+'1.0','helpful','reducing energy intake','high')]),
'1.b':(2,[]),
'1.0':(1,[L(P+'1.7','essential','uses LDL cholesterol','high')]),
'1.1':(1,[L(P+'1.7','essential','uses LDL and HDL cholesterol','high')]),
'1.2':(1,[L(P+'1.7','helpful','uses HDL cholesterol','high')]),
'1.3':(1,[L(V4+'7.4','helpful','excess sodium raises blood pressure','low')]),
'1.4':(1,[L(C5+'1.6','helpful','soluble fibre lowers LDL','high')]),
'1.5':(2,[]),
'1.6':(2,[]),
'1.7':(2,[L(P+'1.6','essential','uses cholesterol','high')]),
'2.b':(1,[]),
'2.0':(2,[L(P+'2.b','essential','uses insulin and diabetes','high')]),
'2.1':(2,[L(P+'2.b','essential','uses insulin and diabetes','high')]),
'2.2':(1,[L(P+'2.1','essential','Type 2 diabetes','high')]),
'2.3':(1,[L(P+'2.1','essential','Type 2 diabetes','high')]),
'2.4':(1,[L(P+'2.b','helpful','uses diabetes','high')]),
'2.5':(2,[L(P+'2.b','helpful','uses diabetes','high')]),
'3.b':(1,[L(C5+'1.0','helpful','fibre adds bulk to stools','high')]),
'3.0':(1,[]),
'3.1':(1,[L(P+'3.0','essential','straining from constipation','high')]),
'3.2':(1,[L(P+'3.1','essential','uses diverticula','high')]),
'3.3':(1,[L(P+'3.0','essential','straining during constipation','high')]),
'3.4':(1,[]),
'3.5':(2,[L(C5+'1.b','helpful','uses dietary fibre','high')]),
'3.6':(1,[]),
'3.7':(1,[L(C5+'1.3','helpful','low fibre bowel risk','high')]),
'4.b':(1,[]),
'4.0':(1,[L(P+'4.b','essential','uses osteoporosis and bone loss','high')]),
'4.1':(2,[L(V4+'1.2','helpful','calcium builds bone','high')]),
'4.2':(2,[L(V4+'1.2','helpful','calcium absorption','low')]),
'4.3':(1,[]),
'4.4':(2,[]),
'4.5':(1,[]),
'4.6':(2,[L(P+'4.1','essential','nutrients that protect bone','high'),L(P+'4.2','essential','calcium absorption inhibitors','high')]),
'5.b':(1,[]),
'5.0':(1,[]),
'5.1':(1,[L(P+'5.0','essential','plaque acid causes decay','high')]),
'5.2':(1,[L(P+'5.0','helpful','acid dissolves enamel','high')]),
'5.3':(1,[]),
'5.4':(1,[L(P+'5.0','helpful','uses plaque','low')]),
'5.5':(2,[L(P+'5.1','helpful','frequent sugar causes decay','high')]),
'6.b':(1,[]),
'6.0':(1,[L(P+'0.4','essential','obesity raises disease risk','high')]),
'6.1':(1,[L(P+'1.3','essential','salt raises blood pressure','high')]),
'6.2':(1,[L(P+'5.0','helpful','sugar causes dental caries','high')]),
'6.3':(1,[L(P+'3.1','essential','diverticular disease from straining','high')]),
'6.4':(1,[L(P+'4.1','helpful','calcium and vitamin D for bone','high'),L(V4+'2.4','helpful','iron deficiency causes anaemia','high')]),
'6.5':(2,[]),
}
g2={k:[] for k in g1}
D='hom-energy-nutrition-s4.'
g2['0.5']=[L(D+'1.5','helpful','limit foods high in fat, sugar, salt','low')]
g2['0.6']=[L(D+'1.7','helpful','low-fat cooking methods','low')]
g2['1.4']=[L(D+'2.0','helpful','fruit and vegetable protective nutrients','low')]
g2['1.5']=[L(D+'9.b','helpful','lifestyle risk habits','low')]
g2['4.5']=[L(D+'9.0','helpful','weight-bearing exercise','high')]
def ids(f):
    return re.findall(r'^\[([^\]]+)\]',open(B+'packs/'+f).read(),re.M)
def target_ids(f):
    t=open(B+'packs/'+f).read().split('\nCANDIDATES')[0]
    return re.findall(r'^\[([^\]]+)\]',t,re.M)
def run(f,out):
    tid=target_ids(f); allid=set(ids(f))
    assert [P+k for k in (g1 if '1.txt' in f else g2)]==tid,(len(tid))
    res={}
    for k in (g1 if 'g1' in f else g2):
        if 'g1' in f: c,n=g1[k]; res[P+k]={"cost":c,"needs":n}
        else: res[P+k]={"needs":g2[k]}
    for v in res.values():
        for n in v['needs']: assert n['id'] in allid,n
    json.dump(res,open(B+'point-links/'+out,'w'),indent=1)
    nl=sum(len(v['needs']) for v in res.values())
    print(out,len(res),nl,sum(v.get('cost')==2 for v in res.values()),sum(n['confidence']=='low' for v in res.values() for n in v['needs']))
run('hom-meal-planning-s3.t1g1.txt','hom-meal-planning-s3.t1g1.json')
run('hom-meal-planning-s3.t1g2.txt','hom-meal-planning-s3.t1g2.json')
