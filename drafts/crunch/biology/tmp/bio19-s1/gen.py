import json,re
P='bio19-s1.'
E,H='essential','helpful'
# id: (cost, [(target,strength,why,conf)])
d={
'0.b':(1,[]),'0.0':(1,[]),
'0.1':(1,[('0.0',E,'defined relative to the CNS','high')]),
'0.2':(1,[('0.0',H,'CNS as brain and spinal cord','high')]),
'0.3':(1,[('0.5',E,'nerve impulses','high'),('0.0',H,'CNS','high')]),
'0.4':(1,[]),
'0.5':(1,[('0.4',H,'neuron','high')]),
'1.b':(1,[]),
'1.0':(1,[('0.4',E,'neuron','high')]),
'1.1':(1,[('0.4',E,'neuron','high')]),
'1.2':(1,[('0.4',E,'nerves as bundles of fibres','high')]),
'1.3':(1,[('1.2',H,'spinal nerves are nerves','low')]),
'1.4':(2,[('1.3',E,'spinal nerves','high')]),
'1.5':(1,[('1.4',E,'roots of spinal nerve','high')]),
'1.6':(1,[('1.4',E,'roots of spinal nerve','high')]),
'2.b':(1,[]),
'2.0':(2,[('1.5',E,'dorsal root','high')]),
'2.1':(2,[('1.6',E,'ventral root','high'),('4.1',H,'grey matter','low')]),
'2.2':(1,[('0.0',H,'CNS as brain and spinal cord','high')]),
'3.b':(1,[]),
'3.0':(1,[('1.0',H,'sensory and motor impulses','low')]),
'3.1':(1,[('3.0',H,'spinal cord function','low')]),
'4.b':(1,[]),'4.0':(1,[]),
'4.1':(1,[('4.0',H,'central canal position','high')]),
'4.2':(1,[('4.1',H,'surrounds the grey matter','high')]),
'4.3':(2,[('4.1',E,'grey matter','high')]),
'4.4':(2,[('4.2',E,'white matter','high')]),
'4.5':(1,[('4.1',E,'grey matter','high')]),
'4.6':(2,[('4.1',E,'grey and white matter layout','high'),('1.5',H,'dorsal root','low')]),
'5.b':(1,[]),'5.0':(1,[]),
'5.1':(1,[('3.b',H,'spinal cord in vertebral column','low')]),
'5.2':(1,[]),
'5.3':(1,[('5.2',E,'meninges','high')]),
'5.4':(1,[('5.3',E,'cerebrospinal fluid','high')]),
'5.5':(1,[('5.2',E,'meninges','high')]),
'6.b':(1,[]),'6.0':(1,[]),
'6.1':(2,[('6.0',E,'cerebrum','high')]),
'6.2':(1,[('6.0',E,'cerebral hemispheres','high')]),
'6.3':(1,[('6.0',H,'cerebrum','high')]),
'6.4':(1,[('6.0',H,'cerebrum','high')]),
'7.b':(1,[]),
'7.0':(1,[('6.0',H,'position relative to cerebrum','high')]),
'7.1':(1,[('7.0',E,'cerebellum','high')]),
'8.b':(1,[]),
'8.0':(1,[('3.b',H,'joins the spinal cord','low')]),
'8.1':(1,[('8.0',E,'medulla oblongata','high')]),
'8.2':(1,[('8.0',E,'medulla oblongata','high')]),
'9.b':(1,[]),
'9.0':(1,[('6.0',H,'position below cerebrum','high')]),
'9.1':(2,[('9.0',E,'hypothalamus','high')]),
'9.2':(1,[('9.0',E,'hypothalamus','high')]),
'10.b':(1,[]),
'10.0':(2,[('6.0',H,'cerebrum','high'),('7.0',H,'cerebellum','high'),('8.0',H,'medulla oblongata','high'),('9.0',H,'hypothalamus','high')]),
}
txt=open('../../points/bio19-s1.txt').read()
ids=re.findall(r'^\[(bio19-s1\.[^\]]+)\]',txt,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
out={}
for i in ids:
    c,n=d[i[len(P):]]
    out[i]={'cost':c,'needs':[{'id':P+t,'strength':s,'why':w,'confidence':f} for t,s,w,f in n]}
assert set(d)=={i[len(P):] for i in ids}
for v in out.values():
    for n in v['needs']: assert n['id'] in allids
json.dump(out,open('../../point-links/bio19-s1.json','w'),indent=1)
l=[n for v in out.values() for n in v['needs']]
print(len(out),len(l),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for n in l))
