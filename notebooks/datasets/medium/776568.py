numeros = []
while True:
    entrada = int(input())
    if entrada == -1:
        break
    numeros.append(entrada)

for numero in numeros:
    n = numero
    factor = 2
    factores = {}

    while factor * factor <= n:
        while n % factor == 0:
            if factor in factores:
                factores[factor] += 1
            else:
                factores[factor] = 1
            n //= factor
        factor += 1

    if n > 1:
        if n in factores:
            factores[n] += 1
        else:
            factores[n] = 1

    salida = str(numero) + " = "
    partes = []
    for f in sorted(factores):
        if factores[f] == 1:
            partes.append(str(f))
        else:
            partes.append(str(f) + "^" + str(factores[f]))
    salida += "*".join(partes)
    print(salida)