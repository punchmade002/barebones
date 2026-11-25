import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/history/'
E='essential'
def n(i,s='helpful',w='',c='high'): return ('hist-ire1-'+i,s,w,c)
D={
'0.0':(1,[n('s3.5.0',E,'laissez-faire policy'),n('s3.6.2',w='Irish property must pay')]),
'0.1':(1,[]),
'0.2':(1,[n('s3.4.2',w='local relief committees under Peel')]),
'0.3':(1,[]),'0.4':(1,[]),
'1.0':(1,[]),
'1.1':(1,[n('s4.1.0',w='the Quakers')]),
'1.2':(1,[n('s4.1.1',E,'the Quaker tour of the west')]),
'1.3':(1,[n('s4.1.0',w='the Friends committee')]),
'1.4':(1,[n('s4.1.0',E,'the Central Relief Committee')]),
'1.5':(1,[]),
'1.6':(1,[n('s4.1.3',w='Quaker mass feeding')]),
'1.7':(1,[n('s4.1.0',w='the Central Relief Committee')]),
'2.0':(1,[]),
'2.1':(1,[n('s4.2.0',w='the British Relief Association')]),
'2.2':(1,[n('s4.2.0',E,'the British Relief Association'),n('s3.4.2',w="Routh's commissariat")]),
'2.3':(1,[n('s4.2.0',E,'the British Relief Association')]),
'2.4':(1,[]),'2.5':(2,[]),'2.6':(1,[]),
'3.0':(1,[n('s3.3.6',w='clergy dying of fever')]),
'3.1':(1,[n('s3.3.6',w='clergy dying of fever')]),
'3.2':(1,[n('s3.3.5',w='nursing fever victims')]),
'3.3':(1,[]),
'3.4':(2,[n('s4.3.3',E,'souperism')]),
'3.5':(1,[n('s4.3.3',E,'souperism')]),
'3.6':(1,[n('s4.3.3',E,'souperism')]),
'4.0':(1,[]),
'4.1':(2,[n('s3.6.3',E,'the Gregory clause'),n('s3.6.4',w='landlords clearing estates')]),
'4.2':(1,[n('s4.4.1',w='clearances using the Gregory clause')]),
'4.3':(1,[n('s4.4.1',w='evictions and clearances')]),
'4.4':(2,[]),
'4.5':(1,[n('s4.4.4',w='assisted emigration example')]),
'5.0':(1,[]),'5.1':(1,[]),'5.2':(1,[]),
'5.3':(1,[n('s4.5.1',w='her 1844 tour')]),
'5.4':(1,[n('s4.5.3',w='her relief work')]),
'5.5':(1,[n('s4.3.3',w='proselytisers',c='low')]),
'5.6':(1,[n('s4.5.1',w='her Bible reading')]),
'5.7':(1,[n('s4.5.4',w='participant and witness')]),
'6.0':(1,[n('s4.1.3',w='Quaker soup kitchens'),n('s4.2.3',w="British Relief Association's feeding children")]),
'6.1':(1,[]),'6.2':(2,[]),'6.3':(2,[]),
'6.4':(1,[n('s4.1.6',E,'Quaker withdrawal from feeding'),n('s3.6.2',w='the Poor Law responsible')]),
'7.0':(1,[n('s3.3.8',w='population fall and deaths')]),
'7.1':(1,[n('s3.0.5',w='cottiers')]),
'7.2':(1,[n('s3.1.2',w='holdings under 5 acres')]),
'7.3':(2,[n('s4.4.1',w='bankrupt, indebted landlords')]),
'7.4':(1,[n('s4.7.3',E,'the Encumbered Estates Act')]),
'7.5':(1,[n('s3.2.2',w='pasture farming profitable')]),
'8.0':(1,[n('s3.1.2',w='subdivision of holdings')]),
'8.1':(1,[n('s4.8.0',E,'single-heir inheritance')]),
'8.2':(1,[n('s4.8.1',E,'arranged matches')]),
'8.3':(1,[]),'8.4':(1,[]),'8.5':(1,[]),'8.6':(1,[]),
'9.0':(1,[n('s4.1.5',w='Quaker non-sectarian work')]),
'9.1':(1,[n('s4.0.3',w='weakest in the west')]),
'9.2':(1,[n('s4.3.3',E,'souperism'),n('s4.4.1',E,'landlord clearances')]),
'9.3':(2,[n('s3.3.8',w='deaths and emigration')]),
'9.4':(1,[n('s3.8.6',E,"Mitchel's nationalist view")]),
'9.5':(1,[n('s4.7.5',w='shift to pasture')]),
}
txt=open(P+'packs/hist-ire1-s4.t1g1.txt').read()
tgt=re.findall(r'^\[(hist-ire1-s4\.[^\]]+)\]',txt,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
assert set(D)=={t.split('s4.',1)[1] for t in tgt}, set(D)^{t.split('s4.',1)[1] for t in tgt}
out={}
for t in tgt:
    c,ns=D[t.split('s4.',1)[1]]
    out[t]={'cost':c,'needs':[{'id':i,'strength':s,'why':w,'confidence':cf} for i,s,w,cf in ns]}
for t,v in out.items():
    for x in v['needs']: assert x['id'] in allids and x['id']!=t,x
json.dump(out,open(P+'point-links/hist-ire1-s4.t1g1.json','w'),indent=1)
json.load(open(P+'point-links/hist-ire1-s4.t1g1.json'))
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
