def dfs(grid, x, y, visited):
    # Dirección de los movimientos: arriba, abajo, izquierda, derecha
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    stack = [(x, y)]
    count = 0

    while stack:
        curr_x, curr_y = stack.pop()
        if (curr_x, curr_y) in visited:
            continue
        visited.add((curr_x, curr_y))
        count += 1
        
        for dx, dy in directions:
            new_x, new_y = curr_x + dx, curr_y + dy
            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
                if grid[new_x][new_y] in {'.', '@'} and (new_x, new_y) not in visited:
                    stack.append((new_x, new_y))
    
    return count

def main():
    while True:
        # Leer las dimensiones
        x, y = map(int, input().split())
        if x == 0 and y == 0:
            break
        
        # Leer la ciudad
        grid = [input().strip() for _ in range(x)]
        
        # Buscar la posición de '@'
        start_x, start_y = -1, -1
        for i in range(x):
            for j in range(y):
                if grid[i][j] == '@':
                    start_x, start_y = i, j
                    break
            if start_x != -1:
                break
        
        # Usar DFS para contar los lugares accesibles
        visited = set()
        result = dfs(grid, start_x, start_y, visited)
        
        # Imprimir el resultado
        print(result)

if __name__ == "__main__":
    main()
