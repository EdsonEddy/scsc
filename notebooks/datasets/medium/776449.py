def descomponer_en_factores_primos(n):
    factores = {}
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            if divisor in factores:
                factores[divisor] += 1
            else:
                factores[divisor] = 1
            n //= divisor
        divisor += 1
        if divisor * divisor > n:
            if n > 1:
                factores[n] = 1
            break
    return factores

def formatear_factores(factores):
    partes = []
    for base, exponente in factores.items():
        if exponente > 1:
            partes.append(f"{base}^{exponente}")
        else:
            partes.append(f"{base}")
    return '*'.join(partes)

while True:
    n = int(input().strip())
    if n == -1:
        break
    factores = descomponer_en_factores_primos(n)
    resultado = formatear_factores(factores)
    print(f"{n} = {resultado}")