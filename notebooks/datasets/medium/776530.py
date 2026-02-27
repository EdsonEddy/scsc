import sys
import math

def generar_criba(n):
    criba = [True] * (n + 1)
    criba[0] = criba[1] = False
    for i in range(2, int(math.isqrt(n)) + 1):
        if criba[i]:
            for j in range(i * i, n + 1, i):
                criba[j] = False
    primos = [i for i, es_primo in enumerate(criba) if es_primo]
    return primos

def factorizar(n, primos):
    factores = {}
    if n == 1:
        return factores
    for p in primos:
        if p * p > n:
            break
        while n % p == 0:
            factores[p] = factores.get(p, 0) + 1
            n = n // p
    if n > 1:
        factores[n] = factores.get(n, 0) + 1
    return factores

def formatear_factores(factores):
    partes = []
    for p in sorted(factores.keys()):
        exp = factores[p]
        if exp == 1:
            partes.append(str(p))
        else:
            partes.append(f"{p}^{exp}")
    return '*'.join(partes)

def main():
    primos = generar_criba(1000000)
    for line in sys.stdin:
        n = int(line.strip())
        if n == -1:
            break
        if n == 1:
            print("1 = 1")
            continue
        factores = factorizar(n, primos)
        resultado = formatear_factores(factores)
        print(f"{n} = {resultado}")

if __name__ == "__main__":
    main()