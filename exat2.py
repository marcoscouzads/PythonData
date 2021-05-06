import matplotlib.pyplot as plt

def juros_compostos(valor_inicial, taxa, aporte, periodo):
    juros = []
    
    for i in range (periodo):
        valor_inicial = (valor_inicial + (valor_inicial * (taxa / 100))) + aporte
        print(f"\t Após{i+1}º período(s), o montante será de R$ {valor_inicial:,.2f}")
        juros.append(valor_inicial)
        
    plt.plot(juros)
    plt.title("Rendimento estipulado")
    plt.xlabel("mêses")
    plt.ylabel("valores acumulados")
    plt.show()
    
valor_inicial = float(input("Digite valor inicial: R$ "))
taxa = float(input("Rendimento por período (%): "))
aporte  = float(input("Aporte a cada período: R$ "))
periodo = int(input("Total de períodos:  "))
juros_compostos(valor_inicial, taxa, aporte, periodo)