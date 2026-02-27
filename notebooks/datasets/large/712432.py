def procesar_numero(n, k):
    for _ in range(k):
        suma_digitos = sum(int(digito) for digito in str(n))
        while suma_digitos >= 10:
            suma_digitos = sum(int(digito) for digito in str(suma_digitos))
        n = int(str(suma_digitos) + str(n)[:-1])
    return n

casos_prueba = int(input())
for _ in range(casos_prueba):
    n, k = map(int, input().split())
    resultado = procesar_numero(n, k)
    print(resultado)