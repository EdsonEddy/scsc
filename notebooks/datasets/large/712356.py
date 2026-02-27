def sumar_digitos(n):
    while n >= 10:
        n = sum(int(d) for d in str(n))
    return n

def procesar_numero(n, k):
    for _ in range(k):
        suma = sumar_digitos(n)
        n = int(str(suma) + str(n)[:-1])  
    return n
casos = int(input())
for _ in range(casos):
    n, k = map(int, input().split())
    print(procesar_numero(n, k))