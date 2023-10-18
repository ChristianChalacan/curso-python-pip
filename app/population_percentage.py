from read_csv import read_csv
from charts import generate_bar_chart, generate_pie_chart

def get_countries(data):
  countries = []
  for country_dict in data:
    countries.append(country_dict['Country/Territory'])
  return countries
  
def get_percentage(data):
  percentages = []
  for percentage_dict in data:
    percentages.append(float(percentage_dict['World Population Percentage']))
  return percentages

  
data = read_csv('./data.csv')
countries = get_countries(data)
percentages = get_percentage(data)

#Metodo rapido para obtener los datos
countries_v2 = list(map(lambda x: x['Country/Territory' ], data))
percentages_v2 = list(map(lambda x: float(x['World Population Percentage' ]), data))

print(countries_v2)
print(percentages_v2)

generate_pie_chart(countries, percentages)
generate_pie_chart(countries_v2, percentages_v2)