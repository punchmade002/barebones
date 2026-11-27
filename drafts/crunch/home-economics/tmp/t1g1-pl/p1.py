import json
P='hom-education-s2.'
def L(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
S='hom-sociological-concepts-s2.'
c2={'0.4','1.3','1.4','1.5','3.0','3.2','4.3'}
ids='0.b 0.0 0.1 0.2 0.3 0.4 0.5 0.6 1.b 1.0 1.1 1.2 1.3 1.4 1.5 1.6 2.b 2.0 2.1 2.2 3.b 3.0 3.1 3.2 3.3 4.b 4.0 4.1 4.2 4.3 5.b 5.0 5.1 5.2 5.3 5.4 5.5'.split()
links={
'1.3':[L(S+'2.0','helpful','socio-economic group meaning'.replace('2.0','')) ] ,
}
links={
'1.3':[L(S+'2.0','helpful','uses socio-economic background')],
'1.6':[L(P+'1.3','helpful','uses family finances and poverty','low')],
'3.0':[L('hom-education-s1.0.1','helpful','uses school ethos')],
'4.0':[L(S+'2.7','helpful','disadvantaged areas and early leaving','low')],
'5.0':[L(P+'0.5','helpful','repeats choice of course')],
'5.1':[L(P+'0.6','helpful','part-time work cuts study time')],
'5.2':[L(P+'1.4','helpful','uses home environment for study')],
'5.3':[L(P+'2.0','helpful','uses peer influence'),L(P+'1.0','helpful','uses parental attitude')],
'5.5':[L(P+'0.2','helpful','uses work ethic'),L(P+'0.0','helpful','uses intellectual ability')],
}
d={P+i:{"cost":2 if i in c2 else 1,"needs":links.get(i,[])} for i in ids}
json.dump(d,open('/Users/gabrielwhelan/barebones/.claude/worktrees/crunch-chem-home/drafts/crunch/home-economics/point-links/hom-education-s2.t1g1.json','w'),indent=1)
