import json,re
D='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
P='geo-option-atmosphere-ocean-s6.'
A='geo-option-atmosphere-ocean-s5.'
S3='geo-option-atmosphere-ocean-s3.'
E='geo-economic-development-s2.'
two={'1.1','2.4','3.2','5.3','7.2','8.2','10.0','10.3','10.4','13.3','15.3','19.0','21.2','26.0','29.3'}
H,h='helpful','essential'
def L(pre,rows):
    d={}
    for k,t,s,w,c in rows: d.setdefault(P+k,[]).append({'id':pre+t,'strength':s,'why':w,'confidence':c})
    return d
g1=L(A,[('0.2','27.0',H,'climate change mechanism','low'),('1.1','9.1',H,'Irish rainfall pattern','high'),
('1.4','9.5',H,'brown earths soil','low'),('3.2','9.4',H,'anticyclones bring dry spells','high'),
('4.0','26.1',H,'warming trend','low'),('4.1','20.0',H,'greenhouse gas sources','high'),
('5.b','4.b',H,'monsoon climate','high'),('5.0','4.3',H,'monsoon timing and rainfall share','high'),
('5.1','7.3',H,'kharif and rabi crops','high'),('7.0','12.1',H,'dry summers and irrigation','high'),
('10.0','9.1',H,'Irish rainfall east-west','high'),('12.0','11.b',h,'Mediterranean climate','high'),
('13.3','1.4',h,'ITCZ','high'),('13.3','31.b',h,'El Nino','high'),('13.3','9.4',H,'blocking anticyclones','low'),
('16.0','34.b',h,'La Nina','high'),('19.0','1.4',H,'ITCZ','high'),('21.0','16.0',H,'Dust Bowl','high'),
('23.0','11.b',H,'Mediterranean climate','high'),('23.4','12.1',H,'dry summer','high'),
('24.1','12.4',H,'Canary Current','low'),('25.1','26.1',H,'warming','low'),
('28.0','28.1',H,'heatwaves','low'),('28.3','28.5',H,'sea-level rise','high')])
g2=L(S3,[('1.1','34.1',H,'Irish rainfall figures','high'),('5.b','33.1',H,'monsoon rainfall regime','high'),
('7.0','33.2',H,'Mediterranean dry summer','high'),('8.0','35.0',H,'Sahel rainfall variability','high'),
('8.2','35.b',H,'rainfall variability','high'),('9.0','0.1',H,'precipitation refills stores','low'),
('10.0','34.1',H,'Irish rainfall east-west','high'),('13.3','30.0',H,'ITCZ convergence','low'),
('19.0','35.0',H,'Sahel rainfall','high'),('23.0','33.2',H,'Mediterranean regime','high'),
('23.4','33.2',H,'dry summer','high'),('24.1','32.3',H,'cold ocean currents','low')])
g3=L(E,[('0.0','0.b',H,'rich vs poor countries','low'),('0.1','0.b',H,'rich vs poor countries','low'),
('1.6','3.3',H,'peripheral western region','high'),('10.1','3.1',H,'Dublin population share','high'),
('15.3','0.b',H,'rich and poor contrast','low'),('16.5','6.1',H,'Ethiopia famine and Live Aid','high'),
('16.b','6.0',H,'Sahel drought and famine','low'),('19.1','6.0',H,'Sahel droughts','high'),
('29.2','6.4',H,'tropical disease burden','high'),('29.3','6.3',H,'climate does not decide development','high')])
ids=re.findall(r'^\[(geo-option-atmosphere-ocean-s6\.[^\]]+)\]',open(D+'packs/'+P+'t1g1.txt').read().split('CANDIDATES')[0],re.M)
for n,(g,mode) in enumerate([(g1,1),(g2,0),(g3,0)],1):
    out={i:({'cost':2 if i[len(P):] in two else 1} if mode else {}) for i in ids}
    for i in ids: out[i]['needs']=g.get(i,[])
    json.dump(out,open(D+f'point-links/{P}t1g{n}.json','w'),indent=1)
    pk=open(D+f'packs/{P}t1g{n}.txt').read()
    pids=set(re.findall(r'^\[([^\]]+)\]',pk,re.M)); tg=re.findall(r'^\[([^\]]+)\]',pk.split('CANDIDATES')[0],re.M)
    assert tg==ids, n
    assert all(x['id'] in pids for v in out.values() for x in v['needs']) and all(x['id']!=i for i,v in out.items() for x in v['needs']),n
    ls=[x for v in out.values() for x in v['needs']]
    print(n,len(out),len(ls),sum(v.get('cost')==2 for v in out.values()),sum(x['confidence']=='low' for x in ls))
