import json
O='/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/geography-pp-2017-higher-%s.json'
def edit(q,f):
    p=O%q; d=json.load(open(p)); f(d); json.dump(d,open(p,'w'))
W='geo-rocks-weathering-'
def q2(d): d['(ii)']=[{"k":2,"of":["geo-glaciation-s1.11.b","geo-glaciation-s1.7.3"]},{"k":1,"of":["geo-rocks-weathering-s4.4.0"]}]
def q4(d):
    d['(i)']=[{"k":2,"of":[W+"s3.6.2",W+"s3.5.b"]},{"k":2,"of":[W+"s3.2.0",W+"s3.1.b"]}]
    d['(ii)']=[{"k":2,"of":[W+"s3.6.b",W+"s3.5.b"]},{"k":1,"of":[W+"s3.1.b"]}]
R='geo-region-concept-'
def q5(d): d['']=[{"k":2,"of":[R+"s1.13.0",R+"s1.13.2"]},{"k":2,"of":[R+"s3.3.1",R+"s5.0.b"]},{"k":2,"of":[R+"s2.0.3",R+"s2.1.1"]},{"k":2,"of":[R+"s3.7.b",R+"s1.2.b"]}]
def q6(d): d['(iii)']=[{"k":1,"of":["geo-rivers-s1.6.5"]}]
def q7(d):
    d['(iii)']=[{"k":2,"of":["geo-mapwork-s1.0.4","geo-mapwork-s1.5.b"]}]
    d['(iv)']=[{"k":2,"of":["geo-mapwork-s1.6.b","geo-mapwork-s1.6.1"]}]
def q11(d): d['(iii)']=[{"k":1,"of":["geo-graph-skills-s1.0.4"]}]
def q12(d): d['(iv)']=[{"k":1,"of":["geo-graph-skills-s2.14.1"]}]
for q,f in [('q2',q2),('q4',q4),('q5',q5),('q6',q6),('q7',q7),('q11',q11),('q12',q12)]: edit(q,f)
