import json,re,sys
B='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
P='hom-cooking-methods-s3.t1g1'
s2='hom-cooking-methods-s2.';s1='hom-cooking-methods-s1.';m2='hom-meal-planning-s2.';s3='hom-cooking-methods-s3.'
H,E='helpful','essential'
D={
'0.b':(1,[]),
'0.0':(2,[]),
'0.1':(1,[(s2+'1.3',H,'food type governs cooking method','high')]),
'0.2':(1,[(s1+'5.0',H,'water-soluble vitamins dissolve in water','high')]),
'0.3':(1,[(s1+'4.2',H,'dry heat browns surfaces','low')]),
'0.4':(1,[]),
'0.5':(1,[(m2+'4.6',H,'older people chewing and swallowing difficulties','high')]),
'0.6':(1,[(s3+'1.7',H,'pressure cooking shortens time','high')]),
'0.7':(1,[(s2+'6.0',H,'tough cuts need long moist cooking','high')]),
'1.b':(1,[]),
'1.0':(2,[(s1+'5.0',H,'vitamins leach into water','high')]),
'1.1':(1,[]),
'1.2':(1,[]),
'1.3':(1,[(s1+'5.0',H,'nutrients lost into cooking water','low')]),
'1.4':(2,[(s2+'3.3',H,'steam carries heat to food','low')]),
'1.5':(1,[]),
'1.6':(2,[]),
'1.7':(1,[]),
'2.b':(1,[]),
'2.0':(1,[(s2+'5.0',H,'roasting uses conduction and convection','high')]),
'2.1':(2,[(s2+'3.b',H,'convection heat transfer','high')]),
'2.2':(2,[(s2+'4.b',H,'radiant heat','high')]),
'2.3':(1,[(s3+'2.2',E,'barbecuing is outdoor grilling','high')]),
'2.4':(1,[]),
'3.b':(1,[]),
'3.0':(1,[]),
'3.1':(1,[]),
'3.2':(1,[(s2+'1.1',H,'thickness governs cooking time','high')]),
'3.3':(1,[]),
'3.4':(1,[]),
'3.5':(1,[]),
'4.b':(1,[]),
'4.0':(1,[]),
'4.1':(1,[(s2+'3.2',H,'convection in hot oil','low')]),
'4.2':(1,[(s1+'5.1',H,'vitamin C destroyed by heat','low')]),
'4.3':(1,[]),
'4.4':(1,[]),
'5.b':(1,[]),
'5.0':(1,[]),
'5.1':(1,[(s1+'4.0',H,'browning reactions need heat','low')]),
'5.2':(1,[]),
'6.b':(1,[]),
'6.0':(2,[(s3+'2.1',H,'baking method','high')]),
'6.1':(2,[(s3+'2.2',H,'grilling method','high')]),
'6.2':(2,[(s3+'1.4',H,'steaming method','high')]),
'6.3':(2,[]),
'6.4':(2,[]),
'7.b':(1,[(s3+'1.4',E,'steaming method','high')]),
'7.0':(1,[]),
'7.1':(1,[(m2+'4.6',H,'older people chewing difficulties','high')]),
'7.2':(1,[(s1+'5.0',H,'water-soluble vitamins lost in water','high')]),
'7.3':(1,[]),
'7.4':(1,[]),
'7.5':(1,[(m2+'4.5',H,'older people reduce salt','low')]),
}
txt=open(B+'packs/'+P+'.txt').read()
tg=re.findall(r'^\[(\S+?)\]',txt.split('CANDIDATES')[0],re.M)
allids=set(re.findall(r'^\[(\S+?)\]',txt,re.M))
assert [s3+k for k in D]==tg,(set(tg)^{s3+k for k in D})
out={}
for k,(c,n) in D.items():
    for x in n: assert x[0] in allids and x[0]!=s3+k,x
    out[s3+k]={'cost':c,'needs':[{'id':a,'strength':b,'why':w,'confidence':f} for a,b,w,f in n]}
json.dump(out,open(B+'point-links/'+P+'.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
