
movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dfs(ciudad, x, y, visitado):

    visitado[x][y] = True

    lugares_visitables = 1

    for dx, dy in movimientos:
        nuevo_x, nuevo_y = x + dx, y + dy

        if 0 <= nuevo_x < len(ciudad) and 0 <= nuevo_y < len(ciudad[0]) and not visitado[nuevo_x][nuevo_y] and ciudad[nuevo_x][nuevo_y] == '.':
            lugares_visitables += dfs(ciudad, nuevo_x, nuevo_y, visitado)
    
    return lugares_visitables


def contar_lugares_visitables():
    while True:

        dimensiones = input().split()
        filas, columnas = int(dimensiones[0]), int(dimensiones[1])
        if filas == 0 and columnas == 0:
            break
        

        ciudad = [input() for _ in range(filas)]
        

        inicio_x, inicio_y = 0, 0
        for i in range(filas):
            for j in range(columnas):
                if ciudad[i][j] == '@':
                    inicio_x, inicio_y = i, j
                    ciudad[i] = ciudad[i][:j] + '.' + ciudad[i][j+1:]
                    break
        visitado = [[False] * columnas for _ in range(filas)]

        resultado = dfs(ciudad, inicio_x, inicio_y, visitado)

        print(resultado)

contar_lugares_visitables()
