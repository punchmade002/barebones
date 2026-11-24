import json,re,sys
E,H='essential','helpful'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
S='hist-eur1-s7.'
T='hist-eur1-s8.'
def a(i,s,w,c='high'): return L(i,s,w,c)
D={
'0.b':(1,[]),
'0.0':(1,[]),
'0.1':(1,[L(T+'0.0',E,'repeal of the Combination Acts')]),
'0.2':(1,[L(T+'0.0',H,'union oath banned by combination laws','low')]),
'0.3':(1,[L(T+'1.2',H,'Robert Owen and his ideas','low')]),
'0.4':(1,[]),
'0.5':(2,[L(T+'0.4',H,'New Model unions of skilled workers')]),
'1.0':(1,[]),
'1.1':(1,[L(T+'1.0',H,'what socialism meant')]),
'1.2':(1,[L(T+'1.1',H,'utopian model communities')]),
'1.3':(2,[L(T+'2.2',H,'Marx and Engels drafting the programme')]),
'2.b':(1,[]),
'2.0':(1,[]),
'2.1':(1,[]),
'2.2':(1,[L(T+'1.3',H,'Communist League that commissioned it')]),
'2.3':(1,[]),
'2.4':(1,[]),
'2.5':(1,[L(T+'2.4',H,'class struggle and capitalism theory')]),
'2.6':(1,[]),
'2.7':(1,[L(T+'2.1',H,'Marx as exile in London','low')]),
'2.8':(2,[L(T+'2.4',H,'predictions of revolution')]),
'2.9':(1,[L(T+'2.5',H,'Das Kapital volumes')]),
'3.b':(1,[]),
'3.0':(1,[]),
'3.1':(2,[]),
'3.2':(2,[]),
'3.3':(1,[L(T+'2.4',H,"Marx's workers' state idea",'low')]),
'3.4':(1,[L(T+'2.6',E,'the First International'),L(T+'3.3',H,'Bakunin versus Marx on the state')]),
'3.5':(1,[]),
'3.6':(2,[L(T+'3.3',H,'anarchist tradition')]),
'4.b':(1,[]),
'4.0':(2,[]),
'4.1':(1,[L(T+'4.0',E,'drafted the People\'s Charter')]),
'4.2':(2,[L(T+'4.0',E,'petitions for the Charter')]),
'4.3':(1,[]),
'4.4':(1,[]),
'4.5':(1,[]),
'4.6':(1,[L(T+'6.0',H,'voting rights and the franchise','low')]),
'4.7':(2,[L(T+'6.0',H,'the 1832 Reform Act'),L(S+'5.2',H,'the New Poor Law of 1834')]),
'4.8':(2,[L(T+'4.1',H,'Lovett as moral-force leader','low')]),
'5.b':(1,[]),
'5.0':(1,[]),
'5.1':(1,[L(T+'4.5',H,'National Charter Association')]),
'5.2':(1,[L(T+'4.5',H,'Northern Star newspaper')]),
'5.3':(1,[L(T+'4.2',H,'the Chartist petitions')]),
'5.4':(1,[L(T+'4.6',E,'the National Land Company')]),
'5.5':(1,[L(T+'4.2',H,'the 1848 petition')]),
'5.6':(1,[]),
'5.7':(2,[L(T+'4.8',H,'moral-force versus physical-force split')]),
'6.0':(2,[]),
'6.1':(1,[L(T+'6.0',H,'the 1832 franchise')]),
'6.2':(1,[]),
'7.0':(1,[]),
'7.1':(1,[]),
'7.2':(1,[]),
'7.3':(1,[L(T+'7.0',H,'Peel as Conservative leader')]),
'7.4':(1,[]),
'7.5':(1,[]),
'7.6':(2,[L(S+'5.1',H,'the Corn Laws and their repeal'),L(S+'1.3',E,'the Irish potato famine')]),
'7.7':(1,[L(T+'7.6',E,'repeal of the Corn Laws')]),
'7.8':(2,[L(T+'7.6',E,'repeal of the Corn Laws')]),
'8.0':(1,[L(T+'1.2',E,"Owen's model communities")]),
'8.1':(1,[L(T+'1.2',E,"Owen's co-operation and communal ownership")]),
'8.2':(1,[L(T+'7.1',E,'the Metropolitan Police'),L(T+'7.5',E,'the Bank Charter Act')]),
'8.3':(1,[]),
'9.0':(1,[L(T+'0.1',E,'repeal of the Combination Acts')]),
'9.1':(1,[L(T+'0.0',E,'the Combination Acts'),L(T+'0.2',E,'Tolpuddle sentences'),L(T+'0.3',E,'failure of the GNCTU')]),
'9.2':(1,[L(T+'4.0',H,'the Charter demands later achieved','low')]),
'9.3':(1,[L(T+'4.2',E,'rejected petitions'),L(T+'4.8',H,'divisions and loss of momentum')]),
'9.4':(1,[L(T+'7.1',E,'Metropolitan Police'),L(T+'7.5',E,'Bank Charter Act'),L(T+'7.4',E,'tariff cuts')]),
'9.5':(2,[L(T+'9.4',H,"Peel's state reforms")]),
}
sub=sys.argv[1]; pack=sys.argv[2]; out=sys.argv[3]
J={}
for k,(c,n) in D.items(): J[sub+'.'+k]={"cost":c,"needs":n}
json.dump(J,open(out,'w'),indent=1,ensure_ascii=False)
txt=open(pack).read()
tgt=[]; ids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M)); sec=None
for l in txt.split('\n'):
    if l.startswith('TARGET'): sec='t'
    elif l.startswith('CANDIDATES'): sec='c'
    m=re.match(r'\[([^\]]+)\]',l)
    if m and sec=='t': tgt.append(m.group(1))
j=json.load(open(out))
assert list(j)==tgt,(set(tgt)^set(j))
assert all(n['id'] in ids and n['id']!=k for k,v in j.items() for n in v['needs'])
print(len(j),sum(len(v['needs']) for v in j.values()),sum(v['cost']==2 for v in j.values()),sum(n['confidence']=='low' for v in j.values() for n in v['needs']))
