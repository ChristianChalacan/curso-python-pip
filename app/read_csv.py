import csv

def read_csv(path):
  with open(path, 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      #Se transforma las tuplas en diccionarios
      country_dict = dict(iterable)
      #Se puede crear de forma manual cada uno de los diccionarios
      country_dict_v2 = { key:value for key, value in iterable}
      data.append(country_dict)
  return data

if __name__ == '__main__':
  print(read_csv('./data.csv'))