import sys;sys.path.insert(0,'../hom-social-change-s6')
from common import *
P='hom-unemployment-poverty-s6.';F='hom-personal-finance-s1.';S1='hom-unemployment-poverty-s1.'
def n(i,s,w,c='high'):return {"id":i,"strength":s,"why":w,"confidence":c}
H='helpful';E='essential'
one=['0.b','1.b','1.0','1.4','2.b','2.0','2.1','2.2','2.5','3.b','3.0','3.2','3.3','3.4','3.5','3.6','4.b','4.0','4.1','4.2']
T={k:(1,[]) for k in one}
T.update({
'0.0':(1,[n(F+'4.3',H,'uses PRSI contributions')]),
'0.1':(1,[n(F+'6.4',H,'uses means test')]),
'0.2':(1,[n(P+'0.0',E,'social insurance payments')]),
'0.3':(1,[n(P+'0.1',E,'social assistance, means-tested'),n(P+'0.2',H,'Jobseeker\'s Benefit it follows')]),
'0.4':(2,[n(S1+'0.0',H,'unemployed, available, seeking work'),n(P+'0.3',E,'Jobseeker\'s Allowance')]),
'0.5':(1,[n(P+'0.1',H,'means-tested social assistance')]),
'1.1':(1,[n(P+'0.1',H,'means-tested payments')]),
'1.2':(2,[n(P+'0.1',H,'means-tested payment'),n(F+'7.1',H,'Working Family Payment details','low')]),
'1.3':(1,[n(P+'0.1',E,'means-tested payments')]),
'2.3':(2,[]),'2.4':(2,[]),'2.5':(1,[]),
'3.1':(2,[]),
'3.7':(2,[]),
'4.3':(1,[n(P+'4.b',H,'foreign direct investment')]),
'4.4':(1,[n(P+'4.3',H,'foreign investment creating jobs')]),
'4.5':(1,[n(P+'4.3',H,'multinational foreign investment')]),
'4.6':(1,[n(P+'4.0',H,'IDA Ireland role')]),
})
run('hom-unemployment-poverty-s6.t1g1',P,T)
