# Definir las direcciones de movimiento posibles: arriba, abajo, izquierda, derecha
movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
 
# Función DFS para explorar las celdas accesibles
def dfs(ciudad, x, y, visitado):
    # Marcar la celda actual como visitada
    visitado[x][y] = True
    # Iniciar el contador de celdas accesibles con 1 (la celda actual)
    conteo = 1
    
    # Explorar las celdas vecinas en las cuatro direcciones posibles
    for dx, dy in movimientos:
        nx, ny = x + dx, y + dy
        # Verificar si la celda vecina está dentro de los límites y si es visitable
        if 0 <= nx < len(ciudad) and 0 <= ny < len(ciudad[0]) and not visitado[nx][ny] and ciudad[nx][ny] == '.':
            conteo += dfs(ciudad, nx, ny, visitado)
    
    return conteo
 
# Leer múltiples casos de prueba
while True:
    # Leer las dimensiones de la ciudad
    x, y = map(int, input().split())
    
    # Condición de término
    if x == 0 and y == 0:
        break
    
    # Leer la ciudad (tablero) como una lista de cadenas
    ciudad = [input().strip() for _ in range(x)]
    
    # Crear una matriz para llevar registro de las celdas visitadas
    visitado = [[False for _ in range(y)] for _ in range(x)]
    
    # Encontrar la posición inicial (donde está el '@')
    for i in range(x):
        for j in range(y):
            if ciudad[i][j] == '@':
                inicio_x, inicio_y = i, j
    
    # Iniciar la DFS desde la posición del '@' y contar los lugares accesibles
    resultado = dfs(ciudad, inicio_x, inicio_y, visitado)
    
    # Imprimir el resultado
    print(resultado)