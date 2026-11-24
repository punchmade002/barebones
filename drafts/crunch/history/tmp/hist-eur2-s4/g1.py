import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/history/'
E,H='essential','helpful'
def L(i,s,w,c='high'):return {"id":i,"strength":s,"why":w,"confidence":c}
p='hist-eur2-s4.'
D=[
('0.b',1,[]),
('0.0',1,[L('hist-eur2-s1.3.4',H,'Congress of Berlin recognised independence')]),
('0.1',1,[]),
('0.2',1,[]),
('0.3',1,[L(p+'0.0',H,'Obrenović dynasty')]),
('0.4',1,[L(p+'0.3',H,'new Karadjordjević regime')]),
('0.5',2,[L(p+'0.1',E,'Serbian livestock exports to Habsburg market')]),
('0.6',1,[L(p+'0.2',H,'South Slav unity threat')]),
('1.0',1,[L('hist-eur2-s1.3.4',H,'Austria allowed to administer Bosnia')]),
('1.1',1,[L(p+'1.0',E,'Austrian hold on Bosnia')]),
('1.2',2,[L(p+'1.0',E,'Bosnia and its status')]),
('1.3',1,[L(p+'1.2',E,'Buchlau deal on annexation')]),
('1.4',2,[L(p+'1.3',E,'the Austrian annexation of Bosnia')]),
('1.5',2,[L(p+'1.3',E,'the annexation Russia was told to accept'),L('hist-eur2-s2.5.4',H,'Russia weakened by war with Japan','low')]),
('1.6',1,[L(p+'1.5',E,'Russia and Serbia forced to back down')]),
('2.0',2,[L(p+'0.4',H,'Russian backing of Serbia','low')]),
('2.1',1,[L(p+'2.0',E,'the Balkan League')]),
('2.2',2,[L(p+'2.1',E,'League victory in First Balkan War')]),
('2.3',2,[L(p+'2.0',E,'Balkan League members')]),
('2.4',1,[L(p+'2.3',E,'ends the Second Balkan War')]),
('2.5',1,[L(p+'2.4',E,'Serbia's gains in 1913'.replace("'","")),L(p+'0.6',H,'Conrad urging preventive war')]),
('2.6',2,[L(p+'2.2',H,'London Conference diplomacy')]),
('3.0',1,[]),
('3.1',1,[L(p+'3.0',E,'the Black Hand society')]),
('3.2',2,[]),
('3.3',2,[L(p+'3.2',E,'the Sarajevo visit')]),
('3.4',1,[L(p+'3.3',E,'Princip and the assassination'),L(p+'3.1',H,'Black Hand arming Bosnians')]),
('3.5',1,[L(p+'3.3',E,'the assassins')]),
('3.6',1,[L(p+'3.3',H,'the murder of the Archduke')]),
('4.0',2,[L(p+'3.6',E,'Austria seeking German response')]),
('4.1',1,[L('hist-eur2-s2.0.2',H,'Franco-Russian Alliance')]),
('4.2',2,[L(p+'3.6',H,'Austria resolved to destroy Serbia')]),
('4.3',1,[L(p+'4.2',E,'the ultimatum')]),
('4.4',2,[L(p+'4.3',E,'Austria declaring war on Serbia')]),
('4.5',2,[L(p+'4.4',E,'Germany declaring war on Russia'),L('hist-eur2-s2.0.4',H,'Schlieffen Plan origin','low')]),
('4.6',2,[L(p+'4.5',E,'Germany attacking France through Belgium')]),
('4.7',1,[L(p+'4.6',E,'Britain entering over Belgium')]),
('5.b',1,[]),
('5.0',1,[]),
('5.1',2,[]),
('5.2',2,[L(p+'5.1',H,'Luxemburg and Lenin positions')]),
('5.3',1,[L(p+'2.1',H,'the First Balkan War')]),
('5.4',1,[L(p+'5.1',H,'Jaurès general strike stance')]),
('5.5',2,[L(p+'5.0',H,'the German SPD')]),
('5.6',2,[L(p+'5.5',E,'socialists backing their governments')]),
('5.7',2,[L(p+'5.6',E,'anti-war socialist minority')]),
('6.b',1,[L(p+'5.b',H,'the Second International')]),
('6.0',1,[]),
('6.1',1,[]),
('6.2',2,[L(p+'6.1',H,'her SPD membership','low')]),
('6.3',1,[L(p+'6.1',H,'her SPD membership','low')]),
('6.4',2,[L(p+'5.5',E,'SPD vote for war credits')]),
('6.5',2,[L(p+'6.4',H,'her opposition to the war')]),
('6.6',1,[]),
('6.7',1,[]),
('6.8',2,[L(p+'6.5',H,'Spartacus League origins')]),
('6.9',1,[]),
('6.10',1,[]),
('7.0',1,[L('hist-eur2-s2.1.5',H,'Triple Entente and Triple Alliance')]),
('7.1',1,[L('hist-eur2-s2.0.4',H,'Schlieffen Plan')]),
('7.2',1,[L('hist-eur2-s2.7.0',H,'Moroccan crises')]),
('7.3',2,[L('hist-eur2-s1.2.0',H,'French revanche and Alsace-Lorraine')]),
('7.4',2,[L(p+'4.0',H,'the blank cheque','low')]),
('7.5',1,[L(p+'1.6',H,'Austro-Russian Balkan rivalry','low')]),
('8.0',1,[L(p+'4.4',H,'Russian mobilisation')]),
('8.1',1,[L(p+'4.0',H,'the blank cheque')]),
('8.2',2,[L(p+'4.0',H,'German leaders risking war')]),
('8.3',2,[L(p+'8.2',H,'earlier Fischer thesis','low')]),
('8.4',2,[L(p+'4.0',H,'Germany blank cheque')]),
('8.5',1,[]),
]
txt=open(P+'packs/hist-eur2-s4.t1g1.txt').read()
tg=re.findall(r'^\[(hist-eur2-s4\.[^\]]+)\]',txt,re.M)
ids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
out={}
for k,c,n in D:out['hist-eur2-s4.'+k]={"cost":c,"needs":n}
assert list(out)==tg,(set(tg)^set(out))
for k,v in out.items():
  for n in v['needs']:assert n['id'] in ids and n['id']!=k,n
json.dump(out,open(P+'point-links/hist-eur2-s4.t1g1.json','w'),ensure_ascii=False)
j=json.load(open(P+'point-links/hist-eur2-s4.t1g1.json'))
ns=[n for v in j.values() for n in v['needs']]
print(len(j),len(ns),sum(v['cost']==2 for v in j.values()),sum(n['confidence']=='low' for n in ns))
