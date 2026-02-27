def dfs(x, y, ciudad, visitado):
    # Verificamos si estamos fuera de los límites o si es un lugar inaccesible o ya visitado
    if x < 0 or x >= len(ciudad) or y < 0 or y >= len(ciudad[0]):
        return 0
    if ciudad[x][y] == '#' or visitado[x][y]:
        return 0
    
    # Marcamos el lugar como visitado
    visitado[x][y] = True
    
    # Contamos el lugar actual
    contador = 1
    
    # Direcciones de movimiento: arriba, abajo, izquierda, derecha
    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Exploramos las cuatro direcciones
    for dx, dy in direcciones:
        contador += dfs(x + dx, y + dy, ciudad, visitado)
    
    return contador

def resolver_caso(x, y, ciudad):
    # Inicializar matriz de visitados
    visitado = [[False] * y for _ in range(x)]
    
    # Encontrar la posición inicial marcada con '@'
    inicio_x, inicio_y = -1, -1
    for i in range(x):
        for j in range(y):
            if ciudad[i][j] == '@':
                inicio_x, inicio_y = i, j
                break
        if inicio_x != -1:
            break
    
    # Realizar DFS desde la posición inicial
    if inicio_x != -1 and inicio_y != -1:
        return dfs(inicio_x, inicio_y, ciudad, visitado)
    
    return 0

# Lectura de la entrada
resultados = []
while True:
    # Leer dimensiones de la ciudad
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    
    # Leer la representación de la ciudad
    ciudad = [input().strip() for _ in range(x)]
    
    # Resolver el caso y agregar el resultado
    resultado = resolver_caso(x, y, ciudad)
    resultados.append(resultado)

# Imprimir los resultados
for resultado in resultados:
    print(resultado)