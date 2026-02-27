def dfs(x, y, ciudad, visitado):
    if x < 0 or x >= len(ciudad) or y < 0 or y >= len(ciudad[0]):
        return 0
    if ciudad[x][y] == '#' or visitado[x][y]:
        return 0
    
    visitado[x][y] = True
    
    contador = 1
    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in direcciones:
        contador += dfs(x + dx, y + dy, ciudad, visitado)
    
    return contador

def resolver_caso(x, y, ciudad):
    visitado = [[False] * y for _ in range(x)]
    inicio_x, inicio_y = -1, -1
    for i in range(x):
        for j in range(y):
            if ciudad[i][j] == '@':
                inicio_x, inicio_y = i, j
                break
        if inicio_x != -1:
            break
    
    if inicio_x != -1 and inicio_y != -1:
        return dfs(inicio_x, inicio_y, ciudad, visitado)
    
    return 0

resultados = []
while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    
    ciudad = [input().strip() for _ in range(x)]
    
    resultado = resolver_caso(x, y, ciudad)
    resultados.append(resultado)

for resultado in resultados:
    print(resultado)
