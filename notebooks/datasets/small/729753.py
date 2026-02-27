from collections import deque
movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(mapa, start_x, start_y, filas, columnas):
    cola = deque([(start_x, start_y)])
    visitados = [[False] * columnas for _ in range(filas)]
    visitados[start_x][start_y] = True
    lugares_visitados = 1
    while cola:
        x, y = cola.popleft()
        for dx, dy in movimientos:
            nuevo_x, nuevo_y = x + dx, y + dy
            if 0 <= nuevo_x < filas and 0 <= nuevo_y < columnas and not visitados[nuevo_x][nuevo_y] and mapa[nuevo_x][nuevo_y] == '.':
                visitados[nuevo_x][nuevo_y] = True
                lugares_visitados += 1
                cola.append((nuevo_x, nuevo_y))

    return lugares_visitados

def resolver_caso(filas, columnas, mapa):
    for i in range(filas):
        for j in range(columnas):
            if mapa[i][j] == '@':
                mapa[i][j] = '.'
                return bfs(mapa, i, j, filas, columnas)

while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break

    mapa = [list(input().strip()) for _ in range(x)]
    print(resolver_caso(x, y, mapa))