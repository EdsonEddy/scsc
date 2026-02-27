# Función que ejecuta la búsqueda en profundidad (DFS) para contar lugares visitables
def dfs(matriz, x, y, visitados, filas, columnas):
    # Verificar que estamos dentro de los límites de la matriz y que el lugar no ha sido visitado
    if x < 0 or x >= filas or y < 0 or y >= columnas:
        return 0
    if visitados[x][y] or matriz[x][y] == '#':
        return 0
    
    # Marcar como visitado
    visitados[x][y] = True
    
    # Contar el lugar actual como visitado
    conteo = 1
    
    # Recorrer en las cuatro direcciones (arriba, abajo, izquierda, derecha)
    conteo += dfs(matriz, x - 1, y, visitados, filas, columnas)  # Arriba
    conteo += dfs(matriz, x + 1, y, visitados, filas, columnas)  # Abajo
    conteo += dfs(matriz, x, y - 1, visitados, filas, columnas)  # Izquierda
    conteo += dfs(matriz, x, y + 1, visitados, filas, columnas)  # Derecha
    
    return conteo

def resolver_casos():
    while True:
        # Leer las dimensiones de la matriz
        x, y = map(int, input().split())
        if x == 0 and y == 0:
            break
        
        # Leer la matriz
        matriz = [input().strip() for _ in range(x)]
        
        # Crear una matriz de visitados
        visitados = [[False for _ in range(y)] for _ in range(x)]
        
        # Encontrar la posición inicial marcada con '@'
        for i in range(x):
            for j in range(y):
                if matriz[i][j] == '@':
                    inicio_x, inicio_y = i, j
                    break
        
        # Ejecutar DFS desde la posición inicial
        resultado = dfs(matriz, inicio_x, inicio_y, visitados, x, y)
        
        # Imprimir el resultado
        print(resultado)

# Ejecutar la función principal
resolver_casos()
