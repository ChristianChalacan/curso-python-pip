from read_csv import read_csv
#from charts import generate_bar_chart, generate_pie_chart
import charts

def filter_country_dict(data, country):
  for country_dict in data:
    if country_dict['Country/Territory'] == country:
        return country_dict

def get_population(data):
  population = []
  years = ['2022 Population', '2020 Population', '2015 Population', '2010 Population', '2000 Population', '1990 Population','1980 Population','1970 Population']
  for year in years:
    population.append(int(data[year]))
  return population

data = read_csv('./data.csv')
years = ['2022','2020','2015','2010','2000','1990','1980','1970']
country = input('Ingrese el pais => ')
data_country = filter_country_dict(data, country)
population = get_population(data_country)
charts.generate_bar_chart(years, population)