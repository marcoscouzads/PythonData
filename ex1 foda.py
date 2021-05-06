def diagnosticar(renda_familiar, num_integrantes):
    sal_min = 1045
    max_renda_familiar = 3 * sal_min
    max_renda_por_pessoa = 0.5 * sal_min
    
    renda_por_pessoa = renda_familiar / num_integrantes
    renda_por_pessoa = round(renda_por_pessoa, 2)
    
    diagnostico = ""
    
    comparar_renda_familiar = ""
    comparar_renda_por_pessoa = ""
    elegivel = ""
    
    if renda_familiar <= max_renda_familiar:
       comparar_renda_familiar = "inferior ou igual"
    else:
       comparar_renda_familiar = "superior"   
       
    if renda_por_pessoa <= max_renda_por_pessoa:
       comparar_renda_por_pessoa = "inferior ou igual"
    else:
       comparar_renda_por_pessoa = "superior"
       
    if renda_familiar <= max_renda_familiar or renda_por_pessoa <= max_renda_por_pessoa:
        elegivel = "pode"
    else:
        elegivel = "não pode"
        
    diagnostico += f"A renda familiar total é de R$ {renda_familiar:.2f}, é {comparar_renda_familiar} a R$ {max_renda_familiar:.2f}.\n"  
    diagnostico += f"A renda por pessoa é de R$ {renda_por_pessoa:.2f}, é {comparar_renda_por_pessoa} a R$ {max_renda_por_pessoa:.2f}.\n"
    diagnostico += f"O cidadão {elegivel} ser beneficiario do auxilio emergencial."
        
    print(diagnostico)
    
renda_familiar = float(input("Informe a renda familiar total mensal: "))
num_integrantes = int(input("Informe o número de membros da família: "))
diagnosticar(renda_familiar, num_integrantes)
    
    