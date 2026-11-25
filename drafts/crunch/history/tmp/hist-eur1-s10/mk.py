import json,re
H,E,h,l='helpful','essential','high','low'
P='hist-eur1-s10.'
S='hist-eur1-s10.'
D={
'0.b':(1,[('hist-eur1-s7.7.0',H,'overcrowding and disease in towns',h)]),
'0.0':(1,[('hist-eur1-s7.6.2',H,'migration into cities',h)]),
'0.1':(1,[]),
'0.2':(1,[('hist-eur1-s7.7.0',H,'poor sanitation and disease',h)]),
'0.3':(1,[]),
'0.4':(1,[('hist-eur1-s10.1.4',H,'barricade revolutions in Paris',h)]),
'0.5':(1,[]),
'1.0':(1,[('hist-eur1-s7.6.4',H,'Paris population growth',h)]),
'1.1':(1,[]),
'1.2':(1,[]),
'1.3':(1,[]),
'1.4':(1,[('hist-eur1-s6.2.4',H,'the June Days',h)]),
'2.0':(1,[('hist-eur1-s6.4.2',H,'Napoleon III',h)]),
'2.1':(1,[('hist-eur1-s10.2.0',H,'Napoleon III\'s modernising aims',h)]),
'2.2':(1,[('hist-eur1-s10.2.1',E,'Haussmann as Prefect',h)]),
'2.3':(1,[('hist-eur1-s10.2.1',H,'Haussmann\'s powers',h)]),
'2.4':(1,[('hist-eur1-s10.2.1',H,'Haussmann\'s Prefecture',h)]),
'2.5':(1,[('hist-eur1-s6.4.5',H,'1855 Paris Exposition',h)]),
'2.6':(1,[('hist-eur1-s10.2.0',H,'public works to cut unemployment',h)]),
'2.7':(1,[('hist-eur1-s10.2.0',H,'Napoleon III\'s plans for Paris',h)]),
'3.0':(1,[('hist-eur1-s10.2.1',H,'Haussmann directed the works',h)]),
'3.1':(2,[('hist-eur1-s10.3.0',H,'the grands travaux',h)]),
'3.2':(1,[('hist-eur1-s10.3.0',H,'the grands travaux',h)]),
'3.3':(1,[('hist-eur1-s10.3.0',H,'the new avenues',h)]),
'3.4':(1,[('hist-eur1-s10.0.4',H,'fear of barricade revolution',h)]),
'3.5':(2,[('hist-eur1-s10.3.0',H,'the new avenues',h),('hist-eur1-s10.5.0',H,'the Opera building',l)]),
'3.6':(1,[('hist-eur1-s10.3.3',H,'uniform facades',h)]),
'4.0':(1,[('hist-eur1-s10.0.2',H,'need for clean water',h)]),
'4.1':(1,[('hist-eur1-s10.4.0',H,'Belgrand',h)]),
'4.2':(1,[]),
'4.3':(1,[('hist-eur1-s10.4.2',H,'Bois de Boulogne counterpart',h)]),
'4.4':(1,[]),
'4.5':(1,[]),
'4.6':(1,[]),
'4.7':(1,[('hist-eur1-s10.4.0',H,'Belgrand\'s aqueducts',h)]),
'5.0':(1,[]),
'5.1':(1,[('hist-eur1-s10.1.1',H,'Les Halles district',l)]),
'5.2':(1,[('hist-eur1-s10.3.1',H,'boulevards linking stations',h)]),
'5.3':(1,[('hist-eur1-s10.3.3',H,'uniform street look',h)]),
'5.4':(1,[('hist-eur1-s10.3.3',H,'boulevard vistas',h)]),
'6.0':(1,[]),
'6.1':(1,[('hist-eur1-s10.6.0',E,'the 1860 annexation',h)]),
'6.2':(1,[('hist-eur1-s10.6.0',H,'the 1860 annexation',h)]),
'6.3':(1,[]),
'6.4':(1,[('hist-eur1-s10.6.3',E,'cost and borrowing',h)]),
'6.5':(1,[('hist-eur1-s6.5.5',H,'Ollivier\'s liberal ministry',h),('hist-eur1-s10.6.4',H,'criticism of Haussmann',h)]),
'6.6':(1,[('hist-eur1-s10.2.1',H,'Haussmann as Prefect',h)]),
'7.0':(1,[('hist-eur1-s10.3.0',H,'demolition for new avenues',h)]),
'7.1':(1,[('hist-eur1-s10.7.0',H,'displacement of the poor',h)]),
'7.2':(1,[('hist-eur1-s10.1.0',H,'wealthy west, poor east',h)]),
'7.3':(1,[('hist-eur1-s10.7.0',H,'displaced workers',h)]),
'7.4':(1,[('hist-eur1-s10.3.0',H,'the new boulevards',h)]),
'7.5':(2,[('hist-eur1-s10.3.4',H,'military value of boulevards',h),('hist-eur1-s6.8.3',E,'the Paris Commune',h)]),
'8.0':(1,[]),
'8.1':(1,[('hist-eur1-s10.8.0',E,'the Ringstrasse',h)]),
'8.2':(1,[]),
'8.3':(1,[('hist-eur1-s7.7.2',H,'Chadwick\'s sanitary report',h)]),
'8.4':(2,[('hist-eur1-s10.3.0',H,'Haussmann\'s works',h),('hist-eur1-s10.2.3',H,'expropriation powers',h)]),
'8.5':(2,[]),
'9.0':(1,[('hist-eur1-s10.4.1',H,'Belgrand\'s sewers',h)]),
'9.1':(1,[('hist-eur1-s10.3.0',H,'boulevards, parks, buildings',h)]),
'9.2':(1,[]),
'9.3':(1,[('hist-eur1-s10.7.0',H,'displacement of the poor',h)]),
'9.4':(1,[('hist-eur1-s10.6.3',H,'financing and debt',h),('hist-eur1-s10.6.5',H,'Haussmann\'s dismissal',h)]),
'9.5':(2,[('hist-eur1-s10.9.1',H,'success as planning model',h),('hist-eur1-s10.9.3',H,'displacement of the poor',h)]),
}
pk='/Users/gabrielwhelan/barebones/drafts/crunch/history/packs/hist-eur1-s10.t1g1.txt'
out='/Users/gabrielwhelan/barebones/drafts/crunch/history/point-links/hist-eur1-s10.t1g1.json'
txt=open(pk).read()
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
tgt=re.findall(r'^\[([^\]]+)\]',txt.split('CANDIDATES')[0],re.M)
assert set(P+k for k in D)==set(tgt) and len(tgt)==len(D)==len(set(tgt)),(set(tgt)^set(P+k for k in D))
R={}
for t in tgt:
    c,n=D[t[len(P):]]
    for x in n: assert x[0] in allids and x[0]!=t,(t,x)
    R[t]={'cost':c,'needs':[{'id':a,'strength':b,'why':w,'confidence':f} for a,b,w,f in n]}
json.dump(R,open(out,'w'),indent=1,ensure_ascii=False)
v=R.values()
print(len(R),sum(len(x['needs']) for x in v),sum(x['cost']==2 for x in v),sum(n['confidence']=='low' for x in v for n in x['needs']))
