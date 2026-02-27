def Factorizar(n):
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

def Imprimir(n, factores):
    partes = []
    for primo in sorted(factores):
        exponente = factores[primo]
        if exponente == 1:
            partes.append(f"{primo}")
        else:
            partes.append(f"{primo}^{exponente}")
    print(f"{n} = {'*'.join(partes)}")

numeros = []
while True:
    entrada = input()
    if entrada == "-1":
        break
    numeros.append(int(entrada))

for numero in numeros:
    factores = Factorizar(numero)
    Imprimir(numero, factores)
