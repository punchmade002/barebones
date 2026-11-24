import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
txt=open(P+'packs/geo-economic-activities-s2.t1g2.txt').read()
targets=[];allids=set()
sec=None
for l in txt.splitlines():
    if l.startswith('TARGET'):sec='T'
    elif l.startswith('CANDIDATES'):sec='C'
    m=re.match(r'\[(\S+)\]',l)
    if m:
        allids.add(m.group(1))
        if sec=='T':targets.append(m.group(1))
E,H='essential','helpful'
# id -> list of (target, strength, why, conf)
L={
'0.1':[('0.0',H,'contrast with bulk-reducing','high')],
'0.2':[('0.0',E,'bulk-reducing pulls to raw material','high'),('0.1',E,'bulk-gaining pulls to market','high')],
'2.0':[('0.0',E,'weight-losing raw materials','high')],
'2.3':[('2.2',H,'labour skills','high')],
'2.4':[('2.2',H,'labour examples','high')],
'3.0':[('0.1',H,'bulk-gaining goods near market','high')],
'3.2':[('3.1',H,'ports','high')],
'3.3':[('3.1',H,'port location','low')],
'3.5':[('3.4',H,'airports','high')],
'4.3':[('4.1',H,'state agencies attracting firms','low')],
'4.6':[('4.1',H,'grants and subsidies','low')],
'5.3':[('1.7',H,'infrastructure services','high')],
'6.0':[('1.5',H,'cluster/agglomeration term','high')],
'6.1':[('6.0',E,'clusters from agglomeration','high')],
'6.3':[('6.2',H,'historical factors','low')],
'6.4':[('2.2',H,'skilled labour','high')],
'7.1':[('7.0',H,'Corrib project','high')],
'7.2':[('7.1',H,'opposition delay','high')],
'8.0':[('2.1',H,'energy as factor','high')],
'8.1':[('3.0',H,'markets','high')],
'8.2':[('1.0',E,'footloose industry','high')],
'9.b':[('0.0',E,'bulk-reducing industry','high')],
'9.1':[('0.0',E,'bulk-reducing','high')],
'9.3':[('3.1',H,'ports and deep water','high')],
'9.4':[('5.0',H,'site requirements','high')],
'10.b':[('9.3',H,'deep water estuary','high')],
'11.b':[('1.0',E,'footloose industry','high')],
'11.1':[('2.2',E,'labour skills','high')],
'11.2':[('4.1',E,'IDA support','high')],
'11.3':[('3.0',H,'EU single market access','high')],
'11.4':[('3.7',H,'transport connections','high')],
'11.5':[('1.3',E,'greenfield site','high')],
'11.6':[('1.0',E,'footloose','high')],
'11.7':[('1.1',E,'branch plant','high')],
'12.b':[('6.0',H,'agglomeration clusters','high')],
'12.1':[('3.1',H,'deep-water port','high')],
'12.2':[('5.1',H,'site water and waste','low')],
'12.3':[('2.2',H,'skilled labour','high')],
'12.4':[('6.0',H,'clustering','high')],
'13.b':[('6.0',H,'cluster','high')],
'13.1':[('21.3',E,'DEC closure facts','high')],
'13.2':[('6.0',H,'cluster supplier network','low')],
'14.b':[('0.0',H,'bulk-reducing idea','high')],
'14.1':[('0.0',E,'bulk-reducing','high')],
'14.3':[('0.0',E,'bulk-reducing','high')],
'14.5':[('0.1',E,'bulk-gaining','high')],
'14.6':[('6.3',E,'industrial inertia','high')],
'15.b':[('1.0',H,'footloose activity','high')],
'15.1':[('15.0',H,'data centre demand','low')],
'16.0':[('3.6',H,'freight modes','high')],
'16.1':[('3.7',H,'communications','low')],
'16.2':[('2.3',H,'standardised assembly','high')],
'16.3':[('3.0',H,'EU single market','high')],
'17.b':[('1.1',E,'branch plant','high')],
'17.1':[('1.1',E,'branch plant','high')],
'17.2':[('4.2',H,'tax incentives','high')],
'18.b':[('1.1',H,'branch plant','high')],
'18.0':[('3.0',H,'markets','low')],
'18.1':[('3.0',H,'EU single market','high')],
'18.3':[('2.2',H,'skilled labour','high')],
'18.4':[('1.5',H,'cluster','high')],
'18.5':[('4.2',H,'corporation tax','high')],
'19.b':[('18.b',H,'opposite of opening strategies','low')],
'19.1':[('18.2',H,'lower costs','high')],
'19.5':[('22.3',H,'decline stage','high')],
'20.b':[('1.1',H,'branch plant','high')],
'20.0':[('1.2',E,'R&D','high')],
'20.1':[('20.0',H,'moving up value chain','high')],
'21.b':[('1.1',H,'branch plants','low')],
'21.1':[('21.0',H,'Dell Limerick','high')],
'22.0':[('1.2',E,'HQ and R&D','high')],
'22.1':[('1.1',H,'branch plants','high')],
'22.2':[('2.3',H,'low-wage standardised work','low')],
'23.b':[('22.b',H,'product life cycle','low')],
'23.1':[('23.0',H,'Cork site history','high')],
'23.2':[('1.2',E,'headquarters','high')],
'24.0':[('22.0',H,'early life cycle','high')],
'24.1':[('2.2',H,'skills and education','low')],
'24.2':[('2.3',H,'graduates for high-tech firms','high')],
'25.b':[('1.0',H,'footloose services','low')],
'25.0':[('1.0',E,'footloose','high')],
'25.2':[('25.1',E,'teleservices','high')],
'25.3':[('25.1',H,'teleservices','high')],
'26.1':[('26.0',H,'e-commerce','high')],
'26.2':[('26.0',E,'e-commerce','high')],
'27.1':[('3.7',H,'broadband infrastructure','high')],
'27.2':[('27.0',H,'remote working','high')],
'27.4':[('27.1',H,'broadband rollout','high')],
'28.1':[('19.3',H,'automation','high')],
'29.1':[('29.0',E,'named factor with evidence','high')],
'29.3':[('29.1',H,'same structure','high')],
'30.b':[('29.b',H,'map question method','high')],
'30.0':[('5.0',E,'site requirements','high')],
'30.1':[('3.6',H,'transport modes','low')],
'30.2':[('2.2',H,'labour','high')],
'30.3':[('1.4',H,'industrial estate','high')],
'31.b':[('0.0',E,'bulk-reducing raw material','high')],
'31.0':[('14.2',H,'fishing port','low')],
'31.1':[('3.0',H,'markets','low')],
'31.2':[('5.1',H,'water supply','high')],
'31.3':[('5.0',H,'flat land site','high')],
'33.b':[('29.b',H,'map question method','low')],
'33.0':[('5.0',H,'site needs flat land','high')],
'33.2':[('4.5',H,'planning permission','low')],
'34.b':[('29.b',H,'map question method','high')],
'34.0':[('29.0',E,'factor plus evidence','high'),('5.0',H,'flat site','high')],
'34.1':[('29.1',E,'explain why factor matters','high')],
'34.2':[('33.1',H,'floodplain reason against','high')],
'35.0':[('29.0',H,'map evidence structure','low')],
}
out={}
for t in targets:
    k=t.replace('geo-economic-activities-s2.','')
    out[t]={'needs':[{'id':'geo-economic-activities-s2.'+i,'strength':s,'why':w,'confidence':c} for i,s,w,c in L.get(k,[])]}
unused=set(L)-{t.replace('geo-economic-activities-s2.','') for t in targets}
assert not unused,unused
for t,v in out.items():
    for n in v['needs']:
        assert n['id'] in allids and n['id']!=t,(t,n)
json.dump(out,open(P+'point-links/geo-economic-activities-s2.t1g2.json','w'),indent=1)
d=json.load(open(P+'point-links/geo-economic-activities-s2.t1g2.json'))
assert list(d)==targets
print(len(d),sum(len(v['needs']) for v in d.values()),sum(n['confidence']=='low' for v in d.values() for n in v['needs']))
