from matplotlib import pyplot as plt

def generate_pie_chart():
    labels = ['A','B','C']
    values = [1,2,3]
    
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('pie.png')
    #ax.axis('equal')
    #plt.show()
    plt.close()