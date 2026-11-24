import sys;sys.path.insert(0,'/Users/gabrielwhelan/barebones/drafts/crunch/geography/tmp/job-41')
from chk import build
G='/Users/gabrielwhelan/barebones/drafts/crunch/geography/'
ids="20.2 20.3 20.4 20.5 21.b 21.0 21.1 21.2 21.3 21.4 21.5 22.b 22.0 22.1 22.2 22.3 22.4 23.b 23.0 23.1 23.2 23.3 24.b 24.0 24.1 24.2 24.3 24.4 24.5 25.b 25.0 25.1 25.2 25.3 25.4 25.5 25.6 26.b 26.0 26.1 26.2 26.3 27.b 27.0 27.1 27.2 27.3 28.b 28.0 28.1 28.2 28.3 28.4 28.5 29.b 29.0 29.1 30.b 30.0 30.1 30.2 30.3 30.4 30.5 31.b 31.0 31.1 31.2 31.3 31.4 31.5 32.b 32.0 32.1 32.2 33.b 33.0 33.1 34.b 34.0 34.1 34.2 34.3 35.b 35.0 35.1 35.2 35.3 35.4 36.b 36.0 36.1 36.2 36.3 37.b 37.0 37.1 37.2 37.3 37.4 38.b 38.0 38.1 38.2 38.3 39.b 39.0 39.1 39.2 39.3 40.b 40.0 40.1 40.2 40.3 41.b 41.0 41.1 41.2 41.3 41.4".split()
L={
'20.5':[('geo-weather-climate-s1.9.3','h','Red warning meaning','h')],
'21.0':[('geo-weather-climate-s1.2.0','h','isobars','h')],
'21.3':[('geo-weather-climate-s1.3.5','h','ridge of high pressure','h')],
'24.5':[('geo-weather-climate-s1.9.3','h','warning colours','h')],
'25.1':[('geo-weather-climate-s1.2.0','h','isobars','h')],
'25.2':[('geo-weather-climate-s1.5.1','h','isobar spacing and wind strength','h')],
'36.1':[('geo-weather-climate-s1.6.1','h','cold front','h')],
}
S=[(i,0,L.get(i,[])) for i in ids]
assert all(k in ids for k in L)
build(G+'packs/geo-option-atmosphere-ocean-s4.t2g3.txt',G+'point-links/geo-option-atmosphere-ocean-s4.t2g3.json',S,False)
