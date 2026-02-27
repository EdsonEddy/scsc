def desproporcion(m):
    n = len(m)
    p = sum(m[i][i] for i in range(n))
    s = sum(m[i][n - i - 1] for i in range(n))
    return p - s

t = int(input())
for _ in range(t):
    n = int(input())
    m = [list(map(int, input())) for _ in range(n)]
    d = desproporcion(m)
    print(d)