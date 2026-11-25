import json,re
H='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
E='essential';L='helpful'
P='hist-ire2-s11.'
def n(i,s,w,c='high'):return (P+i,s,w,c)
A={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),'0.2':(1,[n('0.1',L,'evidence behind accounts')]),'0.3':(1,[]),
'0.4':(1,[n('0.1',E,'what counts as evidence')]),'0.5':(2,[n('0.4',E,'source versus evidence')]),
'1.b':(1,[]),'1.0':(1,[]),'1.1':(1,[]),'1.2':(1,[]),'1.3':(2,[]),'1.4':(1,[]),'1.5':(1,[]),
'1.6':(1,[n('1.0',L,'state records'),n('1.1',L,'organisation papers')]),
'1.7':(1,[n('1.3',L,'newspapers and pamphlets')]),
'2.b':(1,[]),'2.0':(1,[]),'2.1':(1,[]),'2.2':(1,[]),'2.3':(1,[]),'2.4':(1,[]),
'3.b':(1,[]),'3.0':(1,[n('0.4',L,'source as evidence for a question')]),
'3.1':(1,[n('1.6',L,'archives, libraries, museums')]),
'3.2':(1,[n('2.b',E,'the five source questions')]),
'3.3':(1,[]),'3.4':(1,[n('0.2',L,'historian interpretations')]),
'3.5':(1,[n('3.4',E,'the interpretation being tested')]),
'3.6':(1,[n('3.3',L,'comparing sources')]),
'4.b':(1,[]),'4.0':(1,[]),'4.1':(1,[n('4.0',L,'primary sources')]),
'4.2':(1,[n('4.0',E,'primary source'),n('4.1',E,'secondary source')]),
'4.3':(1,[n('4.0',E,'primary source'),n('4.1',E,'secondary source')]),
'5.b':(1,[]),'5.0':(1,[]),'5.1':(1,[]),'5.2':(1,[n('5.1',L,'opinion versus fact')]),
'5.3':(1,[n('5.2',E,'bias defined there')]),
'6.b':(1,[n('5.2',L,'bias')]),'6.0':(1,[n('5.2',L,'bias contrasted')]),
'6.1':(1,[n('5.2',E,'bias'),n('6.0',E,'propaganda')]),
'6.2':(1,[]),
'7.b':(1,[]),'7.0':(1,[]),'7.1':(1,[]),'7.2':(1,[n('0.3',L,'accounts revised')]),
'7.3':(2,[n('0.3',L,'Pigott forgeries example')]),
'8.b':(1,[]),'8.0':(1,[]),'8.1':(1,[]),'8.2':(1,[]),
'8.3':(1,[n('8.2',E,'part (d) marks')]),
'8.4':(1,[n('8.0',L,'parts (a) to (c)')]),
'8.5':(1,[n('4.0',E,'primary source'),n('5.1',L,'fact and opinion')]),
'8.6':(1,[n('6.0',E,'propaganda'),n('6.2',L,'objectivity')]),
'9.b':(1,[]),'9.0':(1,[]),'9.1':(1,[]),'9.2':(1,[]),'9.3':(1,[]),'9.4':(1,[]),
'10.b':(1,[]),'10.0':(1,[]),'10.1':(1,[n('10.0',E,'chosen point of comparison')]),
'10.2':(1,[n('10.1',L,'first document comparison')]),'10.3':(1,[]),
'10.4':(1,[n('2.0',L,'authors positions')]),
'10.5':(1,[n('2.4',L,'audience affects content')]),'10.6':(1,[]),
'11.b':(1,[]),'11.0':(1,[]),'11.1':(1,[]),'11.2':(1,[]),
'11.3':(1,[n('11.0',L,'provenance as one test')]),
'11.4':(1,[]),'11.5':(1,[n('5.3',L,'biased source still useful')]),
'11.6':(1,[]),
'11.7':(1,[n('5.0',L,'fact versus opinion'),n('6.0',L,'propaganda defined')]),
'12.b':(1,[]),'12.0':(2,[]),'12.1':(1,[]),'12.2':(1,[]),'12.3':(1,[]),
'12.4':(1,[n('5.1',L,'opinion versus record')]),
'12.5':(1,[]),'12.6':(1,[]),
'12.7':(1,[n('12.6',L,'photographs can mislead')]),
'13.b':(1,[n('8.2',L,'part (d)')]),'13.0':(1,[]),'13.1':(1,[]),'13.2':(1,[]),'13.3':(1,[]),'13.4':(1,[]),'13.5':(1,[]),'13.6':(1,[]),
'14.b':(1,[]),'14.0':(2,[]),'14.1':(2,[n('14.0',L,'continues the same case study')]),
'14.2':(2,[]),'14.3':(2,[]),'14.4':(2,[]),'14.5':(2,[]),'14.6':(2,[]),
'15.b':(1,[]),'15.0':(2,[]),'15.1':(2,[]),'15.2':(2,[]),
'16.b':(1,[]),
'16.0':(1,[n('9.b',L,'part (a) comprehension')]),
'16.1':(1,[n('10.b',L,'comparison part')]),
'16.2':(1,[n('11.b',L,'criticism part')]),
'16.3':(1,[n('13.b',L,'part (d) essay')]),
'16.4':(1,[]),'16.5':(1,[]),
}
t=open(H+'packs/hist-ire2-s11.t1g1.txt').read()
ids=re.findall(r'^\[(\S+)\]',t,re.M)
assert set(ids)=={P+k for k in A} and len(ids)==len(A),set(ids)^{P+k for k in A}
d={}
for i in ids:
    c,nl=A[i[len(P):]]
    for x in nl: assert x[0] in ids and x[0]!=i,x
    d[i]={'cost':c,'needs':[{'id':a,'strength':b,'why':w,'confidence':f} for a,b,w,f in nl]}
json.dump(d,open(H+'point-links/hist-ire2-s11.t1g1.json','w'),indent=1)
print(len(d),sum(len(v['needs']) for v in d.values()),sum(v['cost']==2 for v in d.values()),0)
