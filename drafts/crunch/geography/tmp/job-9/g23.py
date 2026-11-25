import json,re
P='geo-economic-development-s3.'
def n(i,s,w,c='high'):
    return {"id":i if i.startswith('geo-') else P+i,"strength":{'E':'essential','H':'helpful'}[s],"why":w,"confidence":c}
C='geo-region-continental-s1.'
L2={'4.3':n(C+'37.4','H','cotton and jute cash crops'),
'4.4':n(C+'27.7','H','Hooghly river port Kolkata','low'),
'9.0':n(C+'1.4','H','Green Revolution high-yield crops','low'),
'12.1':n(C+'36.1','H','agriculture low productivity')}
L3={'4.4':n(C+'54.2','H','Hooghly jute mills'),
'6.0':n(C+'75.0','H','first train 1853'),
'6.3':n(C+'61.0','H','ports Mumbai and Kolkata','low'),
'7.0':n(C+'68.0','H','English workforce for IT'),
'8.0':n(C+'55.0','H','First Five-Year Plan'),
'8.1':n(C+'55.2','H','imports protected from competition'),
'8.2':n(C+'55.1','H','state-built steel plants'),
'8.3':n(C+'55.3','H','Licence Raj permits'),
'9.0':n(C+'42.1','H','Green Revolution package'),
'9.1':n(C+'42.2','H','food-grain output rise'),
'9.2':n(C+'42.3','H','food self-sufficiency'),
'10.0':n(C+'56.0','H','balance-of-payments crisis 1991'),
'10.2':n(C+'56.1','H','1991 reforms'),
'11.0':n(C+'66.0','H','services share of GDP'),
'11.1':n(C+'67.b','H','outsourcing and Bengaluru IT'),
'11.2':n(C+'57.0','H','Make in India'),
'11.3':n(C+'66.1','H','five largest economies'),
'12.0':n(C+'59.2','H','informal sector defined')}
base='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
for g,L in (('g2',L2),('g3',L3)):
    f=base+'packs/geo-economic-development-s3.t1'+g+'.txt'
    txt=open(f).read(); tg=re.findall(r'^\[(geo-economic-development-s3\.[^\]]+)\]',txt.split('CANDIDATES')[0],re.M)
    ids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    out={t:{"needs":[L[t[len(P):]]] if t[len(P):] in L else []} for t in tg}
    for v in out.values():
        for x in v['needs']: assert x['id'] in ids,x
    json.dump(out,open(base+'point-links/geo-economic-development-s3.t1'+g+'.json','w'),indent=0)
    json.load(open(base+'point-links/geo-economic-development-s3.t1'+g+'.json'))
    print(g,len(out),sum(len(v['needs']) for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
