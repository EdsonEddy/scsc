def procesar_numero(n, k):
    for _ in range(k):
        suma_digitos = sum(int(digit) for digit in str(n))
        while suma_digitos >= 10:
            suma_digitos = sum(int(digit) for digit in str(suma_digitos))
        n = str(suma_digitos) + str(n)[:-1]
    return int(n)

casos_de_prueba = int(input())
for _ in range(casos_de_prueba):
    n, k = map(int, input().split())
    print(procesar_numero(n, k))