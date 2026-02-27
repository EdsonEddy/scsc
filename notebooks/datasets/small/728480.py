def count_places(rows, cols, city_map):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    start = None
    for i in range(rows):
        for j in range(cols):
            if city_map[i][j] == '@':
                start = (i, j)
                break
        if start:
            break
    
    visited = set()
    
    def dfs(position):
        if position in visited:
            return
        visited.add(position)
        i, j = position
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < rows and 0 <= nj < cols and city_map[ni][nj] in ('.', '@'):
                dfs((ni, nj))
    
    dfs(start)
    
    return len(visited)

while True:
    rows, cols = map(int, input().split())
    if rows == 0 and cols == 0:
        break
    city_map = [input() for _ in range(rows)]
    
    result = count_places(rows, cols, city_map)
    print(result)