import sys

def descomponer_factores_primos(n):
    factores = []
    i = 2
    while i * i <= n:
        cuenta = 0
        while n % i == 0:
            n //= i
            cuenta += 1
        if cuenta == 1:
            factores.append(f"{i}")
        elif cuenta > 1:
            factores.append(f"{i}^{cuenta}")
        i += 1
    if n > 1:
        factores.append(f"{n}")
    return factores

for linea in sys.stdin:
    n = int(linea.strip())
    if n == -1:
        break
    factores = descomponer_factores_primos(n)
    print(f"{n} = {'*'.join(factores)}")