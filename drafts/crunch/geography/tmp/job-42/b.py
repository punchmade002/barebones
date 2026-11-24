import json,re
P='geo-option-atmosphere-ocean-s5.'
D='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
# explicit target list: section -> last bullet index (each also has .b)
secs={0:4,1:4,2:6,3:1,4:3,5:3,6:5,7:3,8:3,9:5,10:5,11:3,12:5,13:3,14:5,15:5,16:2,17:5,18:1}
ids=[]
for s,n in secs.items():
    ids.append(f'{s}.b'); ids+= [f'{s}.{i}' for i in range(n+1)]
cost2={'0.3','1.1','2.2','2.5','5.2','5.3','6.0','8.0','9.2','10.3','11.0','12.2','12.3','14.0','15.3','16.0','17.0','17.5'}
def L(i,s,w,c='high'):return {"id":i,"strength":s,"why":w,"confidence":c}
S2='geo-option-atmosphere-ocean-s2.';S4='geo-option-atmosphere-ocean-s4.';S3='geo-option-atmosphere-ocean-s3.'
p1={'0.2':[L(S2+'11.0','helpful','latitude controls temperature')],
'0.3':[L(S2+'0.2','helpful','insolation'),L(S2+'12.0','helpful','continentality')],
'1.2':[L(S2+'9.1','essential','overhead sun at equinoxes')],
'1.3':[L(S2+'10.1','helpful','cloud reflects insolation')],
'2.1':[L(P+'1.4','helpful','ITCZ defined there')],
'2.3':[L(P+'1.4','essential','ITCZ and trade winds')],
'2.5':[L(P+'2.2','helpful','convectional rain process')],
'2.6':[L(P+'1.2','helpful','steady heat input all year')],
'10.1':[L(S2+'13.0','helpful','North Atlantic Drift')],
'10.2':[L(S2+'12.0','helpful','sea heats and cools slowly')],
'10.5':[L(P+'14.b','helpful','continental climate')],
'11.3':[L(S2+'12.0','helpful','continentality moderates coasts')],
'12.4':[L(S2+'13.1','helpful','cold currents lower temperatures')],
'14.4':[L(S2+'12.3','helpful','Verkhoyansk annual range')],
'15.1':[L(P+'2.b','helpful','convection explained')],
'15.2':[L(S2+'12.0','helpful','land heats and cools quickly')],
'17.3':[L(S2+'13.1','helpful','cold currents chill air')],
'18.0':[L(S2+'11.0','helpful','latitude and temperature')],
'18.1':[L(S2+'12.1','helpful','continentality and annual range')]}
p2={'0.3':[L(S4+'3.b','helpful','pressure belts'),L(S4+'9.b','helpful','air masses')],
'1.4':[L(S4+'3.0','helpful','ITCZ / equatorial low')],
'2.3':[L(S4+'4.0','helpful','trade winds')],
'5.1':[L(S4+'6.0','essential','ITCZ moves north in summer')],
'5.2':[L(S4+'0.2','helpful','Coriolis deflection')],
'5.3':[L(S4+'7.0','helpful','jet stream')],
'7.1':[L(S4+'38.b','helpful','tropical cyclones')],
'8.b':[L(S4+'4.1','helpful','westerlies')],
'9.2':[L(S4+'17.0','helpful','depression structure')],
'9.3':[L(S4+'17.b','helpful','depressions')],
'9.4':[L(S4+'21.0','helpful','anticyclone')],
'10.0':[L(S4+'4.1','helpful','south-westerly westerlies')],
'10.3':[L(S4+'18.0','essential','polar front depressions'),L(S4+'7.2','helpful','jet stream steers depressions')],
'10.4':[L(S4+'9.b','helpful','air masses')],
'12.2':[L(S4+'6.2','essential','summer subtropical high shift')],
'12.3':[L(S4+'6.0','essential','seasonal shift of pressure belts')],
'12.4':[L(S4+'13.1','helpful','cold eastern-boundary currents')],
'12.5':[L(S4+'32.0','helpful','mistral and bora')],
'15.3':[L(S4+'4.1','helpful','westerlies')],
'15.4':[L(S4+'21.4','essential','thermal anticyclone')],
'17.0':[L(S4+'3.1','essential','subtropical high pressure')],
'17.5':[L(S4+'13.1','helpful','cold eastern-boundary currents')]}
p3={'1.4':[L(S3+'15.1','helpful','convection')],
'2.2':[L(S3+'27.b','essential','convectional rain process')],
'2.3':[L(S3+'30.0','helpful','convergence rainfall')],
'2.4':[L(S3+'6.1','helpful','relative humidity')],
'2.5':[L(S3+'20.1','helpful','cumulonimbus cloud')],
'6.0':[L(S3+'28.b','helpful','relief rain')],
'6.1':[L(S3+'28.2','helpful','rain shadow')],
'9.2':[L(S3+'29.b','essential','frontal rain')],
'15.1':[L(S3+'27.b','helpful','convectional rain')],
'17.2':[L(S3+'7.1','helpful','low humidity, large daily range')],
'17.3':[L(S3+'11.2','helpful','advection cooling forms fog')]}
for k in list(p1)+list(p2)+list(p3): assert k in ids,k
assert cost2<=set(ids) and len(ids)==len(set(ids))
def out(n,pl,withcost):
    d={}
    for i in ids:
        e={}
        if withcost:e['cost']=2 if i in cost2 else 1
        e['needs']=pl.get(i,[])
        d[P+i]=e
    json.dump(d,open(f'{D}point-links/geo-option-atmosphere-ocean-s5.t1g{n}.json','w'),indent=1)
    # check
    txt=open(f'{D}packs/geo-option-atmosphere-ocean-s5.t1g{n}.txt').read()
    allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    tg=[re.match(r'\[([^\]]+)\]',l).group(1) for l in txt.split('CANDIDATES')[0].splitlines() if l.startswith('[')]
    assert tg==list(d),n
    links=[x for v in d.values() for x in v['needs']]
    assert all(x['id'] in allids for x in links)
    print(n,len(d),len(links),sum(v.get('cost')==2 for v in d.values()),sum(x['confidence']=='low' for x in links))
out(1,p1,True);out(2,p2,False);out(3,p3,False)
