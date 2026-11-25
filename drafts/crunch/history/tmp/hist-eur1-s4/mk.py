import json,re
H,E,h,l='helpful','essential','high','low'
P='hist-eur1-s4.'
D={
'0.b':(1,[('hist-eur1-s1.0.4',H,'Austria dominant in Italy',h)]),
'0.0':(1,[('hist-eur1-s1.0.3',H,'Piedmont-Sardinia strengthened in 1815',h)]),
'0.1':(1,[('hist-eur1-s1.0.4',H,'Austria gained Lombardy-Venetia',h)]),
'0.2':(1,[('hist-eur1-s1.0.8',H,'Papal States restored',h)]),
'0.3':(1,[('hist-eur1-s1.0.2',H,'Bourbons restored to Naples',h)]),
'0.4':(1,[]),
'0.5':(1,[('hist-eur1-s4.0.4',E,'uses the Carbonari',h),('hist-eur1-s1.2.4',H,'Austrian troops crushed Naples, Piedmont',h)]),
'0.6':(1,[('hist-eur1-s1.4.8',H,'same 1831 risings',h)]),
'0.7':(1,[]),
'1.b':(1,[]),
'1.0':(1,[('hist-eur1-s4.0.4',H,'uses the Carbonari',h)]),
'1.1':(1,[('hist-eur1-s4.1.0',H,'Mazzini and his exile',h)]),
'1.2':(2,[('hist-eur1-s4.1.1',H,'Young Italy',h)]),
'1.3':(1,[('hist-eur1-s4.1.1',H,'Young Italy',h)]),
'1.4':(1,[]),
'1.5':(1,[('hist-eur1-s4.2.4',H,'the Roman Republic of 1849',h)]),
'1.6':(1,[('hist-eur1-s4.1.1',H,'Young Italy conspiracies',l)]),
'1.7':(1,[('hist-eur1-s4.3.2',H,'Cavour',h)]),
'1.8':(2,[('hist-eur1-s4.5.4',H,'the Kingdom of Italy of 1861',h)]),
'1.9':(1,[]),
'1.10':(1,[('hist-eur1-s4.1.1',H,'Young Italy',h)]),
'2.0':(2,[('hist-eur1-s6.2.0',H,'February 1848 revolution in Paris',h)]),
'2.1':(1,[('hist-eur1-s4.2.0',H,'Milan rising of 1848',h)]),
'2.2':(2,[('hist-eur1-s4.2.0',H,'1848 revolutions against Austria',h)]),
'2.3':(2,[('hist-eur1-s4.2.2',H,'the war against Austria',h),('hist-eur1-s4.2.0',H,'Pius IX granting constitution',l)]),
'2.4':(2,[('hist-eur1-s4.2.3',H,'Pope fled Rome',h),('hist-eur1-s4.1.b',H,'Mazzini',h)]),
'2.5':(1,[('hist-eur1-s4.2.0',H,'Venice rising of 1848',h)]),
'2.6':(1,[('hist-eur1-s4.2.2',E,'Charles Albert and the war',h)]),
'2.7':(1,[('hist-eur1-s4.2.4',E,'captured the Roman Republic',h),('hist-eur1-s6.3.1',H,'Louis-Napoleon as president',h)]),
'3.0':(1,[('hist-eur1-s4.2.2',H,'Charles Albert in 1848',h)]),
'3.1':(1,[('hist-eur1-s4.0.2',H,'Papal States clerical control',h)]),
'3.2':(2,[('hist-eur1-s4.0.0',H,'Piedmont-Sardinia',h)]),
'3.3':(1,[('hist-eur1-s4.3.2',E,'Cavour',h),('hist-eur1-s6.5.2',H,'the Crimean War',l)]),
'3.4':(1,[('hist-eur1-s4.3.3',E,'Congress of Paris seat',h)]),
'3.5':(2,[('hist-eur1-s4.3.2',E,'Cavour',h),('hist-eur1-s6.4.2',H,'Napoleon III',h)]),
'3.6':(1,[('hist-eur1-s4.3.5',E,'Nice and Savoy deal',h),('hist-eur1-s4.2.4',H,'Garibaldi',l)]),
'3.7':(1,[('hist-eur1-s4.1.b',H,'Mazzini\'s republicanism',h)]),
'4.0':(1,[('hist-eur1-s4.3.5',E,'Plombieres agreement',h)]),
'4.1':(2,[('hist-eur1-s4.4.0',E,'the 1859 war',h)]),
'4.2':(2,[('hist-eur1-s4.4.1',H,'the 1859 battles',h),('hist-eur1-s4.3.5',H,'Cavour\'s French alliance',h)]),
'4.3':(1,[('hist-eur1-s4.4.2',H,'Villafranca terms',h)]),
'4.4':(1,[('hist-eur1-s4.3.5',H,'Nice and Savoy bargain',h)]),
'4.5':(1,[('hist-eur1-s4.3.5',H,'Nice and Savoy bargain',h)]),
'5.0':(1,[('hist-eur1-s4.2.4',H,'Garibaldi',h)]),
'5.1':(1,[('hist-eur1-s4.5.0',E,'the Thousand',h),('hist-eur1-s4.0.3',H,'Two Sicilies',h)]),
'5.2':(1,[('hist-eur1-s4.5.1',H,'Sicily campaign',h),('hist-eur1-s4.0.3',H,'Bourbon Two Sicilies',h)]),
'5.3':(2,[('hist-eur1-s4.5.2',H,'Garibaldi in Naples',h),('hist-eur1-s4.0.2',H,'Papal States',h)]),
'5.4':(1,[('hist-eur1-s4.5.3',H,'annexations to Victor Emmanuel',h)]),
'5.5':(1,[('hist-eur1-s4.3.2',E,'Cavour',h),('hist-eur1-s4.5.4',H,'1861 proclamation',h)]),
'5.6':(1,[('hist-eur1-s4.2.7',H,'French garrison in Rome',h)]),
'6.0':(1,[('hist-eur1-s4.4.2',H,'Austria kept Venetia',h)]),
'6.1':(1,[('hist-eur1-s4.6.0',E,'the 1866 war',h),('hist-eur1-s4.4.3',H,'Austria kept Venetia',h)]),
'6.2':(1,[('hist-eur1-s4.2.7',H,'French garrison in Rome',h)]),
'6.3':(1,[('hist-eur1-s4.6.2',H,'garrison withdrawn',h)]),
'6.4':(2,[('hist-eur1-s4.6.3',H,'Rome annexed',h),('hist-eur1-s4.0.2',H,'the Pope\'s rule',h)]),
'7.0':(1,[('hist-eur1-s4.2.1',H,'the Quadrilateral',h),('hist-eur1-s4.6.1',H,'Venetia gained 1866',h)]),
'7.1':(1,[('hist-eur1-s4.2.7',E,'French garrison in Rome',h)]),
'7.2':(1,[]),
'7.3':(1,[('hist-eur1-s4.1.b',H,'Mazzini republicanism',h),('hist-eur1-s4.3.2',H,'Cavour',h)]),
'7.4':(1,[('hist-eur1-s4.3.0',H,'Piedmont constitution',h),('hist-eur1-s4.3.2',H,'Cavour\'s modernisation',h)]),
'7.5':(1,[('hist-eur1-s4.3.5',E,'Plombieres French support',h),('hist-eur1-s4.3.3',E,'Crimean War place',h)]),
'7.6':(1,[('hist-eur1-s4.5.1',H,'Thousand in Sicily',h)]),
'8.0':(1,[('hist-eur1-s4.6.3',H,'Rome annexed 1870',h)]),
'8.1':(1,[('hist-eur1-s4.5.4',H,'Kingdom of Italy 1861',h)]),
'8.2':(1,[('hist-eur1-s4.7.4',H,'Piedmontese model',h)]),
'8.3':(1,[('hist-eur1-s4.5.5',H,'aftermath of unification',l)]),
'8.4':(2,[('hist-eur1-s4.3.2',H,'Cavour',h),('hist-eur1-s4.5.3',H,'Garibaldi and Cavour',h)]),
'8.5':(2,[('hist-eur1-s4.7.5',H,'Piedmontese diplomacy',h),('hist-eur1-s4.7.6',H,'Garibaldi\'s volunteers',h),('hist-eur1-s4.1.8',H,'Mazzini rejected 1861',h)]),
}
pk='/Users/gabrielwhelan/barebones/drafts/crunch/history/packs/hist-eur1-s4.t1g1.txt'
out='/Users/gabrielwhelan/barebones/drafts/crunch/history/point-links/hist-eur1-s4.t1g1.json'
txt=open(pk).read()
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
tgt=re.findall(r'^\[([^\]]+)\]',txt.split('CANDIDATES')[0],re.M)
assert set(P+k for k in D)==set(tgt) and len(tgt)==len(D)==len(set(tgt))
R={}
for t in tgt:
    c,n=D[t[len(P):]]
    for x in n: assert x[0] in allids and x[0]!=t,(t,x)
    R[t]={'cost':c,'needs':[{'id':a,'strength':b,'why':w,'confidence':f} for a,b,w,f in n]}
json.dump(R,open(out,'w'),indent=1,ensure_ascii=False)
v=R.values()
print(len(R),sum(len(x['needs']) for x in v),sum(x['cost']==2 for x in v),sum(n['confidence']=='low' for x in v for n in x['needs']))
