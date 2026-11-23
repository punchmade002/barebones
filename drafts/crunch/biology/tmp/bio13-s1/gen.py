import json,re
P='bio13-s1.'
E,H='essential','helpful'
# id: (cost, [(target,strength,why,conf)])
d={
'0.b':(1,[]),'0.0':(1,[]),
'0.1':(1,[('0.0',H,'catalyst definition','high')]),
'0.2':(1,[('0.0',E,'catalyst definition','high')]),
'0.3':(2,[('bio8-s2.8.5',H,'globular proteins','high'),('bio8-s2.8.0',H,'tertiary structure folding','low')]),
'0.4':(1,[('bio8-s2.7.6',H,'gene sets amino-acid sequence','low')]),
'1.b':(1,[('0.2',H,'enzyme as biological catalyst','high')]),
'1.0':(1,[('0.0',H,'catalyst reused','high')]),
'1.1':(1,[('0.0',E,'catalyst unchanged','high')]),
'1.2':(2,[('4.2',E,'active site','high'),('4.0',H,'substrate','low')]),
'1.3':(1,[('bio8-s2.8.3',E,'denaturation','high')]),
'2.b':(1,[]),
'2.0':(1,[('4.0',E,'substrate','high')]),
'2.1':(1,[('2.0',H,'-ase naming rule','high')]),
'2.2':(1,[]),
'2.3':(1,[('2.2',H,'intracellular contrast','low')]),
'3.b':(1,[('3.0',H,'activation energy','high')]),
'3.0':(1,[]),
'3.1':(1,[('3.0',E,'activation energy','high')]),
'3.2':(1,[('3.0',E,'activation energy','high')]),
'3.3':(1,[('3.2',H,'slow reactions at body temperature','high')]),
'3.4':(2,[('3.0',E,'activation energy','high')]),
'3.5':(1,[('3.4',H,'lowered activation energy','high')]),
'3.6':(2,[('3.0',E,'activation energy','high')]),
'3.7':(2,[('3.6',E,'energy-profile graph','high')]),
'4.b':(1,[]),'4.0':(1,[]),
'4.1':(1,[('4.0',H,'substrate and products','high')]),
'4.2':(1,[('4.0',E,'substrate','high')]),
'4.3':(2,[('4.2',E,'active site','high')]),
'4.4':(1,[('4.3',E,'complementary shape','high')]),
'5.b':(1,[('4.2',H,'active site','high')]),
'5.0':(2,[('4.2',E,'active site','high')]),
'5.1':(1,[('5.0',H,'enzyme-substrate binding','high')]),
'5.2':(2,[('3.0',E,'activation energy','high')]),
'5.3':(1,[('5.0',E,'enzyme-substrate complex','high')]),
'5.4':(1,[('4.3',E,'complementary shape','high')]),
'5.5':(1,[('5.4',E,'products released','high')]),
'5.6':(1,[('5.0',H,'enzyme-substrate complex','high')]),
'5.7':(2,[('5.0',E,'three-stage mechanism','high')]),
'6.b':(1,[('4.2',H,'active site mechanism','low')]),
'6.0':(1,[('bio8-s1.2.3',E,'catabolism breaks molecules down','high')]),
'6.1':(2,[('bio8-s1.2.1',E,'anabolism builds molecules','high')]),
'6.2':(1,[('6.1',H,'anabolic joining reaction','high')]),
'7.b':(1,[('4.3',H,'active-site shape','high')]),
'7.0':(1,[('4.3',E,'complementary shape','high')]),
'7.1':(1,[('7.0',E,'specificity','high')]),
'7.2':(1,[('4.3',E,'complementary fit','high')]),
'7.3':(1,[('7.2',E,'lock-and-key model','high')]),
'7.4':(1,[('7.0',E,'specificity','high')]),
'7.5':(1,[('bio8-s2.8.3',E,'denaturation','high')]),
'7.6':(2,[('bio8-s2.7.6',E,'amino-acid sequence set by gene','high')]),
'8.b':(1,[('bio8-s1.2.0',H,'metabolism','high')]),
'8.0':(1,[('bio8-s1.2.0',H,'metabolism','high')]),
'8.1':(1,[('3.2',H,'reactions too slow','high')]),
'8.2':(2,[('8.0',H,'enzyme per reaction','low')]),
'8.3':(1,[('8.2',E,'metabolic pathways','high')]),
'8.4':(1,[('8.2',E,'metabolic pathway','high')]),
'9.b':(1,[('8.2',H,'pathway steps','high')]),
'9.0':(2,[('0.4',H,'genes code for enzymes','low')]),
'9.1':(1,[('8.2',E,'metabolic pathway','high')]),
'9.2':(1,[]),
'10.b':(1,[]),
'10.0':(1,[('4.2',H,'enzyme blocked','low')]),
'10.1':(2,[('bio8-s2.2.5',H,'lactose sugar','high')]),
'10.2':(1,[('10.1',E,'lactase digests lactose','high')]),
'10.3':(2,[('bio8-s2.7.1',H,'amino acids','high')]),
'10.4':(1,[('10.3',E,'PKU','high')]),
}
txt=open('../../points/bio13-s1.txt').read()
tids=[]
for l in txt.split('\nCANDIDATES')[0].splitlines():
    m=re.match(r'\[(.+?)\]',l)
    if m: tids.append(m.group(1))
allids=set(re.findall(r'^\[(.+?)\]',txt,re.M))
f=lambda x:x if x.startswith('bio') else P+x
out={}
for t in tids:
    c,n=d[t[len(P):]]
    out[t]={'cost':c,'needs':[{'id':f(a),'strength':s,'why':w,'confidence':q} for a,s,w,q in n]}
assert set(out)==set(tids) and len(d)==len(tids)
for t,v in out.items():
    for n in v['needs']: assert n['id'] in allids and n['id']!=t,(t,n)
json.dump(out,open('../../point-links/bio13-s1.json','w'),indent=1)
L=[n for v in out.values() for n in v['needs']]
print(len(out),len(L),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for n in L))
