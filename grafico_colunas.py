import matplotlib.pyplot as plt

categorias = ['A', 'B', 'C', 'D', 'E']
valores = [10, 23, 17, 12, 15]

plt.bar(categorias, valores)
plt.xlabel('Categorias')
plt.ylabel('Valores')
plt.title('Gráfico de Colunas')
plt.show()