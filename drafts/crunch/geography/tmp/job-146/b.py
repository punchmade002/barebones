import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
V='geo-volcanoes-earthquakes-s1.';R='geo-rocks-weathering-s1.';T='geo-plate-tectonics-s3.';S='geo-volcanoes-earthquakes-s3.'
def L(i,s,w,c='high'):
    if not i.startswith('geo-'): i=S+i
    return (i,s,w,c)
H,E='helpful','essential'
D={
'0.b':(1,[]),
'0.0':(1,[]),
'0.1':(1,[(R+'3.1',H,'plutonic rock cools slowly underground')]),
'0.2':(1,[(R+'0.1',H,'exogenic weathering and erosion')]),
'1.b':(1,[]),'1.0':(1,[]),
'1.1':(1,[(R+'3.b',H,'igneous rock from cooled magma')]),
'1.2':(1,[(R+'4.0',H,'granite as plutonic rock')]),
'1.3':(1,[(R+'0.1',H,'weathering and erosion')]),
'2.b':(1,[]),
'2.0':(1,[(V+'2.0',H,'basic lava is runny')]),
'2.1':(1,[('2.0',H,'runny basic lava')]),
'2.2':(1,[('2.1',H,'lava flows spreading')]),
'2.3':(1,[]),'2.4':(1,[]),
'2.5':(1,[('2.3',H,'plateau shape being drawn')]),
'3.b':(1,[]),
'3.0':(2,[(V+'7.2',H,'Antrim basalts from fissure eruptions')]),
'3.1':(1,[(R+'9.4',H,'chalk lies beneath Antrim basalt')]),
'3.2':(2,[(R+'13.3',H,'Mourne granite age'),('14.b',H,'Leinster granite comparison','low')]),
'3.3':(1,[('3.2',E,'Slieve Donard is in Mournes')]),
'4.b':(1,[('1.0',H,'joint pattern')]),
'4.0':(2,[('1.1',H,'joints form by cooling contraction')]),
'4.1':(1,[('4.0',E,'cracks from contraction in columnar jointing')]),
'4.2':(2,[('4.1',E,'cracks at 120 degrees')]),
'4.3':(2,[('4.2',H,'six-sided basalt columns')]),
'4.4':(1,[('4.2',H,'columnar jointing','low')]),
'4.5':(1,[('4.3',H,'Giant\'s Causeway columns')]),
'4.6':(1,[('4.2',E,'columns at right angles to surface')]),
'5.b':(1,[(V+'2.0',H,'low viscosity runny lava')]),
'5.0':(1,[(V+'2.0',H,'basic lava is low viscosity')]),
'5.1':(1,[(V+'2.1',E,'effusive eruptions')]),
'5.2':(1,[(V+'0.1',H,'main (central) vent')]),
'5.3':(1,[]),
'5.4':(1,[('5.1',H,'broad gentle cone shape')]),
'6.b':(1,[]),
'6.0':(1,[(V+'6.1',H,'Hawaii over a hot spot')]),
'6.1':(1,[('5.0',H,'runny lava spreads far')]),
'6.2':(1,[]),'6.3':(1,[]),
'7.b':(1,[('5.b',H,'shield contrast')]),
'7.0':(1,[(V+'2.2',H,'viscous acidic lava')]),
'7.1':(1,[(V+'2.3',H,'acidic lava explosive eruptions')]),
'7.2':(1,[(V+'0.3',H,'crater at summit')]),
'7.3':(1,[(V+'0.2',H,'secondary vent')]),
'7.4':(2,[]),
'7.5':(2,[(V+'0.6',H,'labelled volcano cross-section')]),
'8.b':(1,[]),
'8.0':(1,[(V+'1.2',H,'pyroclastic fragments')]),
'8.1':(1,[]),
'8.2':(1,[('8.0',H,'cinder cone shape')]),
'9.b':(1,[]),
'9.0':(2,[(V+'0.0',H,'magma chamber')]),
'9.1':(1,[('9.0',E,'caldera forms by collapse')]),
'9.2':(1,[('9.0',E,'caldera filling with water')]),
'9.3':(2,[('9.2',H,'crater lake in caldera')]),
'9.4':(1,[('9.0',H,'caldera definition')]),
'9.5':(2,[('9.0',H,'caldera definition')]),
'10.b':(1,[]),
'10.0':(1,[(V+'0.1',H,'vent of volcano')]),
'10.1':(1,[('10.0',H,'plug in the vent')]),
'10.2':(1,[('10.1',H,'cone eroded leaving plug')]),
'10.3':(2,[('10.2',H,'volcanic plug')]),
'10.4':(1,[('10.2',E,'plug standing above eroded cone')]),
'11.b':(1,[]),'11.0':(1,[]),
'11.1':(1,[('11.0',E,'contrast with geyser')]),
'11.2':(1,[]),
'11.3':(1,[('11.0',E,'geyser definition')]),
'12.b':(1,[('2.0',H,'fissure eruption')]),
'12.0':(2,[('2.0',H,'fissure eruption')]),
'12.1':(1,[('11.0',E,'geyser definition')]),
'12.2':(1,[]),'12.3':(1,[]),
'13.b':(1,[('0.1',H,'plutonic cooling underground')]),
'13.0':(1,[(R+'4.1',H,'batholith dome-shaped plutonic mass')]),
'13.1':(2,[(R+'11.0',H,'metamorphic aureole')]),
'13.2':(1,[('13.0',E,'batholith being exposed')]),
'14.b':(1,[('13.0',H,'batholith')]),
'14.0':(1,[(R+'13.5',H,'Caledonian mountain building','low')]),
'14.1':(1,[]),
'14.2':(1,[('13.2',H,'erosion exposes granite')]),
'14.3':(1,[('13.1',E,'metamorphic aureole')]),
'14.4':(1,[('13.2',H,'granite uplands','low')]),
'14.5':(1,[('14.4',E,'Lugnaquilla named')]),
'15.b':(1,[]),
'15.0':(1,[(R+'7.1',H,'layers and bedding','low')]),
'15.1':(1,[('15.0',E,'laccolith')]),
'15.2':(1,[('15.0',H,'contrast with laccolith')]),
'16.b':(1,[]),
'16.0':(1,[(R+'4.3',H,'sill along bedding planes')]),
'16.1':(1,[('16.0',E,'sill definition')]),
'16.2':(1,[('16.0',H,'dolerite sill')]),
'16.3':(1,[('16.0',H,'sill definition')]),
'16.4':(1,[(R+'4.2',H,'dyke cuts across beds')]),
'16.5':(2,[('16.4',E,'dyke definition'),('17.b',H,'differential erosion')]),
'16.6':(1,[('16.4',E,'dyke definition')]),
'17.b':(1,[]),
'17.0':(1,[('17.b',H,'differential erosion')]),
'17.1':(1,[('17.0',E,'resistant rock stands as upland')]),
'17.2':(2,[('13.0',E,'batholith'),('15.0',E,'laccolith'),('15.2',E,'lopolith'),('16.0',E,'sill'),('16.4',E,'dyke'),('10.2',E,'volcanic plug')]),
'18.b':(1,[('13.b',H,'exposed batholith')]),
'18.0':(1,[('14.b',H,'Wicklow granite comparison')]),
'18.1':(1,[]),'18.2':(1,[]),
}
txt=open(P+'packs/geo-volcanoes-earthquakes-s3.t1g1.txt').read()
ids=re.findall(r'^\[(geo-volcanoes-earthquakes-s3\.[^\]]+)\]',txt,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
out={}
for i in ids:
    k=i[len(S):]
    c,n=D[k]
    out[i]={'cost':c,'needs':[{'id':(x[0] if x[0].startswith('geo-') else S+x[0]),'strength':x[1],'why':x[2],'confidence':(x[3] if len(x)>3 else 'high')} for x in n]}
assert set(D)=={i[len(S):] for i in ids}, set(D)^{i[len(S):] for i in ids}
for i,v in out.items():
    for n in v['needs']:
        assert n['id'] in allids and n['id']!=i,(i,n)
        assert len(n['why'].split())<=8
json.dump(out,open(P+'point-links/geo-volcanoes-earthquakes-s3.t1g1.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
