import json,re
h='helpful';e='essential';H='high';L='low'
P='/Users/gabrielwhelan/barebones/drafts/crunch/history/'
pre='hist-ire4-s1.'
def n(i,s,w,c=H): return (pre+i,s,w,c)
D=[
('0.b',1,[]),('0.0',1,[]),('0.1',1,[]),('0.2',1,[]),
('0.3',1,[n('0.2',h,'earlier Protestant emigrants contrasted')]),
('0.4',1,[]),('0.5',1,[]),('0.6',1,[]),
('1.0',1,[]),('1.1',1,[]),('1.2',1,[]),('1.3',1,[]),('1.4',2,[]),('1.5',1,[]),
('1.6',1,[n('0.4',h,'cheap fares to Canada')]),
('2.b',1,[]),('2.0',2,[]),
('2.1',2,[n('2.0',e,'the blight and failed crop')]),
('2.2',1,[]),('2.3',2,[]),
('2.4',1,[n('1.4',h,'population of 8.2 million in 1841')]),
('2.5',2,[n('0.3',h,'Catholic emigrants from south and west')]),
('2.6',1,[n('0.5',h,'cheap crossing to Liverpool')]),
('2.7',1,[n('2.6',h,'arrival at Liverpool in 1847')]),
('3.0',1,[]),
('3.1',1,[n('3.0',h,'public works it replaced')]),
('3.2',2,[]),
('3.3',1,[n('3.2',e,'Poor Law rates and the Gregory clause')]),
('3.4',1,[n('3.3',h,'clearing tenants to avoid rates')]),
('3.5',2,[n('3.4',e,'landlord assisted emigration')]),
('3.6',2,[n('3.4',e,'landlord assisted emigration')]),
('3.7',1,[n('3.4',h,'assisted emigration schemes')]),
('3.8',1,[n('3.3',h,'landlord clearances','low')]),
('4.0',1,[]),
('4.1',1,[n('4.0',e,'pre-paid passages')]),
('4.2',1,[]),
('4.3',1,[n('4.2',h,'chain emigration')]),
('4.4',1,[n('4.2',h,'chain emigration','low')]),
('5.0',1,[]),
('5.1',1,[n('0.4',h,'cheap fares to Canada')]),
('5.2',2,[n('5.1',e,'cheaper Quebec fares')]),
('5.3',1,[]),
('5.4',1,[n('5.3',h,'steerage conditions')]),
('5.5',2,[n('5.4',h,'deaths from typhus at sea')]),
('5.6',1,[]),
('6.b',1,[]),('6.0',1,[]),('6.1',1,[]),('6.2',1,[]),
('6.3',1,[n('6.2',h,'running the quarantine station')]),
('6.4',1,[n('6.2',h,'the station\'s inspection function','low')]),
('7.0',1,[n('6.4',h,'limited hospital capacity')]),
('7.1',1,[n('7.0',h,'ships queuing from mid-May')]),
('7.2',1,[n('6.2',h,'inspection at Grosse Isle')]),
('7.3',1,[n('7.1',h,'ships anchored waiting')]),
('7.4',2,[n('6.3',e,'Dr Douglas')]),
('7.5',1,[]),('7.6',1,[]),
('7.7',1,[n('7.2',h,'typhus spreading among healthy passengers')]),
('7.8',1,[n('7.6',h,'orphans of the 1847 deaths','low')]),
('8.0',1,[n('6.b',h,'quarantine stations')]),
('8.1',2,[n('5.2',e,'US Passenger Acts diverting emigrants')]),
('8.2',1,[n('7.6',h,'the dead of 1847')]),
('8.3',2,[]),('8.4',1,[]),
('8.5',2,[n('7.6',h,'deaths on Grosse Isle','low')]),
('8.6',2,[n('7.8',h,'French-Canadian generosity','low')]),
('9.0',1,[n('2.3',h,'mass Famine emigration')]),
('9.1',2,[n('3.5',h,'Mahon\'s assisted emigration')]),
('9.2',2,[n('8.5',h,'John Mitchel\'s view')]),
('9.3',2,[]),('9.4',2,[]),
('9.5',1,[n('2.3',h,'most emigrants went to US and Britain')]),
]
pk='hist-ire4-s1.t1g1.txt'
t=open(P+'packs/'+pk).read()
ids=re.findall(r'^\[('+re.escape(pre)+r'[^\]]*)\]',t,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',t,re.M))
r={pre+k:{'cost':c,'needs':[{'id':i,'strength':s,'why':w,'confidence':cf} for i,s,w,cf in ls]} for k,c,ls in D}
assert list(r)==ids,set(ids)^set(r)
for k,v in r.items():
    for x in v['needs']: assert x['id'] in allids and x['id']!=k
json.dump(r,open(P+'point-links/hist-ire4-s1.t1g1.json','w'),indent=1)
print(len(r),sum(len(v['needs']) for v in r.values()),sum(v['cost']==2 for v in r.values()),sum(x['confidence']=='low' for v in r.values() for x in v['needs']))
