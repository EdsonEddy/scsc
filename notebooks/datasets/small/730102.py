def dfs(x, y, mapa, visitado):
    if x < 0 or x >= len(mapa) or y < 0 or y >= len(mapa[0]) or visitado[x][y] or mapa[x][y] == '#':
        return 0
    visitado[x][y] = True
    lugares_accesibles = 1
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in movimientos:
        lugares_accesibles += dfs(x + dx, y + dy, mapa, visitado) 
    return lugares_accesibles

def contar_lugares_visitables(mapa, filas, columnas):
    for i in range(filas):
        for j in range(columnas):
            if mapa[i][j] == '@':
                pos_inicial_x, pos_inicial_y = i, j
                break
    visitado = [[False for _ in range(columnas)] for _ in range(filas)]
    return dfs(pos_inicial_x, pos_inicial_y, mapa, visitado)

while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    mapa = [input() for _ in range(x)]
    resultado = contar_lugares_visitables(mapa, x, y)
    print(resultado)