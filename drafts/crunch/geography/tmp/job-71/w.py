import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
# bullet counts per block (explicit), every item judged: no Brazil item is used by these generic/Global Interdependence items
n=[4,4,6,5,7,5,3,6,1,6,5,4,5,6,4,5,6,5,7,4,7,3,0]
ids=[]
for i,c in enumerate(n):
    ids.append(f'geo-option-global-interdependence-s3.{i}.b')
    ids+= [f'geo-option-global-interdependence-s3.{i}.{j}' for j in range(c)]
for k in ['4','5','6']:
    name=f'geo-option-global-interdependence-s3.t1g{k}'
    txt=open(P+f'packs/{name}.txt').read()
    tg=re.findall(r'^\[(geo-option-global-interdependence-s3\.[^\]]+)\]',txt,re.M)
    assert tg==ids,(len(tg),len(ids))
    json.dump({i:{'needs':[]} for i in ids},open(P+f'point-links/{name}.json','w'),ensure_ascii=False)
    d=json.load(open(P+f'point-links/{name}.json')); print(name,len(d),0,0)
