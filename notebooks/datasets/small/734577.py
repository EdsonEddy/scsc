def dfs(grid, x, y, visited):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == '#' or (x, y) in visited:
        return 0
    
    visited.add((x, y))
    
    count = 1
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dx, dy in directions:
        count += dfs(grid, x + dx, y + dy, visited)
    
    return count

while True:
    x, y = map(int, input().strip().split())
    if x == 0 and y == 0:
        break
    
    grid = [input().strip() for _ in range(x)]
    
    start_x, start_y = None, None
    for i in range(x):
        for j in range(y):
            if grid[i][j] == '@':
                start_x, start_y = i, j
                break
        if start_x is not None:
            break
    
    visited = set()
    total_places = dfs(grid, start_x, start_y, visited)
    
    print(total_places)