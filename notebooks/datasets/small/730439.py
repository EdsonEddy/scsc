import sys

sys.setrecursionlimit(10000)


movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dfs(mapa, x, y, visitado, filas, columnas):
    
    visitado[x][y] = True
   
    contador = 1


    for dx, dy in movimientos:
        nx, ny = x + dx, y + dy
        if 0 <= nx < filas and 0 <= ny < columnas and not visitado[nx][ny] and mapa[nx][ny] == '.':
            contador += dfs(mapa, nx, ny, visitado, filas, columnas)

    return contador



while True:
   
    filas, columnas = map(int, input().split())

   
    if filas == 0 and columnas == 0:
        break

  
    mapa = [list(input().strip()) for _ in range(filas)]

  
    visitado = [[False] * columnas for _ in range(filas)]

 
    for i in range(filas):
        for j in range(columnas):
            if mapa[i][j] == '@':
                inicio_x, inicio_y = i, j
                break

    
    mapa[inicio_x][inicio_y] = '.'

    resultado = dfs(mapa, inicio_x, inicio_y, visitado, filas, columnas)

   
    print(resultado)
