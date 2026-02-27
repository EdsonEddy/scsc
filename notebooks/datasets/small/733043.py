def dfs(matriz, x, y, visitados):
    if (x < 0 or x >= len(matriz) or y < 0 or y >= len(matriz[0]) or 
        matriz[x][y] == '#' or (x, y) in visitados):
        return 0
    
    visitados.add((x, y))
    conteo = 1
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        conteo += dfs(matriz, x + dx, y + dy, visitados)
    
    return conteo
 
def resolver_caso(filas, columnas):
    matriz = [input().strip() for _ in range(filas)]
    inicio_x, inicio_y = -1, -1
    
    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] == '@':
                inicio_x, inicio_y = i, j
                break
        if inicio_x != -1:
            break
    
    visitados = set()
    resultado = dfs(matriz, inicio_x, inicio_y, visitados)
    print(resultado)
while True:
    filas, columnas = map(int, input().split())
    if filas == 0 and columnas == 0:
        break
    resolver_caso(filas, columnas)
