import json
P='geo-option-global-interdependence-'
O='/Users/gabrielwhelan/barebones/drafts/crunch/geography/exam-tags/out/geography-pp-2017-higher-%s.json'
d=json.load(open(O%'q113'))
L=d['13']
def setof(old,new):
    for m in L:
        if m['of']==[P+old]: m['of']=[P+n for n in new]; return
    raise Exception(old)
setof('s3.2.b',['s3.2.2','s3.2.3'])
setof('s3.4.b',['s3.4.1','s3.4.b'])
setof('s3.23.3',['s3.23.2','s3.23.3'])
setof('s3.24.0',['s3.24.0','s3.24.1'])
setof('s3.26.2',['s3.26.1','s3.26.2'])
json.dump(d,open(O%'q113','w'))
json.dump({"14":[{"k":1,"of":[P+"s4.9.4"]}]},open(O%'q114','w'))
d=json.load(open(O%'q115'))
for m in d['15']:
    if m['of']==[P+'s4.16.0']: m['of']=[P+'s4.16.0',P+'s4.16.1']
    if m['of']==[P+'s4.22.3']: m['of']=[P+'s4.22.3',P+'s4.20.4']
    if m['of']==[P+'s4.24.2']: m['of']=[P+'s4.24.1',P+'s4.24.2']
json.dump(d,open(O%'q115','w'))
