from math import isqrt

def es_primo(i):
    
    if i < 2:
        return False
    for j in range(2, isqrt(i) + 1):
        if i % j == 0:
            return False
    return True

while True:
    n = int(input())
    t=n
    if n == -1:
        break
    
    i = 2
    lista = []
    
    
    while n > 1:
        if n % i == 0:
            lista.append(i)
            n = n // i
        else:
            i += 1
        
            while not es_primo(i):
                i += 1
    diccionario={}
    for numero in lista:
        if numero in diccionario:
            diccionario[numero]+=1
        else:
            diccionario[numero]=1

    resultado=[]
    
    for clave ,valor in diccionario.items():
        if valor>=2:
            resultado.append(f"{clave}^{valor}")
        else:
            resultado.append(str(clave))
    final="*".join(resultado)
    print(f"{t} = {final}")