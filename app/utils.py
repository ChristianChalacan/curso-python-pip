def get_population():
  keys = ['col', 'bol','ecu','ven']
  values = [300,400,500,100]
  return keys, values
#*****************************************
#Ejemplo con tuplas - personalizado
def population_by_country(data, country):
  data = trans_to_dict(data)
  return data.get(country)

#Transforma una tupla a un diccionario
def trans_to_dict(data):
  new_dict = {}
  print('tamaño data => ',len(data[0]))
  for i in range(len(data[0])):
    new_dict[data[0][i]] = data[1][i]
  return new_dict
#*****************************************
#Ejemplo con una lista como esta en el curso
def population_by_country_list(data, country):
  return list(filter(lambda x: x['Country/Territory'] == country, data))