import sys
import math

def generar_criba(limite):
    criba = [True] * (limite + 1)
    criba[0] = criba[1] = False
    for i in range(2, int(math.sqrt(limite)) + 1):
        if criba[i]:
            for j in range(i*i, limite + 1, i):
                criba[j] = False
    return criba

# Precalcular primos hasta 1,000,000
limite_maximo = 10**6
criba = generar_criba(limite_maximo)
primos = [i for i, es_primo in enumerate(criba) if es_primo]

def descomponer_factores(n):
    if n == 1:
        return {1: 1}
    
    factores = {}
    for primo in primos:
        if primo * primo > n:
            break
        while n % primo == 0:
            factores[primo] = factores.get(primo, 0) + 1
            n = n // primo
    if n > 1:
        factores[n] = 1
    
    return factores

def formatear_factores(n, factores):
    if n == 1:
        return "1 = 1"
    
    partes = []
    for primo in sorted(factores.keys()):
        exp = factores[primo]
        if exp == 1:
            partes.append(str(primo))
        else:
            partes.append(f"{primo}^{exp}")
    return f"{n} = {'*'.join(partes)}"

# Leer entrada hasta encontrar -1
for line in sys.stdin:
    n = int(line.strip())
    if n == -1:
        break
    factores = descomponer_factores(n)
    print(formatear_factores(n, factores))