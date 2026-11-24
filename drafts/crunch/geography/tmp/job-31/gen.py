import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
M='geo-mapwork-s1.'
# (id, cost, [(target, strength E/H, why, conf H/L)])
E,H='essential','helpful'
d=[
('0.b',1,[]),('0.0',1,[]),('0.1',1,[('0.0',H,'legend defined there','H')]),
('0.2',1,[]),('0.3',1,[]),
('0.4',1,[('0.2',E,'uses ratio 1:50 000','H')]),
('0.5',1,[('0.2',H,'uses ratio scale','H')]),
('0.6',1,[('0.5',H,'scale size comparison','H')]),
('1.b',1,[]),('1.0',1,[]),
('1.1',1,[]),('1.2',1,[('1.1',H,'across before up order','H')]),
('1.3',1,[('1.1',H,'easting then northing order','H')]),
('1.4',1,[('1.1',E,'uses eastings','H'),('1.2',E,'uses northings','H')]),
('1.5',2,[('1.4',E,'divides the four-figure square','H')]),
('1.6',1,[('1.5',E,'six-figure reference method','H')]),
('1.7',1,[('1.4',E,'four-figure reference','H')]),
('2.b',1,[]),
('2.0',1,[('1.1',E,'eastings','H'),('1.2',E,'northings','H')]),
('2.1',1,[('2.0',E,'naming feature at reference','H')]),
('2.2',1,[('1.5',E,'six-figure reference','H')]),
('2.3',1,[('1.5',H,'grid reference location','H')]),
('2.4',1,[('2.3',H,'contrast with absolute','H')]),
('2.5',1,[('7.0',H,'compass points','H')]),
('3.b',1,[]),('3.0',1,[]),('3.1',1,[]),
('3.2',1,[('3.0',E,'latitude','H'),('3.1',E,'longitude','H')]),
('3.3',2,[('3.0',E,'latitude lines','H'),('3.1',H,'date line is longitude','L')]),
('3.4',2,[('3.0',E,'latitude parallels','H'),('3.1',E,'longitude meridians','H')]),
('4.b',1,[]),
('4.0',1,[('3.1',E,'longitude','H')]),
('4.1',1,[('4.0',E,'15 degrees per hour','H')]),
('4.2',2,[('3.0',E,'latitude','H'),('3.1',E,'longitude','H')]),
('4.3',1,[('3.2',E,'latitude longitude format','H')]),
('4.4',1,[('1.5',H,'grid reference use','H'),('3.2',H,'latitude longitude','H')]),
('5.b',1,[]),
('5.0',1,[('0.4',E,'1 cm = 0.5 km','H'),('0.3',H,'scale bar','H')]),
('5.1',2,[('1.1',E,'difference in eastings','H'),('1.2',E,'difference in northings','H')]),
('5.2',1,[('0.3',E,'scale bar','H')]),
('5.3',1,[('5.2',H,'curved distance measuring','H')]),
('5.4',2,[('5.1',E,'grid Pythagoras method','H'),('5.0',E,'ruler and scale','H')]),
('5.5',1,[('5.2',E,'curved distance method','H')]),
('6.b',1,[]),
('6.0',1,[('0.4',E,'1 km grid square','H')]),
('6.1',2,[('0.4',E,'grid square area','H')]),
('6.2',1,[('6.1',H,'estimate part squares','H')]),
('6.3',1,[('6.1',E,'counting part squares','H')]),
('6.4',1,[('6.0',E,'rectangular area','H'),('1.2',H,'northing line','H')]),
('6.5',1,[('6.1',E,'half-square counting rule','H')]),
('7.b',1,[]),('7.0',1,[]),
('7.1',1,[('7.0',E,'compass points','H')]),
('7.2',1,[('7.0',E,'compass points','H')]),
('7.3',1,[('7.1',H,'direction method','H'),('geo-rivers-s1.0.0',H,'river source','H')]),
('7.4',1,[('7.0',E,'compass points','H')]),
('7.5',1,[('7.1',E,'direction method','H')]),
('8.b',1,[]),('8.0',1,[]),
('8.1',1,[('8.0',H,'contour heights','H')]),
('8.2',1,[('8.0',E,'contour interval','H'),('8.1',E,'spot heights pillars','H')]),
('8.3',1,[('8.1',E,'spot heights pillars','H')]),
('9.b',1,[]),
('9.0',1,[('8.0',E,'contours','H')]),
('9.1',1,[('9.0',E,'contour spacing','H')]),
('9.2',2,[('9.0',E,'contour spacing','H')]),
('9.3',2,[('9.0',E,'contour spacing','H')]),
('9.4',1,[('9.0',E,'contour spacing','H')]),
('10.b',1,[]),
('10.0',1,[('8.0',E,'contours','H')]),
('10.1',2,[('8.0',E,'contour shapes','H'),('10.0',H,'contrast with valley','H')]),
('10.2',1,[('9.0',H,'crowded contours','H')]),
('10.3',1,[('8.0',E,'contours','H')]),
('10.4',1,[('8.0',H,'contours','H')]),
('10.5',1,[('9.0',E,'contour spacing','H')]),
('10.6',1,[('8.0',E,'closed contour ring','H')]),
('11.b',1,[]),
('11.0',2,[('8.2',H,'reading heights','H')]),
('11.1',2,[('11.0',E,'VI over HE','H'),('8.2',E,'heights of points','H'),('5.0',E,'measuring distance','H')]),
('11.2',1,[('7.0',E,'compass directions','H')]),
('11.3',1,[('11.2',E,'south-facing aspect','H')]),
('11.4',1,[('9.3',H,'convex slope blocks view','H'),('12.b',H,'cross-section check','H')]),
('11.5',2,[('11.0',E,'gradient formula','H'),('11.1',E,'gradient method','H')]),
('12.b',1,[]),('12.0',1,[]),
('12.1',1,[('8.0',E,'contours crossed','H'),('12.0',H,'joined line','H')]),
('12.2',1,[('0.2',H,'horizontal scale = map scale','H'),('12.1',H,'marked points','H')]),
('12.3',1,[('12.1',E,'marked heights','H')]),
('12.4',1,[('12.3',H,'drawn profile','H'),('1.5',H,'grid references at ends','H')]),
('12.5',2,[('12.2',E,'horizontal and vertical scales','H')]),
('12.6',2,[('12.5',E,'vertical exaggeration','H'),('0.2',H,'ratio scale','H')]),
('12.7',1,[('9.2',E,'concave slope','H'),('12.3',H,'drawn cross-section','H')]),
('13.b',1,[]),
('13.0',1,[('12.3',H,'profile drawn from map','H'),('1.2',H,'northing lines','H')]),
('13.1',1,[('13.0',E,'matching profile points','H')]),
('13.2',1,[('14.1',H,'road letters','H')]),
('13.3',1,[('8.2',E,'height of a point','H')]),
('13.4',1,[('9.0',H,'slope from contours','H')]),
('13.5',1,[('14.2',E,'vegetation terms','H')]),
('13.6',1,[('geo-mapwork-s1.31.4',H,'townland','H')]),
('13.7',2,[('13.0',E,'matching profile points','H'),('13.1',H,'river dip','H')]),
('14.b',1,[]),
('14.0',1,[('0.0',H,'legend','H')]),
('14.1',1,[]),('14.2',1,[]),
('14.3',2,[('14.0',H,'legend groups','H')]),
('15.b',1,[]),
('15.0',2,[('14.0',H,'legend groups','H'),('geo-mapwork-s1.27.0',H,'megalithic tombs','H'),('geo-mapwork-s1.28.0',H,'early Christian sites','H'),('geo-mapwork-s1.29.0',H,'Norman sites','H')]),
('15.1',1,[]),
('15.2',1,[('15.1',E,'cultural area','H'),('geo-mapwork-s1.31.b',H,'Irish place names','H')]),
('16.b',1,[]),('16.0',1,[]),
('16.1',1,[('0.4',E,'2 cm square = 1 km','H'),('16.0',H,'half scale','H')]),
('16.2',1,[('1.1',E,'eastings','H'),('1.2',E,'northings','H')]),
('16.3',1,[('16.2',H,'grid lines on frame','H')]),
('16.4',1,[]),
('16.5',1,[('8.0',E,'contour lines','H')]),
('16.6',1,[]),('16.7',1,[]),
('17.b',1,[('16.0',H,'half scale frame','H')]),
('17.0',1,[('16.3',E,'drawing a river','H'),('1.5',E,'six-figure reference','H')]),
('17.1',1,[('16.4',E,'drawing roads','H')]),
('17.2',1,[('16.4',E,'drawing railways','H')]),
('17.3',1,[('16.4',E,'drawing shaded areas','H')]),
('17.4',1,[('16.5',E,'land above a contour','H')]),
('18.b',1,[]),
('18.0',1,[('18.b',E,'tributaries','H')]),
('18.1',1,[('18.b',E,'tributaries','H')]),
]
def mk(i): return i if i.startswith('geo-') else M+i
def build(rows,cost):
    out={}
    for i,c,n in rows:
        v={}
        if cost: v['cost']=c
        v['needs']=[{'id':mk(t),'strength':s,'why':w,'confidence':'high' if k=='H' else 'low'} for t,s,w,k in n]
        out[M+i]=v
    return out
def ids(path):
    t=open(path).read().split('CANDIDATES')[0]
    return re.findall(r'^\[(\S+?)\]',t,re.M)
def allids(path): return set(re.findall(r'^\[(\S+?)\]',open(path).read(),re.M))
def write(pk,out,cost,links):
    pf=P+f'packs/geo-mapwork-s1.{pk}.txt'
    tg=ids(pf); a=allids(pf)
    assert list(out)==tg,(pk,set(tg)^set(out))
    for k,v in out.items():
        for n in v['needs']: assert n['id'] in a and n['id']!=k,(k,n['id'])
    json.dump(out,open(P+f'point-links/geo-mapwork-s1.{pk}.json','w'),indent=1)
    nl=sum(len(v['needs']) for v in out.values())
    c2=sum(1 for v in out.values() if v.get('cost')==2)
    low=sum(1 for v in out.values() for n in v['needs'] if n['confidence']=='low')
    print(pk,len(out),nl,c2,low)
write('t1g1',build(d,True),True,None)
d2=[(i,c,[]) for i,c,n in d]
d2=[(i,c,[('geo-glaciation-s1.9.3',H,'U-shaped valley contours','H')] if i=='10.0' else []) for i,c,n in d]
write('t1g2',build(d2,False),False,None)
d3=[(i,c,[]) for i,c,n in d]
write('t1g3',build(d3,False),False,None)
