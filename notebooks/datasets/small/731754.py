def flood_fill(grid, x, y):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == '#':
        return 0
    
    if grid[x][y] == '.' or grid[x][y] == '@':
        grid[x][y] = '#'  # Mark as visited
        return 1 + flood_fill(grid, x+1, y) + flood_fill(grid, x-1, y) + \
               flood_fill(grid, x, y+1) + flood_fill(grid, x, y-1)
    
    return 0

def find_start(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '@':
                return i, j
    return -1, -1  # Start not found

while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    
    grid = [list(input().strip()) for _ in range(x)]
    
    start_x, start_y = find_start(grid)
    if start_x != -1 and start_y != -1:
        result = flood_fill(grid, start_x, start_y)
        print(result)
    else:
        print(0)  # No starting point found