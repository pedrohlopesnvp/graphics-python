import matplotlib.pyplot as plt

rotulos = ['Maçãs', 'Laranjas', 'Banas', 'Uvas', 'Figos']
tamanhos = [25, 30, 20, 25, 27]
cores = ['red', 'orange', 'yellow', 'blue', 'purple']

fig, ax = plt.subplots()
ax.pie(tamanhos, labels=rotulos, colors=cores, autopct='%1.1f%%')
ax.set_title('Distribuição das Frutas')

plt.show()