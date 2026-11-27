import json,re,os
B='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
def L(i,w,s='helpful',c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
D={}
# proteins s9
p='hom-proteins-s9.'
D['hom-proteins-s9']={
'0.b':(1,[]),'0.0':(2,[]),'0.1':(2,[]),'0.2':(1,[]),
'0.3':(1,[L(p+'0.2','micro-organism sources')]),'0.4':(1,[]),
'1.b':(1,[]),'1.0':(1,[]),'1.1':(1,[]),
'1.2':(1,[L(p+'1.0','compares with tofu')]),'1.3':(1,[]),
'1.4':(1,[L(p+'1.1','soya milk as starting material')]),
'2.b':(1,[]),'2.0':(1,[]),'2.1':(1,[]),'2.2':(1,[]),'2.3':(2,[]),'2.4':(1,[]),'2.5':(1,[]),'2.6':(1,[]),
'3.b':(1,[]),'3.0':(1,[L(p+'0.3','mycoprotein from fungus')]),'3.1':(1,[]),
'3.2':(1,[L('hom-proteins-s4.1.0','egg albumen protein','helpful','low')]),'3.3':(1,[]),'3.4':(1,[]),
'4.b':(1,[]),'4.0':(2,[L('hom-proteins-s7.0.2','soya is HBV')]),'4.1':(1,[]),'4.2':(1,[]),
'4.3':(2,[L('hom-proteins-s7.0.0','high biological value protein')]),'4.4':(1,[]),
'4.5':(2,[L(p+'3.2','egg binder in Quorn','helpful','low')]),'4.6':(1,[]),
'4.7':(1,[L('hom-proteins-s7.1.4','meat extenders')]),
'5.b':(1,[]),'5.0':(1,[]),'5.1':(1,[]),'5.2':(1,[]),
'5.3':(1,[L(p+'2.b','TVP')]),'5.4':(1,[]),'5.5':(1,[]),'5.6':(1,[]),'5.7':(1,[]),
'6.b':(1,[]),'6.0':(1,[L(p+'2.4','extrusion step')]),
'6.1':(1,[L(p+'1.0','tofu is bland')]),'6.2':(1,[L(p+'1.b','fermented soya foods')]),
'6.3':(1,[L(p+'3.4','steaming sets binder')]),'6.4':(1,[]),
'7.b':(1,[]),'7.0':(1,[]),'7.1':(1,[]),
'7.2':(1,[L('hom-proteins-s7.0.0','high biological value protein')]),
'7.3':(1,[]),'7.4':(1,[]),'7.5':(1,[]),'7.6':(2,[]),'7.7':(2,[L(p+'7.0','compare per portion')]),
}
c='hom-cereals-grains-s3.'
D['hom-cereals-grains-s3']={
'0.b':(1,[]),'0.0':(2,[]),'0.1':(1,[L('hom-cereals-grains-s1.0.1','endosperm')]),
'0.2':(1,[L('hom-cereals-grains-s1.0.1','endosperm and bran')]),
'0.3':(1,[L('hom-cereals-grains-s1.0.b','bran, germ, endosperm')]),'0.4':(1,[]),
'0.5':(2,[L(c+'3.0','gluten strength')]),
'0.6':(2,[L('hom-cereals-grains-s1.0.b','three parts of grain')]),'0.7':(1,[]),'0.8':(2,[]),
'1.b':(1,[]),'1.0':(1,[L('hom-cereals-grains-s1.0.1','endosperm')]),
'1.1':(1,[L('hom-cereals-grains-s1.1.5','refining removes nutrients')]),'1.2':(1,[]),
'1.3':(1,[L('hom-cereals-grains-s1.0.2','oil in germ','helpful','low')]),
'2.b':(1,[]),'2.0':(1,[]),'2.1':(1,[]),'2.2':(1,[L(c+'3.1','gluten traps gas')]),
'2.3':(1,[L(c+'3.1','gluten strands','helpful','low')]),'2.4':(1,[]),'2.5':(1,[]),
'2.6':(1,[L('hom-cereals-grains-s1.5.0','coeliac disease and gluten')]),
'3.b':(1,[]),'3.0':(1,[L('hom-proteins-s4.4.1','gluten formation')]),
'3.1':(1,[L('hom-proteins-s4.4.2','gluten elasticity')]),'3.2':(1,[]),'3.3':(1,[]),
'4.b':(1,[]),'4.0':(1,[]),'4.1':(1,[]),'4.2':(2,[]),
'4.3':(1,[L('hom-cereals-grains-s1.5.0','coeliac disease and gluten')]),
'4.4':(1,[]),'4.5':(1,[]),'4.6':(1,[]),
}
w='hom-work-leisure-s3.'
D['hom-work-leisure-s3']={
'0.b':(1,[]),'0.0':(2,[L('hom-work-leisure-s1.0.3','unpaid work in the home')]),
'0.1':(1,[]),'0.2':(1,[]),'0.3':(1,[]),'0.4':(1,[]),'0.5':(1,[]),'0.6':(1,[]),
'1.b':(1,[]),'1.0':(1,[]),'1.1':(1,[]),'1.2':(1,[]),
'2.b':(1,[L('hom-work-leisure-s1.0.5','voluntary work defined')]),'2.0':(1,[]),
'2.1':(2,[]),'2.2':(2,[]),'2.3':(2,[]),'2.4':(1,[]),'2.5':(1,[]),
'3.b':(1,[]),'3.0':(1,[L('hom-work-leisure-s1.0.3','unpaid home work')]),'3.1':(1,[]),'3.2':(1,[]),
'4.b':(1,[]),'4.0':(1,[]),'4.1':(1,[]),'4.2':(1,[]),'4.3':(1,[]),'4.4':(1,[]),'4.5':(1,[]),'4.6':(1,[]),
'5.b':(1,[]),'5.0':(1,[]),'5.1':(2,[]),'5.2':(1,[]),'5.3':(1,[]),'5.4':(1,[]),'5.5':(1,[]),'5.6':(1,[]),
'6.b':(1,[]),'6.0':(1,[]),'6.1':(1,[]),'6.2':(1,[]),'6.3':(1,[]),'6.4':(1,[]),'6.5':(1,[]),
'7.b':(1,[]),'7.0':(1,[]),'7.1':(1,[]),'7.2':(1,[]),
'7.3':(1,[L(w+'0.4','no pay or pension')]),
'7.4':(1,[L(w+'2.5','training and Garda vetting')]),
'8.b':(1,[]),'8.0':(2,[]),'8.1':(1,[L(w+'7.2','out-of-pocket costs')]),
}
for sub,d in D.items():
    name={'hom-proteins-s9':'hom-proteins-s9','hom-cereals-grains-s3':'hom-cereals-grains-s3','hom-work-leisure-s3':'hom-work-leisure-s3'}[sub]
    txt=open(B+f'packs/{name}.t1g1.txt').read()
    ids=re.findall(r'^\[([^\]]+)\]',txt,re.M)
    tgt=[i for i in ids if i.startswith(sub+'.')]
    out={}
    for t in tgt:
        k=t[len(sub)+1:]; cost,n=d[k]; out[t]={"cost":cost,"needs":n}
    assert set(d)=={t[len(sub)+1:] for t in tgt},(sub,set(d)^{t[len(sub)+1:] for t in tgt})
    for v in out.values():
        for n in v['needs']: assert n['id'] in ids,n
    json.dump(out,open(B+f'point-links/{name}.t1g1.json','w'),indent=1)
    print(sub,len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
