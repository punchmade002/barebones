import json,re
P='hist-eur1-s7.'
H,E='helpful','essential'
def n(t,s,w,c='high'): return (t,s,w,c)
d={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[n('0.0',H,'industrialisation defined')]),'0.2':(2,[]),'0.3':(2,[]),'0.4':(1,[]),'0.5':(1,[]),'0.6':(1,[]),
'1.b':(1,[]),'1.0':(1,[]),'1.1':(1,[n('1.0',E,'uses enclosure')]),'1.2':(1,[n('1.1',E,'enclosure by private Acts')]),
'1.3':(1,[n('1.0',E,'enclosed farms')]),'1.4':(1,[n('1.0',E,'enclosure and common land')]),'1.5':(1,[n('1.4',E,'loss of land and common rights')]),
'2.b':(1,[]),'2.0':(2,[]),'2.1':(1,[n('2.0',E,'uses turnips and clover rotation')]),'2.2':(1,[n('2.0',H,'Norfolk rotation')]),'2.3':(1,[]),'2.4':(1,[]),
'3.b':(1,[]),'3.0':(1,[]),'3.1':(2,[]),'3.2':(2,[]),'3.3':(2,[]),'3.4':(1,[n('3.3',H,'machines replacing hand work')]),
'3.5':(2,[n('3.3',E,'uses threshing machines')]),'3.6':(2,[]),
'4.b':(1,[]),'4.0':(1,[]),'4.1':(1,[n('4.0',E,'uses the Corn Law of 1815')]),'4.2':(1,[n('4.0',E,'uses the Corn Laws')]),
'5.b':(1,[]),'5.0':(1,[]),'5.1':(1,[n('5.0',H,'peasant small farms')]),'5.2':(2,[]),
'5.3':(2,[n('5.2',H,'Stein reforms ending serfdom')]),'5.4':(1,[n('5.3',H,'noble estates after reforms')]),'5.5':(1,[]),
'6.b':(1,[]),'6.0':(2,[n('5.5',H,'potato as staple of the poor')]),'6.1':(1,[n('6.0',H,'1840s hunger')]),
'6.2':(2,[n('6.0',E,'hunger of 1845-47')]),'6.3':(1,[n('6.0',H,'hunger driving emigration')]),'6.4':(1,[n('6.0',H,'potato blight')]),
'7.b':(1,[]),'7.0':(2,[]),'7.1':(1,[n('7.0',E,'uses Watt steam engine')]),'7.2':(2,[]),'7.3':(1,[n('7.2',H,'mechanised spinning')]),'7.4':(1,[]),
'7.5':(1,[n('7.4',H,'raw cotton imports')]),
'8.b':(1,[]),'8.0':(1,[]),'8.1':(1,[n('8.0',H,'iron industry growth','low')]),'8.2':(1,[]),'8.3':(1,[]),
'9.b':(1,[]),'9.0':(1,[]),'9.1':(1,[n('9.0',H,'early steam locomotives')]),'9.2':(1,[n('9.1',H,'Rocket and steam locomotives')]),
'9.3':(1,[n('9.2',H,'first inter-city railway')]),'9.4':(1,[]),'9.5':(1,[]),
'10.b':(1,[]),'10.0':(2,[]),'10.1':(1,[n('10.0',H,'obstacles to continental industry')]),'10.2':(1,[]),'10.3':(1,[]),
'10.4':(1,[n('10.3',H,'Belgian industrialisation')]),'10.5':(1,[n('10.3',H,'Belgian industrialisation')]),'10.6':(2,[]),
'11.b':(1,[]),'11.0':(1,[]),'11.1':(1,[]),'11.2':(1,[]),'11.3':(2,[]),'11.4':(1,[]),
'12.b':(1,[]),'12.0':(1,[]),'12.1':(1,[]),'12.2':(1,[]),'12.3':(1,[n('12.2',H,'Ruhr coal and iron','low')]),'12.4':(2,[n('12.0',H,'tariffs among German states','low')]),'12.5':(1,[]),
'13.b':(1,[]),'13.0':(1,[]),'13.1':(1,[n('7.3',H,'power loom replaced hand weavers')]),'13.2':(1,[]),'13.3':(1,[]),'13.4':(1,[]),'13.5':(1,[]),'13.6':(1,[]),
'14.b':(1,[]),'14.0':(1,[]),'14.1':(2,[]),'14.2':(2,[n('14.1',H,'Sadler evidence on child workers')]),
'14.3':(1,[n('14.2',E,'uses the 1833 Factory Act')]),'14.4':(1,[]),'14.5':(2,[n('14.2',H,'earlier Factory Act')]),
'15.b':(1,[]),'15.0':(1,[]),'15.1':(2,[]),'15.2':(1,[n('15.0',E,'laissez-faire as free trade'),n('4.2',H,'repeal of Corn Laws')]),
'15.3':(2,[n('15.0',E,'laissez-faire principle')]),'15.4':(1,[n('15.0',E,'limits of laissez-faire'),n('14.2',H,'Factory Acts')]),
'15.5':(1,[n('12.4',H,'List on protection')]),
'16.b':(1,[]),'16.0':(1,[]),'16.1':(1,[]),'16.2':(2,[n('1.5',H,'enclosure pushing people off land'),n('6.0',H,'1840s crisis')]),
'16.3':(1,[n('6.4',E,'uses the Irish Famine')]),'16.4':(1,[]),'16.5':(1,[]),'16.6':(1,[]),
'17.b':(1,[]),'17.0':(2,[]),'17.1':(1,[]),'17.2':(2,[n('17.1',H,'Little Ireland slum')]),'17.3':(2,[]),
'18.b':(1,[]),'18.0':(1,[n('17.3',H,'disease and sanitation')]),'18.1':(1,[n('18.0',H,'Chadwick report')]),'18.2':(1,[n('18.1',E,'uses 1848 Public Health Act')]),
'18.3':(1,[n('17.3',E,'uses cholera')]),'18.4':(1,[]),'18.5':(1,[]),'18.6':(1,[n('18.2',H,'permissive 1848 Act')]),
'19.b':(1,[]),'19.0':(1,[]),'19.1':(1,[n('19.0',H,'states expanding schooling')]),'19.2':(2,[]),'19.3':(1,[n('19.2',H,'Prussian schooling')]),
'19.4':(2,[]),'19.5':(1,[n('19.4',E,'uses the Guizot Law')]),'19.6':(1,[n('19.4',H,'French communal schools')]),
'20.b':(1,[]),'20.0':(1,[]),'20.1':(1,[n('20.0',E,'the two religious societies')]),'20.2':(1,[n('20.0',E,'the two societies')]),
'20.3':(2,[n('20.2',H,'first government grant')]),'20.4':(1,[]),'20.5':(2,[n('20.4',H,'poorly taught children')]),'20.6':(2,[n('20.0',H,'voluntary schools')]),
'21.b':(1,[]),'21.0':(1,[]),'21.1':(1,[n('21.0',H,'literacy rates')]),'21.2':(1,[]),'21.3':(1,[n('21.2',E,'uses spread of print')]),
'22.b':(1,[]),'22.0':(1,[]),'22.1':(2,[n('1.4',H,'loss of common rights'),n('17.0',H,'slum conditions')]),'22.2':(1,[]),
'22.3':(2,[n('15.0',E,'laissez-faire slowing response')]),'22.4':(2,[]),'22.5':(2,[n('17.2',H,'Engels witness account'),n('18.0',H,'Chadwick report'),n('8.3',H,'Great Exhibition')]),
'22.6':(2,[]),'22.7':(2,[]),
}
out={P+k:{'cost':c,'needs':[{'id':P+t,'strength':s,'why':w,'confidence':f} for t,s,w,f in ns]} for k,(c,ns) in d.items()}
txt=open('../../packs/hist-eur1-s7.t1g1.txt').read()
tg=re.findall(r'^\[(hist-eur1-s7\.\S+?)\]',txt,re.M)
assert tg==list(out),(set(tg)^set(out))
assert all(x['id'] in tg for v in out.values() for x in v['needs'])
assert all(x['id']!=k for k,v in out.items() for x in v['needs'])
json.dump(out,open('../../point-links/hist-eur1-s7.t1g1.json','w'),indent=1)
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(x['confidence']=='low' for v in out.values() for x in v['needs']))
