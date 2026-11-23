import json,re
E,H='essential','helpful'
def n(i,s,w,c='high'):return {"id":i if '.' in i and i.startswith('bio') else 'bio18-s4.'+i,"strength":s,"why":w,"confidence":c}
d={
'0.b':(1,[]),
'0.0':(1,[]),
'0.1':(1,[n('0.0',H,'joint definition')]),
'0.2':(1,[n('0.0',H,'joint definition')]),
'0.3':(1,[n('0.0',H,'joint definition')]),
'1.b':(1,[n('0.3',E,'freely movable joints')]),
'1.0':(1,[n('0.3',H,'freely movable joint')]),
'1.1':(1,[n('0.3',H,'freely movable joint')]),
'1.2':(2,[n('0.3',H,'freely movable joint')]),
'1.3':(1,[n('0.3',H,'freely movable joint')]),
'2.b':(1,[n('0.3',E,'synovial joint')]),
'2.0':(1,[n('0.3',E,'synovial joint cavity')]),
'2.1':(1,[n('2.0',E,'articular cartilage')]),
'2.2':(1,[n('2.0',E,'articular cartilage'),n('2.4',H,'synovial fluid')]),
'2.3':(1,[n('3.0',H,'joint capsule')]),
'2.4':(1,[n('2.3',H,'membrane secretes the fluid')]),
'2.5':(1,[n('2.4',E,'synovial fluid'),n('2.2',H,'cartilage lacks blood supply')]),
'3.b':(1,[]),
'3.0':(1,[n('2.4',H,'synovial fluid')]),
'3.1':(1,[]),
'3.2':(1,[n('3.1',E,'ligament structure')]),
'3.3':(1,[n('3.1',E,'ligament definition'),n('3.0','helpful','capsule','low')]),
'3.4':(1,[]),
'3.5':(1,[n('3.4',E,'tendon structure')]),
'3.6':(1,[n('2.0',H,'cartilage at joints')]),
'3.7':(2,[n('3.0',H,'joint capsule'),n('2.0',H,'articular cartilage')]),
'4.b':(1,[n('0.3',H,'synovial joint')]),
'4.0':(1,[n('2.0',E,'articular cartilage'),n('2.4',H,'synovial fluid')]),
'4.1':(1,[n('3.2',E,'ligament function')]),
'4.2':(1,[n('3.5',E,'tendon transmits pull')]),
'5.b':(1,[]),
'5.0':(1,[n('3.1',E,'ligament definition'),n('3.4',E,'tendon definition'),n('2.0',E,'articular cartilage')]),
'5.1':(2,[n('3.2',E,'ligament elasticity'),n('3.5',E,'tendon inelastic'),n('2.1',H,'cartilage absorbs shock')]),
'5.2':(2,[n('3.2',E,'ligament function'),n('3.5',E,'tendon function'),n('2.1',E,'cartilage function')]),
'6.b':(1,[]),
'6.0':(1,[]),
'6.1':(2,[n('6.0',E,'muscle only pulls')]),
'6.2':(1,[n('6.1',H,'antagonistic pair')]),
'6.3':(2,[n('3.4',E,'tendons join muscle to bone')]),
'6.4':(1,[n('6.3',E,'origin and insertion')]),
'7.b':(1,[n('6.1',E,'antagonistic pair')]),
'7.0':(1,[n('6.3',E,'origin and insertion')]),
'7.1':(1,[n('6.3',E,'origin and insertion')]),
'7.2':(2,[n('6.2',E,'flexion and flexor'),n('6.4',H,'contraction moves bone')]),
'7.3':(2,[n('6.2',E,'extension and extensor'),n('7.2',H,'opposite of flexion')]),
'7.4':(1,[n('6.2',E,'flexor and extensor')]),
'8.b':(1,[n('6.1',H,'antagonistic pair')]),
'8.0':(1,[n('1.1',H,'elbow hinge joint')]),
'8.1':(2,[n('8.0',E,'lever and pivot'),n('7.0',H,'biceps insertion')]),
'8.2':(1,[n('6.1',E,'antagonistic pair'),{"id":"bio19-s1.1.1","strength":H,"why":"motor neurons carry impulses","confidence":"high"}]),
'8.3':(1,[n('6.1',E,'antagonistic pair')]),
'8.4':(2,[n('7.2',E,'bending the arm'),n('7.3',E,'straightening the arm')]),
'9.b':(1,[n('6.1',H,'antagonistic pair')]),
'9.0':(1,[n('1.1',H,'hinge joint')]),
'9.1':(2,[n('6.3',E,'origin and insertion')]),
'9.2':(1,[n('7.2',H,'flexion of arm')]),
'9.3':(1,[n('7.3',H,'extension of arm')]),
'9.4':(1,[n('6.0',E,'muscle only pulls')]),
'9.5':(2,[n('8.1',E,'lever action')]),
'10.b':(1,[n('9.b',H,'the arm model')]),
'10.0':(1,[n('6.4',H,'muscles shorten and fatten')]),
'10.1':(1,[n('2.1',H,'cartilage reduces friction')]),
'10.2':(1,[n('1.2',H,'radius rotation, pivot joint')]),
'10.3':(1,[{"id":"bio19-s1.0.5","strength":H,"why":"nerve impulses","confidence":"low"}]),
'10.4':(1,[n('3.4',E,'tendons are inelastic')]),
}
out={}
for k,(c,ns) in d.items():
    out['bio18-s4.'+k]={"cost":c,"needs":ns}
open('../../point-links/bio18-s4.json','w').write(json.dumps(out,indent=0))
# validate
pkg=open('../../points/bio18-s4.txt').read()
ids=re.findall(r'^\[([^\]]+)\]',pkg,re.M)
tg=[i for i in ids if i.startswith('bio18-s4.')]
o=json.load(open('../../point-links/bio18-s4.json'))
assert list(o)==tg,(set(tg)^set(o))
L=[x for v in o.values() for x in v['needs']]
assert all(x['id'] in ids for x in L)
assert all(x['id']!=k for k,v in o.items() for x in v['needs'])
print(len(o),len(L),sum(v['cost']==2 for v in o.values()),sum(x['confidence']=='low' for x in L))
