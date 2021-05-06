import matplotlib.pyplot as plt

def calcular_depreciacao(modelo, valor, vida_util):
    depreciacao_mensal = valor / vida_util / 12
    print(f"depreciação do {modelo} ao longo de um ano")
    print(f"valor inicial: R$ {valor:.2f}.")
   
    periodos = []
    valores_mensais = []

    for i in range (12):
        valor = valor - depreciacao_mensal
        print(f"\t {i+1}º mês: R$ {valor:.2f}")
        periodos.append(i+1)
        valores_mensais.append(valor)


    plt.plot(valores_mensais)
    plt.show()

modelo = input("Modelo do carro: ")
valor = float(input("Informe o valor do carro 0km: R$"))
vida_util = int(input("Informe a vida útil do carro: "))

calcular_depreciacao(modelo, valor, vida_util)

