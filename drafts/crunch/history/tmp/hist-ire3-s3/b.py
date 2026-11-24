import json,re,sys
E,H='essential','helpful'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
P='hist-ire3-s3.'
D={
'0.b':(1,[]),
'0.0':(1,[L('hist-ire3-s1.1.1',H,'uses the Ulster Covenant'),L('hist-ire3-s1.1.2',H,'uses the UVF')]),
'0.1':(2,[L('hist-ire3-s1.2.0',E,'county option proposal'),L('hist-ire3-s1.2.2',E,'Buckingham Palace Conference'),L('hist-ire3-s1.6.7',E,'Lloyd George proposals of 1916')]),
'0.2':(1,[L('hist-ire3-s1.6.7',E,'the 1916 Lloyd George plan')]),
'0.3':(1,[L('hist-ire3-s1.6.b',H,'effect of the Rising on opinion','low')]),
'0.4':(1,[L('hist-ire3-s2.2.2',E,'1918 election seat results')]),
'0.5':(2,[L('hist-ire3-s3.0.4',H,'1918 election divide','low')]),
'0.6':(1,[]),
'0.7':(1,[L('hist-ire3-s3.1.0',H,'Government of Ireland Act detail')]),
'1.b':(1,[]),
'1.0':(1,[]),
'1.1':(1,[L('hist-ire3-s3.1.0',E,'the Northern parliament created by the Act')]),
'1.2':(1,[L('hist-ire3-s3.7.3',H,'Craig becoming Prime Minister')]),
'1.3':(1,[L('hist-ire3-s3.1.0',E,'Southern Ireland parliament created by the Act')]),
'1.4':(1,[L('hist-ire3-s3.1.0',H,'Northern Ireland created by the Act')]),
'1.5':(2,[L('hist-ire3-s3.1.4',H,'Treaty opt-out of Northern Ireland')]),
'1.6':(2,[L('hist-ire3-s3.1.5',E,'the Boundary Commission and its members')]),
'1.7':(1,[L('hist-ire3-s3.1.6',E,'the 1925 agreement on the border')]),
'2.b':(1,[]),
'2.0':(1,[]),
'2.1':(1,[]),
'2.2':(1,[L('hist-ire3-s2.3.0',H,'the Dáil that organised the boycott','low')]),
'2.3':(2,[]),
'2.4':(1,[L('hist-ire3-s3.2.3',H,'the Special Constabulary context','low')]),
'2.5':(1,[L('hist-ire3-s3.7.5',H,'Craig negotiating with Collins','low')]),
'2.6':(1,[L('hist-ire3-s3.2.5',H,'internment after the IRA offensive')]),
'2.7':(1,[L('hist-ire3-s3.2.6',H,'internment under the Special Powers Act')]),
'3.b':(1,[]),
'3.0':(1,[L('hist-ire3-s2.2.4',H,'Devlin and the Nationalist Party','low')]),
'3.1':(1,[]),
'3.2':(1,[]),
'3.3':(1,[L('hist-ire3-s3.3.2',H,'earlier abolition of PR locally')]),
'3.4':(1,[L('hist-ire3-s3.3.2',H,'redrawn electoral areas and gerrymandering','low')]),
'3.5':(1,[]),
'3.6':(1,[]),
'4.b':(1,[]),
'4.0':(1,[]),
'4.1':(1,[]),
'4.2':(1,[]),
'4.3':(1,[]),
'4.4':(1,[]),
'4.5':(2,[L('hist-ire3-s3.4.b',H,'the discrimination debate')]),
'4.6':(1,[L('hist-ire3-s3.3.0',H,'nationalist abstention')]),
'5.b':(1,[]),
'5.0':(1,[]),
'5.1':(1,[]),
'5.2':(1,[]),
'5.3':(1,[]),
'5.4':(1,[]),
'5.5':(1,[L('hist-ire3-s3.5.1',H,'unemployment behind the strike')]),
'6.b':(1,[]),
'6.0':(1,[]),
'6.1':(1,[L('hist-ire3-s3.5.0',H,'linen and shipbuilding industries')]),
'6.2':(1,[]),
'6.3':(1,[]),
'6.4':(1,[]),
'6.5':(1,[]),
'7.b':(1,[]),
'7.0':(1,[]),
'7.1':(1,[L('hist-ire3-s1.1.2',H,'uses the UVF'),L('hist-ire3-s1.1.4',E,'the Larne gun-running')]),
'7.2':(1,[]),
'7.3':(1,[L('hist-ire3-s1.1.0',H,'Carson as Unionist leader')]),
'7.4':(1,[]),
'7.5':(1,[L('hist-ire3-s3.1.5',E,'the Boundary Commission'),L('hist-ire3-s3.2.5',H,'Craig-Collins pacts')]),
'7.6':(1,[L('hist-ire3-s3.2.4',E,'creation of the RUC'),L('hist-ire3-s3.2.6',E,'the Special Powers Act'),L('hist-ire3-s3.3.2',E,'abolition of PR')]),
'7.7':(1,[L('hist-ire3-s3.5.3',H,'copying British social policy')]),
'7.8':(1,[]),
'7.9':(2,[]),
'8.b':(1,[]),
'8.0':(1,[L('hist-ire3-s1.1.2',H,'uses the UVF')]),
'8.1':(1,[L('hist-ire3-s3.2.6',E,'the Special Powers Act'),L('hist-ire3-s3.2.4',H,'the RUC')]),
'8.2':(1,[L('hist-ire3-s3.3.2',E,'Local Government Act 1922'),L('hist-ire3-s3.3.3',E,'1929 change for Stormont')]),
'8.3':(1,[L('hist-ire3-s3.2.6',H,'powers under the Special Powers Act')]),
'8.4':(1,[]),
'8.5':(2,[]),
'9.b':(1,[]),
'9.0':(1,[]),
'9.1':(1,[L('hist-ire3-s3.5.3',E,'step-by-step welfare policy')]),
'9.2':(1,[L('hist-ire3-s3.2.6',E,'emergency powers'),L('hist-ire3-s3.2.4',H,'largely Protestant police'),L('hist-ire3-s3.3.2',H,'manipulated electoral rules')]),
'9.3':(1,[L('hist-ire3-s3.3.5',H,'one-party permanent majority')]),
'9.4':(1,[]),
'9.5':(1,[L('hist-ire3-s3.4.5',H,'the discrimination debate among historians')]),
}
sub=sys.argv[1]; pack=sys.argv[2]; out=sys.argv[3]
J={P+k.replace('s3.',''):{"cost":c,"needs":n} for k,(c,n) in D.items()} if False else {}
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
