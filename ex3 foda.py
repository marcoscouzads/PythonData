import matplotlib.pyplot as plt
def extrair_dados(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
    #saindo do with o arquivo será fechado
    conteudo = conteudo.splitlines()
    rotulos = conteudo[0]
    rotulos = rotulos.split(',')
    conteudo = conteudo[1:]
   # print(conteudo)
    
    dados = []  #tudo isso é para extrair os dados
    
    for elemento in conteudo:
        elemento = elemento.split(',')
        dados.append(elemento)
       # print(dados)
    return rotulos, dados

def calcular_pontos(temporada):
    rotulos, dados = extrair_dados('dados_kobe.csv')
    indice_pontos = rotulos.index('PONTOS')
    indice_partida = rotulos.index('PARTIDAS')
    indice_temporada = rotulos.index('TEMPORADA')
    
    for elemento in dados:
        if int(elemento[indice_temporada]) == temporada:
            media_pontos = float(elemento[indice_pontos])
            num_partidas = int(elemento[indice_partida])
            total_pontos = media_pontos * num_partidas
            return int(total_pontos)       
    
temporada = int(input("Informe uma temporada, entre 1997 e 2016: "))
print(f"na temporada {temporada}, kobe bryant marcou {calcular_pontos(temporada)} pontos.")


def exibir_grafico(x, y):
    plt.plot(x, y)
    plt.show()


def exibir_grafico_percentual_pontos():
    rotulos, dados = extrair_dados('dados_kobe.csv')
    percent_cestas = rotulos.index('% CESTAS')
    temporada = rotulos.index('TEMPORADA')
    
    lista_temporadas = [] #eixo X
    lista_percent_cestas = [] # eixo Y

    for elemento in dados:
        lista_temporadas.append(int(elemento[temporada]))
        lista_percent_cestas.append(float(elemento[percent_cestas]))
        
    exibir_grafico(lista_temporadas, lista_percent_cestas)
    