def dfs(matriz, x, y, visitado):
    # me estoy volviendo loco
    # Comprobar límites y condiciones de visita
    if x < 0 or x >= len(matriz) or y < 0 or y >= len(matriz[0]) or visitado[x][y] or matriz[x][y] == '#':
        return 0
    
    # Marcar el lugar como visitado
    # ...
    visitado[x][y] = True
    
    # Contar el lugar actual (1) y explorar los 4 vecinos
    # vivimos en una sociedad
    contador = 1  # Contamos el lugar actual
    
    # Direcciones: arriba, abajo, izquierda, derecha
    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dx, dy in direcciones:
        contador += dfs(matriz, x + dx, y + dy, visitado)
    
    return contador

def contar_lugares(matriz, inicio_x, inicio_y):
    visitado = [[False] * len(matriz[0]) for _ in range(len(matriz))]
    return dfs(matriz, inicio_x, inicio_y, visitado)

def main():
    while True:
        # Leer filas y columnas
        entrada = input().strip()
        x, y = map(int, entrada.split())
        
        if x == 0 and y == 0:
            break
        
        matriz = []
        
        # Leer la matriz
        for _ in range(x):
            fila = input().strip()
            matriz.append(fila)
        
        # Encontrar la posición inicial '@'
        inicio_x, inicio_y = None, None
        for i in range(x):
            for j in range(y):
                if matriz[i][j] == '@':
                    inicio_x, inicio_y = i, j
                    break
            if inicio_x is not None:
                break
        
        # Contar lugares visitables...
        resultado = contar_lugares(matriz, inicio_x, inicio_y)
        
        # Imprimir el resultado...
        print(resultado)

main()
