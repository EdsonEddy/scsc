def dfs(grid, x, y, visitado, filas, columnas):
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    visitado[x][y] = True
    contador = 1

    for dx, dy in movimientos:
        nuevo_x = x + dx
        nuevo_y = y + dy
        
        if 0 <= nuevo_x < filas and 0 <= nuevo_y < columnas:
            if not visitado[nuevo_x][nuevo_y] and grid[nuevo_x][nuevo_y] == '.':
                contador += dfs(grid, nuevo_x, nuevo_y, visitado, filas, columnas)
    
    return contador

def resolver_paseo():
    while True:
        x, y = map(int, input().split())
        
        if x == 0 and y == 0:
            break

        grid = []
        for _ in range(x):
            grid.append(list(input()))
        
        inicio_x, inicio_y = -1, -1
        for i in range(x):
            for j in range(y):
                if grid[i][j] == '@':
                    inicio_x, inicio_y = i, j
                    grid[i][j] = '.'

        visitado = [[False for _ in range(y)] for _ in range(x)]
        
        resultado = dfs(grid, inicio_x, inicio_y, visitado, x, y)
        
        print(resultado)

resolver_paseo()
