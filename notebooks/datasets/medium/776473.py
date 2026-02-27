def descomponer_factores_primos(n):
    i = 2
    factores = {}
    while i * i <= n:
        while n % i == 0:
            factores[i] = factores.get(i, 0) + 1
            n //= i
        i += 1
    if n > 1:
        factores[n] = factores.get(n, 0) + 1
    return factores

while True:
    n = int(input())
    if n == -1:
        break

    factores = descomponer_factores_primos(n)
    salida = f"{n} = "
    partes = []
    for factor in sorted(factores):
        exponente = factores[factor]
        if exponente == 1:
            partes.append(f"{factor}")
        else:
            partes.append(f"{factor}^{exponente}")
    salida += "*".join(partes)
    print(salida)