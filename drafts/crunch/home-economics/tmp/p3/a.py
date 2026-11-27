import json
P='hom-marriage-s3.'
def n(i,s,w,c='high'): return {"id":i,"strength":s,"why":w,"confidence":c}
E,H='essential','helpful'
d={
"0.b":(1,[]),
"0.0":(1,[]),
"0.1":(1,[]),
"0.2":(1,[n(P+"0.0",H,"pre-marriage course")]),
"0.3":(1,[n(P+"0.0",H,"pre-marriage preparation")]),
"1.b":(1,[n(P+"0.0",H,"pre-marriage courses")]),
"1.0":(2,[n("hom-marriage-s1.2.b",H,"legal requirements of marriage","low")]),
"1.1":(1,[n(P+"1.0",H,"financial and housing topics")]),
"1.2":(1,[n(P+"1.0",H,"roles topic in courses")]),
"1.3":(1,[]),
"1.4":(1,[]),
"2.b":(1,[n(P+"1.b",H,"course topics")]),
"2.0":(1,[n(P+"0.1",H,"expectations and realities of marriage")]),
"2.1":(1,[n(P+"1.0",H,"communication topic")]),
"2.2":(1,[n(P+"1.2",H,"roles and expectations")]),
"2.3":(1,[n(P+"1.1",H,"money and housing advice")]),
"2.4":(2,[n(P+"1.0",H,"conflict resolution topic")]),
"2.5":(1,[]),
"3.b":(1,[n(P+"0.b",H,"pre-marriage courses")]),
"3.0":(1,[n("hom-marriage-s1.2.4",E,"notice of intention to marry")]),
"3.1":(1,[n("hom-marriage-s1.2.7",H,"approved venue"),n(P+"3.0",H,"registrar role")]),
"3.2":(1,[n(P+"0.3",H,"religious preparation")]),
"3.3":(1,[n("hom-marriage-s2.5.b",H,"roles and responsibilities of partners","low")]),
"3.4":(2,[]),
}
out={P+k:{"cost":c,"needs":nn} for k,(c,nn) in d.items()}
json.dump(out,open('point-links/hom-marriage-s3.t1g1.json','w'),indent=1)
