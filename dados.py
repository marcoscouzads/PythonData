import matplotlib.pyplot as plt
x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]
z = [0, 1, 8, 37, 64, 125]

plt.plot(y,y, 'r--p', label ="curva 1") #desenha o gráfico
plt.plot(x,z, 'b')
plt.legend(loc="upper right")
plt.show()  # mostra o gráfico

