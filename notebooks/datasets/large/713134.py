def suma(n):
    while n >= 10:
        n = sum(int(d) for d in str(n))
    return n
def procesar(n, k):
    n = str(n)
    for i in range(k):
        s = suma(int(n))
        n = str(s) + n[:-1]
    return int(n)
T = int(input())
for i in range(T):
    n, k = map(int, input().split())
    r = procesar(n, k)
    print(r)