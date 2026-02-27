def dfs(c, v, x, y, filas, col):
    if x < 0 or x >= filas or y < 0 or y >= col: 
        return 0
    if v[x][y] or c[x][y] == '#': 
        return 0
    v[x][y] = True 
    count = 1 
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in dir:
        count += dfs(c, v, x + dx, y + dy, filas, col)
    
    return count

while True:
    filas, col = map(int, input().split())
    if filas == 0 and col == 0:
        break 
    
    c = []
    i_x = i_y = -1

    for i in range(filas):
        fila = list(input().strip())
        c.append(fila)
        if '@' in fila:
            i_x = i
            i_y = fila.index('@')
    
    v = [[False] * col for _ in range(filas)]
    
    res = dfs(c, v, i_x, i_y, filas, col)
    
    print(res)
