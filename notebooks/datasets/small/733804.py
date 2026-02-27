import sys
sys.setrecursionlimit(10000)
def dfs(mapa, visitado, x, y, filas, columnas):
    if x < 0 or x >= filas or y < 0 or y >= columnas:
        return 0
    if mapa[x][y] == '#' or visitado[x][y]:
        return 0
    visitado[x][y] = True
    cuenta = 1
    cuenta += dfs(mapa, visitado, x + 1, y, filas, columnas)  
    cuenta += dfs(mapa, visitado, x - 1, y, filas, columnas)  
    cuenta += dfs(mapa, visitado, x, y + 1, filas, columnas)  
    cuenta += dfs(mapa, visitado, x, y - 1, filas, columnas)  
    return cuenta

while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    mapa = []
    for i in range(x):
        mapa.append(list(input().strip()))
    pos_inicial = None
    for i in range(x):
        for j in range(y):
            if mapa[i][j] == '@':
                pos_inicial = (i, j)
                break
        if pos_inicial:
            break
    visitado = [[False] * y for _ in range(x)]
    resultado = dfs(mapa, visitado, pos_inicial[0], pos_inicial[1], x, y)
    print(resultado)