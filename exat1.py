def diagnosticar_limite(renda, lar, edu, mov):
    
    max_lar = renda * (30 / 100)
    max_edu = renda * (20 / 100)
    max_mov = renda * (15 / 100)
    
    porcentagem_lar = lar * 100 / renda
    porcentagem_edu = edu * 100 / renda
    porcentagem_mov = mov * 100 / renda   
   
    diagnostico = ""
    comparar_lar = ""
    comparar_edu = ""
    comparar_mov = ""
    
    
    if lar <= max_lar:
        comparar_lar = "seus gastos estão dentro da margem recomendada"
    
    else:
        comparar_lar = f"Portanto, idealmente, o máximo de sua comprometida com moradia devereia ser de R$ {max_lar:.2f}"
    ###############################    
    
    if edu <= max_edu:
        comparar_edu = "seus gastos estão dentro da margem recomendada"
    
    else:
        comparar_edu = f"Portanto, idealmente, o máximo de sua comprometida com moradia devereia ser de R$ {max_edu:.2f}"
    ################################
    
    if mov <= max_mov:
        comparar_mov = "seus gastos estão dentro da margem recomendada"
    
    else:
        comparar_mov = f"Portanto, idealmente, o máximo de sua comprometida com moradia devereia ser de R$ {max_mov:.2f}"
    
    
    diagnostico += f"Seus gastos totais com moradia comprometem {porcentagem_lar:.2f}% de sua renda total. O máximo recomendado é de 30%. {comparar_lar}.\n"
    diagnostico += f"Seus gastos totais com educação comprometem {porcentagem_edu:.2f}% de sua renda total. O máximo recomendado é de 20%. {comparar_edu}.\n"
    diagnostico += f"Seus gastos totais com transporte comprometem {porcentagem_mov:.2f}% de sua renda total. O máximo recomendado é de 15%. {comparar_mov}."
    
    print(diagnostico)

renda = float(input("Digite sua renda mensal: R$ ")) 
lar = float(input("Digite seus gastos com moradia: R$ "))     # max 30%
edu = float(input("Digite seus gastos com educação: R$ "))    # max 20%
mov = float(input("Digite seus gastos com transporte: R$ "))  # max 15%
diagnosticar_limite(renda, lar, edu, mov) 