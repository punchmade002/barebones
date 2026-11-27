import json,re
B='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
name='hom-consumer-rights-s2.t1g1'
H,E='helpful','essential'
T='hom-consumer-rights-s2.';S1='hom-consumer-rights-s1.';PF='hom-personal-finance-s3.'
D={
'0.b':(1,[]),
'0.0':(2,[]),
'0.1':(1,[]),
'0.2':(2,[]),
'0.3':(2,[]),
'0.4':(2,[(S1+'5.5',H,'discount stores lower cost','low')]),
'0.5':(2,[(S1+'9.b',H,'online shopping','low')]),
'0.6':(1,[]),
'0.7':(1,[(T+'0.0',H,'independent retailer','high'),(T+'0.1',H,'chain store','high')]),
'1.b':(1,[]),
'1.0':(1,[]),
'1.1':(1,[]),
'1.2':(1,[]),
'1.3':(1,[]),
'1.4':(1,[]),
'1.5':(1,[]),
'2.b':(1,[]),
'2.0':(1,[]),
'2.1':(1,[(S1+'5.2',H,'was/now reduction labels','low')]),
'2.2':(1,[(S1+'4.5',H,'in-store stimuli','high')]),
'2.3':(1,[(S1+'2.0',H,'brand','high')]),
'2.4':(1,[]),
'2.5':(1,[]),
'2.6':(1,[]),
'2.7':(1,[(S1+'0.4',H,'needs versus wants','high')]),
'3.b':(1,[]),
'3.0':(1,[]),
'3.1':(1,[]),
'3.2':(1,[]),
'3.3':(1,[(S1+'9.b',H,'online shopping','high')]),
'3.4':(1,[(S1+'6.4',H,'loyalty card data','high')]),
'3.5':(1,[]),
'3.6':(2,[]),
'4.b':(1,[(PF+'1.b',H,'criteria for payment methods','high')]),
'4.0':(1,[]),
'4.1':(1,[]),
'4.2':(1,[]),
'4.3':(1,[]),
'5.b':(1,[]),
'5.0':(1,[]),
'5.1':(1,[]),
'5.2':(1,[(T+'5.1',H,'desk research','high')]),
'5.3':(1,[(T+'5.1',H,'desk research','high')]),
'5.4':(2,[]),
'5.5':(1,[(T+'5.4',H,'field research','high')]),
'5.6':(1,[]),
'5.7':(1,[]),
'5.8':(1,[(S1+'6.4',H,'loyalty card data','high')]),
'6.b':(1,[(T+'5.b',H,'consumer research','high')]),
'6.0':(1,[]),
'6.1':(1,[]),
'6.2':(1,[]),
'6.3':(1,[]),
}
out={T+k:{'cost':c,'needs':[{'id':i,'strength':s,'why':w,'confidence':f} for i,s,w,f in n]} for k,(c,n) in D.items()}
pk=open(B+'packs/'+name+'.txt').read()
tg=re.findall(r'^\[(\S+)\]',pk.split('CANDIDATES')[0],re.M)
allid=set(re.findall(r'^\[(\S+)\]',pk,re.M))
assert list(out)==tg,(set(tg)^set(out))
for k,v in out.items():
    for n in v['needs']: assert n['id'] in allid and n['id']!=k,(k,n)
json.dump(out,open(B+'point-links/'+name+'.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
