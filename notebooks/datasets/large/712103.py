casos = int(input())
for _ in range(casos):
    n, k = map(int, input().split())
    n = str(n)
    for _ in range(k):
        suma = int(n)
        while suma >= 10:
            suma = sum(int(d) for d in str(suma))
        n = str(suma) + n[:-1]
    print(n)