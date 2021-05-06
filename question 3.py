def julgar_vencedor():
    participantes = int(input("digite a quantidade de participantes: "))
    for i in range(participantes):
        nome = input("nome do participante: ")
        
        nota = float(input("nota do participante: "))
        while nota < 0 or nota > 10:
            print("nota inválida - deve estar entre 0 e 10.")
            nota = float(input("Nota do participante: "))
            
        if i == 0:
            nome_vencedor = nome
            nota_vencedor = nota
        elif nota > nota_vencedor:
            nota_vencedor = nota
            nome_vencedor = nome
            
    print(f"O(A) nome do(a) vencedor(a): {nome_vencedor} com nota {nota_vencedor}")

julgar_vencedor()