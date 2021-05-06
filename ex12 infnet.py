print("inicio do programa")

print ("o valor minimo para saque é de 10,00 reais e o máximo é de 600,00 reais")
print("as notas disponiveis são de: 1$, 5$, 10$, 50$ e 100$")
valor = int(input("digite o valor para saque: "))
if valor >= 10 and valor <= 600:
    print("processando pagamento!")
    # tirando o resto da divisão
    cem = valor % 100
    cin = cem % 50
    dez = cin % 10
    ci = dez % 5
    um = ci % 1
    #fazendo a divisão inteira para saber o valor
    n100 = valor // 100
    n50 = cem // 50
    n10 = cin // 10
    n5 = dez // 5
    n1 = ci // 1
    
    print(f" {n100} nota de 100,00 e {n50} nota de 50,00 e {n10} nota de 10,00 e {n5} nota de 5,00 e {n1} nota de 1,00")
    
else:
    print("valor invalido")
    print("retire-se")


print("fim do programa")