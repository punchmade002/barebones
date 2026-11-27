import json,re
B='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
name='hom-carbohydrates-s5.t1g1'
H,E='helpful','essential'
T='hom-carbohydrates-s5.';C4='hom-carbohydrates-s4.';C2='hom-carbohydrates-s2.';DG='hom-digestion-metabolism-s2.'
D={
'0.b':(1,[]),
'0.0':(1,[]),
'0.1':(1,[]),
'0.2':(1,[]),
'0.3':(1,[(C2+'3.5',H,'glycogen as glucose polymer','high')]),
'0.4':(1,[(T+'0.3',E,'uses full glycogen stores','high')]),
'0.5':(1,[(DG+'0.1',H,'starch broken to glucose','high')]),
'0.6':(1,[(T+'0.5',H,'starch gives energy slowly','high')]),
'1.b':(1,[(C4+'3.4',H,'cellulose not digested','high')]),
'1.0':(1,[]),
'1.1':(1,[(T+'1.0',H,'fibre bulk','high')]),
'1.2':(1,[(T+'1.1',H,'peristalsis moves waste','high')]),
'1.3':(2,[]),
'1.4':(1,[]),
'1.5':(1,[]),
'1.6':(1,[]),
'1.7':(2,[(T+'1.5',H,'soluble fibre','high'),(T+'1.1',H,'insoluble fibre speeds waste','high')]),
'2.b':(1,[]),
'2.0':(1,[]),
'2.1':(1,[(T+'1.1',H,'peristalsis','high')]),
'2.2':(1,[(T+'2.0',H,'constipation','high')]),
'2.3':(1,[(T+'2.1',H,'cause of constipation','high')]),
'2.4':(1,[(T+'1.3',H,'bowel conditions and low fibre','high')]),
'2.5':(2,[]),
'3.b':(1,[]),
'3.0':(1,[]),
'3.1':(1,[]),
'3.2':(1,[]),
'3.3':(2,[(C4+'4.4',H,'Maillard reaction','high'),(C4+'7.0',H,'caramelisation','high')]),
'3.4':(1,[(C4+'7.3',H,'controlled crystallisation','high')]),
'3.5':(1,[]),
'3.6':(1,[]),
'3.7':(1,[(C4+'1.6',H,'hygroscopic sugar','high')]),
'4.b':(1,[]),
'4.0':(1,[(C4+'1.0',H,'gelatinisation','high')]),
'4.1':(1,[(C4+'1.4',H,'roux','high')]),
'4.2':(1,[]),
'4.3':(2,[(C4+'1.0',H,'gelatinisation','high')]),
'4.4':(1,[(C4+'7.5',H,'dextrinisation','high')]),
'4.5':(1,[(C4+'8.3',H,'pectin, sugar, acid gel','high')]),
'4.6':(2,[(T+'4.5',H,'pectin as gelling agent','high')]),
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
