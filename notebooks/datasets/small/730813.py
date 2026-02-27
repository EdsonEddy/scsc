def puedoVisitar(x, y, grid, visited, directions):
    if (x, y) in visited or grid[x][y] == '#':
        return 0
    
    visited.add((x, y))
    count = 1
    
    for dx, dy in directions:
        next_x, next_y = x + dx, y + dy
        if 0 <= next_x < len(grid) and 0 <= next_y < len(grid[0]):
            count += puedoVisitar(next_x, next_y, grid, visited, directions)
    
    return count

while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break

    caracter = []
    for _ in range(x):
        caracter.append(input().strip())

    pos_x, pos_y = None, None
    for i in range(x):
        for j in range(y):
            if caracter[i][j] == '@':
                pos_x, pos_y = i, j
                break
        if pos_x is not None:
            break

    visited = set()
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    print(puedoVisitar(pos_x, pos_y, caracter, visited, directions))