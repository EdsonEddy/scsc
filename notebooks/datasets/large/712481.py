def sumar_digitos(n):
    while n >= 10:
        suma = 0
        while n > 0:
            suma += n % 10
            n //= 10
        n = suma
    return n
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())

    for _ in range(k):
        suma = sumar_digitos(n)
        n //= 10
        n = int(str(suma) + str(n))
    print(n)