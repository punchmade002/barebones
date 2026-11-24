import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
S='geo-volcanoes-earthquakes-s4.'
S1='geo-rocks-weathering-s1.'
S3='geo-rocks-weathering-s3.'
E,H='essential','helpful'
def L(i,s,w,c='high'): return (i,s,w,c)
D={
'0.b':(1,[]),
'0.0':(1,[]),
'0.1':(1,[L(S1+'7.1',H,'bedding plane definition')]),
'0.2':(1,[L(S+'0.1',E,'uses bedding plane')]),
'0.3':(1,[L(S+'0.1',E,'uses bedding planes')]),
'1.b':(1,[]),
'1.0':(1,[L(S1+'7.2',H,'joint defined')]),
'1.1':(1,[L(S+'1.0',E,'uses joints'),L(S+'0.1',E,'uses bedding planes')]),
'1.2':(1,[L(S+'1.0',H,'uses joints')]),
'1.3':(1,[L(S+'1.0',E,'uses joints'),L(S+'0.1',E,'uses bedding planes')]),
'2.b':(1,[]),
'2.0':(1,[L(S+'0.0',H,'strata are layers')]),
'2.1':(1,[L(S+'2.0',E,'uses dip')]),
'2.2':(1,[L(S+'2.0',E,'uses dip and tilt')]),
'3.b':(1,[]),
'3.0':(1,[L(S+'1.3',E,'bedding planes and joints'),L(S3+'0.0',H,'weathering defined')]),
'3.1':(1,[L(S+'3.0',E,'erosion follows planes')]),
'4.b':(1,[]),
'4.0':(1,[L(S+'0.3',H,'layers differ in resistance')]),
'4.1':(1,[L(S+'4.0',E,'uses differential erosion')]),
'5.b':(1,[]),
'5.0':(1,[L(S+'1.3',H,'joints and bedding planes'),L(S1+'7.3',H,'permeable defined',)]),
'5.1':(1,[L(S+'5.0',E,'contrasts with permeable')]),
'5.2':(2,[L(S+'5.0',E,'permeable layer'),L(S+'5.1',E,'impermeable layer')]),
'6.b':(1,[]),
'6.0':(1,[L(S+'0.0',E,'uses horizontal strata'),L(S+'4.1',H,'resistant layers stand out')]),
'6.1':(2,[L(S+'4.0',E,'uses differential erosion'),L(S+'6.0',E,'uses cap rock')]),
'6.2':(1,[L(S+'6.0',E,'uses cap rock')]),
'6.3':(1,[L(S+'6.0',H,'diagram of cap rock'),L(S+'6.1',H,'diagram of cliffed edges')]),
'7.b':(1,[]),
'7.0':(1,[L(S+'4.0',E,'uses differential erosion')]),
'7.1':(1,[L(S+'7.0',E,'uses differing erosion rates'),L(S3+'1.5',H,'scree defined','low')]),
'7.2':(1,[L(S+'7.1',E,'repeats cliff and slope')]),
'8.b':(2,[L(S+'6.b',H,'flat-topped upland'),L(S1+'9.0',H,'Carboniferous limestone')]),
'8.0':(1,[]),
'8.1':(1,[L(S3+'5.3',H,'karst formed by carbonation')]),
'9.b':(1,[L(S+'6.0',H,'resistant cap')]),
'9.0':(1,[L(S+'6.b',H,'flat-topped upland')]),
'9.1':(1,[L(S+'6.0',H,'resistant cap')]),
'9.2':(1,[L(S+'7.1',H,'soft rock forms slopes, scree')]),
'9.3':(1,[]),
'10.b':(1,[L(S+'7.b',H,'stepped profile')]),
'10.0':(1,[]),
'10.1':(2,[L(S+'7.1',H,'cliffs and slopes of layers')]),
'10.2':(1,[]),
'10.3':(1,[L(S+'8.1',H,'caves in limestone')]),
'11.b':(1,[L(S+'6.b',H,'plateau defined')]),
'11.0':(1,[L(S+'6.1',H,'edges worn back')]),
'11.1':(1,[L(S+'6.0',H,'resistant cap')]),
'11.2':(1,[L(S+'11.1',E,'uses remnants')]),
'11.3':(1,[L(S+'11.2',H,'mesa or butte example')]),
'11.4':(1,[L(S+'11.2',E,'mesa and butte shapes')]),
'12.b':(1,[L(S+'2.0',E,'uses dip')]),
'12.0':(1,[L(S+'2.0',E,'uses dip'),L(S+'4.0',H,'resistant layer')]),
'12.1':(1,[L(S+'12.0',E,'uses exposed resistant layer')]),
'12.2':(1,[L(S+'12.1',E,'continues from scarp slope'),L(S+'2.0',E,'uses dip')]),
'12.3':(1,[L(S+'4.0',H,'weak rock erodes faster')]),
'12.4':(2,[L(S+'12.b',H,'cuesta defined')]),
'12.5':(1,[L(S+'12.1',E,'scarp slope'),L(S+'12.2',E,'dip slope')]),
'13.b':(1,[L(S+'12.b',H,'same process as cuesta')]),
'13.0':(1,[L(S+'2.2',E,'steep dip attitude')]),
'13.1':(1,[L(S+'12.b',E,'compares with cuesta')]),
'13.2':(1,[]),
'14.b':(1,[]),
'14.0':(2,[L(S+'1.3',H,'joints and bedding planes')]),
'14.1':(1,[L(S+'0.1',H,'bedding planes')]),
'14.2':(1,[L(S+'6.0',H,'horizontal cap rock')]),
'14.3':(1,[L(S+'1.0',H,'joints')]),
'15.b':(2,[L(S+'12.b',E,'escarpments on gentle dip'),L(S+'2.2',H,'gently dipping attitude')]),
'15.0':(1,[]),
'15.1':(1,[]),
'15.2':(2,[L(S+'12.b',E,'escarpment or cuesta'),L(S+'12.2',H,'dip slope')]),
'15.3':(1,[L(S+'4.0',H,'weak clay eroded faster')]),
'16.b':(1,[L(S+'12.b',H,'gently dipping escarpments')]),
'16.0':(1,[]),
'16.1':(1,[L(S+'12.1',H,'escarpment and dip slope')]),
'16.2':(1,[]),
'16.3':(1,[]),
}
txt=open(P+'packs/geo-volcanoes-earthquakes-s4.t1g1.txt').read()
tg=re.findall(r'^\[(geo-volcanoes-earthquakes-s4\.\d+\.\w+)\]',txt,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
assert [t[len(S):] for t in tg]==list(D), 'order'
out={};n=lo=c2=0
for k,(c,ns) in D.items():
    for i,*_ in ns: assert i in allids and i!=S+k,(k,i)
    out[S+k]={'cost':c,'needs':[{'id':i,'strength':s,'why':w,'confidence':cf} for i,s,w,cf in ns]}
    n+=len(ns);c2+=c==2;lo+=sum(x[3]=='low' for x in ns)
json.dump(out,open(P+'point-links/geo-volcanoes-earthquakes-s4.t1g1.json','w'),indent=1)
print(len(out),n,c2,lo)
