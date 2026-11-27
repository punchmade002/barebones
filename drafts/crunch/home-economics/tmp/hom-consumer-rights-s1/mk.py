import json,re,sys
P='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
N='hom-consumer-rights-s1.t1g1'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
p='hom-personal-finance-s3.'; q='hom-consumer-rights-s1.'
D={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),'0.2':(1,[]),'0.3':(1,[]),'0.4':(1,[]),
'0.5':(1,[L(p+'2.b','helpful','credit as borrowing now, paying later')]),
'1.b':(1,[]),'1.0':(1,[]),'1.1':(1,[]),'1.2':(1,[]),'1.3':(1,[]),
'1.4':(2,[L(q+'11.6','helpful','quality marks','low'),L(p+'2.b','helpful','using credit to pay','low')]),
'1.5':(1,[]),
'1.6':(1,[L(q+'3.b','helpful','advertising as a purchase factor'),L(q+'0.4','helpful','wants-driven decisions','low')]),
'2.b':(1,[]),'2.0':(1,[]),
'2.1':(1,[L(q+'2.0','helpful','what a brand is'),L(q+'3.b','helpful','national advertising')]),
'2.2':(1,[L(q+'2.1','helpful','branded goods comparison'),L(q+'3.b','helpful','national advertising cost','low')]),
'2.3':(1,[L(q+'2.0','essential','brand meaning')]),
'3.b':(1,[]),
'3.0':(1,[L(q+'2.3','helpful','brand loyalty')]),
'3.1':(1,[]),'3.2':(1,[]),'3.3':(1,[]),
'3.4':(1,[L(q+'2.0','helpful','brand identity','low')]),
'3.5':(1,[L(q+'1.6','helpful','impulse buying'),L(p+'2.b','helpful','use of credit','low')]),
'3.6':(1,[L(q+'1.6','helpful','impulse buying')]),
'3.7':(2,[]),
'4.b':(1,[]),'4.0':(1,[]),'4.1':(1,[]),
'4.2':(1,[L(q+'1.6','helpful','impulse buying')]),
'4.3':(1,[]),'4.4':(1,[]),'4.5':(1,[]),'4.6':(1,[]),
'5.b':(1,[]),'5.0':(1,[]),'5.1':(1,[]),
'5.2':(1,[L(q+'1.6','helpful','impulse buying')]),
'5.3':(1,[]),
'5.4':(1,[L(q+'6.b','helpful','loyalty schemes','low')]),
'5.5':(1,[]),
'6.b':(1,[]),'6.0':(1,[]),'6.1':(1,[]),'6.2':(1,[]),'6.3':(1,[]),'6.4':(1,[]),'6.5':(1,[]),
'7.b':(1,[L(p+'2.b','helpful','credit meaning')]),
'7.0':(1,[]),
'7.1':(1,[L(p+'3.b','helpful','hire purchase explained')]),
'7.2':(2,[L(p+'7.b','helpful','Consumer Credit Act 1995'),L(p+'4.3','helpful','APR meaning'),L(q+'7.1','helpful','hire purchase')]),
'7.3':(2,[L(q+'7.b','helpful','easy-pay as credit','low')]),
'7.4':(2,[L(p+'4.2','helpful','cost of credit above cash price')]),
'8.b':(1,[]),'8.0':(1,[]),'8.1':(1,[]),'8.2':(1,[]),'8.3':(1,[]),
'8.4':(1,[L(q+'8.b','helpful','buying without inspecting goods','low')]),
'9.b':(1,[]),'9.0':(1,[]),'9.1':(1,[]),'9.2':(2,[]),'9.3':(1,[]),
'9.4':(1,[L(q+'1.6','helpful','impulse buying')]),
'9.5':(1,[L(q+'3.b','helpful','targeted advertising','low')]),
'10.b':(1,[]),'10.0':(1,[]),'10.1':(1,[]),'10.2':(1,[]),'10.3':(1,[]),'10.4':(1,[]),
'11.b':(1,[]),'11.0':(2,[]),'11.1':(1,[]),'11.2':(1,[]),'11.3':(2,[]),'11.4':(1,[]),'11.5':(1,[]),'11.6':(1,[]),'11.7':(1,[]),
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
