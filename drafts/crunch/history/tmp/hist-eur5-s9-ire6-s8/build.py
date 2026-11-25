import json,re,sys
H='helpful';E='essential'
def run(pack,out,spec,prefix):
    txt=open(pack).read()
    targets=re.findall(r'^\[('+prefix+r'\.[^\]]+)\]',txt,re.M)
    allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
    res={}
    for tid,cost,needs in spec:
        res[prefix+'.'+tid]={"cost":cost,"needs":[{"id":(n[0] if n[0].startswith('hist-') else prefix+'.'+n[0]),"strength":n[1],"why":n[2],"confidence":n[3]} for n in needs]}
    assert list(res)==targets,(set(targets)-set(res),set(res)-set(targets))
    for k,v in res.items():
        for n in v['needs']:
            assert n['id'] in allids and n['id']!=k,(k,n)
    json.dump(res,open(out,'w'),indent=1,ensure_ascii=False)
    json.loads(open(out).read())
    print(len(res),sum(len(v['needs']) for v in res.values()),sum(v['cost']==2 for v in res.values()),sum(n['confidence']=='low' for v in res.values() for n in v['needs']))
P='/Users/gabrielwhelan/barebones/drafts/crunch/history/'
S9=[
('0.b',1,[('0.0',H,'uses banlieues','high')]),
('0.0',1,[]),
('0.1',1,[('0.0',E,'banlieues estate','high')]),
('0.2',1,[]),
('0.3',1,[('0.0',H,'banlieues','high')]),
('0.4',1,[('0.0',H,'banlieues','high')]),
('0.5',1,[]),
('0.6',1,[('0.0',H,'banlieue housing estates','high')]),
('0.7',1,[]),
('1.0',1,[('0.1',E,'Minguettes estate','high')]),
('1.1',1,[('1.0',E,'the Minguettes unrest','high')]),
('1.2',1,[('1.0',H,'unrest being responded to','high')]),
('1.3',2,[('1.2',H,'Mitterrand government programmes','high')]),
('1.4',1,[]),
('1.5',1,[('1.2',H,'Mitterrand government reforms','high')]),
('1.6',1,[('1.2',H,'Mitterrand government promises','high')]),
('2.0',2,[('0.1',H,'Minguettes estate','high')]),
('2.1',1,[('2.0',E,'the march','high'),('1.5',H,'ten-year residence card','high')]),
('2.2',1,[('2.0',E,'the march','high')]),
('2.3',1,[('2.0',E,'the march','high')]),
('3.0',2,[]),
('3.1',1,[('3.0',E,'SOS Racisme','high')]),
('3.2',1,[('3.0',E,'SOS Racisme','high')]),
('3.3',1,[('3.0',E,'SOS Racisme','high')]),
('3.4',1,[('3.0',E,'SOS Racisme','high')]),
('3.5',1,[('3.0',E,'SOS Racisme','high'),('2.0',H,'1983 marchers','high')]),
('4.0',2,[('s4.3.0',H,'French Algeria cause','low')]) if False else ('4.0',2,[('hist-eur5-s4.3.0',H,'French Algeria cause','low')]),
('4.1',1,[('4.0',E,'the Front National','high')]),
('4.2',2,[('4.0',E,'the Front National','high')]),
('4.3',1,[('4.0',E,'the Front National','high')]),
('4.4',1,[('4.0',E,'the Front National','high')]),
('4.5',1,[('4.0',H,'the Front National','high')]),
('4.6',2,[('4.0',E,'Le Pen and the FN','high')]),
('4.7',2,[('4.0',E,'Le Pen','high')]),
('5.0',1,[]),
('5.1',2,[('5.0',H,'Chirac government policy','high'),('3.0',H,'SOS Racisme','high')]),
('5.2',1,[('5.0',E,'Chirac government laws','high')]),
('5.3',2,[('5.2',H,'the 1986 restrictions','high'),('hist-eur5-s8.7.1',H,'assimilation','high')]),
('5.4',1,[('5.0',H,'Chirac government','high')]),
('6.0',1,[]),
('6.1',1,[('6.0',E,'Creil headscarf affair','high')]),
('6.2',2,[('6.1',E,'Conseil d\'Etat ruling','high'),('hist-eur5-s8.7.2',E,'laicite','high')]),
('6.3',1,[('6.1',H,'Conseil d\'Etat ruling','high')]),
('7.0',1,[('hist-eur5-s4.5.3',H,'Algerian independence 1962','high')]),
('7.1',1,[('hist-eur5-s4.6.1',E,'the harkis','high')]),
('7.2',1,[('4.0',E,'the Front National','high')]),
('7.3',1,[('hist-eur5-s4.5.0',E,'Evian Accords','high'),('hist-eur5-s4.6.0',H,'settler departure','high')]),
('7.4',1,[('hist-eur5-s4.6.0',E,'pieds-noirs departure','high'),('4.5',H,'FN southern support','high')]),
('7.5',2,[('hist-eur5-s8.6.0',H,'Algerians French before 1962','high'),('5.1',H,'nationality reform proposals','low')]),
('8.0',1,[('1.0',H,'French urban unrest','high'),('4.0',H,'French far-right party','high'),('hist-eur5-s8.4.1',H,'British 1981 riots','high')]),
('8.1',1,[('hist-eur5-s8.7.3',H,'no ethnic statistics','high')]),
('8.2',1,[('hist-eur5-s8.7.1',E,'assimilation model','high')]),
('8.3',1,[('hist-eur5-s8.4.3',E,'Scarman Report','high'),('hist-eur5-s8.3.2',H,'Race Relations Acts','high')]),
('8.4',1,[('1.6',E,'voting rights promise','high'),('hist-eur5-s8.0.5',H,'Commonwealth migrants voting','high')]),
('8.5',2,[('hist-eur5-s8.4.3',E,'Scarman Report','high'),('1.0',H,'French unrest','high'),('1.3',H,'regeneration programmes','high')]),
('9.0',1,[('2.0',E,'1983 march','high'),('3.0',E,'SOS Racisme','high')]),
('9.1',1,[('5.0',H,'immigration control laws','high')]),
('9.2',1,[('6.1',E,'1989 headscarf ruling','high')]),
('9.3',1,[('4.2',H,'FN electoral success','high')]),
('9.4',2,[('1.0',H,'banlieue unrest','high')]),
('9.5',2,[('0.0',H,'banlieues','high')]),
('9.6',2,[('5.3',E,'integration over assimilation','high'),('4.1',H,'FN anti-immigration stance','high')]),
]
S9=[(a,b,c) for a,b,c in S9]
run(P+'packs/hist-eur5-s9.t1g1.txt',P+'point-links/hist-eur5-s9.t1g1.json',S9,'hist-eur5-s9')
