def unDigitoMod(x, k):
    if x == 0:
        return 0
    x = x % 9
    if x == 0:
        return 9
    r = pow(x, k, 9)
    return 9 if r == 0 else r

n = int(input())
for i in range(n):
    x, k = map(int, input().split())
    print(unDigitoMod(x, k))
