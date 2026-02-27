# Función para ejecutar la búsqueda en profundidad (DFS)
def dfs(city_map, visited, x, y, rows, cols):
    # Verificar si estamos fuera de los límites o si la posición es inaccesible o ya visitada
    if x < 0 or x >= rows or y < 0 or y >= cols or city_map[x][y] == '#' or visited[x][y]:
        return 0
    
    # Marcar la posición como visitada
    visited[x][y] = True
    
    # Contamos el lugar actual como accesible
    count = 1
    
    # Movimientos posibles (arriba, abajo, izquierda, derecha)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Explorar las 4 direcciones
    for dx, dy in moves:
        count += dfs(city_map, visited, x + dx, y + dy, rows, cols)
    
    return count

# Función principal
def main():
    while True:
        # Leer las dimensiones del mapa
        x, y = map(int, input().split())
        
        # Terminar cuando x, y sean ambos 0
        if x == 0 and y == 0:
            break
        
        # Leer el mapa de la ciudad
        city_map = [list(input().strip()) for _ in range(x)]
        
        # Inicializar la matriz de visitados
        visited = [[False] * y for _ in range(x)]
        
        # Encontrar la posición inicial del '@'
        start_x, start_y = -1, -1
        for i in range(x):
            for j in range(y):
                if city_map[i][j] == '@':
                    start_x, start_y = i, j
                    break
            if start_x != -1:
                break
        
        # Realizar DFS desde la posición inicial y contar los lugares accesibles
        result = dfs(city_map, visited, start_x, start_y, x, y)
        
        # Imprimir el resultado
        print(result)

# Llamar a la función principal
if __name__ == "__main__":
    main()
