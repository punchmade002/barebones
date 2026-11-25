import json
P='hist-eur3-s13.'
counts={0:4,1:2,2:6,3:3,4:4,5:5,6:5,7:3,8:6,9:4,10:3,11:3,12:4,13:5,14:5,15:3,16:5,17:2}
out={}
for s,n in counts.items():
    for k in ['b']+list(range(n+1)):
        out[f'{P}{s}.{k}']={"needs":[]}
out[P+'5.0']['needs']=[{"id":"hist-eur3-s9.13.0","strength":"helpful","why":"uses the Rome-Berlin Axis alliance","confidence":"high"}]
json.dump(out,open('point-links/hist-eur3-s13.t1g3.json','w'),indent=1)
import re
txt=open('packs/hist-eur3-s13.t1g3.txt').read()
tg=txt.split('CANDIDATES')[0]
ids=re.findall(r'^\[([^\]]+)\]',tg,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
print(len(ids),ids==list(out),sum(len(v['needs']) for v in out.values()))
