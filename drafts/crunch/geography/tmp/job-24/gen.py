import json,re
P='geo-economic-globalisation-s2'
A='geo-economic-activities-s2'
S1='geo-economic-globalisation-s1'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
E=[]
T={ # id suffix: (cost, links)
'0.b':(1,[]),
'0.0':(1,[L(A+'.3.4','helpful','air freight of light goods')]),
'0.1':(1,[]),
'0.2':(1,[L(S1+'.0.1','helpful','headquarters and branch structure')]),
'0.3':(1,[L(S1+'.2.2','helpful','EU single market')]),
'0.4':(1,[L(A+'.4.1','helpful','IDA grants')]),
'0.5':(1,[L(S1+'.0.2','helpful','plants compete for investment')]),
'1.b':(1,[]),
'1.0':(1,[]),
'1.1':(1,[L(A+'.4.1','helpful','grants as location factor','low')]),
'1.2':(1,[L(S1+'.2.2','helpful','single market without tariffs','low')]),
'1.3':(1,[L(A+'.3.0','helpful','market access as location factor','low')]),
'1.4':(1,[L(A+'.2.2','helpful','labour skills as location factor','low')]),
'1.5':(1,[L(S1+'.4.0','helpful','Intel arrival at Leixlip')]),
'1.6':(1,[L(P+'.6.0','helpful','Dell 2009 move to Poland')]),
'2.b':(1,[]),
'2.0':(1,[L(P+'.1.2','helpful','tariffs and trade blocs')]),
'2.1':(2,[]),
'2.2':(1,[L(S1+'.16.1','helpful','India iPhone assembly')]),
'2.3':(2,[L(S1+'.4.2','helpful','Fab 34 at Leixlip')]),
'3.b':(1,[]),
'3.0':(1,[]),
'3.1':(1,[]),
'3.2':(1,[]),
'4.b':(1,[]),
'4.0':(2,[L(P+'.1.2','helpful','trade bloc strategy')]),
'4.1':(1,[]),
'4.2':(1,[]),
'4.3':(1,[]),
'4.4':(1,[]),
'5.b':(1,[]),'5.0':(1,[]),'5.1':(1,[]),'5.2':(1,[]),'5.3':(1,[]),
'6.b':(1,[L(P+'.5.2','helpful','Dell in Limerick')]),
'6.0':(1,[L(P+'.5.2','helpful','Dell in Limerick')]),
'6.1':(1,[L(P+'.1.0','helpful','labour and land costs')]),
'6.2':(1,[]),'6.3':(1,[]),'6.4':(1,[]),'6.5':(1,[]),
'7.b':(1,[L(S1+'.3.0','helpful','Intel company background')]),
'7.0':(1,[]),
'7.1':(2,[L(S1+'.4.4','helpful','Fab 34 joint venture','low')]),
'7.2':(1,[]),
'7.3':(1,[L(P+'.4.1','essential','CHIPS Act subsidy')]),
'8.b':(2,[]),
'8.0':(1,[]),
'8.1':(1,[L(S1+'.0.1','helpful','core and headquarters R&D')]),
'8.2':(2,[L(P+'.8.1','helpful','core versus other countries')]),
'8.3':(1,[]),
'9.b':(1,[L(P+'.8.2','essential','maturity stage relocation')]),
'9.0':(1,[L(P+'.8.2','essential','maturity stage standardisation')]),
'9.1':(1,[L(P+'.6.0','helpful','Dell move to Poland')]),
'9.2':(1,[L(P+'.8.2','essential','mature-stage pattern')]),
'10.b':(1,[]),'10.0':(1,[]),
'10.1':(2,[L(S1+'.3.3','helpful','Hillsboro development fab')]),
'10.2':(1,[]),
'10.3':(1,[L(S1+'.4.3','essential','Fab 34 Intel 4 and 3')]),
'10.4':(2,[L(S1+'.10.0','helpful','Nvidia and rivals')]),
'11.b':(1,[L(P+'.8.b','helpful','product life cycle','low')]),
'11.0':(1,[L(S1+'.3.3','helpful','what a fab is')]),
'11.1':(1,[L(P+'.0.2','helpful','ICT lets HQ direct branches')]),
'11.2':(1,[]),
'11.3':(1,[L(P+'.5.1','essential','Dell direct model')]),
'11.4':(1,[L(S1+'.9.1','helpful','cloud computing server makers','low')]),
'11.5':(1,[]),
'12.b':(1,[]),
'12.0':(2,[L(S1+'.1.0','helpful','IDA Ireland role')]),
'12.1':(1,[L(S1+'.13.2','helpful','AppleCare in Cork')]),
'12.2':(1,[L(S1+'.1.2','helpful','Microsoft in Ireland')]),
'12.3':(1,[L(P+'.12.b','helpful','teleservices meaning')]),
'13.b':(1,[]),
'13.0':(1,[L(S1+'.1.2','helpful','Google Dublin headquarters','low')]),
'13.1':(1,[L(S1+'.1.2','helpful','Meta Dublin headquarters','low')]),
'13.2':(1,[]),
'14.b':(1,[]),'14.0':(1,[]),'14.1':(1,[]),'14.2':(1,[]),
'14.3':(1,[L(P+'.14.1','helpful','data centre share of electricity')]),
'15.b':(1,[]),'15.0':(1,[]),'15.1':(1,[]),'15.2':(1,[]),
'15.3':(1,[L(P+'.5.1','essential','Dell direct online model')]),
'15.4':(1,[]),
'16.b':(1,[]),'16.0':(1,[]),'16.1':(1,[]),
'16.2':(1,[L(P+'.4.4','essential','reshoring defined')]),
'16.3':(2,[L(S1+'.2.0','essential','15% minimum tax rate')]),
}
txt=open('/Users/gabrielwhelan/barebones/drafts/crunch/geography/packs/geo-economic-globalisation-s2.t1g1.txt').read()
ids=re.findall(r'^\[([^\]]+)\]',txt,re.M)
tg=[i for i in ids if i.startswith(P+'.')]
assert [P+'.'+k for k in T]==tg,(set(tg)^{P+'.'+k for k in T})
out={}
for k,(c,n) in T.items():
    for x in n:
        assert x['id'] in ids and x['id']!=P+'.'+k,(k,x)
    out[P+'.'+k]={"cost":c,"needs":n}
json.dump(out,open('/Users/gabrielwhelan/barebones/drafts/crunch/geography/point-links/geo-economic-globalisation-s2.t1g1.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
