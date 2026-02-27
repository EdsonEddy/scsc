import sys
sys.setrecursionlimit(100000)

# Función para realizar DFS en la ciudad
def dfs(ciudad, x, y, visitado, filas, columnas):
    # Si está fuera de los límites o ya fue visitado o no es un lugar accesible, retornar 0
    if x < 0 or x >= filas or y < 0 or y >= columnas or visitado[x][y] or ciudad[x][y] == '#':
        return 0
    
    # Marcar como visitado
    visitado[x][y] = True
    # Contar el lugar actual
    cuenta = 1

    # Movimientos posibles: arriba, abajo, izquierda, derecha
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Explorar las celdas adyacentes
    for dx, dy in movimientos:
        cuenta += dfs(ciudad, x + dx, y + dy, visitado, filas, columnas)
    
    return cuenta

# Leer los casos de prueba
while True:
    # Leer dimensiones
    x, y = map(int, input().split())
    
    # Condición de finalización
    if x == 0 and y == 0:
        break
    
    # Leer la ciudad
    ciudad = [input().strip() for _ in range(x)]
    
    # Encontrar la posición inicial del '@'
    inicio_x, inicio_y = 0, 0
    for i in range(x):
        for j in range(y):
            if ciudad[i][j] == '@':
                inicio_x, inicio_y = i, j
    
    # Crear una matriz para marcar los lugares visitados
    visitado = [[False] * y for _ in range(x)]
    
    # Llamar a DFS para contar los lugares accesibles
    resultado = dfs(ciudad, inicio_x, inicio_y, visitado, x, y)
    
    # Imprimir el resultado
    print(resultado)