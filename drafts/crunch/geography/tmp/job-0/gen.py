import json,re
G='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
A='geo-aerial-photographs-s1.'
M='geo-mapwork-s1.'
def t(*a): return [A+x for x in a]
cost2=set(A+x for x in "1.1 9.0 10.1 11.0 11.1 12.0 12.1 13.1 13.4 15.0 15.3 17.0 20.1 20.2 21.0 21.1 26.0 26.1 28.0 28.1 30.1 32.4".split())
# (target, strength, why, conf)
def l(t_,s,w,c='high'): return {"id":t_,"strength":{'e':'essential','h':'helpful'}[s],"why":w,"confidence":c}
P1={
'1.1':[l(A+'0.1','h','scale of a photograph')],
'1.3':[l(A+'0.0','h','horizon defined for vertical')],
'2.0':[l(A+'1.1','h','foreground larger than background')],
'2.1':[l(A+'0.0','h','vertical shows only roofs')],
'3.2':[l(A+'3.0','e','left, centre, right strips'),l(A+'3.1','e','foreground, middleground, background strips')],
'3.3':[l(A+'3.2','h','accepted zone notation')],
'3.4':[l(A+'3.2','e','zone notation to state')],
'3.5':[l(A+'3.4','e','grid method for zones')],
'4.0':[l(A+'3.1','e','foreground and background meaning')],
'4.1':[l(A+'3.0','h','across strips left centre right')],
'5.0':[l(A+'3.2','e','zone notation')],'5.1':[l(A+'3.2','e','zone notation')],'5.2':[l(A+'3.2','e','zone notation')],
'5.3':[l(A+'3.2','e','zone notation')],'5.4':[l(A+'3.2','e','zone notation')],'5.5':[l(A+'3.2','e','zone notation')],
'5.6':[l(A+'5.5','e','waste ground location'),l(A+'3.5','h','true or false zone method')],
'6.0':[l(A+'6.1','h','graveyard clue','low')],
'7.2':[l(A+'7.4','h','waste ground contrast')],
'9.1':[l(A+'6.0','h','church clues spire cruciform')],
'9.2':[l(A+'3.2','e','zone notation')],
'10.0':[l(A+'3.2','h','nine-area zone notation')],
'10.1':[l(M+'1.5','e','six-figure grid reference method'),l(M+'1.4','h','four-figure grid reference')],
'10.2':[l(M+'14.0','h','map symbols in legend','low')],
'10.3':[l(M+'14.1','h','road letters M N R')],
'11.0':[l(A+'3.1','h','foreground and background'),l(M+'7.2','h','direction from A to B','low')],
'11.1':[l(M+'7.0','e','eight-point compass directions'),l(A+'11.0','e','camera direction method')],
'11.2':[l(A+'11.1','e','camera direction method')],
'11.3':[l(A+'3.2','h','zone notation')],
'11.4':[l(A+'11.0','e','foreground to background direction')],
'12.1':[l(M+'8.0','h','contours on the map')],
'12.2':[l(A+'1.1','h','oblique scale changes'),l(M+'0.2','h','constant map scale','low')],
'13.0':[l(A+'1.1','e','oblique scale not constant')],
'13.1':[l(M+'0.2','e','ratio scale meaning'),l(A+'0.1','h','vertical photograph scale')],
'13.2':[l(M+'0.4','h','1:50 000 means 2 cm to 1 km')],
'13.3':[l(M+'0.4','e','2 cm = 1 km on 1:50 000'),l(A+'13.2','h','example distances')],
'13.4':[l(A+'13.3','e','ground distance in cm'),l(A+'13.2','e','5 cm photograph distance')],
'14.2':[l(A+'14.1','e','half length and breadth rule')],
'14.3':[l(A+'3.4','e','nine-area grid method')],
'15.2':[l(A+'3.2','e','zone notation')],
'16.0':[l(A+'14.1','e','halving each side')],
'16.2':[l(A+'15.0','e','river drawn as double line')],
'16.3':[l(A+'15.0','h','bridge drawn as symbol')],
'16.4':[l(A+'15.0','h','building as small symbol','low')],
'16.5':[l(A+'15.2','e','feature drawn in specified zone')],
'16.6':[l(A+'15.0','h','areas as outlined shapes')],
'19.5':[l(A+'19.4','e','CBD definition')],
'19.0':[l(A+'7.1','h','terraced houses share walls')],
'19.1':[l(A+'7.1','h','semi-detached and detached')],
'19.2':[l(A+'6.5','h','apartment block clues')],
'21.0':[l(A+'3.2','e','accepted zone notation')],
'21.3':[l(A+'21.0','h','function answer formula')],'21.4':[l(A+'21.0','h','function answer formula')],'21.5':[l(A+'21.0','h','function answer formula')],
'24.7':[l(A+'24.0','h','planned or unplanned patterns','low')],
'26.2':[l(A+'3.2','e','zone notation')],
'26.4':[l(A+'26.1','h','bypass and other measures')],
'27.0':[l(A+'25.2','h','routes converging on bridge')],
'27.1':[l(A+'26.0','h','roundabouts as measures')],
'27.2':[l(A+'26.4','e','solution justified with evidence')],
'28.1':[l(A+'28.0','h','listed change comparison')],
'28.4':[l(A+'28.2','e','change method')],'28.5':[l(A+'28.2','e','change method')],
'30.3':[l(A+'30.1','e','suitability tests')],
'31.7':[l(A+'31.0','h','leafy trees mean summer'),l(A+'31.3','h','silage bales mean summer')],
'32.4':[l(A+'32.1','e','morning shadows point west'),l(A+'11.0','e','camera direction from map')],
'32.5':[l(A+'32.2','e','long shadows mean low sun')],
'32.2':[l(A+'32.1','h','sun position through day','low')],
}
U4='geo-urban-s4.';U3='geo-urban-s3.'
P2={
'18.0':[l(U4+'8.2','h','industry moves to edge reasons')],
'18.1':[l(U4+'8.0','h','old inner-city industry by port')],
'19.0':[l(U4+'0.2','h','inner terraced housing')],
'19.1':[l(U4+'0.3','h','suburban semi-detached housing')],
'19.3':[l(U4+'3.0','h','density falls with distance','low')],
'19.4':[l(U4+'0.0','h','CBD defined')],
'19.5':[l(U4+'1.1','h','tall buildings in CBD')],
'20.0':[l(U3+'2.0','h','list of town functions')],
'20.1':[l(U3+'2.1','h','industrial, port, transport functions')],
'20.2':[l(U3+'2.0','h','market and services functions')],
'21.1':[l(U3+'0.b','h','site meaning'),l(U3+'1.b','h','situation meaning'),l(U3+'7.b','h','hinterland meaning')],
'22.2':[l(U3+'0.0','h','bridging point and river sites','low')],
'23.0':[l(U3+'0.b','e','site advantages of towns')],
'28.3':[l(U4+'15.1','h','farmland lost to housing','low')],
'29.2':[l(U4+'10.0','h','retail parks at edge'),l(U4+'8.1','h','industrial estates at edge')],
'30.2':[l(U4+'12.2','h','industry outbids housing','low')],
'25.2':[l(U3+'0.1','h','route focus','low')],
}
U1='geo-urban-s1.';U5='geo-urban-s5.'
P3={
'18.1':[l(U1+'14.1','h','mills as 19th-century industry','low')],
'20.2':[l(U1+'8.2','h','castles for defence','low')],
'22.0':[l(U1+'9.0','h','walled Norman towns'),l(U1+'8.2','h','castles and mottes')],
'22.3':[l(U1+'14.0','h','railways created 19th-century towns')],
'22.4':[l(U1+'15.2','h','suburban expansion','low')],
'23.0':[l(U1+'1.4','h','bridging points as routeways')],
'24.0':[l(U1+'12.2','h','planned town features'),l(U1+'13.b','h','landlord planned towns')],
'24.1':[l(U1+'9.b','h','medieval town layout','low')],
'25.b':[l(U5+'0.b','h','congestion meaning')],
'25.0':[l(U5+'0.2','h','narrow streets at historic centre')],
'25.2':[l(U5+'2.1','h','few crossings of river')],
'25.4':[l(U5+'0.4','h','delivery vehicles share streets')],
'25.5':[l(U5+'0.3','h','peak journey times')],
'26.0':[l(U5+'3.2','h','bus lanes priority')],
'26.1':[l(U5+'4.0','h','pedestrianisation'),l(U5+'3.6','h','orbital roads and bypasses')],
'26.4':[l(U5+'3.6','h','bypass removes through-traffic')],
'29.0':[l(U5+'10.0','h','why edge development grows','low')],
'29.4':[l(U5+'10.b','h','sprawl defined')],
'30.1':[l(U5+'27.0','h','flood risk on paved land','low')],
'28.1':[l(U5+'5.0','h','industry closing in inner city','low')],
}
def run(pack,links,name,cost):
    txt=open(G+'packs/'+pack).read()
    tgt=txt.split('CANDIDATES')[0]
    ids=re.findall(r'^\[(\S+?)\]',tgt,re.M)
    allids=set(re.findall(r'^\[(\S+?)\]',txt,re.M))
    out={};nl=0;c2=0;low=0
    for i in ids:
        k=i[len(A):]
        d={}
        if cost:
            d['cost']=2 if i in cost2 else 1;c2+=d['cost']==2
        d['needs']=links.get(k,[])
        for n in d['needs']:
            assert n['id'] in allids and n['id']!=i,(i,n)
            nl+=1;low+=n['confidence']=='low'
        out[i]=d
    for k in links: assert A+k in out,k
    json.dump(out,open(G+'point-links/'+name,'w'),indent=1)
    d=json.load(open(G+'point-links/'+name));assert list(d)==ids
    print(name,len(ids),nl,c2 if cost else '-',low)
run('geo-aerial-photographs-s1.t1g1.txt',P1,'geo-aerial-photographs-s1.t1g1.json',True)
run('geo-aerial-photographs-s1.t1g2.txt',P2,'geo-aerial-photographs-s1.t1g2.json',False)
run('geo-aerial-photographs-s1.t1g3.txt',P3,'geo-aerial-photographs-s1.t1g3.json',False)
