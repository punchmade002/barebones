import json,re,sys
P='hom-marriage-s2.'
def L(i,s,w,c='high'):return {"id":i,"strength":s,"why":w,"confidence":c}
d={
"0.b":(1,[]),
"0.0":(1,[]),
"0.1":(1,[L("hom-marriage-s1.0.0","helpful","consent to marriage","low")]),
"0.2":(1,[L(P+"0.1","essential","arranged marriage meaning")]),
"0.3":(1,[]),
"0.4":(1,[L("hom-marriage-s1.0.1","helpful","one spouse at a time")]),
"0.5":(1,[L("hom-marriage-s1.0.1","helpful","bigamy and one marriage at a time")]),
"0.6":(1,[L(P+"0.5","essential","polygamy meaning")]),
"0.7":(1,[L("hom-marriage-s1.1.2","helpful","Marriage Act 2015 effect","low")]),
"1.b":(1,[]),
"1.0":(1,[L("hom-marriage-s1.1.5","helpful","civil and religious ceremonies")]),
"1.1":(1,[]),
"1.2":(1,[]),
"2.b":(1,[]),
"2.0":(1,[L("hom-sociological-concepts-s1.2.3","helpful","customs as traditional practices","low")]),
"2.1":(1,[]),
"2.2":(1,[]),
"2.3":(1,[]),
"2.4":(1,[L("hom-marriage-s2.1.0","helpful","church, registry office venues","low")]),
"3.b":(1,[]),
"3.0":(1,[]),
"3.1":(1,[L("hom-marriage-s1.0.3","helpful","legal rights and duties of spouses")]),
"3.2":(1,[]),
"3.3":(1,[]),
"4.b":(1,[]),
"4.0":(1,[]),
"4.1":(1,[L("hom-marriage-s1.3.2","helpful","unconsummated marriage annulment")]),
"4.2":(1,[L(P+"0.4","helpful","monogamous marriage")]),
"4.3":(2,[]),
"4.4":(1,[L(P+"4.3","helpful","intestate inheritance rules")]),
"4.5":(2,[L(P+"4.3","helpful","spouse inheritance of estate","low")]),
"5.b":(1,[]),
"5.0":(1,[L("hom-marriage-s1.0.3","helpful","duty of financial support")]),
"5.1":(2,[]),
"5.2":(2,[]),
"5.3":(1,[L(P+"3.2","helpful","maintaining commitment","low")]),
"5.4":(1,[]),
"5.5":(1,[]),
}
out={P+k:{"cost":c,"needs":n} for k,(c,n) in d.items()}
op='point-links/hom-marriage-s2.t1g1.json'
json.dump(out,open(op,'w'),indent=1)
txt=open('packs/hom-marriage-s2.t1g1.txt').read()
ids=set(re.findall(r'^\[([^\]]+)\]',txt,re.M))
tg=re.findall(r'^\[([^\]]+)\]',txt.split('CANDIDATES')[0],re.M)
assert sorted(tg)==sorted(out) and len(tg)==len(out)
assert all(n['id'] in ids and n['id']!=k for k,v in out.items() for n in v['needs'])
print(len(out),sum(len(v['needs']) for v in out.values()),sum(v['cost']==2 for v in out.values()),sum(n['confidence']=='low' for v in out.values() for n in v['needs']))
