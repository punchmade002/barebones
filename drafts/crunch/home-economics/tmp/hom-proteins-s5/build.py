import json,re
P='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
S='hom-proteins-s5.'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
def H(i,w,c='high'): return L(i,'helpful',w,c)
def E(i,w,c='high'): return L(i,'essential',w,c)
D={
'0.b':(2,[]),
'0.0':(2,[H('hom-proteins-s2.3.b','secondary and tertiary structure')]),
'0.1':(1,[E(S+'0.0','denaturation')]),
'0.2':(1,[E(S+'0.0','denatured chains')]),
'0.3':(1,[H(S+'0.2','coagulation as linking')]),
'0.4':(1,[H(S+'0.0','denaturation')]),
'0.5':(2,[]),
'0.6':(1,[H(S+'0.3','coagulation')]),
'0.7':(1,[H(S+'0.3','coagulation')]),
'0.8':(1,[H(S+'0.3','coagulation')]),
'1.b':(1,[H('hom-proteins-s4.1.b','albumin in egg white')]),
'1.0':(2,[H(S+'0.0','denaturation by unfolding')]),
'1.1':(1,[H(S+'1.0','albumen around bubbles')]),
'1.2':(1,[H(S+'0.3','coagulation by heat')]),
'1.3':(1,[H(S+'0.0','over-denaturation')]),
'1.4':(1,[]),
'2.b':(1,[]),
'2.0':(2,[H('hom-proteins-s4.3.0','gelatine from collagen')]),
'2.1':(1,[H('hom-proteins-s4.3.b','gelatine')]),
'2.2':(1,[H(S+'2.0','gel network')]),
'2.3':(1,[H(S+'2.0','gel')]),
'3.b':(1,[]),
'3.0':(1,[H(S+'0.3','denaturation and coagulation')]),
'3.1':(1,[H(S+'3.0','dry heat effect on protein')]),
'3.2':(1,[H(S+'4.0','Maillard reaction')]),
'4.b':(1,[]),
'4.0':(2,[H('hom-proteins-s2.0.b','amino acids','low')]),
'4.1':(1,[H(S+'4.0','Maillard reaction')]),
'4.2':(1,[H(S+'4.0','Maillard reaction')]),
'5.b':(1,[]),
'5.0':(1,[H('hom-proteins-s4.3.0','collagen to gelatine')]),
'5.1':(1,[E(S+'5.0','collagen conversion')]),
'5.2':(1,[]),
'5.3':(1,[H('hom-proteins-s2.2.4','bonds broken by heat')]),
'6.b':(1,[]),
'6.0':(1,[H(S+'0.0','unfolding of protein')]),
'6.1':(2,[H('hom-proteins-s4.4.1','gluten formation')]),
'6.2':(1,[]),
'6.3':(1,[H(S+'0.0','denaturation')]),
'7.b':(1,[]),
'7.0':(1,[H(S+'0.0','denaturation by acid')]),
'7.1':(1,[H(S+'7.0','acid denatures protein')]),
'7.2':(1,[]),
'7.3':(2,[H('hom-proteins-s4.2.2','casein coagulation')]),
'7.4':(1,[H(S+'0.0','denaturation')]),
'8.b':(1,[]),
'8.0':(1,[H('hom-proteins-s4.2.0','casein')]),
'8.1':(1,[]),
'8.2':(1,[H('hom-proteins-s2.0.1','peptide bonds')]),
'8.3':(1,[H(S+'8.2','proteolytic hydrolysis')]),
'8.4':(1,[]),
'9.b':(1,[H(S+'0.0','denaturation')]),
'9.0':(1,[H(S+'0.5','heat and mechanical denaturation')]),
'9.1':(1,[]),'9.2':(1,[]),'9.3':(1,[]),'9.4':(1,[]),'9.5':(1,[]),'9.6':(1,[]),
'9.7':(1,[H(S+'0.0','denaturation')]),
}
txt=open(P+'packs/hom-proteins-s5.t1g1.txt').read()
tgt=re.findall(r'^\[('+re.escape(S)+r'[^\]]+)\]',txt,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
out={}
for t in tgt:
    c,n=D[t[len(S):]]; out[t]={"cost":c,"needs":n}
assert len(out)==len(D)==len(tgt),(len(out),len(D),len(tgt))
assert all(n['id'] in allids and n['id']!=k for k,v in out.items() for n in v['needs'])
json.dump(out,open(P+'point-links/hom-proteins-s5.t1g1.json','w'),indent=1)
v=out.values()
print(len(out),sum(len(x['needs']) for x in v),sum(x['cost']==2 for x in v),sum(n['confidence']=='low' for x in v for n in x['needs']))
