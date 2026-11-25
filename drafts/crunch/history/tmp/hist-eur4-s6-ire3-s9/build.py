import json,re
B='/Users/gabrielwhelan/barebones/.claude/worktrees/history-crunch/drafts/crunch/history/'
def L(i,s,w,c='high'): return (i,s,w,c)
E,H='essential','helpful'
P1='hist-eur4-s6.'; P2='hist-ire3-s9.'
def build(pre,spec,short):
    out={}
    for k,(cost,links) in spec:
        out[pre+k]={"cost":cost,"needs":[{"id":(i if i.startswith('hist-') else pre+i),"strength":s,"why":w,"confidence":c} for i,s,w,c in links]}
    return out
s1=[
('0.b',(1,[])),('0.0',(1,[])),('0.1',(1,[])),('0.2',(1,[])),('0.3',(1,[])),('0.4',(1,[])),
('1.b',(1,[])),('1.0',(1,[])),('1.1',(1,[])),('1.2',(1,[])),('1.3',(1,[])),('1.4',(2,[])),('1.5',(1,[])),
('1.6',(1,[L('hist-eur4-s1.9.1',H,'communism feeds on poverty'),L('2.0',H,'the Marshall Plan offer','low')])),
('2.b',(1,[])),
('2.0',(1,[L('hist-eur4-s1.10.0',H,'Molotov and the Paris talks')])),
('2.1',(1,[])),('2.2',(2,[L('2.0',H,'the Marshall aid offer')])),
('2.3',(1,[L('1.3',E,'the dollar gap')])),('2.4',(1,[])),
('2.5',(1,[L('2.1',E,'uses the OEEC')])),
('3.b',(1,[])),('3.0',(1,[L('0.1',H,'protectionism of the 1930s')])),
('3.1',(1,[])),('3.2',(1,[])),
('3.3',(1,[L('hist-eur4-s1.7.2',H,'containment policy','low'),L('1.6',H,'communist threat in France, Italy','low')])),
('3.4',(2,[])),('3.5',(2,[L('1.3',H,'the dollar shortage')])),
('4.b',(1,[])),('4.0',(2,[])),('4.1',(1,[L('4.0',E,'fixed rates from Bretton Woods')])),
('4.2',(2,[L('0.1',H,'tariffs and protectionism')])),
('4.3',(1,[L('4.2',E,'the GATT rounds')])),
('4.4',(1,[L('1.3',H,'the dollar gap')])),
('5.b',(1,[])),('5.0',(2,[])),('5.1',(1,[])),('5.2',(2,[])),
('5.3',(2,[L('5.2',E,'uses the EEC')])),
('5.4',(2,[L('0.4',H,'common external tariff')])),
('6.b',(1,[])),('6.0',(1,[])),
('6.1',(1,[L('6.0',E,'currency reform "days later"')])),
('6.2',(1,[L('6.1',E,'uses Erhard')])),
('6.3',(1,[L('6.0',E,'currency reform and price reform')])),
('6.4',(1,[L('6.3',H,'the Wirtschaftswunder')])),
('7.b',(1,[])),('7.0',(2,[])),
('7.1',(1,[L('7.0',E,'the Commissariat and plans')])),
('7.2',(1,[])),('7.3',(2,[])),('7.4',(1,[])),('7.5',(2,[])),
('8.b',(1,[])),('8.0',(1,[])),('8.1',(2,[])),('8.2',(1,[])),
('8.3',(1,[L('8.1',H,'West German guest workers')])),
('8.4',(1,[L('8.1',H,'guest workers')])),
('9.b',(1,[])),('9.0',(1,[])),('9.1',(1,[])),('9.2',(1,[])),
('9.3',(2,[L('9.2',H,'Commonwealth migration')])),
('9.4',(1,[L('9.2',H,'Commonwealth migrants')])),
('9.5',(1,[L('9.4',H,'discrimination faced by migrants')])),
('9.6',(1,[])),('9.7',(1,[])),
('10.b',(1,[])),('10.0',(2,[])),
('10.1',(1,[L('10.0',H,'national insurance idea')])),
('10.2',(1,[])),
('10.3',(1,[L('10.1',E,'Attlee government')])),
('10.4',(1,[])),
('11.b',(1,[])),('11.0',(1,[])),
('11.1',(1,[L('6.2',H,'social market economy')])),
('11.2',(1,[])),('11.3',(1,[])),('11.4',(1,[])),
('12.b',(1,[])),
('12.0',(1,[L('8.1',H,'guest workers')])),
('12.1',(1,[])),
('12.2',(1,[L('2.2',H,'Marshall Aid')])),
('12.3',(1,[L('0.1',H,'full employment aim')])),
('12.4',(1,[])),
('12.5',(1,[L('1.3',H,'the dollar shortage')])),
('12.6',(1,[L('7.4',H,'stop-go policy')])),
('12.7',(1,[L('4.1',H,'fixed exchange rates')])),
('13.b',(1,[])),('13.0',(1,[])),
('13.1',(1,[L('4.0',H,'dollar-based Bretton Woods system')])),
('13.2',(1,[L('4.0',E,'Bretton Woods system')])),
('13.3',(1,[])),
('13.4',(2,[L('3.4',E,'Milward argument')])),
('13.5',(1,[L('7.5',H,'catching up with US methods')])),
]
s9=[
('0.b',(1,[])),
('0.0',(1,[L('hist-ire3-s3.1.0',H,'the Government of Ireland Act')])),
('0.1',(1,[L('hist-ire3-s8.0.3',H,'the Emergency')])),
('0.2',(1,[])),('0.3',(1,[])),('0.4',(1,[])),
('0.5',(2,[L('0.4',E,'conscription not applied')])),
('0.6',(2,[])),
('0.7',(1,[L('0.6',E,'Tom Williams execution')])),
('1.b',(1,[])),
('1.0',(1,[L('hist-ire3-s3.7.2',H,'Craig as Prime Minister')])),
('1.1',(1,[L('1.0',E,'Andrews as Prime Minister')])),
('1.2',(2,[L('1.1',E,'criticism of Andrews')])),
('1.3',(2,[L('1.2',H,'Andrews resigning')])),
('1.4',(1,[L('1.3',E,'Brooke as Prime Minister')])),
('2.b',(1,[])),
('2.0',(1,[L('hist-ire3-s3.5.0',H,'shipbuilding and linen')])),
('2.1',(1,[])),('2.2',(1,[])),('2.3',(1,[])),
('2.4',(1,[L('hist-ire3-s8.5.2',H,'compulsory tillage orders','low')])),
('2.5',(1,[L('2.0',H,'war orders end unemployment')])),
('2.6',(1,[])),('2.7',(1,[])),
('3.b',(1,[])),('3.0',(1,[])),
('3.1',(1,[L('2.1',H,'the shipyard')])),
('3.2',(1,[L('3.0',H,'Belfast in bomber range')])),
('3.3',(1,[])),('3.4',(1,[])),
('3.5',(1,[L('3.2',H,'assumption of safety')])),
('3.6',(1,[])),
('3.7',(1,[L('hist-ire3-s3.5.4',H,'slum housing in Belfast')])),
('4.b',(1,[])),('4.0',(1,[])),('4.1',(1,[])),
('4.2',(1,[L('4.1',E,'the Easter Tuesday raid')])),
('4.3',(1,[])),('4.4',(1,[])),('4.5',(1,[])),
('5.b',(1,[])),('5.0',(1,[])),
('5.1',(2,[L('hist-ire3-s8.10.3',H,'southern fire brigades went north')])),
('5.2',(1,[L('hist-ire3-s8.0.b',E,'the South was neutral')])),
('5.3',(1,[])),
('6.b',(1,[])),('6.0',(1,[])),('6.1',(1,[])),('6.2',(1,[])),('6.3',(1,[])),
('6.4',(1,[L('1.2',E,'Andrews ending his premiership')])),
('7.b',(1,[])),('7.0',(1,[])),('7.1',(1,[])),('7.2',(1,[])),('7.3',(1,[])),('7.4',(1,[])),
('8.b',(1,[])),('8.0',(1,[L('3.7',H,'housing damage')])) ,
('8.1',(2,[L('hist-ire3-s3.5.3',H,'step by step policy with Britain')])),
('8.2',(1,[L('hist-ire3-s3.3.5',H,'Unionist domination at Stormont','low')])),
('8.3',(1,[L('8.2',E,'Labour win in Belfast West')])),
('8.4',(2,[L('8.1',H,'Beveridge and welfare reform')])),
('8.5',(1,[L('hist-ire3-s3.3.3',H,'electoral system changes','low')])),
('9.b',(1,[])),('9.0',(1,[])),('9.1',(1,[])),('9.2',(1,[])),
('9.3',(1,[L('hist-ire3-s3.3.5',H,'Unionist control of Stormont','low')])),
('9.4',(1,[L('8.1',H,'welfare reform promise')])),
('9.5',(1,[])),
('10.b',(1,[])),('10.0',(1,[])),
('10.1',(1,[L('8.1',H,'the post-war welfare state')])),
('10.2',(1,[])),
('10.3',(1,[L('hist-ire3-s3.4.b',H,'discrimination against Catholics')])),
('10.4',(1,[])),('10.5',(1,[])),
]
for pre,spec,name in ((P1,s1,'hist-eur4-s6.t1g1'),(P2,s9,'hist-ire3-s9.t1g1')):
    out=build(pre,spec,name)
    txt=open(B+'packs/'+name+'.txt').read()
    ids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    tgt=[m for m in re.findall(r'^\[([^\]]+)\]',txt.split('CANDIDATES')[0],re.M)]
    assert list(out)==tgt,(set(tgt)^set(out))
    n=lc=c2=0
    for k,v in out.items():
        n+=1;c2+=v['cost']==2
        for x in v['needs']:
            lc+=1;assert x['id'] in ids and x['id']!=k,(k,x)
    json.dump(out,open(B+'point-links/'+name.replace('.t1g1','')+'.t1g1.json','w'),indent=1)
    low=sum(x['confidence']=='low' for v in out.values() for x in v['needs'])
    print(name,n,lc,c2,low)
