import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/biology/'
txt=open(P+'points/bio18-s3.txt').read()
head,cand=txt.split('\nCANDIDATES',1)
tids=re.findall(r'^\[([^\]]+)\]',head,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
p='bio18-s3.'
# id: (cost, [(need, strength, why, conf)])
E,H='essential','helpful'
S={
'0.b':(1,[('bio18-s2.0.0',H,'axial skeleton parts','high')]),
'0.0':(1,[]),
'0.1':(1,[('bio18-s1.0.2',H,'bones as levers for muscles','high')]),
'1.b':(1,[]),'1.0':(1,[]),
'1.1':(2,[('1.0',H,'shaft of a long bone','high')]),
'1.2':(1,[('bio18-s1.2.3',H,'red marrow in spongy bone','high')]),
'1.3':(1,[('bio18-s1.2.5',H,'yellow marrow in shafts','high')]),
'1.4':(1,[('bio18-s1.0.0',H,'cartilage and joints','high')]),
'1.5':(1,[('bio18-s1.0.1',H,'tendons join muscle to bone','high')]),
'1.6':(2,[('1.2',H,'spongy bone and red marrow','low')]),
'2.b':(1,[('0.0',H,'girdle definition','high')]),
'2.0':(1,[('0.0',E,'girdle definition','high')]),
'2.1':(1,[('bio18-s2.6.6',H,'sternum','high')]),
'2.2':(1,[('2.1',H,'clavicle shape and position','high')]),
'2.3':(1,[('2.1',E,'clavicle-sternum joint','high')]),
'2.4':(1,[]),
'2.5':(1,[('2.4',E,'scapula','high')]),
'2.6':(1,[('2.4',E,'scapula surface','high')]),
'2.7':(2,[('2.4',E,'scapula socket','high')]),
'3.b':(1,[('0.0',H,'girdle definition','high')]),
'3.0':(1,[('bio18-s2.2.5',E,'sacrum','high')]),
'3.1':(1,[('3.0',H,'hip bones','high')]),
'3.2':(2,[('3.0',E,'pelvic girdle joined to sacrum','high')]),
'3.3':(1,[('3.0',E,'pelvic girdle structure','high')]),
'3.4':(1,[('3.3',E,'deep hip socket','high')]),
'3.5':(1,[('bio18-s1.2.1',H,'protection function of bones','low')]),
'3.6':(1,[]),
'3.7':(1,[('3.0',H,'pelvic girdle structure','high')]),
'4.b':(1,[]),
'4.0':(2,[('3.2',H,'rigid pelvic girdle','high')]),
'4.1':(2,[('2.7',E,'shallow shoulder socket','high')]),
'4.2':(1,[('4.0',H,'attachment comparison','low')]),
'5.b':(1,[]),
'5.0':(1,[('2.7',E,'shoulder ball-and-socket joint','high')]),
'5.1':(2,[('5.0',H,'humerus','high')]),
'5.2':(1,[]),
'5.3':(1,[('5.1',E,'elbow hinge joint','high')]),
'5.4':(1,[('5.2',E,'ulna','high')]),
'5.5':(1,[]),
'5.6':(2,[('5.5',E,'radius','high')]),
'5.7':(2,[('5.6',E,'radius rotation','high')]),
'6.b':(1,[]),'6.0':(1,[]),
'6.1':(1,[('3.3',E,'hip socket of pelvic girdle','high')]),
'6.2':(1,[('6.0',H,'femur','high')]),
'6.3':(1,[('bio18-s1.0.1',H,'tendons join muscle to bone','high')]),
'6.4':(2,[('6.3',E,'patella in quadriceps tendon','high')]),
'6.5':(1,[('6.1',H,'knee joint with femur','high')]),
'6.6':(1,[('6.5',H,'tibia','high')]),
'6.7':(1,[]),
'7.b':(1,[]),
'7.0':(2,[('5.b',H,'arm bone layout','low')]),
'7.1':(2,[('7.0',E,'limb plan pattern','high')]),
'8.b':(1,[('0.b',H,'axial and appendicular parts','high')]),
'8.0':(2,[('bio18-s2.0.0',E,'axial skeleton parts','high')]),
}
out={}
for t in tids:
    c,n=S[t.replace(p,'')]
    out[t]={'cost':c,'needs':[{'id':(i if i.startswith('bio') else p+i),'strength':s,'why':w,'confidence':f} for i,s,w,f in n]}
json.dump(out,open(P+'point-links/bio18-s3.json','w'),indent=1)
d=json.load(open(P+'point-links/bio18-s3.json'))
assert list(d)==tids and len(set(tids))==len(tids)
assert all(n['id'] in allids and n['id']!=k for k,v in d.items() for n in v['needs'])
print(len(d),sum(len(v['needs']) for v in d.values()),sum(v['cost']==2 for v in d.values()),sum(n['confidence']=='low' for v in d.values() for n in v['needs']))
