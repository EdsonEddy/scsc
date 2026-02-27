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
    partes = []
    for p in sorted(factores):
        if factores[p] == 1:
            partes.append(str(p))
        else:
            partes.append(f"{p}^{factores[p]}")
    return "*".join(partes)
while True:
    try:
        linea = input().strip()
        if linea == "":
            continue
        numero = int(linea)
        if numero == -1:
            break
        print(f"{numero} = {descomponer_factores_primos(numero)}")
    except EOFError:
        break