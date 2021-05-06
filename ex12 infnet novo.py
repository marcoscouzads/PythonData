soma = 0
for x in range(1, 101):
    soma += x
    if (x% 1 == 0):
        print(f"valor da soma {x}  e a soma {soma} ")
print(f"o resultado final é {soma}")