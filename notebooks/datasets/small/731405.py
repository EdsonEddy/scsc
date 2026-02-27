def contar_lugares(ciudad, x, y, visitado):
    if x < 0 or x >= len(ciudad) or y < 0 or y >= len(ciudad[0]) or ciudad[x][y] == '#' or visitado[x][y]:
        return 0
    visitado[x][y] = True
    conteo = 1
    conteo += contar_lugares(ciudad, x-1, y, visitado)  # Arriba
    conteo += contar_lugares(ciudad, x+1, y, visitado)  # Abajo
    conteo += contar_lugares(ciudad, x, y-1, visitado)  # Izquierda
    conteo += contar_lugares(ciudad, x, y+1, visitado)  # Derecha
    return conteo

def principal():
    while True:
        x, y = map(int, input().split())
        if x == 0 and y == 0:
            break
        ciudad = [input() for _ in range(x)]
        for i in range(x):
            for j in range(y):
                if ciudad[i][j] == '@':
                    x_inicio, y_inicio = i, j
                    break
        visitado = [[False for _ in range(y)] for _ in range(x)]
        print(contar_lugares(ciudad, x_inicio, y_inicio, visitado))

if __name__ == "__main__":
    principal()
