import json,re
B='/Users/gabrielwhelan/barebones/drafts/crunch/biology/'
pk=open(B+'points/bio23-s2.txt').read()
allids=set(re.findall(r'^\[([^\]]+)\]',pk,re.M))
tgt=re.findall(r'^\[(bio23-s2\.[^\]]+)\]',pk.split('CANDIDATES')[0],re.M)
P='bio23-s2.'
H,E='helpful','essential'
d={ # id: (cost, [(need,strength,why,conf)])
'0.b':(1,[]),
'0.0':(1,[]),
'0.1':(1,[]),
'0.2':(1,[]),
'0.3':(1,[]),
'0.4':(1,[(P+'0.3',H,'egg route to fallopian tube','high')]),
'1.b':(1,[]),
'1.0':(1,[]),
'1.1':(1,[(P+'1.0',H,'openings of the vulva','low')]),
'1.2':(1,[(P+'1.1',E,'labia defined','high')]),
'1.3':(1,[(P+'1.1',E,'labia as folds over openings','high')]),
'1.4':(1,[(P+'1.0',H,'clitoris is part of vulva','high')]),
'1.5':(1,[(P+'1.4',E,'clitoris defined','high')]),
'1.6':(1,[(P+'1.0',H,'urethral opening in vulva','high')]),
'1.7':(1,[(P+'1.6',E,'female urethra carries urine only','high'),('bio23-s1.3.6',E,'male urethra carries semen and urine','high')]),
'2.b':(1,[]),
'2.0':(1,[(P+'1.0',H,'vulva as outer area','low')]),
'2.1':(1,[(P+'2.0',E,'vagina structure','high'),('bio23-s1.0.2',H,'semen','low')]),
'2.2':(1,[(P+'2.0',E,'vagina muscular elastic tube','high')]),
'2.3':(1,[(P+'2.0',E,'vagina as passage','high'),(P+'4.5',H,'menstruation','low')]),
'2.4':(2,[(P+'2.0',E,'vaginal lining','high')]),
'3.b':(1,[]),
'3.0':(1,[(P+'4.0',H,'uterus','high')]),
'3.1':(1,[(P+'3.0',E,'cervix defined','high')]),
'3.2':(2,[(P+'3.1',E,'cervical mucus','high'),(P+'6.1',H,'ovulation','high')]),
'3.3':(1,[(P+'3.1',E,'cervical mucus protects','high')]),
'3.4':(1,[(P+'3.0',E,'cervix defined','high')]),
'3.5':(1,[(P+'3.0',H,'cervix','high')]),
'4.b':(1,[]),
'4.0':(1,[]),
'4.1':(1,[(P+'4.0',H,'uterus','high')]),
'4.2':(1,[(P+'4.0',E,'muscular uterine wall','high')]),
'4.3':(1,[(P+'4.0',E,'uterus lining','high')]),
'4.4':(1,[(P+'4.3',E,'endometrium','high'),('bio20-s1.8.2',H,'oestrogen thickens endometrium','low')]),
'4.5':(1,[(P+'4.3',E,'endometrium','high')]),
'4.6':(1,[(P+'4.3',E,'endometrium','high')]),
'4.7':(1,[(P+'4.5',E,'menstruation sheds endometrium','high')]),
'5.b':(1,[]),
'5.0':(1,[(P+'4.0',H,'uterus','high')]),
'5.1':(1,[(P+'5.0',E,'fallopian tube','high'),(P+'6.0',H,'ovary','low')]),
'5.2':(1,[(P+'5.0',E,'fallopian tube','high'),('bio23-s1.3.3',H,'peristalsis','low')]),
'5.3':(1,[(P+'5.0',E,'fallopian tube','high'),(P+'0.4',H,'sperm route','high')]),
'5.4':(2,[(P+'5.0',E,'fallopian tube','high'),(P+'4.1',H,'implantation in uterus','high')]),
'5.5':(1,[(P+'5.4',E,'ectopic pregnancy','high')]),
'6.b':(1,[]),
'6.0':(1,[(P+'5.0',H,'fallopian tube','high')]),
'6.1':(2,[(P+'6.0',E,'ovaries','high')]),
'6.2':(1,[(P+'6.0',E,'ovaries','high')]),
'6.3':(1,[(P+'5.1',E,'funnel sweeps egg in','high'),(P+'6.0',H,'ovary not attached','high')]),
'7.b':(1,[]),
'7.0':(2,[(P+'5.1',H,'funnel and projections','low')]),
'7.1':(2,[(P+'7.0',H,'organs labelled','low'),(P+'1.0',H,'vulva parts','low')]),
'8.b':(1,[]),
'8.0':(1,[(P+'1.0',E,'vulva','high')]),
'8.1':(1,[(P+'1.3',E,'labia function','high')]),
'8.2':(1,[(P+'1.5',E,'clitoris function','high')]),
'8.3':(1,[(P+'2.0',E,'vagina','high')]),
'8.4':(1,[(P+'3.1',E,'cervix mucus','high')]),
'8.5':(1,[(P+'4.0',E,'uterus','high')]),
'8.6':(1,[(P+'4.3',E,'endometrium','high')]),
'8.7':(1,[(P+'5.2',E,'tube cilia and muscle','high')]),
'8.8':(1,[(P+'6.1',E,'follicles in ovary','high')]),
'9.b':(1,[]),
'9.0':(1,[('bio23-s1.2.0',H,'testes as male gonads','high'),(P+'6.0',H,'ovaries','high')]),
'9.1':(1,[('bio23-s1.2.1',H,'sperm production','high'),(P+'6.1',H,'one egg monthly','high')]),
'9.2':(1,[(P+'6.2',H,'ovarian hormones','high')]),
'9.3':(1,[('bio23-s1.1.0',H,'scrotum holds testes','high')]),
'9.4':(1,[(P+'1.6',E,'female urethra','high'),('bio23-s1.3.6',E,'male urethra carries semen','high')]),
}
out={}
for t in tgt:
    c,n=d[t.replace(P,'')]
    out[t]=dict(cost=c,needs=[dict(id=i,strength=s,why=w,confidence=f) for i,s,w,f in n])
assert list(out)==tgt and len(set(tgt))==len(d)
for t,v in out.items():
    for n in v['needs']: assert n['id'] in allids and n['id']!=t,(t,n)
json.dump(out,open(B+'point-links/bio23-s2.json','w'),indent=1)
L=sum(len(v['needs']) for v in out.values())
print(len(out),L,sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
