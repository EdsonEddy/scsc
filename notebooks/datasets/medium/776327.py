def criba_eratostenes(limite):
    sieve = [True] * (limite + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limite ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limite + 1, i):
                sieve[j] = False
    return [i for i in range(2, limite + 1) if sieve[i]]

def descomponer_en_factores_primos(n, primos):
    factores = []
    for primo in primos:
        if primo * primo > n:
            break
        count = 0
        while n % primo == 0:
            count += 1
            n //= primo
        if count > 0:
            factores.append((primo, count))
    if n > 1:
        factores.append((n, 1))
    return factores

def formatear_factores(factores):
    resultado = []
    for primo, count in factores:
        if count == 1:
            resultado.append(str(primo))
        else:
            resultado.append(f"{primo}^{count}")
    return "*".join(resultado)

limite = 10**6
primos = criba_eratostenes(limite)

entradas = []
while True:
    n = int(input())
    if n == -1:
        break
    entradas.append(n)

for n in entradas:
    factores = descomponer_en_factores_primos(n, primos)
    factorizacion = formatear_factores(factores)
    print(f"{n} = {factorizacion}")
