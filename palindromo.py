
#palindromo = str(input("digite: "))
def palindromo(s):
    tam = len(s)
    for i in range(tam//2):
        if s[i] != s[tam-i-1]:
            return False
    return True

print(palindromo('absa'))