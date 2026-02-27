movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def dfs(ciudad, x, y, visitado):
    visitado[x][y] = True
    conteo = 1
    for dx, dy in movimientos:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(ciudad) and 0 <= ny < len(ciudad[0]) and not visitado[nx][ny] and ciudad[nx][ny] == '.':
            conteo += dfs(ciudad, nx, ny, visitado)
    return conteo
while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    ciudad = [input().strip() for _ in range(x)]
    visitado = [[False for _ in range(y)] for _ in range(x)]
    for i in range(x):
        for j in range(y):
            if ciudad[i][j] == '@':
                inicio_x, inicio_y = i, j
    resultado = dfs(ciudad, inicio_x, inicio_y, visitado)
    print(resultado)