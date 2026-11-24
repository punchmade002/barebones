import json
H,L='high','low'
def l(n,s,w,c=H): return {"needs":n,"strength":s,"why":w,"confidence":c}
E_,H_='essential','helpful'
d={
"geo-urban-s7":[l("geo-population-migration-s6",E_,"rural-to-urban migration drives rapid developing-world city growth"),
 l("geo-urban-s5",H_,"compares with developed-world urban problems like housing, traffic"),
 l("geo-urban-s6",H_,"planning and renewal ideas behind slum clearance and new towns",L),
 l("geo-economic-development-s2",H_,"developing-world context, informal economy and inequality",L),
 l("geo-region-continental-s1",H_,"India context for Kolkata and Mumbai case studies",L)],
"geo-urban-s8":[l("geo-urban-s5",E_,"builds on housing, transport, sprawl problems of cities"),
 l("geo-urban-s6",H_,"planning approaches such as compact city and renewal"),
 l("geo-urban-s7",H_,"developing-world futures issue uses developing-world city problems"),
 l("geo-population-migration-s1",H_,"ageing populations and urban population trends",L)],
"geo-option-atmosphere-ocean-s1":[l("geo-weather-climate-s1",H_,"weather data, instruments and observing networks",L)],
"geo-option-atmosphere-ocean-s2":[l("geo-option-atmosphere-ocean-s1",E_,"uses atmosphere layers, ocean temperature and heat capacity")],
"geo-option-atmosphere-ocean-s3":[l("geo-option-atmosphere-ocean-s1",E_,"uses atmospheric humidity, temperature and ocean-atmosphere linkage"),
 l("geo-option-atmosphere-ocean-s2",H_,"heat redistribution drives evaporation and cooling")],
"geo-option-atmosphere-ocean-s4":[l("geo-option-atmosphere-ocean-s2",E_,"uses heat budget, Hadley cell and ocean currents"),
 l("geo-option-atmosphere-ocean-s3",E_,"depressions use condensation, fronts, adiabatic cooling"),
 l("geo-option-atmosphere-ocean-s1",H_,"uses pressure, salinity and density basics"),
 l("geo-weather-climate-s1",H_,"depression weather sequence read from weather maps",L)],
"geo-option-atmosphere-ocean-s5":[l("geo-option-atmosphere-ocean-s2",E_,"climate types explained by latitude, heat and circulation"),
 l("geo-option-atmosphere-ocean-s4",E_,"monsoon and oceanic climates use winds, pressure belts, currents"),
 l("geo-option-atmosphere-ocean-s3",H_,"precipitation and humidity patterns of each climate")],
"geo-option-atmosphere-ocean-s6":[l("geo-option-atmosphere-ocean-s5",E_,"uses monsoon, oceanic and arid climate characteristics"),
 l("geo-economic-development-s2",H_,"climate effects on economic development and regions",L),
 l("geo-option-atmosphere-ocean-s3",H_,"rainfall, drought and water supply link to hydrological cycle",L)],
"geo-option-culture-identity-s1":[l("geo-population-migration-s5",H_,"ethnic and racial groups and migration flows",L),
 l("geo-population-migration-s3",H_,"migration patterns such as refugees and labour migration",L)],
"geo-option-culture-identity-s2":[l("geo-option-culture-identity-s5",H_,"language links to nationalism and the nation state",L)],
"geo-option-culture-identity-s3":[l("geo-option-culture-identity-s5",H_,"church-state relations and nationality",L)],
"geo-option-culture-identity-s4":[l("geo-option-culture-identity-s2",H_,"language and Irish-language culture in everyday expression",L),
 l("geo-economic-globalisation-s4",H_,"globalisation pressures on local culture",L)],
"geo-option-culture-identity-s5":[l("geo-option-culture-identity-s2",H_,"language divides cultural groups within states",L),
 l("geo-option-culture-identity-s3",H_,"religion divides cultural groups within states",L)],
"geo-option-culture-identity-s6":[l("geo-option-culture-identity-s2",E_,"Swiss languages use language as cultural indicator"),
 l("geo-option-culture-identity-s3",E_,"Swiss religious geography uses religion as cultural indicator"),
 l("geo-option-culture-identity-s5",E_,"boundaries, federalism and accommodating cultural groups"),
 l("geo-option-culture-identity-s4",H_,"Swiss music, sport and festivals as everyday expressions")],
"geo-option-geoecology-s1":[l("geo-rocks-weathering-s3",E_,"parent material forms by weathering of rock"),
 l("geo-rocks-weathering-s1",H_,"rock types supply soil parent material",L)],
"geo-option-geoecology-s2":[l("geo-option-geoecology-s1",E_,"uses soil profile, texture, humus, pH"),
 l("geo-rocks-weathering-s3",H_,"weathering as a soil-forming process"),
 l("geo-option-atmosphere-ocean-s5",H_,"zonal soils tied to climatic environments",L)],
"geo-option-geoecology-s3":[l("geo-option-geoecology-s1",E_,"uses soil structure, fertility and erosion effects"),
 l("geo-option-geoecology-s2",E_,"uses erosion, leaching, soil processes and soil types"),
 l("geo-option-atmosphere-ocean-s5",H_,"Sahel desertification relates to rainfall and climate",L)],
"geo-option-geoecology-s4":[l("geo-option-atmosphere-ocean-s5",E_,"biome climate and causes of aridity from climate and circulation"),
 l("geo-option-geoecology-s2",H_,"desert and rainforest soils such as latosol"),
 l("geo-rocks-weathering-s6",H_,"desert landscape shaped by wind erosion",L)],
"geo-option-geoecology-s5":[l("geo-option-geoecology-s4",E_,"altering biomes uses biome characteristics, e.g. rainforest"),
 l("geo-option-geoecology-s3",H_,"clearance leads to soil erosion and degradation",L)],
"geo-option-global-interdependence-s1":[l("geo-economic-development-s1",E_,"uses measures of development such as HDI"),
 l("geo-economic-development-s4",H_,"global justice perspective on development",L)],
"geo-option-global-interdependence-s2":[l("geo-economic-globalisation-s1",E_,"uses MNC structure and operation"),
 l("geo-economic-globalisation-s3",H_,"world trade patterns and producer-consumer regions"),
 l("geo-economic-globalisation-s2",H_,"MNC impact on regions",L),
 l("geo-economic-eu-s2",H_,"Irish trade and multinationals in Ireland",L)],
"geo-option-global-interdependence-s3":[l("geo-option-global-interdependence-s1",E_,"uses development theory, growth versus development, dependency"),
 l("geo-economic-development-s1",H_,"uses development indicators",L),
 l("geo-economic-development-s4",H_,"debt, aid and global justice issues",L)],
"geo-option-global-interdependence-s4":[l("geo-economic-environment-s4",E_,"uses sustainable economic development concepts"),
 l("geo-option-global-interdependence-s1",H_,"sustainable development as a development view"),
 l("geo-economic-environment-s1",H_,"Irish energy and renewable resource use",L),
 l("geo-option-global-interdependence-s2",H_,"fair trade relates to interdependent trade",L)],
}
b=open('batch-4.txt').read().split()
assert list(d)==b,(set(b)^set(d))
cat={x.split(' |')[0] for x in open('catalogue.txt') if not x.startswith(' ')}
for k,v in d.items():
    ns=[x['needs'] for x in v]
    assert len(set(ns))==len(ns) and k not in ns and all(n in cat for n in ns),k
json.dump(d,open('prereqs-4.json','w'),indent=1)
a=[x for v in d.values() for x in v]
print(len(d),len(a),sum(x['strength']==E_ for x in a),sum(x['confidence']==L for x in a))
