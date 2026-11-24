import re
src=open('b.py').read()
ns={}
exec(src.split('def build')[0],ns)
L1,L2=ns['L1'],ns['L2']
P=ns['P']
txt=open(P+'packs/geo-option-atmosphere-ocean-s3.t1g1.txt').read().split('CANDIDATES')[0]
ids=[i[len(ns['S3']):] for i in re.findall(r'^\[(\S+?)\]',txt,re.M)]
c2={'1.0','2.5','3.1','6.3','8.0','9.0','12.0','12.2','13.0','13.3','14.2','14.3','16.1','20.1','21.0','21.2','22.0','24.0','26.4','28.2','28.5','31.0','31.2','31.3','31.6','34.1','35.0'}
out=["ROWS = {"]
for i in ids: out.append(f"  {i!r}: ({2 if i in c2 else 1}, {L1[i]!r} if False else None),") if False else None
# explicit rows: cost, links1, links2
out=["import json,re","P='%s'"%P,"S3='geo-option-atmosphere-ocean-s3.'","ROWS = {"]
for i in ids:
    out.append(f"  {i!r}: ({2 if i in c2 else 1}, {L1.get(i,[])!r}, {L2.get(i,[])!r}),")
out.append("}")
out.append('''
for pack,out,idx,mode in (('geo-option-atmosphere-ocean-s3.t1g1.txt','geo-option-atmosphere-ocean-s3.t1g1.json',1,'c'),('geo-option-atmosphere-ocean-s3.t1g2.txt','geo-option-atmosphere-ocean-s3.t1g2.json',2,'l')):
    txt=open(P+'packs/'+pack).read()
    ids=re.findall(r'^\\[(\\S+?)\\]',txt.split('CANDIDATES')[0],re.M)
    allids=set(re.findall(r'^\\[(\\S+?)\\]',txt,re.M))
    assert [S3+k for k in ROWS]==ids
    res={};nl=nc=nlow=0
    for k,row in ROWS.items():
        needs=[]
        for t,st,w,c in row[idx]:
            tid=S3+t if re.match(r'^\\d',t) else 'geo-option-atmosphere-ocean-'+t
            assert tid in allids and tid!=S3+k
            needs.append({'id':tid,'strength':st,'why':w,'confidence':c}); nlow+=c=='low'
        e={'needs':needs}
        if mode=='c': e={'cost':row[0],**e}; nc+=row[0]==2
        res[S3+k]=e; nl+=len(needs)
    json.dump(res,open(P+'point-links/'+out,'w'),indent=0)
    assert list(json.load(open(P+'point-links/'+out)))==ids
    print(out,len(ids),nl,nc,nlow)
''')
open('final.py','w').write("\n".join(out))
