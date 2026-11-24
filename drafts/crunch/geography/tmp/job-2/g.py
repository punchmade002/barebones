import re,json
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
txt=open(P+'packs/geo-economic-activities-s1.t1g4.txt').read()
tgt=[];allids=set()
sec=None
for l in txt.split('\n'):
    if l.startswith('TARGET'):sec='t'
    elif l.startswith('CANDIDATES'):sec='c'
    m=re.match(r'\[([^\]]+)\]',l)
    if m:
        allids.add(m.group(1))
        if sec=='t':tgt.append(m.group(1))
p='geo-economic-activities-s1.'
E,H='essential','helpful'
L={ # id:[(target,strength,why,conf)]
'0.3':[('0.0',E,'primary sector definition','high'),('0.1',E,'secondary sector definition','high'),('0.2',E,'tertiary sector definition','high')],
'1.0':[('0.0',E,'primary activity','high'),('0.1',E,'secondary activity','high'),('0.2',E,'tertiary activity','high')],
'1.1':[('1.0',E,'shift from primary to tertiary','high'),('0.2',H,'tertiary meaning services','high')],
'1.3':[('1.0',H,'primary employment falls with development','high')],
'1.2.2':[('1.2.1',H,'protection and tariffs','high')],
'1.3.2':[('1.2.1',H,'free trade versus tariffs','high')],
'1.3.3':[('1.2.1',H,'trade barriers and tariffs','low')],
'1.4.1':[('1.4.0',E,'free education builds workforce','high')],
'1.4.2':[('1.3.0',E,'IDA agency','high')],
'1.5.0':[('eu-s3.1.0',H,'single market','high')],
'1.5.2':[('1.5.b',E,'corporation tax defined','high')],
'1.5.3':[('1.5.2',E,'corporation tax rate','high')],
'1.6.b':[('1.3.2',H,'export-led growth policies','low')],
'1.6.0':[('1.3.2',H,'export-led growth and foreign investment','high')],
'1.6.3':[('1.2.2',H,'emigration','high')],
'1.7.0':[('1.6.1',E,'property boom','high')],
'1.7.1':[('1.7.0',E,'banks bad loans after crash','high')],
'1.7.2':[('1.7.1',H,'bank rescue','low')],
'1.7.3':[('1.7.0',E,'property bad loans','high')],
'1.8.0':[('1.7.1',E,'bank guarantee debt','high')],
'1.8.1':[('1.8.0',E,'EU-IMF programme','high')],
'1.8.2':[('1.6.3',H,'net emigration','high')],
'1.8.3':[('1.7.1',E,'bank rescue borrowing','high')],
'1.9.0':[('1.8.2',H,'unemployment trend','low')],
'1.9.1':[('1.5.2',E,'corporation tax','high')],
'1.10.0':[('1.9.0',H,'high employment','low')],
'1.10.1':[('1.9.0',H,'full employment','low')],
'1.10.3':[('1.8.2',H,'emigration','high')],
'1.10.4':[('1.10.0',H,'tax revenue','low')],
'1.11.0':[('1.8.3',E,'GDP defined','high')],
'1.11.1':[('1.11.0',E,'GDP distorted by multinationals','high')],
'1.12.2':[('1.12.1',H,'grass-based livestock farming','high')],
'1.12.4':[('1.12.3',E,'tillage farming','high')],
'1.13.0':[('eu-s3.5.0',H,'milk quotas','high')],
'1.13.1':[('1.12.2',H,'beef and dairy cattle','high')],
'1.13.2':[('1.13.1',H,'exports of beef and dairy','high')],
'1.13.3':[('1.12.2',H,'livestock methane','high')],
'1.13.4':[('1.12.2',H,'livestock farming','low')],
'1.14.3':[('1.13.1',H,'food exports','low')],
'1.15.3':[('1.15.1',E,'pelagic fish','high')],
'1.16.0':[('eu-s3.14.0',H,'fishing quotas','high')],
'1.16.1':[('1.16.0',E,'fishing quotas','high')],
'1.16.2':[('1.15.1',E,'pelagic fish','high')],
'1.16.3':[('1.15.2',H,'fishing harbour centres','low')],
'1.17.1':[('1.17.0',H,'small forest cover','low')],
'1.17.2':[('1.17.0',E,'forest cover','high')],
'1.17.3':[('1.17.1',H,'Coillte','high')],
'1.18.3':[('1.18.2',E,'peat power stations','high')],
'1.19.1':[('1.19.0',E,'FDI','high'),('1.3.0',H,'IDA','high')],
'1.19.2':[('1.5.2',E,'low corporation tax','high'),('1.3.0',H,'IDA','high')],
'1.19.3':[('1.4.1',H,'educated workforce','high')],
'1.19.4':[('1.5.0',E,'EU single market','high')],
'1.20.1':[('1.20.0',E,'Cork Harbour plants','high')],
'1.20.2':[('1.20.0',H,'pharmaceutical sector','high')],
'1.21.2':[('1.21.1',E,'Intel Leixlip','high')],
'1.22.0':[('1.19.0',H,'foreign-owned firms','low')],
'1.22.2':[('0.2',E,'tertiary sector','high')],
'1.22.3':[('1.19.1',H,'foreign-owned sector','low')],
'1.23.0':[('1.19.1',E,'multinationals employ many','high')],
'1.23.1':[('1.5.3',E,'15% minimum tax','high'),('1.5.2',H,'low tax rate','high')],
'1.23.2':[('1.5.2',H,'corporation tax','low')],
'1.23.3':[('1.2.1',H,'tariffs','high')],
'1.23.4':[('1.3.4',H,'EU membership','low')],
'1.24.0':[('1.24.b',E,'footloose industry','high')],
'1.24.1':[('1.24.b',E,'footloose industry','high'),('0.2',H,'services','low')],
'1.25.0':[('1.24.1',H,'footloose digital services','low')],
'1.25.1':[('1.25.0',H,'Silicon Docks','high')],
'1.25.2':[('1.25.0',H,'Silicon Docks','high')],
'1.25.3':[('1.25.0',H,'docklands','low')],
'1.26.0':[('1.24.0',H,'footloose skilled labour','low')],
'1.26.2':[('1.24.0',H,'good communications','low')],
'1.26.3':[('1.5.2',H,'low tax rate','high')],
'1.27.0':[('1.25.0',H,'Silicon Docks cluster','low')],
'1.27.1':[('1.26.4',H,'clustering demand','low')],
'1.27.2':[('1.26.4',H,'concentration of firms','low')],
'1.28.1':[('1.26.4',H,'clustering','high')],
'1.28.2':[('1.28.0',E,'data centre electricity use','high')],
'1.29.1':[('1.29.0',H,'duty-free Shannon','high')],
'1.29.2':[('1.29.1',H,'Shannon Free Zone','high')],
'1.29.3':[('1.29.2',E,'aircraft leasing','high')],
'1.30.1':[('1.30.0',H,'Silicon Valley area','high')],
'1.30.2':[('1.30.0',H,'Silicon Valley','high')],
'1.30.3':[('1.30.0',H,'Silicon Valley','high')],
'1.32.0':[('1.31.0',H,'financial services','high')],
'1.32.1':[('1.5.2',E,'corporation tax','high')],
'1.32.2':[('1.32.1',H,'low tax rate','high')],
'1.33.0':[('1.31.0',H,'fund administration','high')],
'1.33.1':[('1.29.2',H,'aircraft leasing','high')],
'1.33.2':[('1.32.0',H,'IFSC docklands','high')],
'1.34.0':[('1.7.0',H,'2008 banking crash','high')],
'1.34.1':[('1.23.4',E,'Brexit','high')],
'1.35.2':[('1.34.1',H,'banks moving after Brexit','high'),('1.23.4',H,'Brexit','high')],
'1.37.1':[('1.37.0',H,'visitor numbers','low')],
'1.37.2':[('1.37.0',H,'overseas visitors','high')],
'1.37.4':[('1.37.3',H,'tourism agencies','low')],
'1.38.0':[('1.37.0',H,'overseas visits','high')],
'1.38.1':[('1.38.0',E,'collapse of visits','high')],
'1.39.2':[('1.39.0',H,'airports','low')],
'1.40.0':[('1.39.0',H,'airports and ports','high'),('1.39.1',H,'ferry ports','high')],
}
out={}
for t in tgt:
    k=t[len(p):]
    out[t]={"needs":[{"id":(i if i.startswith('geo-') else p+i),"strength":s,"why":w,"confidence":c} for i,s,w,c in L.get(k,[])]}
print(sorted(set(L)-{t[len(p):] for t in tgt}))
for v in out.values():
    for n in v['needs']: assert n['id'] in allids,n
json.dump(out,open(P+'point-links/geo-economic-activities-s1.t1g4.json','w'),indent=1)
chk=json.load(open(P+'point-links/geo-economic-activities-s1.t1g4.json'))
assert list(chk)==tgt
print(len(tgt),sum(len(v['needs']) for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
