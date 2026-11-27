from common import *
P='hom-social-change-s6.';S1='hom-unemployment-poverty-s1.';S6='hom-unemployment-poverty-s6.'
def n(i,s,w,c='high'):return {"id":i,"strength":s,"why":w,"confidence":c}
H='helpful'
one=['0.b','0.1','0.2','0.3','1.b','1.0','1.1','1.2','1.3','2.b','2.0','2.1','2.2','2.3','2.4','2.5','2.6','2.7','3.b','3.0','3.2','3.3','3.4','3.5','3.6','3.7','4.b','4.0','4.1','5.b','5.0','5.1','5.2','5.4','5.5','5.6','6.b','6.0','6.3','6.4','7.b','7.0','7.2','7.3','7.4','7.5','8.b']
T={k:(1,[]) for k in one}
T.update({
'0.0':(1,[n(S1+'0.0',H,'three-part definition of unemployed')]),
'3.1':(2,[n(S6+'2.5',H,'MABS money advice service')]),
'5.3':(1,[n(P+'0.3',H,'unemployment black spots')]),
'6.1':(2,[n(S6+'0.0',H,'social insurance payments, PRSI based'),n(S6+'0.1',H,'means-tested social assistance')]),
'6.2':(2,[n(S6+'0.5',H,'Supplementary Welfare Allowance'),n(S6+'1.2',H,'Working Family Payment')]),
'6.5':(2,[n(S6+'3.0',H,'SOLAS and ETBs')]),
'6.6':(2,[n(S6+'3.6',H,'Community Employment scheme')]),
'7.1':(1,[n(S6+'2.5',H,'MABS money advice service')]),
'8.0':(1,[n(P+'2.1',H,'psychological effects of job loss')]),
'8.1':(1,[n(P+'3.4',H,'partner working longer hours'),n(P+'3.2',H,'financial strain on relationship')]),
'8.2':(1,[n(P+'3.5',H,'effects on children')]),
'8.3':(2,[n(P+'6.1',H,'Jobseeker payments'),n(P+'7.1',H,'MABS'),n(P+'7.0',H,'Citizens Information'),n(P+'7.2',H,'SVP'),n(P+'6.4',H,'Back to Education Allowance')]),
})
run('hom-social-change-s6.t1g1',P,T)
