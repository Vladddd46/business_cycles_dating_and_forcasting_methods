import json
from buildgraph import build_graph

with open('statistics/poland_gdp_by_quoter.json') as f:
    gdp = json.load(f)
with open('statistics/poland_employment_rate_by_quoter.json') as f:
    employment_rate = json.load(f)
with open('statistics/poland_industrial_production_by_quoter.json') as f:
    industrial_production = json.load(f)
data = {}
for i in gdp.keys():
	data[i] = gdp[i] + employment_rate[i] + industrial_production[i]
build_graph(data, title='Poland, 2010-2020', xlable_name='Quarter')
