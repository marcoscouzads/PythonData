
arquivo = open("c:\\pyexe\\dados.csv", "w")
# arquivo = open("c:\pyexe\dados.txt", "a")

#arquivo.write("gosto de batata; caca; dd")

for i in range(2):
    print(f" esse é {i+1}º bb")
    nome = input("Nome: ")
    arquivo.write(f"{nome};")

arquivo.close()