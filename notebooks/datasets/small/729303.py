def dfs(grid, x, y, visited):
    if (x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or 
        grid[x][y] == '#' or (x, y) in visited):
        return 0
    
    visited.add((x, y))
    count = 1
    
    # Explorar en las cuatro direcciones
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        count += dfs(grid, x + dx, y + dy, visited)
    
    return count

def solve_case(rows, cols):
    grid = [input().strip() for _ in range(rows)]
    start_x, start_y = -1, -1
    
    # Encontrar la posición inicial (@)
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '@':
                start_x, start_y = i, j
                break
        if start_x != -1:
            break
    
    visited = set()
    result = dfs(grid, start_x, start_y, visited)
    print(result)

# Procesar múltiples casos de prueba
while True:
    rows, cols = map(int, input().split())
    if rows == 0 and cols == 0:
        break
    solve_case(rows, cols)