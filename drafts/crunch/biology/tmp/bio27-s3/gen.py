import json,re
P='/Users/gabrielwhelan/barebones/drafts/crunch/biology/'
txt=open(P+'points/bio27-s3.txt').read()
tgt_txt=txt.split('CANDIDATES')[0]
targets=re.findall(r'^\[([^\]]+)\]',tgt_txt,re.M)
allids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
S='bio27-s3.'
E,H='essential','helpful'
# id: (cost, [(need, strength, why, conf)])
d={
'0.b':(1,[]),
'0.0':(2,[('bio27-s1.0.2',H,'digestion as breakdown','high'),('bio8-s2.2.2',H,'hydrolysis splits bonds with water','low')]),
'0.1':(1,[('bio27-s1.0.3',H,'small soluble products absorbed','high')]),
'0.2':(1,[('bio13-s2.1.0',E,'enzyme specificity','high')]),
'0.3':(1,[(S+'0.2',E,'optimum pH of enzymes','high')]),
'0.4':(1,[]),
'1.b':(1,[]),
'1.0':(1,[('bio27-s1.4.0',H,'salivary glands','low')]),
'1.1':(1,[(S+'0.2',E,'optimum pH','high')]),
'1.2':(1,[('bio8-s2.3.1',H,'starch','high')]),
'1.3':(1,[('bio13-s2.2.2',E,'denaturing changes enzyme shape','high')]),
'1.4':(1,[]),'1.5':(1,[]),'2.b':(1,[]),
'2.0':(1,[('bio27-s1.2.4',H,'gastric juice and chyme','low')]),
'2.1':(1,[(S+'0.2',E,'optimum pH','high')]),
'2.2':(1,[(S+'2.1',H,'acid pH for pepsin','low')]),
'2.3':(2,[(S+'2.0',E,'pepsinogen and pepsin','high'),(S+'1.3',H,'amylase destroyed by acid','low')]),
'2.4':(2,[('bio8-s2.7.4',E,'peptide bonds','high'),(S+'0.0',H,'hydrolysis','high')]),
'2.5':(1,[(S+'2.4',E,'protease and polypeptides','high')]),
'2.6':(2,[(S+'2.0',E,'inactive pepsinogen','high')]),
'2.7':(1,[('bio27-s1.1.2',H,'mucus protects gut lining','high')]),
'3.b':(1,[]),
'3.0':(2,[('bio27-s1.4.3',H,'gallbladder stores bile','high'),('bio27-s1.3.0',H,'duodenum','high')]),
'3.1':(1,[]),
'3.2':(1,[('bio27-s2.6.4',H,'emulsification increases surface area','high')]),
'3.3':(2,[(S+'0.3',H,'pH along gut','high'),(S+'2.4',H,'pepsin','low')]),
'3.4':(1,[]),
'4.b':(1,[]),
'4.0':(2,[('bio27-s1.4.4',H,'pancreas and pancreatic duct','high')]),
'4.1':(1,[(S+'1.2',H,'amylase digests starch to maltose','high')]),
'4.2':(1,[(S+'2.4',E,'protease digests protein','high')]),
'4.3':(1,[('bio8-s2.4.2',E,'triglyceride structure','high')]),
'4.4':(1,[(S+'3.2',E,'emulsification makes droplets','high')]),
'4.5':(1,[(S+'3.3',E,'bicarbonate raises pH','high')]),
'5.b':(1,[]),
'5.0':(1,[('bio27-s1.3.1',H,'villi','high')]),
'5.1':(1,[(S+'5.0',H,'lining cells of villi','low')]),
'5.2':(2,[('bio8-s2.2.3',H,'maltose','high'),('bio8-s2.2.4',H,'sucrose','high'),('bio8-s2.2.5',H,'lactose','high')]),
'5.3':(1,[(S+'4.2',H,'peptides from trypsin','low')]),
'5.4':(1,[(S+'4.5',H,'duodenal pH','high')]),
'5.5':(2,[(S+'5.2',E,'lactase digests lactose','high')]),
'6.b':(1,[]),
'6.0':(1,[(S+'1.2',E,'salivary amylase action','high')]),
'6.1':(1,[(S+'2.4',E,'pepsin action','high')]),
'6.2':(1,[(S+'4.1',E,'pancreatic amylase action','high')]),
'6.3':(1,[(S+'4.2',E,'trypsin action','high')]),
'6.4':(1,[(S+'4.3',E,'lipase action','high')]),
'6.5':(1,[(S+'5.2',E,'maltase action','high')]),
'6.6':(1,[(S+'5.3',E,'peptidase action','high')]),
'6.7':(1,[(S+'3.2',E,'bile salts emulsify','high')]),
'7.b':(1,[]),
'7.0':(2,[(S+'6.0',H,'salivary amylase row','high'),(S+'6.2',H,'pancreatic amylase row','high'),(S+'6.5',H,'maltase row','high')]),
'7.1':(1,[(S+'5.2',H,'sucrase and lactase','high'),('bio8-s2.3.5',H,'cellulose not digested','low')]),
'7.2':(2,[(S+'6.1',H,'pepsin row','high'),(S+'6.3',H,'trypsin row','high'),(S+'6.6',H,'peptidase row','high')]),
'7.3':(2,[(S+'3.2',H,'bile salts emulsify','high'),(S+'6.4',H,'lipase row','high')]),
'7.4':(1,[(S+'7.3',H,'fat model','high')]),
'7.5':(1,[(S+'7.3',E,'fat model','high')]),
'7.6':(1,[(S+'4.0',E,'pancreatic juice enzymes','high')]),
'7.7':(2,[(S+'7.0',H,'carbohydrate model','high'),(S+'7.2',H,'protein model','high'),(S+'7.3',H,'fat model','high')]),
'8.b':(1,[('bio25-s1.0.4',H,'semi-permeable Visking tubing','low')]),
'8.0':(2,[('bio25-s1.0.4',E,'semi-permeable membrane','high')]),
'8.1':(1,[(S+'8.0',H,'Visking tubing','high')]),
'8.2':(1,[(S+'1.2',H,'amylase digests starch','high')]),
'8.3':(1,[(S+'8.2',H,'tubes set up','high')]),
'8.4':(2,[(S+'8.3',H,'samples from water outside','high')]),
'8.5':(1,[(S+'8.4',E,'iodine test for starch','high')]),
'8.6':(2,[(S+'8.4',E,'Benedict test for sugar','high')]),
'8.7':(2,[(S+'8.6',E,'results show sugar passes','high'),(S+'8.0',H,'membrane passes small molecules','high')]),
'8.8':(1,[]),
'9.b':(1,[(S+'8.0',H,'tubing as model gut','high')]),
'9.0':(1,[('bio27-s1.3.1',H,'villi surface area','high')]),
'9.1':(1,[('bio25-s1.1.0',E,'concentration gradient','high')]),
'9.2':(1,[('bio25-s1.4.0',E,'active transport','high')]),
'9.3':(1,[(S+'7.0',H,'gut enzyme sequence','low')]),
'9.4':(1,[('bio27-s2.4.0',H,'peristalsis','high')]),
'9.5':(1,[(S+'8.2',E,'method setup','high')]),
}
out={}
for t in targets:
    c,n=d[t.replace(S,'')]
    out[t]={'cost':c,'needs':[{'id':i,'strength':s,'why':w,'confidence':f} for i,s,w,f in n]}
assert set(out)==set(targets) and len(out)==len(targets)
for t,v in out.items():
    for n in v['needs']: assert n['id'] in allids and n['id']!=t,(t,n)
json.dump(out,open(P+'point-links/bio27-s3.json','w'),indent=0)
json.load(open(P+'point-links/bio27-s3.json'))
L=[n for v in out.values() for n in v['needs']]
print(len(out),len(L),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for n in L))
