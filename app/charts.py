import matplotlib.pyplot as plt

def generate_bar_chart(labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.show()

def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.show()
  
def generate_pie_chart_img(name, labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig(f'./imgs/{name}.png')
    plt.close()

if __name__ == '__main__':
  labels = ['a','b','c','d','e']
  values = [1,1,3,5,4]
  #generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)

  
  