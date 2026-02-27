import sys
sys.setrecursionlimit(10000)


def dfs(ciudad, x, y, filas, columnas):
    
    if x < 0 or x >= filas or y < 0 or y >= columnas or ciudad[x][y] != '.':
        return 0

    
    ciudad[x][y] = '#'

    
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    
    contador = 1
    for dx, dy in movimientos:
        contador += dfs(ciudad, x + dx, y + dy, filas, columnas)

    return contador

def resolver_ciudad():
    while True:
        
        x, y = map(int, input().split())
        if x == 0 and y == 0:
            break

        
        ciudad = []
        for _ in range(x):
            ciudad.append(list(input()))

        
        for i in range(x):
            for j in range(y):
                if ciudad[i][j] == '@':
                    ciudad[i][j] = '.'
                    
                    print(dfs(ciudad, i, j, x, y))


resolver_ciudad()
