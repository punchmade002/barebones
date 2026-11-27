import json,re
S='hom-home-interior-s1.'
def n(i,s,w,c='high'): return {"id":S+i,"strength":s,"why":w,"confidence":c}
H='helpful';E='essential'
d={
'0.b':(2,[]),'0.0':(1,[n('0.b',H,'list of elements')]),'0.1':(2,[n('0.b',H,'the elements')]),
'1.b':(1,[n('0.b',H,'line and shape elements')]),'1.0':(1,[]),'1.1':(1,[]),'1.2':(1,[]),'1.3':(1,[]),
'2.b':(1,[]),'2.0':(1,[]),'2.1':(1,[n('2.0',E,'made by mixing primaries')]),
'2.2':(1,[n('2.1',E,'mixes primary with secondary')]),
'2.3':(2,[n('2.0',H,'uses red, yellow, blue')]),
'2.4':(1,[]),'2.5':(1,[]),'2.6':(1,[n('2.5',H,'pale colours reflect light')]),
'3.b':(1,[]),'3.0':(1,[]),'3.1':(1,[n('3.0',E,'tints, tones and shades')]),
'3.2':(1,[n('2.0',H,'colour wheel colours','low')]),
'3.3':(1,[n('2.0',H,'colour wheel colours','low')]),'3.4':(1,[]),
'4.b':(2,[]),'4.0':(1,[]),'4.1':(1,[n('2.5',H,'pale and dark colours')]),'4.2':(1,[]),
'4.3':(1,[n('2.3',H,'warm and cool colour effects')]),
'4.4':(1,[n('2.3',H,'warm and cool colours')]),
'5.b':(1,[]),'5.0':(1,[]),'5.1':(1,[n('5.0',H,'large and small pattern')]),
'5.2':(1,[n('5.0',H,'combining patterns')]),'5.3':(1,[n('5.0',H,'amount of pattern')]),
'6.b':(1,[]),'6.0':(1,[]),'6.1':(1,[n('6.0',H,'smooth textures')]),
'6.2':(1,[n('6.0',H,'rough and soft textures')]),
'6.3':(1,[n('6.0',H,'texture finish')]),'6.4':(1,[n('6.0',H,'contrasting textures')]),
'7.b':(1,[]),'7.0':(1,[]),'7.1':(1,[n('7.0',H,'size relationships')]),'7.2':(1,[n('7.0',E,'proportion')]),
'8.b':(1,[]),'8.0':(1,[]),'8.1':(1,[]),'8.2':(1,[n('8.1',H,'contrasts with formal balance')]),
'9.b':(1,[]),'9.0':(1,[]),'9.1':(1,[n('9.0',E,'focal point')]),'9.2':(1,[n('9.0',E,'focal point')]),
'10.b':(1,[]),'10.0':(1,[]),'10.1':(1,[n('10.0',E,'repetition creates rhythm')]),
'11.b':(2,[]),'11.0':(1,[]),'11.1':(1,[n('9.0',E,'focal point')]),
'11.2':(1,[n('7.2',E,'proportion guides furniture')]),'11.3':(1,[]),'11.4':(2,[n('9.0',H,'focal point labelled')]),
'12.b':(1,[]),'12.0':(2,[]),'12.1':(1,[]),'12.2':(1,[]),
'13.b':(1,[]),'13.0':(1,[]),'13.1':(1,[]),'13.2':(1,[]),
'13.3':(1,[n('4.4',H,'aspect and warm colours')]),'13.4':(1,[]),
'14.b':(1,[]),'14.0':(1,[]),'14.1':(1,[n('14.0',H,'ergonomics')]),
'14.2':(1,[n('14.0',H,'ergonomics')]),'14.3':(1,[]),'14.4':(1,[]),'14.5':(1,[]),'14.6':(1,[]),
'14.7':(2,[n('14.1',E,'work triangle')]),
'15.b':(1,[]),'15.0':(1,[]),'15.1':(1,[]),'15.2':(1,[]),'15.3':(1,[]),'15.4':(1,[]),'15.5':(1,[]),
'16.b':(1,[]),'16.0':(2,[]),'16.1':(2,[]),'16.2':(1,[]),'16.3':(1,[]),'16.4':(1,[]),'16.5':(1,[]),
'17.b':(1,[]),'17.0':(1,[]),'17.1':(1,[n('9.0',H,'focal point')]),'17.2':(1,[]),'17.3':(1,[]),'17.4':(1,[]),
'18.b':(1,[]),'18.0':(1,[]),'18.1':(1,[]),'18.2':(1,[]),'18.3':(1,[]),'18.4':(1,[]),
'18.5':(1,[n('2.5',H,'light colours reflect light')]),'18.6':(1,[]),
'19.b':(1,[]),'19.0':(1,[]),'19.1':(1,[]),
}
out={S+k:{"cost":c,"needs":v} for k,(c,v) in d.items()}
f='/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/'
txt=open(f+'packs/hom-home-interior-s1.t1g1.txt').read()
ids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
tg=re.findall(r'^\[([^\]]+)\]',txt.split('CANDIDATES')[0],re.M)
assert list(out)==tg,(set(tg)^set(out))
for k,v in out.items():
  for x in v['needs']: assert x['id'] in ids and x['id']!=k
json.dump(out,open(f+'point-links/hom-home-interior-s1.t1g1.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
