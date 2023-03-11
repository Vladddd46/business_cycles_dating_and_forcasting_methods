import json
from forcasting_methods_for_business_cycles import moving_average
from buildgraph import build_2graphs

"""
Example of forcasting ukrainian gdp using moving_average forcast method.
"""

with open('statistics/usa_gdp_by_quoter.json') as f:
    data = json.load(f)

# based on how much previous values forcast would be.
n = 4

forcast = moving_average(list(data.values()), list(data.keys()), n)


print("Прогнозований ВВП", "\tРеальний ВВП", "\tРізниця", "\tРізниця%")

sum_diff_in_percent = 0;
max_diff_in_percent = None
min_diff_in_percent = None
for i in forcast:
    tmp_avg_mistage_in_percent = round(round(forcast[i]-data[i],2)*100/data[i])
    print(i+"|", forcast[i],"\t\t ", data[i], "      ", round(forcast[i]-data[i],2), "\t\t", str(tmp_avg_mistage_in_percent)+"%")
    
    if (tmp_avg_mistage_in_percent < 0):
        tmp_avg_mistage_in_percent *= -1
    # init with first value
    if (max_diff_in_percent == None and min_diff_in_percent==None):
        max_diff_in_percent = tmp_avg_mistage_in_percent
        min_diff_in_percent = tmp_avg_mistage_in_percent
    if (tmp_avg_mistage_in_percent > max_diff_in_percent):
        max_diff_in_percent = tmp_avg_mistage_in_percent
    if (tmp_avg_mistage_in_percent < min_diff_in_percent):
        min_diff_in_percent = tmp_avg_mistage_in_percent
    sum_diff_in_percent += tmp_avg_mistage_in_percent

print("Середнє значення Різниці% = ", round(sum_diff_in_percent/len(forcast)), "%")
print("Максимальне значення Різниці%", max_diff_in_percent, "%")
print("Мінімальне значення Різниці%", min_diff_in_percent, "%")

build_2graphs(data, forcast, title='USA moving avarage GDP forcast, 2010-2020', xlable_name='Quarter')