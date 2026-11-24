import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/history/'
pk=open(P+'packs/hist-eur2-s8.t1g1.txt').read()
targets=re.findall(r'^\[(hist-eur2-s8\.[^\]]+)\]',pk,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',pk,re.M))
E,H='essential','helpful'
def n(i,s,w,c='high'):return dict(id=('hist-eur2-' if i[0]=='s' else 'hist-eur2-s8.')+i,strength=s,why=w,confidence=c)
D={
'0.b':(1,[]),'0.0':(1,[]),'0.1':(1,[]),'0.2':(1,[]),'0.3':(1,[]),
'0.4':(1,[n('0.0',H,'Alexander II and serf emancipation','low')]),
'0.5':(2,[n('0.4',H,'Alexander II as predecessor')]),
'0.6':(1,[n('0.5',H,'Nicholas II and autocracy')]),
'1.b':(2,[]),'1.0':(1,[n('1.b',H,"Witte's industrialisation policy")]),
'1.1':(2,[n('1.0',H,'state-built railways policy')]),
'1.2':(2,[n('s2.0.2',H,'Franco-Russian Alliance'),n('1.b',H,'Witte financing industry','low')]),
'1.3':(2,[]),'1.4':(1,[]),
'1.5':(1,[n('1.b',H,"Witte's industrial spurt costs",'low')]),
'1.6':(1,[]),
'2.0':(1,[n('0.0',H,'redemption payments')]),
'2.1':(1,[]),'2.2':(1,[n('2.1',E,'the 1891 famine')]),
'2.3':(1,[n('2.1',H,'famine prompting opposition'),n('0.6',H,'Social Revolutionaries','low')]),
'2.4':(1,[]),'2.5':(1,[]),
'3.0':(1,[n('1.1',H,'Trans-Siberian Railway')]),
'3.1':(1,[]),
'3.2':(2,[n('3.0',H,'Port Arthur and rivalry')]),
'3.3':(1,[]),
'3.4':(2,[n('3.2',H,'the war being ended')]),
'3.5':(1,[n('3.2',E,'the defeat in the war')]),
'4.0':(2,[]),
'4.1':(2,[n('4.0',E,'Bloody Sunday massacre')]),
'4.2':(1,[]),
'4.3':(2,[n('1.b',H,'Witte as adviser'),n('4.2',H,'general strike prompting concessions')]),
'4.4':(2,[n('4.3',E,'the October Manifesto'),n('4.2',H,'the Soviet and strike')]),
'4.5':(1,[n('4.3',H,'the Duma','low')]),
'4.6':(2,[n('4.3',E,'October Manifesto and Duma')]),
'5.b':(1,[]),
'5.0':(1,[n('4.3',E,'the Duma created in 1905')]),
'5.1':(2,[n('5.0',H,'the dissolved Dumas'),n('5.b',H,'Stolypin')]),
'5.2':(1,[n('5.b',H,'Stolypin')]),
'5.3':(2,[n('0.1',E,'the mir commune')]),
'5.4':(1,[n('5.3',E,'the land reform leaving communes')]),
'5.5':(1,[n('5.b',H,'Stolypin')]),
'5.6':(1,[]),
'6.0':(2,[n('s5.0.6',H,'Tannenberg and Masurian Lakes'),n('s5.3.1',H,'Brusilov Offensive'),n('s5.3.0',H,'1915 Russian retreat','low')]),
'6.1':(1,[]),
'6.2':(2,[n('6.3',H,'Rasputin')]),
'6.3':(1,[]),
'6.4':(2,[n('6.1',H,'food shortages in cities','low')]),
'6.5':(2,[n('6.4',E,'the March 1917 strikes'),n('4.2',H,'the Soviet idea')]),
'7.0':(2,[n('6.5',E,'Provisional Committee and Soviet'),n('4.2',H,'the Soviet')]),
'7.1':(1,[n('7.0',E,'the Provisional Government')]),
'7.2':(1,[n('7.0',H,'Provisional Government and Soviets')]),
'7.3':(2,[n('7.0',E,'Kerensky and Provisional Government'),n('7.2',H,'Bolsheviks gaining strength')]),
'7.4':(1,[n('7.2',H,'Bolsheviks in the Soviets')]),
'7.5':(2,[n('7.4',E,'Bolsheviks controlling the Soviets'),n('7.2',H,"Lenin's April Theses")]),
'7.6':(2,[n('7.5',E,'the Bolshevik seizure of power')]),
'8.0':(2,[n('7.5',E,'the Bolshevik government'),n('7.4',H,'Trotsky','low')]),
'8.1':(1,[n('7.5',H,'Bolshevik government moving capital')]),
'8.2':(2,[n('7.5',H,'Bolsheviks as the Reds'),n('7.4',H,'Trotsky as organiser','low')]),
'8.3':(1,[n('8.2',E,'the Whites in civil war')]),
'8.4':(1,[n('8.2',E,'Reds and Whites')]),
'8.5':(1,[n('8.2',H,'the civil war','low')]),
'8.6':(2,[n('8.2',E,'Reds, Whites and the civil war')]),
'9.0':(2,[n('1.b',H,"Witte's industrialisation"),n('5.3',H,"Stolypin's reforms")]),
'9.1':(1,[n('1.4',H,'huge factories and workers')]),
'9.2':(1,[n('4.6',H,'Dumas and tsar powers')]),
'9.3':(2,[n('4.4',E,'1905 army loyal, opposition split'),n('6.4',E,'1917 soldiers joining strikers')]),
'9.4':(2,[]),
'9.5':(2,[n('7.5',H,'Bolshevik coup of 1917'),n('7.1',H,'Provisional Government failure','low')]),
}
out={}
for t in targets:
    k=t.replace('hist-eur2-s8.','')
    assert k in D,k
    c,l=D[k]
    for x in l:
        assert x['id'] in allids and x['id']!=t,(t,x['id'])
    out[t]={'cost':c,'needs':l}
assert len(out)==len(D)==len(targets),(len(out),len(D),len(targets))
json.dump(out,open(P+'point-links/hist-eur2-s8.t1g1.json','w'),indent=1)
chk=json.load(open(P+'point-links/hist-eur2-s8.t1g1.json'))
ls=[x for v in chk.values() for x in v['needs']]
print(len(chk),len(ls),sum(v['cost']==2 for v in chk.values()),sum(x['confidence']=='low' for x in ls))
