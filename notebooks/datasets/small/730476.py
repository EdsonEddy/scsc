def es_valido(x, y, filas, columnas, mapa, visitado):
    return 0 <= x < filas and 0 <= y < columnas and mapa[x][y] == '.' and not visitado[x][y]

def dfs(x, y, filas, columnas, mapa, visitado):

    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visitado[x][y] = True
    contador = 1
    
    for dx, dy in direcciones:
        nuevo_x, nuevo_y = x + dx, y + dy
        if es_valido(nuevo_x, nuevo_y, filas, columnas, mapa, visitado):
            contador += dfs(nuevo_x, nuevo_y, filas, columnas, mapa, visitado)
    
    return contador

while True:
    filas, columnas = map(int, input().split())
    
    if filas == 0 and columnas == 0:
        break
    
    mapa = [list(input()) for _ in range(filas)]
    
    visitado = [[False] * columnas for _ in range(filas)]
    
  
    for i in range(filas):
        for j in range(columnas):
            if mapa[i][j] == '@':
                inicio_x, inicio_y = i, j
                mapa[i][j] = '.'  

    resultado = dfs(inicio_x, inicio_y, filas, columnas, mapa, visitado)
    
    print(resultado)