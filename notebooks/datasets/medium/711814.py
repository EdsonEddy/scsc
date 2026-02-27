def criba_eratosthenes(limite):
    es_primo = [True] * (limite + 1)
    p = 2
    while p * p <= limite:
        if es_primo[p]:
            for i in range(p * p, limite + 1, p):
                es_primo[i] = False
        p += 1
    return [p for p in range(2, limite + 1) if es_primo[p]]
def factores_primos(n, primos):
    factores = {}
    for p in primos:
        if p * p > n:
            break
        while n % p == 0:
            if p in factores:
                factores[p] += 1
            else:
                factores[p] = 1
            n //= p
    if n > 1:
        factores[n] = 1
    return factores

def formatear_factores(factores):
    partes = []
    for factor, potencia in sorted(factores.items()):
        if potencia > 1:
            partes.append(f"{factor}^{potencia}")
        else:
            partes.append(f"{factor}")
    return '*'.join(partes)

def main():
    primos = criba_eratosthenes(int(10**6**0.5) + 1)
    resultados = []
    while True:
        dato = input().strip()
        numero = int(dato)
        if numero == -1:
            break
        factores = factores_primos(numero, primos)
        resultado = f"{numero} = {formatear_factores(factores)}"
        print(resultado)
if __name__ == "__main__":
    main()