def dfs(grid, x, y, visited):
    # Verificamos si estamos fuera de los límites o en un lugar no visitable
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == '#' or (x, y) in visited:
        return 0
    
    # Marcamos el lugar como visitado
    visited.add((x, y))
    
    # Contamos este lugar
    count = 1
    
    # Direcciones de movimiento (arriba, abajo, izquierda, derecha)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Recorrer las direcciones
    for dx, dy in directions:
        count += dfs(grid, x + dx, y + dy, visited)
    
    return count

# Leer múltiples casos de prueba
while True:
    x, y = map(int, input().strip().split())
    if x == 0 and y == 0:
        break
    
    grid = [input().strip() for _ in range(x)]
    
    # Encontrar la posición inicial '@'
    start_x, start_y = None, None
    for i in range(x):
        for j in range(y):
            if grid[i][j] == '@':
                start_x, start_y = i, j
                break
        if start_x is not None:
            break
    
    # Usar DFS para contar lugares visitables
    visited = set()
    total_places = dfs(grid, start_x, start_y, visited)
    
    # Imprimir el resultado
    print(total_places)