valor = float(input("Informe o valor total do consumo:R$ "))
pessoas = int(input("Informe o total de pessoas: "))
servico = int(input("Informe o percentual de serviço, entre 0 e 100: "))

if valor > 0:   
    if pessoas > 0:       
        if servico > 0 and servico <= 100:
            
            valor_total = valor + (valor * (servico / 100))
            valor_pessoas = valor_total / pessoas
            valor_pessoas = "{:.2f}".format(valor_pessoas).replace('.',',')
            valor_total = "{:.2f}".format(valor_total).replace('.',',')
            print(f"O valor total da conta, com a taxa de serviço, será de R$ {valor_total}.")
            print(f"Dividindo a conta por {pessoas} pessoa(s), cada pessoa deverá pagar R$ {valor_pessoas}.")
        else:
            print("Percentual de serviço invalido")
    else:
        print("Numero de pessoas invalido")          
else:
    print("valor invalido")
