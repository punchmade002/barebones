import json,re
B='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
P='hom-social-change-s5.t1g1'
t='hom-social-change-s5.';w2='hom-work-leisure-s2.';w5='hom-work-leisure-s5.';f1='hom-family-caring-s1.'
H,E='helpful','essential'
D={
'0.b':(1,[]),
'0.0':(1,[]),
'0.1':(1,[]),
'0.2':(1,[]),
'0.3':(1,[]),
'0.4':(2,[(w2+'3.1',H,'marriage bar removed in 1973','high')]),
'0.5':(1,[]),
'0.6':(2,[(w2+'5.b',H,'flexible working arrangements','high')]),
'0.7':(2,[(w2+'1.2',H,'tertiary service sector growth','low')]),
'1.b':(1,[]),
'1.0':(1,[]),
'1.1':(1,[]),
'1.2':(1,[]),
'1.3':(1,[(w5+'1.0',H,'role overload','high')]),
'1.4':(1,[]),
'1.5':(1,[]),
'1.6':(1,[]),
'2.b':(1,[]),
'2.0':(2,[]),
'2.1':(1,[(t+'2.b',H,'Employment Equality Acts','high')]),
'2.2':(1,[(t+'2.0',H,'nine grounds of discrimination','low')]),
'2.3':(1,[]),
'2.4':(1,[(t+'2.0',H,'family status ground','high')]),
'2.5':(2,[(w2+'5.7',H,'maternity leave law','high')]),
'2.6':(1,[(t+'2.5',H,'maternity leave protection','high')]),
'2.7':(1,[]),
'3.b':(1,[(t+'2.b',H,'Employment Equality Acts','high')]),
'3.0':(1,[]),
'3.1':(1,[(t+'2.b',H,'Employment Equality Acts cover employment','low')]),
'4.b':(1,[]),
'4.0':(1,[]),
'4.1':(1,[(t+'3.0',H,'gender pay gap reporting','low')]),
'4.2':(1,[]),
'4.3':(1,[]),
'4.4':(1,[(f1+'3.1',H,'women do double shift of housework','low')]),
'5.b':(1,[]),
'5.0':(1,[(t+'0.4',H,'marriage bar','high')]),
'5.1':(1,[]),
}
txt=open(B+'packs/'+P+'.txt').read()
tg=re.findall(r'^\[(\S+?)\]',txt.split('CANDIDATES')[0],re.M)
allids=set(re.findall(r'^\[(\S+?)\]',txt,re.M))
assert [t+k for k in D]==tg,(set(tg)^{t+k for k in D})
out={}
for k,(c,n) in D.items():
    for x in n: assert x[0] in allids and x[0]!=t+k,x
    out[t+k]={'cost':c,'needs':[{'id':a,'strength':b,'why':w,'confidence':f} for a,b,w,f in n]}
json.dump(out,open(B+'point-links/'+P+'.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
