# Función para realizar DFS y contar los lugares visitables
def dfs(x, y, grid, visitado):
    # Definimos las direcciones de movimiento: arriba, abajo, izquierda, derecha
    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Marcamos la posición como visitada
    visitado[x][y] = True
    contador = 1  # Contamos el lugar actual

    # Recorremos las 4 direcciones posibles
    for dx, dy in direcciones:
        nx, ny = x + dx, y + dy
        # Verificamos si está dentro del rango y si es un lugar visitable
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and not visitado[nx][ny] and grid[nx][ny] == '.':
            contador += dfs(nx, ny, grid, visitado)
    
    return contador

# Función para procesar los casos de prueba
def contar_lugares(grid, filas, columnas):
    # Crear una matriz para marcar los lugares visitados
    visitado = [[False for _ in range(columnas)] for _ in range(filas)]
    
    # Encontrar la posición inicial '@'
    for i in range(filas):
        for j in range(columnas):
            if grid[i][j] == '@':
                # Realizar DFS desde la posición inicial y contar los lugares visitables
                return dfs(i, j, grid, visitado)

# Leer los casos de prueba
while True:
    # Leer las dimensiones del grid
    x, y = map(int, input().split())
    
    # Si x e y son 0, terminamos el programa
    if x == 0 and y == 0:
        break
    
    # Leer el grid
    grid = [input().strip() for _ in range(x)]
    
    # Llamamos a la función para contar los lugares visitables e imprimimos el resultado
    print(contar_lugares(grid, x, y))
3