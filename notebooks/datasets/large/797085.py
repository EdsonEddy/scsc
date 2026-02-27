import math

def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def contar_primos_consecutivos(k):
    n = 1
    contador = 0
    maximo = 0
    while n <= 500:
        r = n**2 - n + k
        if es_primo(r):
            contador = contador + 1
        else:
            if contador > maximo:
                maximo = contador
            contador = 0
        n = n + 1    
    return maximo

#Programa principal
t = int(input())
for i in range(t):
    k = int(input())
    if k>=3 and k<=100:
        resultado = contar_primos_consecutivos(k)
        print(f"{k}: {resultado}")
