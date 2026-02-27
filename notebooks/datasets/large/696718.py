def Diagonales(m):
    n = len(m)
    m = [[int(cad) for cad in fil] for fil in m]
    dp = sum(m[i][i] for i in range(n))
    ds = sum(m[i][n - 1 - i] for i in range(n))
    return dp, ds
def entrada():
    n = int(input())
    m = [list(input().strip()) for i in range(n)]
    return m
t = int(input())
for i in range(t):
    m = entrada()
    dp, ds = Diagonales(m)
    print(dp - ds)