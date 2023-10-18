import utils
from read_csv import read_csv
import charts

data = [
  {
     'Country': 'Colombia',
    'Population': 500
  },
  {
    'Country': 'Bolivia',
    'Population': 300
  }
]

def run():
  result = utils.get_population()
  #Obtenemos dos listas con los resultados
  countries, population = utils.get_population()
  
  result_filter = utils.population_by_country(result, 'col')
  #print(result_filter)
  

  
  #country = input('Type Country => ')
  
  data = read_csv('./data.csv')
  
  data = list(filter(lambda x: x['Continent'] == 'South America', data))
  
  print(data)
  
  countries = list(map(lambda x: x['Country/Territory' ], data))
  percentages = list(map(lambda x: float(x['World Population Percentage' ]), data))
  print(countries)
  print(percentages)
  name = input('Ingrese nombre de reporte => ')
  charts.generate_pie_chart_img(name, countries, percentages)
  
  #result_list = utils.population_by_country_list(data, country)
  
  #print(result_list)
#ENTRY POINT
#Controla si se esta ejecutando el archivo directamente desde el terminal y siempre se usa al final del documento o del bloque que se quiere ejecutar
if __name__ == '__main__':
    run()
