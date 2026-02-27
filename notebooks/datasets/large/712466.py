def suma_digitos(n):
    suma = 0
    for digito in str(n):
        suma += int(digito)
    return suma

n_casos = int(input())
for _ in range(n_casos):
    n, k = map(int, input().split())
    for _ in range(k):
        suma = suma_digitos(n)
        while suma > 9:
            suma = suma_digitos(suma)
        n = str(suma) + str(n)[:-1]
    print(n)