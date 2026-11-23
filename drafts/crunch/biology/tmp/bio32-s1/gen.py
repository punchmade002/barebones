import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/biology/'
txt=open(P+'points/bio32-s1.txt').read()
tgt,rest=txt.split('CANDIDATES',1)
tids=re.findall(r'^\[([^\]]+)\]',tgt,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
H,L='high','low'
E,Hl='essential','helpful'
c2={'1.3','5.2','8.1','8.5','15.0','15.4'}
N={
'0.0':[('bio31-s1.3.0',Hl,'habitat definition',H)],
'1.0':[('bio31-s1.3.1',Hl,'microhabitats',H)],
'1.4':[('bio32-s1.11.0',Hl,'identification keys',H)],
'3.4':[('bio31-s1.3.1',Hl,'microhabitat location',H)],
'4.2':[('bio32-s1.4.0',Hl,'how pitfall traps work',H)],
'4.3':[('bio32-s1.4.0',Hl,'pitfall trap',H)],
'4.4':[('bio32-s1.4.0',Hl,'pitfall trap',H)],
'4.5':[('bio32-s1.4.0',E,'pitfall trap structure',H)],
'5.1':[('bio32-s1.5.0',Hl,'Tullgren funnel purpose',H)],
'5.2':[('bio32-s1.5.1',E,'funnel set-up',H)],
'5.3':[('bio32-s1.5.1',Hl,'funnel beaker position',H)],
'5.5':[('bio32-s1.5.1',Hl,'funnel mesh and lamp',H)],
'5.6':[('bio32-s1.5.1',E,'funnel parts',H)],
'7.1':[('bio32-s1.7.0',E,'sweep net',H)],
'7.2':[('bio32-s1.7.0',Hl,'sweep net',H)],
'7.3':[('bio32-s1.7.0',Hl,'sweeps',H)],
'7.4':[('bio32-s1.7.0',Hl,'sweep net',H)],
'7.6':[('bio32-s1.7.5',E,'beating tray method',H),('bio32-s1.8.0',Hl,'pooter',H)],
'8.1':[('bio32-s1.8.0',E,'pooter structure',H)],
'8.2':[('bio32-s1.8.1',Hl,'mouthpiece tube',H)],
'8.3':[('bio32-s1.8.0',Hl,'pooter',H)],
'8.4':[('bio32-s1.8.0',Hl,'pooter',H)],
'8.5':[('bio32-s1.8.0',E,'pooter parts',H)],
'9.1':[('bio32-s1.9.0',Hl,'butterfly net catching',L)],
'9.3':[('bio32-s1.9.2',E,'light trap',H)],
'10.1':[('bio32-s1.0.1',Hl,'primary data',H)],
'11.1':[('bio32-s1.11.0',E,'identification key',H)],
'11.2':[('bio32-s1.11.1',E,'couplets',H)],
'11.4':[('bio32-s1.11.3',Hl,'good key features',H)],
'12.0':[('bio32-s1.11.1',E,'couplet format',H)],
'12.5':[('bio32-s1.11.1',Hl,'dichotomous splits',H)],
'12.6':[('bio32-s1.12.5',E,'key construction',H)],
'12.7':[('bio32-s1.11.1',Hl,'dichotomous splits',H)],
'13.3':[('bio6-s3.1.0',Hl,'species concept',L)],
'14.1':[('bio32-s1.14.0',Hl,'daisy and dandelion',H)],
'15.0':[('bio32-s1.7.5',Hl,'beating tray',H),('bio32-s1.5.0',Hl,'Tullgren funnel',H)],
'15.3':[('bio32-s1.7.0',Hl,'sweeping with net',L)],
'15.5':[('bio32-s1.15.4',Hl,'kick sampling',H)],
'18.3':[('bio32-s1.4.3',Hl,'checking traps',L)],
'18.4':[('bio32-s1.11.0',Hl,'identification keys',L)],
}
out={}
for i in tids:
    k=i.split('.',1)[1] if False else i[len('bio32-s1.'):]
    out[i]={'cost':2 if k in c2 else 1,'needs':[{'id':a,'strength':s,'why':w,'confidence':c} for a,s,w,c in N.get(k,[])]}
for v in out.values():
    for n in v['needs']: assert n['id'] in allids,n
open(P+'point-links/bio32-s1.json','w').write(json.dumps(out,indent=1))
d=json.load(open(P+'point-links/bio32-s1.json'))
assert list(d)==tids
ns=[n for v in d.values() for n in v['needs']]
print(len(d),len(ns),sum(v['cost']==2 for v in d.values()),sum(n['confidence']=='low' for n in ns))
