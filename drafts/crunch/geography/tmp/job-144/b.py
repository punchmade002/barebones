import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
V='geo-volcanoes-earthquakes-s1.'
T='geo-plate-tectonics-s3.'
R='geo-rocks-weathering-s1.'
E,H='essential','helpful'
def n(i,s,w,c='high'):
    return (i if '-s' in i and i.startswith('geo-') else V+i,s,w,c)
D={
'0.b':(1,[]),
'0.0':(1,[n('0.b',H,'magma defined')]),
'0.1':(1,[n('0.0',H,'magma chamber source')]),
'0.2':(1,[n('0.1',H,'main vent comparison')]),
'0.3':(1,[n('0.1',H,'crater tops main vent')]),
'0.4':(1,[n('1.3',H,'ash layers')]),
'0.5':(1,[n('1.0',H,'lava')]),
'0.6':(2,[n('0.0',E,'magma chamber label'),n('0.1',E,'main vent label'),n('0.2',E,'secondary vent label'),n('0.4',E,'cone structure'),n('0.5',E,'lava flow label'),n('1.4',H,'volcanic bombs label')]),
'1.b':(1,[]),
'1.0':(1,[n('0.b',H,'lava defined')]),
'1.1':(1,[]),
'1.2':(1,[]),
'1.3':(1,[n('1.2',H,'ash is pyroclastic')]),
'1.4':(1,[n('1.0',H,'lava')]),
'1.5':(1,[n('1.0',H,'lava')]),
'1.6':(1,[n('1.3',H,'ash')]),
'1.7':(1,[n('1.3',H,'ash')]),
'2.b':(1,[]),
'2.0':(1,[n('2.b',H,'silica and viscosity')]),
'2.1':(1,[n('2.0',E,'basic lava is runny')]),
'2.2':(1,[n('2.b',H,'silica and viscosity')]),
'2.3':(1,[n('2.2',E,'acidic lava viscous')]),
'2.4':(2,[n('2.0',E,'low-viscosity basic lava'),n('2.2',E,'viscous acidic lava')]),
'3.b':(1,[]),
'3.0':(1,[n('3.b',H,'volcano activity groups')]),
'3.1':(1,[n('3.b',H,'volcano activity groups')]),
'3.2':(1,[n('3.b',H,'volcano activity groups')]),
'4.b':(1,[n(T+'0.b',H,'plate boundary types')]),
'4.0':(1,[n(T+'0.0',E,'constructive boundary'),n('2.0',H,'basic magma')]),
'4.1':(1,[n('4.0',H,'Mid-Atlantic Ridge constructive')]),
'4.2':(2,[n(T+'5.1',E,'subduction'),n('2.2',H,'acidic magma')]),
'4.3':(1,[n('4.2',E,'subduction volcanoes'),n(T+'6.4',H,'Andes and Nazca subduction')]),
'4.4':(1,[n('4.2',E,'subduction volcanoes'),n(T+'7.1',H,'island arc defined')]),
'4.5':(1,[n(T+'8.1',H,'collision lacks volcanoes'),n(T+'10.1',H,'transform lacks magma')]),
'5.b':(1,[n('4.2',H,'destructive boundary volcanoes')]),
'5.0':(1,[n(T+'13.0',H,'Ring of Fire')]),
'5.1':(1,[n('5.0',H,'Ring of Fire')]),
'5.2':(2,[n('5.0',H,'Ring of Fire')]),
'6.b':(1,[]),
'6.0':(2,[n('6.b',E,'hot spot idea')]),
'6.1':(2,[n('6.0',E,'hot spot island chain ages')]),
'6.2':(1,[n('6.1',H,'Hawaii hot spot')]),
'6.3':(1,[n('6.b',H,'hot spot'),n('4.1',H,'Iceland constructive boundary')]),
'7.b':(1,[]),
'7.0':(1,[]),
'7.1':(1,[n('4.1',H,'Atlantic plates moving apart')]),
'7.2':(2,[n('7.1',E,'Atlantic opening cracked crust'),n('2.0',H,'basic runny lava'),n(T+'3.4.0'.replace('3.4.0','4.0'),H,'fissure eruptions')]),
'7.3':(1,[n(R+'3.2',H,'extrusive rock'),n('7.2',H,'Antrim fissure basalts')]),
'7.4':(1,[n('7.2',H,'Antrim basalts')]),
'8.b':(1,[]),
'8.0':(2,[n('1.0',H,'lava'),n('1.6',H,'pyroclastic flows'),n('1.7',H,'lahars')]),
'8.1':(1,[n('1.0',H,'lava')]),
'8.2':(1,[n('1.3',H,'ash')]),
'8.3':(2,[n('1.3',H,'ash cloud')]),
'8.4':(1,[]),
'8.5':(1,[]),
'8.6':(2,[n('1.1',H,'sulphur dioxide gas')]),
'8.7':(1,[]),
'9.b':(1,[]),
'9.0':(1,[n('1.3',H,'ash')]),
'9.1':(1,[]),
'9.2':(1,[]),
'9.3':(1,[n('1.5',H,'pumice')]),
'9.4':(1,[]),
'10.b':(1,[]),
'10.0':(1,[n(T+'6.5',H,'Juan de Fuca subduction')]),
'10.1':(1,[]),
'10.2':(1,[]),
'10.3':(1,[]),
'10.4':(1,[n('0.3',H,'crater')]),
'11.b':(1,[]),
'11.0':(1,[n('1.3',H,'ash')]),
'11.1':(1,[n('1.7',H,'lahars defined')]),
'11.2':(1,[]),
'11.3':(1,[]),
'12.b':(1,[]),
'12.0':(1,[]),
'12.1':(1,[]),
'12.2':(1,[n('1.1',H,'gases')]),
'12.3':(1,[]),
'12.4':(1,[]),
'12.5':(1,[]),
'12.6':(1,[]),
'13.b':(1,[]),
'13.0':(1,[n('12.0',H,'warning signs monitored')]),
'13.1':(1,[n('12.5',H,'hazard maps')]),
'13.2':(1,[]),
'13.3':(1,[n('0.5',H,'lava flow')]),
'13.4':(2,[n('13.3',H,'lava cooling and diverting')]),
'13.5':(2,[n('12.0',H,'monitoring signs')]),
}
txt=open(P+'packs/geo-volcanoes-earthquakes-s1.t1g1.txt').read()
ids=re.findall(r'^\[([^\]]+)\]',txt,re.M)
tg=[i for i in ids if i.startswith(V)]
assert set(D)=={i[len(V):] for i in tg} and len(D)==len(tg),(set(D)^{i[len(V):] for i in tg})
out={};links=0;c2=0;low=0
for i in tg:
    c,nd=D[i[len(V):]]
    for x in nd: assert x[0] in ids and x[0]!=i,x
    out[i]={'cost':c,'needs':[{'id':a,'strength':s,'why':w,'confidence':cf} for a,s,w,cf in nd]}
    links+=len(nd);c2+=c==2;low+=sum(x[3]=='low' for x in nd)
json.dump(out,open(P+'point-links/geo-volcanoes-earthquakes-s1.t1g1.json','w'),indent=1)
json.loads(open(P+'point-links/geo-volcanoes-earthquakes-s1.t1g1.json').read())
print(len(out),links,c2,low)
