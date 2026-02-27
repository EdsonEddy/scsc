def sumad(n):
    while n >= 10:
        n = sum(int(d) for d in str(n))
    return n

def proceso(n,k):
    for _ in range(k):
        suma = sumad(n)
        n //= 10
        n = int(str(suma) + str(n))
    return n

for _ in range(int(input())):

    n, k = map(int, input().split())

    print(proceso(n, k))