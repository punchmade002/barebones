import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
txt=open(P+'packs/geo-economic-eu-s2.t1g1.txt').read()
ids=re.findall(r'^\[([^\]]+)\]',txt,re.M)
tg=[i for i in ids if i.startswith('geo-economic-eu-s2.')]
c2={'3.0','3.2','5.2','6.1','9.3','11.2','13.2','14.0','16.2','16.4'}
S='geo-economic-eu-s2.';E='geo-economic-eu-s1.';A='geo-economic-activities-s1.'
L={ # id: [(target,strength,why,conf)]
'0.2':[(A+'2.1','helpful','high tariffs as protection','high')],
'2.0':[(S+'0.0','helpful','uses 1960 UK export share','high')],
'2.1':[(S+'2.0','helpful','UK share of exports','high')],
'2.2.1':[(S+'2.0','helpful','falling UK share','high')],
'3.2':[(E+'2.2','helpful','surplus and balance of trade','high')],
'4.1':[(S+'4.0','helpful','uses export total','high')],
'5.0':[(E+'0.b','helpful','trading bloc idea','low')],
'5.2':[(E+'5.2','helpful','Rotterdam effect, Netherlands','low')],
'6.0':[(S+'5.0','helpful','compares with export bloc','low')],
'7.0':[(S+'4.0','helpful','share of goods exports','high')],
'8.1':[(S+'10.1','helpful','aircraft leasing industry','low')],
'9.0':[(S+'4.0','helpful','compares with 2024 exports','high')],
'9.1':[(S+'7.0','essential','pharma export share 2024','high')],
'9.2':[(S+'5.1','helpful','USA share of exports','high')],
'9.3':[(E+'13.0','essential','EU-USA deal and 15% cap','high')],
'9.4':[(S+'9.1','helpful','dependence on pharmaceuticals','high')],
'10.0':[(A+'25.1','helpful','Google, Microsoft in Dublin','high')],
'10.1':[(A+'32.0','helpful','IFSC origin and role','high')],
'10.2':[(S+'10.0','helpful','services sold by multinationals','low')],
'11.0':[(A+'13.1','helpful','beef and dairy exported','high')],
'11.1':[(A+'14.3','helpful','Bord Bia role','high')],
'11.2':[(S+'11.1','essential','uses food export total','high')],
'11.3':[(S+'11.1','helpful','part of food exports','high')],
'12.0':[(S+'11.2','helpful','UK share of food exports','high')],
'12.1':[(S+'11.2','helpful','EU and UK food shares','high')],
'12.2':[(A+'14.0','helpful','Kerrygold and Ornua','high')],
'12.3':[(A+'14.6','helpful','Baileys','low')],
'13.0':[(E+'1.0','helpful','single market freedoms','high')],
'13.1':[(E+'6.1','helpful','euro removes exchange risk','high')],
'13.2':[(S+'13.1','helpful','exchange-rate risk','high')],
'13.3':[(E+'6.5','helpful','CAP and food standards','high')],
'14.0':[(A+'19.0','helpful','foreign direct investment','high')],
'14.1':[(A+'5.2','helpful','12.5% corporation tax','high')],
'14.2':[(A+'5.3','essential','15% minimum tax rule','high')],
'15.1':[(S+'15.0','helpful','island, trade by sea','high')],
'16.0':[(A+'23.4','helpful','Brexit dates','low')],
'16.1':[(S+'16.0','essential','post-Brexit trade rules','high')],
'16.2':[(S+'15.1','helpful','Rosslare as port','high')],
'16.3':[(S+'15.1','helpful','Rosslare as port','high')],
'16.4':[(S+'16.1','helpful','border checks on GB trade','low')],
'16.5':[(S+'16.4','helpful','trade shift after Brexit','high')],
'17.0':[(S+'7.0','helpful','pharma and USA reliance','high')],
'17.1':[(S+'15.0','helpful','peripheral island location','high')],
}
out={};n=0
for i in tg:
    k=i[len(S):]
    nd=[{'id':t,'strength':s,'why':w,'confidence':c} for t,s,w,c in L.get(k,[])]
    n+=len(nd)
    out[i]={'cost':2 if k in c2 else 1,'needs':nd}
bad=[(i,n["id"]) for i,v in out.items() for n in v["needs"] if n["id"] not in ids or n["id"]==i]; print(bad)
json.dump(out,open(P+'point-links/geo-economic-eu-s2.t1g1.json','w'),indent=1)
print(len(out),n,sum(v['cost']==2 for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
