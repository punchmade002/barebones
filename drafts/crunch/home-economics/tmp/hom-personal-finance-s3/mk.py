import json,re,sys
P='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
N='hom-personal-finance-s3.t1g1'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
p='hom-personal-finance-s3.'; q='hom-consumer-rights-s1.'
p='hom-personal-finance-s3.'
D={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),'0.2':(1,[]),
'0.3':(2,[]),'0.4':(1,[]),'0.5':(1,[]),
'0.6':(1,[L(p+'0.5','helpful','direct debit contrast')]),
'0.7':(1,[]),'0.8':(1,[]),
'1.b':(1,[]),'1.0':(1,[]),
'1.1':(1,[L(p+'0.0','helpful','cash leaves no record')]),
'1.2':(1,[]),'1.3':(1,[]),
'1.4':(1,[L(p+'0.2','helpful','debit card spending control','low')]),
'1.5':(1,[L(p+'2.b','helpful','credit spreads cost','low')]),
'2.b':(1,[]),
'2.0':(1,[L(p+'0.3','helpful','credit card basics')]),
'2.1':(1,[L(p+'2.0','helpful','contrast with credit card')]),
'2.2':(1,[L(p+'2.0','helpful','credit card comparison','low')]),
'2.3':(1,[]),'2.4':(1,[]),
'2.5':(1,[L(p+'2.4','essential','loan basics')]),
'2.6':(2,[]),
'3.b':(1,[]),'3.0':(1,[]),'3.1':(1,[]),
'3.2':(2,[L(p+'3.1','helpful','ownership stays with finance company')]),
'3.3':(1,[L(p+'3.2','essential','one-third repossession rule')]),
'3.4':(1,[]),'3.5':(1,[]),'3.6':(1,[]),
'4.b':(1,[]),'4.0':(1,[]),'4.1':(1,[]),
'4.2':(1,[L(p+'4.0','essential','cash price'),L(p+'4.1','essential','total amount repayable')]),
'4.3':(1,[]),
'4.4':(2,[L(p+'4.2','essential','cost of credit calculation'),L(p+'4.1','essential','adding all payments')]),
'5.b':(1,[]),'5.0':(1,[]),'5.1':(1,[]),'5.2':(1,[]),
'5.3':(1,[L(p+'4.2','helpful','extra cost of credit')]),
'5.4':(1,[L('hom-consumer-rights-s1.1.6','helpful','impulse buying','low')]),
'5.5':(1,[]),
'6.b':(1,[]),
'6.0':(1,[L('hom-consumer-rights-s1.0.4','helpful','needs versus wants','low')]),
'6.1':(1,[L(p+'4.3','helpful','APR meaning'),L(p+'4.2','helpful','cost of credit','low')]),
'6.2':(1,[]),'6.3':(1,[]),
'6.4':(1,[L(p+'3.1','helpful','hire purchase ownership')]),
'6.5':(1,[L('hom-personal-finance-s2.2.b','helpful','household budget')]),
'7.b':(1,[]),'7.0':(1,[]),
'7.1':(1,[L(p+'4.3','helpful','APR meaning')]),
'7.2':(1,[]),
'7.3':(1,[L(p+'4.3','helpful','APR meaning')]),
'7.4':(1,[L(p+'3.2','helpful','one-third repossession rule')]),
'7.5':(2,[L('hom-personal-finance-s2.6.0','helpful','what MABS is','low')]),
}
txt=open(P+'packs/'+N+'.txt').read().split('\n')
tg=[];cand=set();mode=None
for l in txt:
    if l.startswith('TARGET'):mode='t'
    elif l.startswith('CANDIDATES'):mode='c'
    m=re.match(r'\[([^\]]+)\]',l)
    if m: (tg.append(m.group(1)) if mode=='t' else cand.add(m.group(1)))
allids=set(tg)|cand
pre=tg[0].split('.')[0]+'.'
assert set(pre+k for k in D)==set(tg) and len(tg)==len(D),(set(tg)^set(pre+k for k in D))
out={}
for t in tg:
    c,n=D[t[len(pre):]]
    for x in n: assert x['id'] in allids and x['id']!=t,x
    out[t]={"cost":c,"needs":n}
json.dump(out,open(P+'point-links/'+N+'.json','w'),indent=1)
chk=json.load(open(P+'point-links/'+N+'.json'))
ls=[x for v in chk.values() for x in v['needs']]
print(len(chk),len(ls),sum(v['cost']==2 for v in chk.values()),sum(x['confidence']=='low' for x in ls))
