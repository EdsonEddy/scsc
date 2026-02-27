import math

numeros = []
while True:
    n = int(input())
    if n == -1:
        break
    numeros.append(n)
for numero in numeros:
    original = numero
    factores = []
    if numero == 1:
        print("1 = 1")
        continue
    contador = 0
    while numero % 2 == 0:
        contador += 1
        numero //= 2
    if contador > 0:
        if contador == 1:
            factores.append("2")
        else:
            factores.append(f"2^{contador}")
    for i in range(3, int(math.sqrt(numero)) + 1, 2):
        contador = 0
        while numero % i == 0:
            contador += 1
            numero //= i
        if contador > 0:
            if contador == 1:
                factores.append(f"{i}")
            else:
                factores.append(f"{i}^{contador}")
    if numero > 2:
        factores.append(f"{numero}")
    resultado = f"{original} = "
    resultado += "*".join(factores)
    
    print(resultado)