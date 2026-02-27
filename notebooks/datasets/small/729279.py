import sys

# Movimientos posibles: izquierda, derecha, arriba, abajo
movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(mapa, visitado, x, y):
    # Si estamos fuera del mapa o en un lugar bloqueado, regresamos
    if x < 0 or x >= len(mapa) or y < 0 or y >= len(mapa[0]) or visitado[x][y] or mapa[x][y] == '#':
        return 0

    # Marcamos la celda actual como visitada
    visitado[x][y] = True
    
    # Contamos este lugar (marcado como '.') o la posición inicial (@)
    contador = 1

    # Exploramos las cuatro direcciones posibles
    for dx, dy in movimientos:
        contador += dfs(mapa, visitado, x + dx, y + dy)

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
    lugares_visitables = dfs(mapa, visitado, inicio_x, inicio_y)
    
    # Imprimir el resultado
    print(lugares_visitables)
