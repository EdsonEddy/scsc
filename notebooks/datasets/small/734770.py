# Definimos las direcciones posibles de movimiento (arriba, abajo, izquierda, derecha)
DIRECCIONES = [(-1, 0), (1, 0), (0, -1), (0, 1)]
 
# Función para realizar DFS y contar los lugares accesibles
def dfs(matriz, visitado, x, y, filas, columnas):
    # Marcamos el lugar actual como visitado
    visitado[x][y] = True
    contador = 1  # Contamos el lugar actual
    
    # Recorremos las direcciones posibles
    for dx, dy in DIRECCIONES:
        nuevo_x, nuevo_y = x + dx, y + dy
        # Verificamos si la nueva posición está dentro de los límites y es accesible
        if 0 <= nuevo_x < filas and 0 <= nuevo_y < columnas:
            if matriz[nuevo_x][nuevo_y] == '.' and not visitado[nuevo_x][nuevo_y]:
                # Realizamos DFS en la nueva posición
                contador += dfs(matriz, visitado, nuevo_x, nuevo_y, filas, columnas)
    
    return contador
 
# Función principal para resolver cada caso de prueba
def resolver_caso():
    while True:
        # Leemos las dimensiones de la ciudad
        filas, columnas = map(int, input().split())
        if filas == 0 and columnas == 0:
            break
        
        # Leemos la matriz de la ciudad
        ciudad = [input() for _ in range(filas)]
        
        # Buscamos la posición inicial '@'
        inicio_x, inicio_y = -1, -1
        for i in range(filas):
            for j in range(columnas):
                if ciudad[i][j] == '@':
                    inicio_x, inicio_y = i, j
                    break
            if inicio_x != -1:
                break
        
        # Creamos una matriz de visitados
        visitado = [[False for _ in range(columnas)] for _ in range(filas)]
        
        # Realizamos DFS desde la posición inicial
        resultado = dfs(ciudad, visitado, inicio_x, inicio_y, filas, columnas)
        
        # Imprimimos el resultado
        print(resultado)
 
# Llamada a la función principal
resolver_caso()