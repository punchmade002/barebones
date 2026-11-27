import json,re
P='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
S='hom-housing-s2.'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
D={
'0.b':(1,[]),'0.0':(2,[]),'0.1':(2,[]),'0.2':(2,[]),'0.3':(1,[]),'0.4':(1,[]),
'0.5':(1,[L(S+'0.4','essential','mortgage as loan')]),
'1.b':(1,[]),
'1.0':(1,[L(S+'0.3','helpful','deposit meaning')]),
'1.1':(1,[L(S+'0.4','helpful','mortgage meaning')]),
'1.2':(1,[]),
'1.3':(1,[L('hom-personal-finance-s3.2.5','helpful','credit union loans')]),
'1.4':(1,[]),'1.5':(2,[]),
'2.b':(1,[]),
'2.0':(1,[L('hom-personal-finance-s1.3.0','helpful','gross income meaning')]),
'2.1':(1,[L(S+'0.3','helpful','deposit meaning')]),
'2.2':(1,[]),'2.3':(2,[]),'2.4':(2,[]),'2.5':(1,[]),
'2.6':(2,[L('hom-personal-finance-s5.4.0','helpful','buildings insurance')]),
'2.7':(1,[L(S+'3.b','helpful','mortgage protection insurance')]),
'3.b':(1,[L('hom-personal-finance-s5.5.0','helpful','life assurance')]),
'3.0':(1,[L('hom-personal-finance-s5.5.1','helpful','term assurance')]),
'3.1':(1,[L(S+'3.0','essential','mortgage protection policy')]),
'3.2':(1,[L(S+'3.0','helpful','mortgage protection policy')]),
'3.3':(2,[L('hom-personal-finance-s5.5.2','helpful','whole-of-life assurance')]),
'3.4':(1,[L('hom-personal-finance-s3.7.0','helpful','Consumer Credit Act 1995','low')]),
'3.5':(1,[]),
'3.6':(1,[L('hom-personal-finance-s5.4.4','helpful','income protection insurance','low')]),
'3.7':(1,[L(S+'4.0','essential','annuity mortgage'),L(S+'4.2','essential','pension-linked mortgage')]),
'3.8':(1,[L(S+'4.1','essential','endowment mortgage')]),
'4.b':(1,[]),
'4.0':(2,[L(S+'5.b','helpful','fixed and variable rates'),L(S+'3.b','helpful','mortgage protection')]),
'4.1':(2,[L('hom-personal-finance-s5.5.3','helpful','endowment assurance')]),
'4.2':(2,[]),'4.3':(2,[]),'4.4':(1,[]),'4.5':(1,[]),'4.6':(1,[]),
'5.b':(1,[]),'5.0':(2,[]),'5.1':(1,[]),
'5.2':(1,[L(S+'5.0','essential','fixed portion'),L(S+'5.1','essential','variable portion')]),
'5.3':(1,[L(S+'5.0','helpful','fixed rate meaning')]),
'5.4':(1,[]),
'5.5':(1,[L(S+'5.4','helpful','longer term comparison')]),
}
txt=open(P+'packs/hom-housing-s2.t1g1.txt').read()
tgt=re.findall(r'^\[('+re.escape(S)+r'[^\]]+)\]',txt,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
out={}
for t in tgt:
    c,n=D[t[len(S):]]; out[t]={"cost":c,"needs":n}
assert len(out)==len(D)==len(tgt),(len(out),len(D),len(tgt))
assert all(n['id'] in allids and n['id']!=k for k,v in out.items() for n in v['needs'])
json.dump(out,open(P+'point-links/hom-housing-s2.t1g1.json','w'),indent=1)
v=out.values()
print(len(out),sum(len(x['needs']) for x in v),sum(x['cost']==2 for x in v),sum(n['confidence']=='low' for x in v for n in x['needs']))
