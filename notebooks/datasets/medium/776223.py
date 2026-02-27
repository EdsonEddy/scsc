def descomponer_factores_primos(n):
    factores = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factores[d] = factores.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factores[n] = factores.get(n, 0) + 1
    return factores
def formato_factores(factores):
    partes = []
    for p in sorted(factores):
        if factores[p] == 1:
            partes.append(f"{p}")
        else:
            partes.append(f"{p}^{factores[p]}")
    return "*".join(partes)
numeros = []
while True:
    entrada = int(input())
    if entrada == -1:
        break
    numeros.append(entrada)
for numero in numeros:
    factores = descomponer_factores_primos(numero)
    print(f"{numero} = {formato_factores(factores)}")