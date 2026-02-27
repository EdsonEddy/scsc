def sumar_digitos(n):

    while n >= 10:
        suma = 0
        while n > 0:
            suma += n % 10
            n //= 10
        n = suma
    return n

casos = int(input())

for _ in range(casos):
    n, k = input().split()
    k = int(k)

    n = list(n)

    for _ in range(k):

        suma = sumar_digitos(int(''.join(n)))

        n.pop()

        n.insert(0, str(suma))

    print(''.join(n))