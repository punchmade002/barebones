import json,re,sys
B='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
H,L='high','low'
def lk(i,s,w,c=H): return {"id":i,"strength":"essential" if s=='E' else "helpful","why":w,"confidence":c}
P={}
# ---- sociological-concepts-s4
p='hom-sociological-concepts-s4'
S1={
'0.b':(1,[]),
'0.0':(1,[lk('hom-sociological-concepts-s1.2.0','H','uses norms'),lk('hom-sociological-concepts-s1.4.0','H','uses values')]),
'0.1':(2,[]),'0.2':(1,[]),
'0.3':(1,[lk('hom-sociological-concepts-s3.4.b','H','agent of socialisation')]),
'0.4':(1,[]),
'0.5':(1,[lk(p+'.0.0','H','uses institution')]),
'0.6':(1,[lk(p+'.0.5','H','uses function idea')]),
'0.7':(1,[lk(p+'.0.6','H','contrasts with manifest function')]),
'1.b':(1,[]),'1.0':(1,[]),
'1.1':(1,[lk('hom-sociological-concepts-s3.3.b','H','socialisation process')]),
'1.2':(1,[]),'1.3':(1,[]),
'1.4':(2,[lk('hom-family-society-s5.0.3','H','adopt and supplement functions')]),
'1.5':(2,[lk('hom-family-society-s5.0.0','H','five family functions'),lk(p+'.1.4','H','supplementing family functions')]),
'2.b':(1,[]),'2.0':(1,[]),
'2.1':(1,[lk(p+'.2.0','H','contrasts with formal curriculum')]),
'2.2':(1,[lk('hom-sociological-concepts-s3.3.b','H','socialisation process')]),
'2.3':(2,[]),'2.4':(1,[]),'2.5':(2,[]),
'3.b':(1,[]),'3.0':(1,[]),
'3.1':(1,[lk(p+'.3.0','H','socio-economic status effects',L)]),
'3.2':(1,[lk(p+'.3.1','H','costs these supports meet')]),
'3.3':(1,[lk(p+'.3.0','H','educational disadvantage by status')]),
'4.b':(1,[]),'4.0':(1,[]),
'4.1':(1,[lk('hom-sociological-concepts-s1.2.0','H','uses norms')]),
'4.2':(2,[]),'4.3':(1,[]),'4.4':(1,[]),'4.5':(1,[]),
'5.b':(1,[]),'5.0':(1,[]),'5.1':(1,[]),'5.2':(1,[]),'5.3':(1,[]),'5.4':(1,[]),
'5.5':(1,[lk(p+'.5.1','H','income and standard of living',L)]),
'5.6':(1,[]),
'6.b':(1,[]),'6.0':(2,[]),'6.1':(2,[]),
'6.2':(1,[lk(p+'.6.1','E','uses three branches')]),
'6.3':(2,[lk(p+'.6.1','H','legislature executive judiciary')]),
'6.4':(1,[]),'6.5':(1,[]),
'6.6':(2,[lk('hom-family-society-s5.0.0','H','five family functions'),lk(p+'.6.0','H','State services')]),
'6.7':(1,[lk('hom-family-society-s5.1.3','H','Tusla child agency')]),
'7.b':(1,[]),'7.0':(1,[]),
'7.1':(1,[lk(p+'.7.0','H','health institution')]),
'7.2':(1,[]),
'7.3':(1,[lk('hom-sociological-concepts-s3.4.3','H','media as agent of socialisation')]),
'7.4':(1,[lk(p+'.6.0','H','government makes laws')]),
}
P[p]=(S1,'hom-sociological-concepts-s4.t1g1')
# ---- social-change-s3
p='hom-social-change-s3'
E='hom-education-s3.';F='hom-personal-finance-s1.'
S2={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),'0.2':(1,[]),
'0.3':(1,[lk(E+'4.4','H','free fees initiative')]),
'0.4':(1,[lk(E+'4.3','H','SUSI means-tested grants')]),
'0.5':(1,[lk(E+'0.0','H','ECCE scheme')]),
'0.6':(2,[lk(E+'4.2','H','PLC courses')]),
'1.b':(1,[]),
'1.0':(1,[lk(E+'6.2','H','special needs assistants')]),
'1.1':(1,[]),'1.2':(1,[]),
'1.3':(1,[lk(E+'2.4','H','Leaving Certificate Applied')]),
'1.4':(1,[lk(E+'2.1','H','Transition Year'),lk(E+'5.1','H','Youthreach second chance')]),
'1.5':(1,[lk('hom-unemployment-poverty-s6.3.7','H','Back to Education Allowance',L)]),
'1.6':(1,[lk(E+'4.5','H','HEAR and DARE routes')]),
'2.b':(1,[]),'2.0':(1,[]),'2.1':(1,[]),'2.2':(1,[]),'2.3':(1,[]),'2.4':(1,[]),
'2.5':(2,[]),'2.6':(1,[]),
'3.b':(2,[lk(F+'4.3','H','PRSI contributions')]),
'3.0':(1,[lk(F+'6.0','H','social insurance payments')]),
'3.1':(1,[lk(F+'6.4','H','means test')]),
'3.2':(2,[lk(p+'.3.1','H','means-tested assistance')]),
'3.3':(1,[lk(p+'.3.1','H','contrast with means-tested')]),
'4.b':(1,[]),
'4.0':(1,[lk(p+'.3.3','H','universal payments')]),
'4.1':(1,[lk(p+'.3.1','H','means-tested payments',L)]),
'4.2':(1,[]),
'4.3':(1,[lk(p+'.3.1','H','means-tested')]),
'4.4':(1,[]),
'4.5':(1,[lk(p+'.3.1','H','means-tested eligibility',L)]),
'4.6':(1,[]),
'5.b':(1,[]),'5.0':(1,[]),'5.1':(1,[]),'5.2':(1,[]),
'5.3':(1,[lk(p+'.4.2','H','One-Parent Family Payment')]),
'5.4':(1,[lk(p+'.3.1','H','means tests')]),
'5.5':(2,[]),
'5.6':(1,[lk(p+'.5.5','H','welfare dependency criticism')]),
'5.7':(1,[lk(p+'.3.b','H','funded by taxes and PRSI')]),
'6.b':(1,[]),'6.0':(1,[]),'6.1':(1,[]),
'6.2':(1,[lk(p+'.1.0','H','special needs assistants'),lk(p+'.1.1','H','School Completion Programme'),lk(p+'.0.5','H','free pre-school')]),
}
P[p]=(S2,'hom-social-change-s3.t1g1')
# ---- textiles-fibres-s4
p='hom-textiles-fibres-s4';T='hom-textiles-fibres-s3.'
S3={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),
'0.2':(1,[lk(T+'0.0','H','staple fibres and filaments')]),
'0.3':(1,[]),'0.4':(1,[]),'0.5':(1,[]),'0.6':(1,[]),'0.7':(1,[]),
'1.b':(1,[]),'1.0':(1,[]),'1.1':(1,[]),'1.2':(1,[]),'1.3':(1,[]),'1.4':(1,[]),
'1.5':(1,[lk(p+'.1.4','H','carding produces sliver')]),
'1.6':(1,[lk(p+'.1.4','H','sliver from carding'),lk(T+'0.0','H','staple fibres need twist')]),
'2.b':(1,[]),'2.0':(2,[]),'2.1':(2,[]),
'2.2':(2,[lk(p+'.9.1','H','burning test method',L)]),
'2.3':(1,[]),'2.4':(1,[]),
'3.b':(1,[]),
'3.0':(2,[lk(p+'.1.4','H','carding'),lk(p+'.1.6','H','spinning')]),
'3.1':(1,[]),'3.2':(1,[]),'3.3':(2,[]),
'3.4':(1,[lk(p+'.2.2','H','cotton burning test')]),
'3.5':(1,[]),'3.6':(1,[]),
'4.b':(1,[]),
'4.0':(1,[lk(T+'0.4','H','monomers and polymers')]),
'4.1':(1,[lk(T+'5.0','H','spinneret extrusion',L)]),
'4.2':(1,[]),
'4.3':(1,[lk(T+'5.2','H','drawing aligns molecules',L)]),
'4.4':(1,[]),
'4.5':(1,[lk(T+'0.0','H','filaments'),lk(p+'.8.1','H','texturing',L)]),
'5.b':(1,[]),'5.0':(2,[]),'5.1':(1,[]),
'5.2':(2,[lk(p+'.9.1','H','burning test method',L)]),
'5.3':(1,[]),'5.4':(1,[]),
'6.b':(1,[]),'6.0':(1,[]),'6.1':(1,[]),'6.2':(1,[]),'6.3':(1,[]),
'6.4':(1,[lk(T+'2.1','H','viscose weak when wet')]),
'7.b':(1,[]),'7.0':(1,[]),'7.1':(1,[]),
'7.2':(1,[lk(p+'.1.4','H','carding')]),
'7.3':(1,[]),
'7.4':(1,[lk(p+'.2.0','H','cotton properties'),lk(p+'.6.1','H','polyester properties')]),
'7.5':(1,[]),
'7.6':(1,[lk(p+'.2.2','H','cotton burning test'),lk(p+'.6.2','H','polyester burning test')]),
'7.7':(1,[lk(p+'.2.3','H','cotton microscope'),lk(p+'.5.3','H','smooth filaments',L)]),
'7.8':(1,[]),
'8.b':(1,[]),'8.0':(2,[]),'8.1':(1,[]),
'8.2':(1,[lk(p+'.8.1','H','texturing')]),
'8.3':(1,[lk(p+'.8.1','H','crimp in textured yarn')]),
'8.4':(1,[]),'8.5':(2,[]),'8.6':(1,[]),'8.7':(1,[]),
'9.b':(1,[]),'9.0':(1,[]),'9.1':(1,[]),
'9.2':(1,[lk(p+'.9.1','H','burning method')]),
'9.3':(1,[lk(p+'.9.1','H','burning method')]),
'9.4':(1,[]),'9.5':(2,[]),
'9.6':(1,[lk(p+'.7.b','H','blends give mixed results',L)]),
'9.7':(1,[lk(p+'.9.1','H','burning result'),lk(p+'.9.4','H','microscope appearance')]),
}
P[p]=(S3,'hom-textiles-fibres-s4.t1g1')
for p,(S,name) in P.items():
    txt=open(B+'packs/'+name+'.txt').read()
    head=txt.split('CANDIDATES')[0]
    tids=re.findall(r'^\[(%s\.[^\]]+)\]'%re.escape(p),head,re.M)
    allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    assert set(S)=={t[len(p)+1:] for t in tids} and len(S)==len(tids),(p,set(S)^{t[len(p)+1:] for t in tids})
    out={}
    for t in tids:
        c,n=S[t[len(p)+1:]]
        for x in n: assert x['id'] in allids and x['id']!=t,(t,x)
        out[t]={"cost":c,"needs":n}
    json.dump(out,open(B+'point-links/'+name+'.json','w'),ensure_ascii=False,indent=1)
    nl=sum(len(v['needs']) for v in out.values())
    print(p,len(out),nl,sum(v['cost']==2 for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
