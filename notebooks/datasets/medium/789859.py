def moduloNumeros(x, k):
    if x % 9 == 0:
        return 9
    else:
        return (x % 9) ** k % 9 or 9

t = int(input())
for _ in range(t):
    x, k = map(int, input().split())
    print(moduloNumeros(x, k))
