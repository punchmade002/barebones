import json,re,sys
D='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
H,E='helpful','essential'
P={}
p='hom-proteins-s3.'
P['hom-proteins-s3.t1g1']={
'0.b':(1,[]),
'0.0':(1,[L('hom-proteins-s1.0.2',H,'uses amino acids')]),
'0.1':(2,[]),
'0.2':(1,[L('hom-proteins-s1.2.6',H,'uses biological value')]),
'1.b':(1,[L('hom-proteins-s1.4.0',H,'uses hydrolysis')]),
'1.0':(1,[]),'1.1':(1,[]),'1.2':(1,[]),
'2.b':(1,[L(p+'0.0',H,'conjugated protein definition')]),
'2.0':(1,[L(p+'2.b',H,'uses prosthetic group')]),
'2.1':(1,[L(p+'2.b',H,'uses prosthetic group')]),
'2.2':(1,[L(p+'2.b',H,'uses prosthetic group')]),
'2.3':(2,[L(p+'2.b',H,'uses prosthetic group')]),
'2.4':(1,[L('hom-proteins-s1.4.0',E,'uses hydrolysis')]),
'3.b':(1,[L('hom-proteins-s2.2.3',H,'fibrous and globular shape')]),
'3.0':(1,[L('hom-proteins-s2.2.3',H,'fibrous shape')]),
'3.1':(2,[L(p+'3.0',H,'fibrous protein definition')]),
'3.2':(1,[L('hom-proteins-s2.2.3',H,'globular shape')]),
'3.3':(2,[L(p+'3.2',H,'globular protein definition')]),
'4.b':(1,[]),
'4.0':(1,[L(p+'1.1',H,'plant simple proteins')]),
'4.1':(2,[]),'4.2':(2,[]),
'4.3':(1,[L(p+'4.1',H,'glutenin is a glutelin','low')]),
}
t='hom-textiles-fibres-s2.'
P['hom-textiles-fibres-s2.t1g1']={
'0.b':(1,[L('hom-textiles-fibres-s1.3.1',H,'uses flammable property')]),
'0.0':(1,[]),'0.1':(1,[]),'0.2':(1,[]),'0.3':(1,[]),'0.4':(1,[]),'0.5':(1,[]),'0.6':(2,[]),
'1.b':(1,[L(t+'0.4',H,'flame-retardant treatment')]),
'1.0':(1,[]),'1.1':(1,[]),'1.2':(1,[]),'1.3':(1,[]),'1.4':(1,[]),'1.5':(1,[]),'1.6':(1,[]),
'1.7':(2,[]),
'2.b':(1,[]),
'2.0':(1,[L('hom-textiles-fibres-s1.3.4',H,'durable property')]),
'2.1':(1,[L('hom-textiles-fibres-s1.3.6',H,'resilient property')]),
'2.2':(1,[]),'2.3':(1,[]),
'2.4':(1,[L(t+'0.5',H,'fire-resistance labels')]),
'2.5':(1,[]),
'3.b':(1,[]),'3.0':(1,[]),
'3.1':(1,[L(t+'3.0',H,'GPSR regulation')]),
'3.2':(2,[L(t+'3.0',H,'GPSR regulation')]),
'3.3':(1,[L(t+'3.0',H,'GPSR regulation')]),
'3.4':(1,[]),
}
c='hom-carbohydrates-s3.'
P['hom-carbohydrates-s3.t1g1']={
'0.b':(1,[L('hom-carbohydrates-s2.1.0',H,'monosaccharides defined')]),
'0.0':(1,[]),'0.1':(1,[]),'0.2':(1,[]),
'0.3':(1,[L(c+'1.2',H,'lactose is milk sugar')]),
'0.4':(1,[L(c+'0.3',H,'galactose from lactose')]),
'1.b':(1,[L('hom-carbohydrates-s2.1.1',H,'disaccharides defined')]),
'1.0':(1,[]),'1.1':(1,[]),'1.2':(2,[]),'1.3':(2,[]),'1.4':(2,[]),
'1.5':(1,[L(c+'1.4',H,'added sugars')]),
'2.b':(1,[L('hom-carbohydrates-s2.1.2',H,'starch is polysaccharide')]),
'2.0':(2,[]),'2.1':(1,[]),'2.2':(1,[]),'2.3':(1,[]),
'2.4':(1,[L('hom-carbohydrates-s2.1.2',H,'glycogen is polysaccharide')]),
'3.b':(1,[L('hom-carbohydrates-s2.1.2',H,'cellulose pectin polysaccharides')]),
'3.0':(2,[]),'3.1':(2,[]),'3.2':(1,[]),'3.3':(1,[]),'3.4':(1,[]),'3.5':(1,[]),
'4.b':(1,[L(c+'3.b',H,'uses dietary fibre')]),
'4.0':(1,[L(c+'3.0',H,'cellulose sources')]),
'4.1':(1,[L(c+'3.1',H,'pectin sources')]),
'5.b':(1,[]),'5.0':(2,[]),'5.1':(1,[]),'5.2':(1,[]),'5.3':(1,[]),'5.4':(2,[]),'5.5':(1,[]),
}
for name,d in P.items():
    pk=open(D+'packs/'+name+'.txt').read()
    sub=pk.split('\n')[1].split()[1].rstrip(':')
    ids=re.findall(r'^\[([^\]]+)\]',pk,re.M)
    tg=re.findall(r'^\[('+re.escape(sub)+r'\.[^\]]+)\]',pk.split('CANDIDATES')[0],re.M)
    out={}
    for t_ in tg:
        k=t_[len(sub)+1:]
        out[t_]={"cost":d[k][0],"needs":d[k][1]}
    assert set(d)==set(k[len(sub)+1:] for k in tg),(name,set(d)^set(k[len(sub)+1:] for k in tg))
    n=l=c2=lo=0
    for k,v in out.items():
        n+=1;l+=len(v['needs']);c2+=v['cost']==2
        for x in v['needs']:
            assert x['id'] in ids and x['id']!=k,(k,x); lo+=x['confidence']=='low'
    json.dump(out,open(D+'point-links/'+name+'.json','w'),indent=1)
    print(name,n,l,c2,lo)
