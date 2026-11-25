import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/biology/'
E,H='essential','helpful'
S='bio30-s2.'
# id: (cost, [(target,strength,why,conf)])
d={
'0.b':(1,[]),
'0.0':(2,[('bio30-s1.2.0',H,'xylem carries water','low')]),
'0.1':(1,[('bio30-s1.10.0',H,'stomata as pores','high')]),
'0.2':(2,[('bio25-s1.2.0',E,'osmosis definition','high'),('bio25-s1.0.6',H,'dilute vs concentrated solutions','high')]),
'0.3':(1,[('bio25-s1.2.0',E,'osmosis direction of water','high')]),
'0.4':(2,[('bio25-s1.2.0',E,'osmosis cell to cell','high')]),
'0.5':(1,[('bio30-s1.5.6',H,'endodermis around vascular tissue','high')]),
'0.6':(2,[(S+'1.2',H,'transpiration pull as driving force','high')]),
'0.7':(1,[(S+'7.0',H,'root pressure','high'),(S+'8.0',H,'cohesion-tension model','high')]),
'1.b':(1,[]),
'1.0':(1,[('bio25-s1.2.0',H,'osmosis into mesophyll','high')]),
'1.1':(2,[('bio25-s1.1.0',E,'diffusion down gradient','high')]),
'1.2':(2,[(S+'1.1',E,'evaporation from leaves','high')]),
'1.3':(1,[(S+'1.2',H,'transpiration pull is passive','high')]),
'1.4':(2,[(S+'0.0',H,'route of water','low')]),
'2.b':(1,[]),
'2.0':(1,[('bio30-s1.10.0',H,'stomata','high')]),
'2.1':(1,[(S+'2.0',H,'transpiration definition','high')]),
'2.2':(1,[(S+'0.1',H,'transpiration stream','high')]),
'2.3':(1,[('bio25-s1.3.3',H,'turgid cells','high')]),
'2.4':(1,[('bio30-s1.10.b',H,'stomata let CO2 in','low')]),
'2.5':(2,[('bio25-s1.3.3',H,'turgor and wilting','high')]),
'2.6':(2,[]),
'3.b':(1,[]),
'3.0':(1,[('bio30-s1.10.0',E,'stoma between guard cells','high')]),
'3.1':(2,[('bio25-s1.4.0',E,'active transport of K+','high'),('bio25-s1.2.0',E,'water enters by osmosis','high')]),
'3.2':(2,[(S+'3.0',E,'thick inner wall','high'),('bio25-s1.3.3',H,'turgid cells','high')]),
'3.3':(1,[(S+'3.1',E,'reverse of opening','high')]),
'3.4':(2,[(S+'3.2',H,'open guard cell shape','high')]),
'4.b':(1,[]),
'4.0':(1,[(S+'2.4',H,'CO2 needed via stomata','high')]),
'4.1':(1,[(S+'4.0',H,'when stomata open','high')]),
'4.2':(1,[(S+'2.5',H,'wilting','high')]),
'4.3':(1,[('bio30-s1.10.2',H,'stomata on shaded lower surface','high')]),
'5.b':(1,[]),
'5.0':(2,[('bio30-s1.9.0',H,'waxy cuticle','high')]),
'5.1':(1,[]),
'5.2':(1,[]),
'5.3':(2,[]),
'6.b':(1,[]),
'6.0':(1,[]),
'6.1':(2,[('bio25-s1.4.0',E,'active transport against gradient','high')]),
'6.2':(1,[('bio25-s1.1.0',E,'diffusion','high')]),
'6.3':(1,[(S+'6.1',E,'active transport needs ATP','high')]),
'6.4':(1,[(S+'6.3',E,'roots need oxygen','high')]),
'6.5':(2,[(S+'0.1',E,'transpiration stream carries minerals','high')]),
'6.6':(1,[(S+'6.1',E,'ion pumping into root','high')]),
'7.b':(1,[]),
'7.0':(1,[('bio30-s1.2.0',H,'xylem','low')]),
'7.1':(2,[(S+'6.1',H,'active pumping of ions','high'),('bio25-s1.2.0',E,'water enters by osmosis','high')]),
'7.2':(1,[(S+'7.1',H,'root pressure cause','high')]),
'7.3':(1,[(S+'7.0',H,'root pressure','high')]),
'7.4':(1,[(S+'7.3',E,'guttation','high')]),
'7.5':(1,[(S+'7.1',H,'active process in living cells','high')]),
'7.6':(1,[(S+'7.5',E,'conditions that stop it','high')]),
'7.7':(1,[(S+'7.0',H,'root pressure','high')]),
'7.8':(1,[(S+'7.0',H,'root pressure','high')]),
'8.b':(1,[]),
'8.0':(1,[]),
'8.1':(1,[(S+'1.1',H,'evaporation and diffusion from leaf','high')]),
'8.2':(1,[(S+'1.0',H,'water to mesophyll by osmosis','high')]),
'8.3':(2,[(S+'1.2',E,'transpiration pull','high')]),
'8.4':(2,[]),
'8.5':(1,[(S+'8.4',H,'cohesion of water column','low')]),
'8.6':(1,[(S+'0.2',H,'water into root hairs','low')]),
'8.7':(1,[('bio30-s1.2.6',H,'lignin stops collapse','high')]),
'9.b':(1,[]),
'9.0':(1,[(S+'8.3',E,'tension in xylem','high')]),
'9.1':(1,[(S+'8.3',E,'xylem under tension','high')]),
'9.2':(1,[(S+'9.1',E,'air breaks column','high')]),
'9.3':(1,[(S+'8.5',H,'adhesion','high')]),
'10.b':(1,[]),
'10.0':(1,[(S+'7.0',E,'root pressure pushes','high'),(S+'8.3',E,'tension pulls','high')]),
'10.1':(1,[(S+'7.1',H,'root pressure uses ATP','high'),(S+'8.7',H,'passive cohesion-tension','high')]),
'10.2':(1,[(S+'7.8',H,'root pressure weak','high')]),
'10.3':(1,[(S+'7.7',H,'root pressure timing','high')]),
}
out={}
for k,(c,n) in d.items():
    out[S+k]={'cost':c,'needs':[{'id':i,'strength':s,'why':w,'confidence':f} for i,s,w,f in n]}
json.dump(out,open(P+'point-links/bio30-s2.json','w'),indent=1)
txt=open(P+'points/bio30-s2.txt').read()
ids=re.findall(r'^\[([^\]]+)\]',txt,re.M)
tgt=[i for i in ids if i.startswith('bio30-s2.')]
o=json.load(open(P+'point-links/bio30-s2.json'))
assert sorted(tgt)==sorted(o) and len(tgt)==len(o)
for k,v in o.items():
    for n in v['needs']: assert n['id'] in ids and n['id']!=k,(k,n)
print(len(o),sum(len(v['needs']) for v in o.values()),sum(v['cost']==2 for v in o.values()),sum(n['confidence']=='low' for v in o.values() for n in v['needs']))
