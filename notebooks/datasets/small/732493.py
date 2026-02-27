def count_accessible_places(grid, start_row, start_col):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    stack = [(start_row, start_col)]
    accessible_count = 0

    while stack:
        row, col = stack.pop()
        if (row, col) in visited:
            continue
        visited.add((row, col))
        accessible_count += 1

        # Movimientos en las 4 direcciones
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < rows and 0 <= new_col < cols:
                if grid[new_row][new_col] == '.' and (new_row, new_col) not in visited:
                    stack.append((new_row, new_col))

    return accessible_count

def main():
    while True:
        x, y = map(int, input().split())
        if x == 0 and y == 0:
            break

        grid = [input().strip() for _ in range(x)]
        start_row, start_col = None, None

        # Encontrar la posición inicial '@'
        for i in range(x):
            for j in range(y):
                if grid[i][j] == '@':
                    start_row, start_col = i, j
                    break
            if start_row is not None:
                break

        # Contar lugares accesibles
        result = count_accessible_places(grid, start_row, start_col)
        print(result)

if __name__ == "__main__":
    main()