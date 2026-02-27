def dfs(grid, x, y, visited):
    # Si estamos fuera de los límites o en una celda no visitable, retornar 0
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == '#' or visited[x][y]:
        return 0

    # Marcamos el lugar como visitado
    visited[x][y] = True

    # Comenzamos contando el lugar actual
    count = 1

    # Movimientos posibles: arriba, abajo, izquierda, derecha
    movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Recursivamente visitamos las celdas adyacentes
    for dx, dy in movements:
        count += dfs(grid, x + dx, y + dy, visited)

    return count

def count_accessible_places(grid, start_x, start_y):
    # Creamos una matriz para marcar los lugares ya visitados
    visited = [[False] * len(grid[0]) for _ in range(len(grid))]
    return dfs(grid, start_x, start_y, visited)

def main():
    while True:
        # Leer dimensiones
        x, y = map(int, input().split())
        if x == 0 and y == 0:
            break

        # Leer el grid
        grid = [input().strip() for _ in range(x)]

        # Encontrar la posición inicial marcada con '@'
        start_x, start_y = -1, -1
        for i in range(x):
            for j in range(y):
                if grid[i][j] == '@':
                    start_x, start_y = i, j
                    break
            if start_x != -1:
                break

        # Calcular y mostrar el número de lugares accesibles
        print(count_accessible_places(grid, start_x, start_y))

if __name__ == "__main__":
    main()
