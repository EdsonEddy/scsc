def calcular_desproporcion_diagonal(matriz, n):
    s = 0
    u = 0
    
    for i in range(n):
        s += int(matriz[i][i])
        u += int(matriz[i][n-1-i])
    return s - u
t = int(input())
for _ in range(t):
    n = int(input())
    m = []
    for _ in range(n):
        f = input().strip()
        m.append(f)
    
    d = calcular_desproporcion_diagonal(m, n)
    print(d)
