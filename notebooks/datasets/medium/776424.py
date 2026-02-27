def descomponer_factores_primos(numero):
    factores = []
    divisor = 2
    while divisor * divisor <= numero:
        exponente = 0
        while numero % divisor == 0:
            numero //= divisor
            exponente += 1
        if exponente > 0:
            if exponente == 1:
                factores.append(f"{divisor}")
            else:
                factores.append(f"{divisor}^{exponente}")
        divisor += 1
    if numero > 1:
        factores.append(f"{numero}")
    return "*".join(factores)

while True:
    entrada = input()
    if entrada.strip() == "-1":
        break
    numero = int(entrada)
    resultado = descomponer_factores_primos(numero)
    print(f"{numero} = {resultado}")