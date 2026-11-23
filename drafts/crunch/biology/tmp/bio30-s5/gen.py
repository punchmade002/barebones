import re,json
P='/Users/gabrielwhelan/barebones/drafts/crunch/biology/'
txt=open(P+'points/bio30-s5.txt').read()
tgt_part=txt.split('CANDIDATES')[0]
tids=re.findall(r'^\[([^\]]+)\]',tgt_part,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
H,E='helpful','essential'
c2={'0.b','0.1','0.5','2.4','3.1','3.2','3.3','5.5','6.1','6.2','6.3','6.5','10.6','16.0','16.3','16.5','16.6','17.2','18.2'}
# id -> (target, strength, why)
n={
'0.0':('s5.0.b',E,'concentration gradient'),
'0.1':('s5.0.b',H,'concentration gradient'),
'0.2':('s2.2.5',H,'wilting when water short'),
'0.4':('s2.2.0',H,'water loss via cuticle and stomata'),
'0.5':('s2.3.b',H,'stomata open and close'),
'0.6':('s2.4.0',H,'CO2 and stomatal control'),
'0.7':('s5.0.b',E,'concentration gradient'),
'1.0':('s5.1.b',H,'one factor at a time'),
'1.1':('s5.1.b',E,'hypothesis as testable prediction'),
'1.2':('s5.1.b',H,'hypothesis as testable prediction'),
'1.4':('s5.1.3',H,'potometer measures uptake'),
'2.0':('bio2-s2.0.1',E,'independent variable'),
'2.1':('bio2-s2.0.2',E,'dependent variable'),
'2.2':('bio2-s2.0.3',E,'controlled variables'),
'2.3':('s5.2.2',H,'controlled variables list'),
'2.4':('bio2-s2.2.1',E,'control as comparison'),
'2.5':('bio2-s2.2.1',H,'control as comparison'),
'3.0':('s5.1.3',H,'potometer measures uptake'),
'4.0':('s2.9.1',H,'air breaks xylem column'),
'4.1':('s2.9.1',H,'air breaks xylem column'),
'4.2':('s5.3.0',H,'bubble potometer parts'),
'4.3':('s5.3.0',H,'potometer parts'),
'4.4':('s5.3.0',H,'capillary tube'),
'4.5':('s5.3.1',H,'petroleum jelly use'),
'5.b':('s5.4.b',E,'built potometer'),
'5.0':('s5.3.0',H,'capillary tube'),
'5.1':('s5.2.3',H,'time allowed to adjust'),
'5.2':('s5.5.0',E,'air bubble in capillary'),
'5.3':('s5.5.2',H,'bubble distance measurement'),
'5.4':('bio2-s2.5.2',H,'repeats and mean'),
'5.5':('s5.3.0',E,'potometer parts'),
'6.0':('s5.5.2',E,'bubble distance moved'),
'6.1':('s5.6.0',H,'bubble distance and rate'),
'6.2':('s5.6.1',E,'volume formula'),
'6.3':('s5.6.0',H,'rate of uptake'),
'6.4':('s5.6.3',E,'dividing by leaf area'),
'6.6':('s5.6.5',E,'percentage mass loss'),
'7.b':('s5.0.0',H,'air movement effect'),
'7.0':('s5.5.2',E,'potometer reading method'),
'7.1':('s5.3.2',H,'fan apparatus'),
'7.2':('s5.7.1',E,'fan settings'),
'7.3':('s5.2.2',H,'temperature controlled'),
'7.4':('s5.0.0',E,'air movement raises rate'),
'8.b':('s5.0.1',H,'temperature effect'),
'8.0':('s5.5.2',H,'potometer reading method'),
'8.1':('s5.5.1',H,'adjusting to conditions'),
'8.2':('s5.3.2',H,'heat shield'),
'8.3':('s5.0.5',H,'light affects rate'),
'8.4':('s5.0.1',E,'temperature raises rate'),
'9.b':('s5.0.3',H,'surface area effect'),
'9.0':('s5.5.2',H,'potometer reading method'),
'9.1':('s5.3.1',H,'petroleum jelly use'),
'9.3':('s5.6.3',E,'leaf area on graph paper'),
'9.4':('s5.0.3',E,'surface area effect'),
'10.b':('s5.0.4',H,'cuticle and water loss'),
'10.1':('s5.2.5',H,'untreated control leaf'),
'10.5':('s5.6.5',E,'percentage mass loss'),
'10.6':('s5.0.4',E,'cuticle and stomata water loss'),
'10.7':('s5.10.6',H,'expected results'),
'11.b':('s5.10.b',H,'cuticle comparison'),
'11.0':('s5.10.1',H,'coating leaf surfaces'),
'11.1':('s5.0.4',H,'thick cuticle'),
'12.b':('s2.1.1',H,'water vapour leaves via stomata'),
'12.1':('s5.3.4',H,'cobalt chloride apparatus'),
'12.3':('s2.4.3',H,'stomata on lower surface'),
'13.b':('s2.3.b',H,'stomata open and close'),
'13.1':('s5.3.2',H,'heat shield'),
'13.2':('s5.13.1',H,'lamp set-up'),
'13.4':('s5.0.5',H,'lamp warms leaf'),
'13.5':('s5.0.5',E,'light controls stomata'),
'14.b':('s5.0.7',H,'humidity in bag'),
'14.0':('bio2-s2.2.1',H,'control for bag effect'),
'14.1':('s5.3.3',H,'CO2 method apparatus'),
'14.2':('s5.3.3',H,'soda lime'),
'14.3':('s5.0.7',H,'humidity builds in bag'),
'14.4':('s5.0.6',E,'CO2 and stomata'),
'15.b':('bio2-s2.7.0',H,'risk assessment'),
'15.0':('bio2-s2.7.4',H,'cutting safely'),
'15.1':('bio2-s2.7.6',H,'electricity and water'),
'16.0':('s5.6.0',H,'rate calculation'),
'16.1':('s5.10.5',H,'percentage mass loss'),
'16.3':('s5.0.b',H,'factors affecting rate'),
'16.4':('s5.0.5',E,'stomata fully open'),
'16.5':('s5.16.3',H,'expected patterns'),
'16.6':('s5.10.1',E,'leaves A to D treatments'),
'17.b':('s5.16.b',H,'primary data'),
'17.1':('bio2-s2.5.4',H,'larger sample reliability'),
'17.2':('s2.4.1',H,'stomata close at night'),
'17.3':('s5.17.2',H,'daily transpiration graph'),
'17.4':('s5.0.2',H,'wilting closes stomata'),
'17.5':('s5.0.6',E,'CO2 closes stomata'),
'18.0':('s5.1.3',E,'uptake versus loss'),
'18.1':('s5.4.1',H,'air breaks water column'),
'18.2':('bio2-s2.3.1',H,'changing one factor changes another'),
'18.4':('s5.5.1',H,'adjusting time'),
'18.6':('s5.5.4',H,'repeat and mean'),
}
out={}
for t in tids:
    k=t.replace('bio30-s5.','')
    needs=[]
    if k in n:
        i,s,w=n[k]
        if not i.startswith('bio'): i='bio30-'+i
        needs=[{'id':i,'strength':s,'why':w,'confidence':'high' if s==E else 'low'}]
    out[t]={'cost':2 if k in c2 else 1,'needs':needs}
for k,v in out.items():
    for x in v['needs']:
        assert x['id'] in allids and x['id']!=k,(k,x)
for k in n: assert 'bio30-s5.'+k in out,k
json.dump(out,open(P+'point-links/bio30-s5.json','w'),indent=0)
d=json.load(open(P+'point-links/bio30-s5.json'))
assert list(d)==tids
print(len(d),sum(len(v['needs']) for v in d.values()),sum(v['cost']==2 for v in d.values()),sum(x['confidence']=='low' for v in d.values() for x in v['needs']))
