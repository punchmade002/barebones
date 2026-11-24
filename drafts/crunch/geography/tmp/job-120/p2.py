from p23 import *
E={}
for i in "21.2 22.0 22.1 23.b 24.b 24.4 25.b 25.0 25.1 25.2 25.3 25.4 26.b 26.0 26.1 26.2 26.3 26.4 26.5 26.6 26.7 27.b 27.0 27.1 27.2 28.b 28.0 28.1 28.2 28.3 28.4 29.b 29.0 29.1 29.2 29.3 29.4 29.5 30.b 30.0 30.1 30.2 30.3 30.4 31.b 31.0 31.1 32.b 32.0 32.1 32.2 32.3 32.4 33.b 33.0 33.1 33.2 33.4 33.5 33.6 34.b 34.0 34.1 34.2 34.3 34.4 34.5 35.b 35.0 35.1 35.2 35.3 35.4 35.5 35.6 35.7 36.b 36.0 36.1 36.2 36.3 36.4 36.5 37.b 37.0 37.1 37.2 37.3 38.0 38.1 38.5 39.b 39.0 39.1 39.2 39.3 40.b 40.0 40.1 40.2 40.3 41.b 41.1 41.2 41.3 41.4 41.5 41.6 41.7 42.b 42.0 42.1 42.2 42.3 42.4 42.5".split(): E[i]=[]
E.update({
"21.1":[L("e2:2.3",H,"high-tech firms seek graduates")],
"21.2":[L("e2:2.2",H,"labour skills supply")],
"22.b":[L("e2:3.0",H,"markets as location factor")],
"22.2":[L("e2:3.1",H,"ports for exports")],
"22.0":[L("e2:3.0",H,"market size","low")],
"23.b":[L("e2:1.7",H,"infrastructure defined")],
"23.0":[L("e2:3.7",H,"motorways, broadband link firms")],
"23.1":[L("e2:4.6",H,"EU funds support regions")],
"23.2":[L("e2:0.0",H,"bulk-reducing food processing near source")],
"23.3":[L("e2:2.0",H,"raw materials as location factor")],
"24.0":[L("e2:0.b",H,"transport costs decide location")],
"24.1":[L("e2:2.2",H,"labour supply")],
"24.2":[L("e2:17.1",H,"branch plant vulnerability"),L("e2:21.3",H,"DEC closure 1993")],
"24.3":[L("e2:4.4",H,"regional policy steers investment","low")],
"24.4":[L("e2:1.7",H,"infrastructure")],
"33.3":[L("e2:13.b",H,"Galway medtech cluster")],
"38.2":[L("e2:27.1",H,"National Broadband Plan")],
"38.3":[L("e2:27.3",H,"Our Rural Future")],
"38.4":[L("e2:27.0",H,"remote working")],
"38.6":[L("e2:4.3",H,"Udaras na Gaeltachta")],
"41.0":[L("e2:4.3",H,"Udaras na Gaeltachta")],
})
for i in ("38.b","38.2","38.3","38.4","38.6"): E.setdefault(i,[])
run('geo-region-ireland-s2.t2g2',E)
