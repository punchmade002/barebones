import json,re
P='geo-economic-environment-s5.';B='geo-region-continental-s2.'
src=open('/Users/gabrielwhelan/barebones/drafts/crunch/geography/packs/geo-economic-environment-s5.t1g5.txt').read()
tl=src.split('CANDIDATES')[0]
tids=re.findall(r'^\[(\S+?)\]',tl,re.M)
allids=set(re.findall(r'^\[(\S+?)\]',src,re.M))
L={ # id:[(target,strength,why,conf)]
'0.2':[('P0.0','helpful','economic vs environmental interests','low')],
'3.1':[('P3.0','helpful','the Corrib gas field','high')],
'3.2':[('P3.1','helpful','gas supply from Corrib','low')],
'4.b':[('P3.b','helpful','Corrib gas project','high')],
'4.0':[('P3.1','helpful','unprocessed gas, Bellanaboy terminal','high')],
'4.1':[('P4.0','essential','onshore processing of raw gas','high')],
'5.0':[('P4.0','helpful','pipeline route at Rossport','low')],
'5.2':[('P4.2','essential','protected Sruwaddacon Bay estuary','high'),('P4.0','helpful','pipeline near houses','low')],
'6.2':[('P6.1','essential','national quotas under CFP','high')],
'7.b':[('P6.1','helpful','quotas set by EU','high')],
'7.0':[('P6.1','essential','quotas','high')],
'7.1':[('P7.0','essential','smaller quota','high')],
'8.1':[('P8.0','essential','the drift-net ban','high')],
'8.2':[('P8.0','essential','the drift-net ban','high')],
'9.0':[('P6.1','helpful','quotas','high')],
'9.1':[('P9.0','essential','Faroese mackerel quota dispute','high')],
'10.1':[('P10.0','helpful','the Burren limestone','high')],
'10.2':[('P10.1','essential','Mullaghmore location','high')],
'11.b':[('P10.2','helpful','Mullaghmore visitor centre','high')],
'11.0':[('P10.2','essential','the proposed visitor centre','high')],
'11.1':[('P10.2','essential','the proposed visitor centre','high')],
'12.0':[('P2.0','essential','planning permission','high')],
'12.1':[('P12.0','helpful','planning case at Mullaghmore','high')],
'13.1':[('P13.0','helpful','Skellig Michael site','high')],
'14.0':[('P13.0','helpful','Skellig Michael','low')],
'14.1':[('P14.0','helpful','rising visitor demand','high')],
'14.3':[('P14.2','helpful','limits on landings','high')],
'15.1':[('P15.0','helpful','Hill of Tara','high')],
'16.1':[('P16.0','essential','the M3 route','high')],
'16.2':[('P15.1','helpful','Tara-Skryne archaeological valley','high')],
'17.0':[('P15.1','essential','archaeological landscape','high')],
'17.1':[('P16.2','helpful','M3 route near Tara','high')],
'17.2':[('P16.0','helpful','the M3','high')],
'18.2':[('P18.1','essential','raised bogs','high')],
'19.b':[('P18.2','helpful','bogs protected by EU law','high')],
'19.0':[('P18.2','essential','raised-bog SACs','high')],
'19.1':[('P2.3','helpful','compensation','high')],
'19.2':[('P19.0','essential','the turf-cutting ban','high')],
'20.2':[('P20.1','helpful','peat stability objection','low')],
'20.3':[('P2.1','essential','environmental impact assessment','high')],
'20.4':[('P20.0','helpful','renewable energy targets','high')],
'21.1':[('P21.0','helpful','end of milk quotas','high')],
'21.3':[('P21.2','helpful','water quality pressure','high')],
'21.4':[('P21.2','helpful','agricultural emissions','high')],
'22.2':[('P22.1','helpful','electricity demand','high')],
'22.3':[('P22.2','essential','grid strain','high')],
'23.1':[(B+'43.2','helpful','cattle ranching clears Amazon','low')],
'23.3':[(B+'61.1','helpful','Trans-Amazonian Highway','low')],
'23.4':[(B+'54.0','helpful','Carajás iron-ore mine','low')],
'24.b':[('P23.b','helpful','Amazon clearing','high')],
'24.1':[('P24.0','helpful','forest carbon store','high')],
'25.1':[('P25.0','essential','PRODES 2004 baseline','high')],
'25.2':[('P25.1','helpful','trend in clearing','high')],
'26.1':[(B+'48.3','helpful','Amazon soy moratorium','low')],
'26.3':[('P25.2','helpful','rise and fall in clearing','high')],
'27.1':[('P27.0','essential','murder of Chico Mendes','high')],
'28.1':[('P28.0','essential','Hambach lignite mine','high')],
'28.2':[('P28.0','essential','Hambach forest and mine','high')],
'28.3':[('P28.0','essential','Hambach Forest','high')],
'29.b':[('P28.2','helpful','Hambach ruling','high')],
'29.0':[('P28.0','helpful','lignite mining','high')],
'29.1':[('P28.3','helpful','coal phase-out','high')],
'30.1':[('P30.0','helpful','Three Gorges Dam','high')],
'30.2':[('P30.0','helpful','Three Gorges Dam','high')],
'31.b':[('P30.b','helpful','the dam economic case','high')],
'31.2':[('P30.0','helpful','the dam on the Yangtze','high')],
'33.0':[('P20.1','helpful','wind farm siting objections','low')],
'33.2':[('P1.b','helpful','stakeholders','high')],
'33.3':[('P0.b','helpful','economic vs environmental conflict','high')],
}
out={}
for t in tids:
    k=t[len(P):]
    out[t]={'needs':[{'id':x.replace('P',P,1) if x.startswith('P') else x,'strength':s,'why':w,'confidence':c} for x,s,w,c in L.get(k,[])]}
for k in L: assert P+k in out,k
for v in out.values():
    for n in v['needs']: assert n['id'] in allids,n
json.dump(out,open('/Users/gabrielwhelan/barebones/drafts/crunch/geography/point-links/geo-economic-environment-s5.t1g5.json','w'),indent=1)
n=sum(len(v['needs']) for v in out.values())
print(len(out),len(tids),n,sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
