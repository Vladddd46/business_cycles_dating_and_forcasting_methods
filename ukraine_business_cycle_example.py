import json
from buildgraph import build_graph

# ukraine example
with open('statistics/ukraine_gdp_by_quoter.json') as f:
	gdp = json.load(f)
with open('statistics/ukraine_employment_rate_by_quoter.json') as f:
	employment_rate = json.load(f)
with open('statistics/ukraine_industrial_production_by_quoter.json') as f:
	industrial_production = json.load(f)

data = {}
for i in gdp.keys():
	data[i] = gdp[i] + employment_rate[i] + industrial_production[i]

build_graph(data, title='Ukraine, 2010-2020', xlable_name='Quarter')
