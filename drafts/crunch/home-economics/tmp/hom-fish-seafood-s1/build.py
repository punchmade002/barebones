import json,re,sys
D='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
P='hom-fish-seafood-s1.';L='hom-lipids-s1.';V='hom-vitamins-minerals-s1.';B='hom-proteins-s7.'
def n(i,s,w,c='high'):return {"id":i,"strength":s,"why":w,"confidence":c}
H='helpful';E='essential'
T={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),'0.2':(1,[]),'0.3':(1,[]),'0.4':(1,[]),
'0.5':(2,[n(B+'0.0.',H,'')]),
'0.6':(1,[]),'1.b':(1,[]),
'1.0':(1,[n(B+'0.0',E,'uses HBV protein')]),
'1.1':(2,[n(L+'0.3',H,'uses polyunsaturated fat'),n(L+'1.3',H,'uses omega-3 fatty acids','low'),n(V+'1.0',H,'fat-soluble vitamins carried in oil','low')]),
'1.2':(1,[]),'1.3':(1,[]),'1.4':(2,[]),'1.5':(2,[]),'1.6':(2,[]),'1.7':(1,[]),
'2.b':(1,[]),'2.0':(1,[]),
'2.1':(1,[n(L+'0.3',H,'uses polyunsaturated fatty acids')]),
'2.2':(1,[n(P+'2.1',H,'uses omega-3 fatty acids')]),
'2.3':(2,[n(P+'2.2',E,'fewer clots from sticky platelets'),n(L+'5.1',H,'uses cholesterol and LDL','low')]),
'2.4':(1,[n(L+'5.1',H,'uses cholesterol build-up in arteries')]),
'2.5':(1,[n(P+'2.1',H,'DHA is an omega-3 fatty acid')]),
'2.6':(2,[n(V+'4.3',H,'uses vitamin D calcium absorption')]),
'2.7':(2,[n(P+'2.6',H,'uses vitamin D role'),n(V+'8.3',H,'vitamin D heat stability','low')]),
'3.b':(1,[]),
'3.0':(1,[n(P+'0.4',E,'uses short fibres, low connective tissue')]),
'3.1':(1,[n(B+'0.0',E,'uses HBV protein')]),
'3.2':(1,[n(P+'1.1',H,'uses white fish having little fat')]),
'3.3':(2,[n(P+'2.1',H,'uses omega-3 fatty acids'),n(L+'5.4',H,'unsaturated fats lower LDL cholesterol')]),
'3.4':(1,[n(P+'1.7',H,'uses cholesterol in shellfish')]),
'3.5':(1,[n(P+'1.2',H,'fish contains no carbohydrate')]),
'3.6':(1,[n(P+'1.5',H,'iodine from sea fish')]),
'3.7':(1,[]),'3.8':(1,[]),'4.b':(1,[]),
'4.0':(1,[n(P+'1.2',H,'fish lacks carbohydrate')]),
'4.1':(1,[]),
'4.2':(1,[n(P+'3.3',H,'health benefits of oily fish','low')]),
'4.3':(1,[]),'4.4':(1,[])}
T['0.5']=(2,[n(B+'0.0',H,'uses HBV protein')])
def run(name,pref,T):
    txt=open(D+'packs/'+name+'.txt').read()
    tg=[];ids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    sec=txt.split('CANDIDATES')[0]
    tg=re.findall(r'^\[([^\]]+)\]',sec,re.M)
    out={}
    for t in tg:
        k=t[len(pref):]
        c,nd=T[k]
        out[t]={"cost":c,"needs":nd}
    assert set(T)==set(k[len(pref):] for k in tg),(set(T)^set(k[len(pref):] for k in tg))
    links=low=c2=0
    for t,v in out.items():
        for x in v['needs']:
            assert x['id'] in ids and x['id']!=t,x['id'];links+=1;low+=x['confidence']=='low'
        c2+=v['cost']==2
    json.dump(out,open(D+'point-links/'+name+'.json','w'),indent=1)
    print(name,len(out),links,c2,low)
run('hom-fish-seafood-s1.t1g1','hom-fish-seafood-s1.',T)
