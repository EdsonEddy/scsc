import sys
movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(mapa, visitado, x, y):
    if x < 0 or x >= len(mapa) or y < 0 or y >= len(mapa[0]) or visitado[x][y] or mapa[x][y] == '#':
        return 0
    visitado[x][y] = True
    contador = 1
    for dx, dy in movimientos:
        contador += dfs(mapa, visitado, x + dx, y + dy)

    return contador

while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    mapa = [input().strip() for _ in range(x)]
    visitado = [[False] * y for _ in range(x)]
    for i in range(x):
        for j in range(y):
            if mapa[i][j] == '@':
                inicio_x, inicio_y = i, j
                break
    lugares_visitables = dfs(mapa, visitado, inicio_x, inicio_y)
    print(lugares_visitables)