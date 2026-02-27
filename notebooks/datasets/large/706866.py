def suma_digitos(n):
    while n >= 10:
        n = sum(int(d) for d in str(n))
    return n

def procesar_numero(n, k):
    n = str(n)
    for _ in range(k):
        suma = suma_digitos(int(n))
        n = str(suma) + n[:-1]
    return int(n)
T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    resultado = procesar_numero(n, k)
    print(resultado)