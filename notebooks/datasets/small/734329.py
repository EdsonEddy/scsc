# Función que realiza una búsqueda en profundidad (DFS) para contar los lugares accesibles
def dfs(mapa, visitado, x, y, filas, columnas):
    # Si estamos fuera de los límites o en una posición ya visitada o en un muro (#)
    if x < 0 or x >= filas or y < 0 or y >= columnas or visitado[x][y] or mapa[x][y] == '#':
        return 0
    
    # Marcamos el lugar como visitado
    visitado[x][y] = True
    
    # Inicialmente contamos el lugar actual
    total = 1
    
    # Movimientos posibles: arriba, abajo, izquierda, derecha
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Recorrer los lugares adyacentes
    for dx, dy in movimientos:
        total += dfs(mapa, visitado, x + dx, y + dy, filas, columnas)
    
    return total

# Procesar múltiples casos de prueba
while True:
    # Leer las dimensiones
    filas, columnas = map(int, input().split())
    
    if filas == 0 and columnas == 0:
        break  # Fin de los casos de prueba
    
    # Leer el mapa de la ciudad
    mapa = []
    start_x = start_y = 0
    
    for i in range(filas):
        fila = input().strip()
        mapa.append(fila)
        # Encontrar la posición inicial '@'
        if '@' in fila:
            start_x = i
            start_y = fila.index('@')
    
    # Matriz para marcar los lugares visitados
    visitado = [[False] * columnas for _ in range(filas)]
    
    # Realizar DFS desde la posición inicial
    resultado = dfs(mapa, visitado, start_x, start_y, filas, columnas)
    
    # Imprimir el resultado
    print(resultado)