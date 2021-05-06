def condicao_eleitoral():
    idade = int(input("digite sua idade: "))
    while idade <= 0:
        print("idade inválida!")
        idade = int(input("Digite uma idade válida: "))

    if idade >= 16 and idade < 18 or idade >= 70:
        print("Não tem obrigação de votar.")
    elif idade > 0 and idade < 16:
        print("não tem direito a voto.")
    else:
        print("tem obrigação de votar.")
    return(idade)
        

print(condicao_eleitoral())
