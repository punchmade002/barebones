import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
S='geo-economic-development-s1.'
G='geo-graph-skills-s1.'
# id suffix: (cost, [(target, strength, why, conf)])
H,E='helpful','essential'
d={
'0.b':(1,[]),'0.0':(1,[]),
'0.1':(1,[('0.0',H,'economic development vs growth','high')]),
'0.2':(1,[('0.0',H,'output and income','high')]),
'0.3':(1,[('1.1.3',H,'GNI definition','high')]),
'0.4':(2,[('0.2',H,'developed vs developing','high')]),
'1.b':(1,[]),'1.0':(1,[]),
'1.1':(2,[('1.0',E,'GDP as base measure','high')]),
'1.2':(2,[('1.0',E,'location measure','high'),('1.1',E,'ownership measure','high')]),
'1.3':(1,[('1.1',E,'GNP is the same','high')]),
'1.4':(2,[('1.0',H,'totals compared in dollars','low')]),
'1.5':(1,[('1.1',H,'GNP example','high')]),
'2.b':(1,[]),
'2.0':(1,[('1.0',E,'output being measured','high')]),
'2.1':(1,[('2.0',H,'economic growth','high')]),
'3.b':(1,[]),
'3.0':(1,[('1.5',H,'per head figure','high')]),
'3.1':(1,[('1.5',H,'per head figure','low')]),
'3.2':(1,[]),
'3.3':(1,[('2.1',H,'growth brings tax revenue','high')]),
'4.b':(1,[]),
'4.0':(1,[('1.5',H,'average per head','high')]),
'4.1':(1,[]),
'4.2':(2,[('1.0',H,'output counts all spending','high')]),
'4.3':(1,[]),
'4.4':(1,[('1.4',E,'PPP adjusts prices','high')]),
'4.5':(1,[('6.0',H,'broader measure is HDI','high')]),
'5.b':(1,[]),
'5.0':(2,[('1.2',E,'GDP vs GNP difference','high')]),
'5.1':(2,[('2.0',H,'GDP growth rate','high')]),
'5.2':(2,[('5.1',H,'the 2015 jump','high')]),
'5.3':(2,[('1.3',E,'GNI definition','high'),('5.2',H,'intellectual property distortion','high')]),
'5.4':(1,[('5.3',E,'GNI* defined','high')]),
'5.5':(1,[('5.3',E,'GNI* as better guide','high')]),
'6.b':(1,[]),'6.0':(1,[]),'6.1':(1,[]),'6.2':(1,[]),'6.3':(1,[]),
'6.4':(1,[('1.3',H,'GNI per head','high'),('1.4',E,'PPP dollars','high')]),
'6.5':(2,[('6.2',E,'health dimension','high'),('6.3',E,'education dimension','high'),('6.4',E,'income dimension','high')]),
'6.6':(1,[('6.5',E,'HDI value 0 to 1','high')]),
'6.7':(1,[('6.3',H,'schooling indicators','high')]),
'7.b':(1,[]),
'7.0':(2,[('6.6',H,'HDI categories','high')]),
'7.1':(1,[]),
'7.2':(1,[('6.6',H,'HDI categories','high')]),
'7.3':(1,[('6.6',H,'HDI categories','high')]),
'7.4':(2,[('6.6',H,'low HDI category','high')]),
'7.5':(1,[('7.4',H,'low HDI countries','high')]),
'8.b':(1,[]),
'8.0':(1,[('6.5',H,'HDI combines three dimensions','high')]),
'8.1':(1,[]),
'8.2':(2,[('6.4',H,'income part of HDI','high')]),
'8.3':(1,[]),
'8.4':(1,[('6.5',H,'weakest dimension','low')]),
'9.b':(1,[]),
'9.0':(1,[('6.5',H,'HDI is a national average','high')]),
'9.1':(1,[]),'9.2':(1,[]),
'9.3':(1,[('6.5',H,'three dimensions combined','high')]),
'9.4':(1,[('6.6',H,'HDI close to 1','high')]),
'9.5':(2,[('6.0',H,'UNDP and HDI','high')]),
'10.b':(1,[]),
'10.0':(1,[('1.1',H,'GNP measures output','high'),('6.b',H,'HDI measures outcomes','high')]),
'10.1':(2,[('10.0',E,'income rank vs HDI rank','high')]),
'10.2':(1,[('10.0',H,'income rank vs HDI rank','high')]),
'10.3':(1,[('10.0',H,'HDI rank vs income rank','high')]),
'10.4':(1,[('6.4',E,'GNI per head in HDI','high')]),
'11.b':(1,[]),'11.0':(2,[]),'11.1':(2,[]),
'11.2':(1,[('11.0',H,'social indicators','low')]),
'12.b':(1,[]),'12.0':(1,[]),'12.1':(1,[]),'12.2':(2,[]),'12.3':(2,[]),'12.4':(1,[]),'12.5':(1,[]),'12.6':(2,[]),
'13.b':(1,[]),'13.0':(1,[]),'13.1':(1,[]),'13.2':(1,[]),'13.3':(1,[]),'13.4':(1,[]),'13.5':(1,[]),
'14.b':(1,[]),'14.0':(1,[]),
'14.1':(1,[('2.1',H,'tax revenue from growth','high')]),
'14.2':(1,[]),'14.3':(1,[]),'14.4':(1,[]),
'14.5':(1,[('14.0',H,'foreign investment and graduates','low')]),
'15.b':(1,[]),'15.0':(1,[]),'15.1':(2,[]),'15.2':(1,[]),
'16.b':(1,[]),
'16.0':(1,[(G+'6.2',H,'axes, units, title rules','high')]),
'16.1':(1,[(G+'11.3',H,'pie chart key and shares','high')]),
'16.2':(1,[(G+'3.1',H,'calculating a difference','high')]),
'16.3':(1,[]),
}
txt=open(P+'packs/geo-economic-development-s1.t1g1.txt').read()
ids=re.findall(r'^\[([^\]]+)\]',txt,re.M)
tgt=[i for i in ids if i.startswith(S)]
out={}
for i in tgt:
    k=i[len(S):]; c,n=d[k]
    out[i]={'cost':c,'needs':[{'id':(t if t.startswith('geo-') else S+t),'strength':s,'why':w,'confidence':f} for t,s,w,f in n]}
assert set(d)=={i[len(S):] for i in tgt},(set(d)^{i[len(S):] for i in tgt})
for v in out.values():
    for n in v['needs']: assert n['id'] in ids,n
json.dump(out,open(P+'point-links/geo-economic-development-s1.t1g1.json','w'),indent=0)
o=json.load(open(P+'point-links/geo-economic-development-s1.t1g1.json'))
print(len(o),sum(len(v['needs']) for v in o.values()),sum(v['cost']==2 for v in o.values()),sum(n['confidence']=='low' for v in o.values() for n in v['needs']))
