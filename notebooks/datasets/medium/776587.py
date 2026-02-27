def factorizar(n):
    factores = {}
    divisor = 2
    while divisor * divisor <= n:
        while n % divisor == 0:
            factores[divisor] = factores.get(divisor, 0) + 1
            n //= divisor
        divisor += 1 if divisor == 2 else 2
    if n > 1:
        factores[n] = factores.get(n, 0) + 1
    return factores

while True:
    n = int(input())
    if n == -1:
        break
    factores = factorizar(n)
    salida = []
    for f in sorted(factores):
        exp = factores[f]
        if exp == 1:
            salida.append(str(f))
        else:
            salida.append(f"{f}^{exp}")
    print(f"{n} = {'*'.join(salida)}")
