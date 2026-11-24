import json,re
P='hist-ire6-s3.'
H,L='high','low'
def n(i,s,w,c=H): return {"id":i if i.startswith('hist-') else P+i,"strength":s,"why":w,"confidence":c}
h='helpful'; e='essential'
D={
'0.b':(1,[]),'0.0':(2,[]),'0.1':(1,[]),
'0.2':(1,[n('hist-ire6-s2.2.b',h,'First Programme for growth')]),
'0.3':(1,[]),
'0.4':(2,[n('0.3',e,'the OECD-assisted survey')]),
'0.5':(2,[n('0.4',e,'Investment in Education report')]),
'1.b':(1,[]),
'1.0':(1,[n('0.5',h,'report’s recommended expansion')]),
'1.1':(1,[n('1.0',e,'comprehensive schools')]),
'1.2':(2,[n('0.0',h,'fee-charging secondary schools')]),
'1.3':(1,[n('1.2',e,'O’Malley’s free education announcement')]),
'1.4':(2,[n('1.2',e,'the free education announcement')]),
'1.5':(1,[n('1.4',e,'the free education scheme')]),
'1.6':(1,[n('1.2',h,'O’Malley as minister')]),
'1.7':(1,[n('0.0',h,'leaving at 14, Primary Certificate','low')]),
'2.0':(1,[n('1.0',h,'comprehensive schools')]),
'2.1':(1,[]),'2.2':(1,[]),'2.3':(1,[]),'2.4':(1,[]),
'2.5':(2,[n('1.4',h,'free second-level expansion')]),
'3.0':(1,[]),
'3.1':(1,[n('3.0',e,'the 1971 curriculum')]),
'3.2':(1,[n('3.0',h,'the 1971 curriculum')]),
'3.3':(1,[n('3.0',h,'the 1971 curriculum')]),
'4.b':(1,[]),
'4.0':(2,[n('hist-ire6-s1.2.7',e,'replaced Mother and Child Scheme')]),
'4.1':(1,[]),'4.2':(1,[]),'4.3':(1,[]),
'4.4':(2,[n('4.1',h,'old county health authorities')]),
'4.5':(1,[n('4.3',h,'hospital services reform','low')]),
'4.6':(1,[n('4.0',h,'means-tested eligibility')]),
'4.7':(1,[n('hist-ire6-s1.1.7',h,'Hospitals Sweepstake funding')]),
'5.b':(1,[]),'5.0':(1,[]),'5.1':(1,[]),
'5.2':(1,[n('5.1',h,'the single social insurance system')]),
'5.3':(1,[]),'5.4':(1,[]),'5.5':(1,[]),'5.6':(2,[]),
'6.0':(1,[]),
'6.1':(1,[n('6.0',h,'local authority housing')]),
'6.2':(2,[n('6.0',h,'local authority flats')]),
'6.3':(1,[]),'6.4':(1,[]),'6.5':(1,[]),
'6.6':(1,[n('6.4',e,'rural electrification'),n('6.5',h,'group water schemes')]),
'7.0':(1,[]),
'7.1':(1,[n('0.4',e,'Investment in Education'),n('1.0',e,'comprehensive schools')]),
'7.2':(1,[]),
'7.3':(1,[n('1.2',e,'free second-level education')]),
'7.4':(2,[n('7.1',h,'Hillery’s groundwork'),n('7.3',h,'O’Malley’s announcement'),n('8.3',h,'costs remaining after free fees')]),
'8.0':(1,[n('2.0',h,'comprehensive and community schools')]),
'8.1':(1,[n('1.5',h,'enrolment rise after 1967')]),
'8.2':(2,[n('0.0',h,'secondary versus vocational schools')]),
'8.3':(1,[n('1.4',e,'free second-level scheme')]),
'8.4':(1,[]),
'9.0':(2,[n('1.4',h,'free post-primary education'),n('4.4',h,'health board structure'),n('5.4',h,'lone mothers’ payments')]),
'9.1':(2,[n('4.2',h,'the VHI'),n('6.2',h,'Ballymun’s problems')]),
'9.2':(1,[n('8.0',h,'churches keeping school control')]),
'9.3':(2,[n('7.4',h,'historians’ view of the reforms','low')]),
}
txt=open('/Users/gabrielwhelan/barebones/drafts/crunch/history/packs/hist-ire6-s3.t1g1.txt').read()
tg=re.findall(r'^\[(hist-ire6-s3\.[^\]]+)\]',txt.split('CANDIDATES')[0],re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
out={}
for t in tg:
    c,nd=D[t[len(P):]]; out[t]={"cost":c,"needs":nd}
assert len(D)==len(tg)==len(out),(len(D),len(tg))
for t,v in out.items():
    for x in v['needs']: assert x['id'] in allids and x['id']!=t,(t,x)
json.dump(out,open('/Users/gabrielwhelan/barebones/drafts/crunch/history/point-links/hist-ire6-s3.t1g1.json','w'),ensure_ascii=False,indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(x['confidence']==L for v in out.values() for x in v['needs']))
