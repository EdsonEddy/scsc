# Función que realiza la búsqueda en profundidad (DFS)
def dfs(city, x, y, visited):
    rows = len(city)
    cols = len(city[0])
    
    # Verificar si estamos fuera de los límites o si ya visitamos esta celda o es inalcanzable
    if x < 0 or x >= rows or y < 0 or y >= cols or city[x][y] == '#' or visited[x][y]:
        return 0

    # Marcar como visitada
    visited[x][y] = True
    count = 1  # Contar el lugar actual

    # Explorar en las 4 direcciones posibles (arriba, abajo, izquierda, derecha)
    count += dfs(city, x - 1, y, visited)  # Arriba
    count += dfs(city, x + 1, y, visited)  # Abajo
    count += dfs(city, x, y - 1, visited)  # Izquierda
    count += dfs(city, x, y + 1, visited)  # Derecha

    return count

while True:
    # Leer las dimensiones
    x, y = map(int, input().split())
    
    # Terminar cuando se ingresen dos ceros
    if x == 0 and y == 0:
        break
    
    # Leer la ciudad
    city = [input() for _ in range(x)]
    
    # Crear la matriz de visitados
    visited = [[False] * y for _ in range(x)]
    
    # Encontrar la posición del '@'
    for i in range(x):
        for j in range(y):
            if city[i][j] == '@':
                start_x, start_y = i, j

    # Realizar DFS desde la posición inicial
    result = dfs(city, start_x, start_y, visited)
    print(result)
