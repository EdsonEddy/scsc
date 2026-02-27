def descomponer_factores_primos(n):
    factores = {}
    divisor = 2
    while divisor * divisor <= n:
        while n % divisor == 0:
            factores[divisor] = factores.get(divisor, 0) + 1
            n //= divisor
        divisor += 1
    if n > 1:
        factores[n] = factores.get(n, 0) + 1
    return factores

while True:
    try:
        numero = int(input())
        if numero == -1:
            break
        factores = descomponer_factores_primos(numero)
        salida = f"{numero} = " + "*".join(
            f"{p}" if e == 1 else f"{p}^{e}" for p, e in sorted(factores.items())
        )
        print(salida)
    except EOFError:
        break
