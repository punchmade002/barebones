import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/biology/'
txt=open(P+'points/bio35-s3.txt').read()
tgt=[];allids=set()
sec=None
for l in txt.split('\n'):
    if l.startswith('TARGET'): sec='t'
    elif l.startswith('CANDIDATES'): sec='c'
    m=re.match(r'\[([^\]]+)\]',l)
    if m:
        allids.add(m.group(1))
        if sec=='t': tgt.append(m.group(1))
H,E='helpful','essential'
c2={'0.6','1.0','2.2','3.4','4.0','4.3','4.4','6.0','6.1','6.2','6.4','8.0','8.1','9.1','10.0','10.6','11.2'}
N={ '0.2':[('bio35-s2.1.1',H,'STR repeat regions','high')],
'0.3':[('bio35-s3.9.b',H,'gel electrophoresis separates by size','high')],
'0.4':[('bio35-s3.10.3',H,'staining makes bands visible','high')],
'0.5':[('bio35-s3.8.0',H,'restriction enzyme method','high')],
'1.3':[('bio13-s2.0.b',H,'protease is an enzyme','low')],
'1.5':[('bio35-s3.1.2',H,'break cells, remove protein','low')],
'2.2':[('bio13-s2.2.2',H,'heat denatures enzymes','high')],
'3.1':[('bio35-s3.1.3',H,'protease digests proteins','high')],
'3.2':[('bio35-s3.1.4',H,'cold ethanol precipitates DNA','high')],
'3.4':[('bio35-s3.1.4',H,'salt and ethanol roles','high')],
'4.0':[('bio35-s2.1.1',H,'STR repeats','high')],
'4.1':[('bio17-s1.0.b',H,'DNA replication','high')],
'4.3':[('bio17-s1.1.1',H,'complementary base pairing','high')],
'4.4':[('bio17-s1.1.2',E,'DNA polymerase adds nucleotides','high')],
'4.5':[('bio17-s1.1.2',H,'DNA polymerase','high')],
'5.1':[('bio13-s2.2.2',H,'denaturation of enzymes','high')],
'5.2':[('bio13-s2.2.2',E,'denatured enzymes stop working','high')],
'5.3':[('bio35-s3.6.b',H,'PCR cycle repeats','low')],
'6.0':[('bio17-s1.1.0',H,'helicase unwinds DNA','high')],
'6.1':[('bio35-s3.4.3',E,'primers complementary to region','high')],
'6.2':[('bio35-s3.4.4',E,'polymerase extends from primer','high')],
'6.3':[('bio35-s3.6.2',H,'extension builds new strand','high')],
'7.0':[('bio35-s3.6.3',E,'each cycle doubles DNA','high')],
'7.1':[('bio35-s3.7.0',E,'2^n copies formula','high')],
'7.4':[('bio35-s3.5.0',H,'Taq polymerase source','high')],
'8.0':[('bio35-s2.1.1',H,'repeat regions','low')],
'8.1':[('bio35-s2.1.2',E,'repeat number varies between people','high')],
'8.2':[('bio35-s3.4.0',H,'PCR needs less DNA','high')],
'9.1':[('bio35-s2.4.1',H,'DNA moves toward positive electrode','low')],
'9.4':[('bio35-s2.4.3',H,'ladder gives fragment sizes','high')],
'10.0':[('bio35-s3.9.1',E,'wells and electrodes set-up','high')],
'10.1':[('bio35-s3.9.0',H,'gel pores act as sieve','high')],
'10.2':[('bio35-s3.9.2',H,'loading dye shows progress','high')],
'10.5':[('bio35-s2.4.4',H,'peaks instead of bands','high')],
'11.0':[('bio35-s3.9.4',H,'ladder gives sizes','high')],
'11.1':[('bio35-s2.5.0',E,'match needs every band same','high')],
'11.2':[('bio35-s2.2.2',E,'child gets one band from each parent','high')],
}
out={}
for i in tgt:
    k=i.split('s3.')[1]
    out[i]={'cost':2 if k in c2 else 1,'needs':[{'id':a,'strength':b,'why':c,'confidence':d} for a,b,c,d in N.get(k,[])]}
json.dump(out,open(P+'point-links/bio35-s3.json','w'),indent=1)
o=json.load(open(P+'point-links/bio35-s3.json'))
assert list(o)==tgt
assert all(n['id'] in allids and n['id']!=k for k,v in o.items() for n in v['needs'])
L=[n for v in o.values() for n in v['needs']]
print(len(o),len(L),sum(v['cost']==2 for v in o.values()),sum(n['confidence']=='low' for n in L))
