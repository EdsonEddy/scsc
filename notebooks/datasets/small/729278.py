import sys
sys.setrecursionlimit(10000)

# Movimientos posibles: izquierda, derecha, arriba, abajo
movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(mapa, visitado, x, y, filas, columnas):
    # Marcamos la celda actual como visitada
    visitado[x][y] = True
    # Iniciamos el contador con 1 porque contamos el lugar actual
    contador = 1

    # Exploramos las cuatro direcciones posibles
    for dx, dy in movimientos:
        nx, ny = x + dx, y + dy
        # Verificamos que el nuevo lugar esté dentro del mapa y no haya sido visitado
        if 0 <= nx < filas and 0 <= ny < columnas and not visitado[nx][ny] and mapa[nx][ny] == '.':
            contador += dfs(mapa, visitado, nx, ny, filas, columnas)

    return contador

while True:
    # Leer dimensiones de la ciudad
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break

    # Leer el mapa
    mapa = [input().strip() for _ in range(x)]
    
    # Matriz para marcar las posiciones visitadas
    visitado = [[False] * y for _ in range(x)]
    
    # Buscar la posición inicial donde está '@'
    for i in range(x):
        for j in range(y):
            if mapa[i][j] == '@':
                inicio_x, inicio_y = i, j
                break

    # Realizamos DFS desde la posición inicial
    lugares_visitables = dfs(mapa, visitado, inicio_x, inicio_y, x, y)
    
    # Imprimir el resultado
    print(lugares_visitables)
