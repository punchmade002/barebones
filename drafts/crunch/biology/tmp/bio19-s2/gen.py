import json,re
H,E='helpful','essential'
def n(i,s,w,c='high'):return {"id":i,"strength":s,"why":w,"confidence":c}
d={
"bio19-s2.0.b":(1,[]),
"bio19-s2.0.0":(1,[]),
"bio19-s2.0.1":(1,[n("bio19-s1.0.5",H,"nerve impulse")]),
"bio19-s2.0.2":(1,[]),
"bio19-s2.1.b":(1,[]),
"bio19-s2.1.0":(1,[n("bio19-s2.0.0",H,"stimulus")]),
"bio19-s2.1.1":(1,[n("bio19-s2.1.0",E,"reflex action definition")]),
"bio19-s2.1.2":(1,[n("bio19-s2.1.0",H,"reflex action definition")]),
"bio19-s2.1.3":(1,[n("bio19-s2.1.0",H,"reflex action definition")]),
"bio19-s2.1.4":(1,[n("bio19-s2.1.0",H,"reflex action definition")]),
"bio19-s2.2.b":(1,[]),
"bio19-s2.2.0":(2,[n("bio19-s1.1.0",E,"sensory neuron carries impulses in"),n("bio19-s1.1.1",E,"motor neuron carries impulses out"),n("bio19-s3.0.4",E,"interneuron connects neurons"),n("bio19-s1.4.1",H,"grey matter of cord","low")]),
"bio19-s2.2.1":(1,[n("bio19-s2.2.0",H,"sensory neuron in the arc")]),
"bio19-s2.2.2":(1,[n("bio19-s2.2.0",H,"motor neuron in the arc")]),
"bio19-s2.2.3":(2,[n("bio19-s2.2.0",E,"order of reflex arc parts"),n("bio19-s2.2.1",E,"dorsal root and ganglion"),n("bio19-s2.2.2",E,"ventral root"),n("bio19-s1.4.2",H,"white matter in cord section")]),
"bio19-s2.3.b":(1,[n("bio19-s2.2.0",H,"reflex arc pathway")]),
"bio19-s2.3.0":(1,[n("bio19-s2.0.1",H,"receptor detects stimulus")]),
"bio19-s2.3.1":(1,[n("bio19-s1.1.0",H,"sensory neuron")]),
"bio19-s2.3.2":(1,[n("bio19-s3.0.4",H,"interneuron")]),
"bio19-s2.3.3":(1,[n("bio19-s1.1.1",H,"motor neuron")]),
"bio19-s2.3.4":(1,[n("bio19-s2.0.2",E,"effector")]),
"bio19-s2.3.5":(1,[n("bio19-s2.0.2",H,"muscle effector contracts")]),
"bio19-s2.4.b":(1,[]),
"bio19-s2.4.0":(2,[n("bio19-s2.3.2",H,"synapse as gap between neurons")]),
"bio19-s2.4.1":(1,[n("bio19-s2.4.0",H,"short route")]),
"bio19-s2.4.2":(1,[n("bio19-s3.0.4",H,"interneuron","low")]),
"bio19-s2.4.3":(1,[n("bio19-s2.1.0",H,"reflex action definition")]),
"bio19-s2.5.b":(1,[n("bio19-s2.2.0",H,"reflex arc with interneuron")]),
"bio19-s2.5.0":(1,[n("bio19-s2.0.0",H,"stimulus")]),
"bio19-s2.5.1":(1,[n("bio19-s2.2.0",E,"sensory-interneuron-motor pathway")]),
"bio19-s2.5.2":(1,[]),
"bio19-s2.6.b":(1,[n("bio19-s2.1.0",H,"reflex action definition")]),
"bio19-s2.6.0":(1,[n("bio19-s2.2.0",H,"spinal cord reflex arc","low")]),
"bio19-s2.6.1":(1,[n("bio19-s1.8.2","helpful","medulla controls reflexes","low")]),
}
out={k:{"cost":c,"needs":nd} for k,(c,nd) in d.items()}
json.dump(out,open("point-links/bio19-s2.json","w"),indent=1)
pk=open("points/bio19-s2.txt").read()
ids=re.findall(r'^\[([^\]]+)\]',pk,re.M)
tg=[i for i in ids if i.startswith("bio19-s2.")]
assert list(out)==tg,(set(tg)^set(out))
allids=set(ids)
L=[x for v in out.values() for x in v["needs"]]
assert all(x["id"] in allids for x in L)
assert all(k!=x["id"] for k,v in out.items() for x in v["needs"])
print(len(out),len(L),sum(v["cost"]==2 for v in out.values()),sum(x["confidence"]=="low" for x in L))
