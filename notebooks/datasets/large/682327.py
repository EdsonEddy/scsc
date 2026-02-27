def d(m):
    n = len(m)
    dp = ds = 0
    for i in range(n):
        dp += m[i][i]
        ds += m[i][n - i - 1]
    return dp - ds 
nc = int(input())
for _ in range(nc):
    nf = int(input())
    m = [list(map(int, input().strip())) for _ in range(nf)]
    print(d(m))       