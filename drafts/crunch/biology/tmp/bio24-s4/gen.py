import json,re
P='bio24-s4.'
def n(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
H,E='helpful','essential'
D={
'0.b':(1,[]),
'0.0':(1,[n(P+'0.b',H,'meaning of dispersal')]),
'0.1':(1,[n(P+'0.b',H,'meaning of dispersal')]),
'0.2':(1,[n(P+'0.b',H,'meaning of dispersal')]),
'0.3':(1,[n(P+'0.0',H,'competition for resources','low')]),
'0.4':(1,[n(P+'0.1',H,'colonising new areas')]),
'1.b':(1,[]),
'1.0':(1,[n('bio24-s1.3.3',E,'ovary becomes fruit')]),
'1.1':(1,[n(P+'1.0',E,'pericarp of a fruit')]),
'1.2':(1,[n(P+'1.0',E,'pericarp of a fruit')]),
'1.3':(2,[n('bio24-s1.1.0',E,'receptacle swells'),n(P+'1.0',H,'true fruit from ovary')]),
'2.b':(1,[]),
'2.0':(1,[n(P+'2.b',H,'slow fall, large surface area')]),
'2.1':(1,[n(P+'2.0',H,'parachutes increase surface area')]),
'2.2':(1,[n(P+'2.0',H,'wings slow the fall')]),
'2.3':(2,[n(P+'1.2',H,'dry fruit such as capsule')]),
'2.4':(1,[n(P+'2.b',H,'light seeds carried by wind')]),
'3.b':(1,[]),
'3.0':(1,[n(P+'3.b',H,'floating carries fruit')]),
'3.1':(1,[n(P+'3.0',H,'air spaces, waterproof covering')]),
'3.2':(1,[n(P+'3.0',H,'floating air-containing fruits')]),
'4.b':(1,[]),
'4.0':(2,[n(P+'1.1',H,'fleshy fruit eaten by animals'),n('bio24-s3.1.0',E,'testa is the seed coat')]),
'4.1':(1,[n(P+'4.0',H,'seeds survive digestion')]),
'4.2':(1,[n(P+'1.1',H,'fleshy fruits colourful, sweet')]),
'4.3':(1,[n(P+'4.2',H,'ripe fruit attracts animals')]),
'4.4':(1,[n(P+'4.2',H,'fleshy fruits eaten by birds')]),
'4.5':(1,[]),
'5.b':(1,[]),
'5.0':(1,[]),
'5.1':(1,[n(P+'5.0',H,'hooks catch on fur')]),
'5.2':(1,[n(P+'5.1',H,'burdock hooked burs')]),
'6.b':(1,[]),
'6.0':(1,[n(P+'1.2',E,'dry fruits split open')]),
'7.b':(1,[]),
'7.0':(1,[n(P+'2.0',H,'wind adaptations')]),
'7.1':(1,[n(P+'3.0',H,'water adaptations')]),
'7.2':(1,[n(P+'4.2',H,'animal-eaten fruit adaptations')]),
'7.3':(1,[n(P+'5.0',H,'hooks on fruits')]),
'7.4':(1,[n(P+'6.0',H,'exploding pods')]),
'7.5':(2,[n(P+'2.2',H,'winged fruit structure','low')]),
}
out={P+k:{"cost":c,"needs":v} for k,(c,v) in D.items()}
o='/Users/gabrielwhelan/barebones/drafts/crunch/biology/point-links/bio24-s4.json'
json.dump(out,open(o,'w'),indent=1)
txt=open('/Users/gabrielwhelan/barebones/drafts/crunch/biology/points/bio24-s4.txt').read()
ids=re.findall(r'^\[([^\]]+)\]',txt,re.M)
tg=[i for i in ids if i.startswith(P)]
r=json.load(open(o))
assert list(r)==tg,(set(tg)^set(r))
assert all(x['id'] in ids and x['id']!=k for k,v in r.items() for x in v['needs'])
L=[x for v in r.values() for x in v['needs']]
print(len(r),len(L),sum(v['cost']==2 for v in r.values()),sum(x['confidence']=='low' for x in L))
