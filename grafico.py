import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y, marker='o', linestyle='-', color='y')
plt.xlabel('Valores de x')
plt.ylabel('Valores de Y')
plt.title('Gráfico de Linha')
plt.grid(True)
plt.show()