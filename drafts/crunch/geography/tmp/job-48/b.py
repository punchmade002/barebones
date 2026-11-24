import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
pk=open(P+'packs/geo-option-atmosphere-ocean-s6.t1g7.txt').read()
tgt=pk.split('CANDIDATES')[0]
ids=re.findall(r'^\[(geo-option-atmosphere-ocean-s6\.[^\]]+)\]',tgt,re.M)
cand=set(re.findall(r'^\[(geo-option-geoecology-s3\.[^\]]+)\]',pk,re.M))
S='geo-option-geoecology-s3.'
def L(i,s,w,c='high'):return {"id":S+i,"strength":s,"why":w,"confidence":c}
# every target id reviewed by hand; ids not in this dict were explicitly judged as having no link
links={
'5.3':[L('14.3','helpful','salinisation and waterlogging from irrigation')],
'6.3':[L('14.3','helpful','salinisation and waterlogging from irrigation','low')],
'8.0':[L('7.1','helpful','Sahel short wet season rainfall')],
'8.2':[L('7.2','helpful','unreliable Sahel rainfall')],
'18.b':[L('5.0','helpful','desertification as land degradation')],
'18.0':[L('5.0','helpful','desertification definition')],
'18.1':[L('5.1','helpful','not advance of sand dunes')],
'18.2':[L('5.0','helpful','desertification as degradation process')],
'19.b':[L('5.0','helpful','desertification meaning')],
'19.0':[L('7.0','helpful','Sahel location'),],
'19.1':[L('8.3','helpful','1970s-80s droughts stripped soil')],
'19.4':[L('9.1','helpful','Lake Chad shrinkage')],
'20.0':[L('10.0','helpful','UNCCD')],
'20.1':[L('10.1','helpful','Great Green Wall')],
'20.2':[L('11.1','helpful','zai pits and stone lines')],
'20.3':[L('12.0','helpful','farmer-managed natural regeneration')],
'21.b':[L('2.b','helpful','Dust Bowl drought and ploughing')],
'21.0':[L('2.1','helpful','ploughing grassland for wheat')],
'21.1':[L('2.2','helpful','drought stripping topsoil')],
'21.2':[L('2.4','helpful','Soil Conservation Service responses')],
'21.3':[L('2.2','helpful','Dust Bowl soil side')],
}
out={}
for i in ids:
    k=i.split('s6.')[1]
    out[i]={"needs":links.get(k,[])}
for v in out.values():
    for n in v['needs']: assert n['id'] in cand,n
json.dump(out,open(P+'point-links/geo-option-atmosphere-ocean-s6.t1g7.json','w'),indent=1)
print(len(ids),len(set(ids)),sum(len(v['needs']) for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
