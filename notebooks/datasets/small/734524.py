def dfs(matriz, fila_actual, columna_actual, celdas_visitadas):
    if fila_actual < 0 or fila_actual >= len(matriz) or columna_actual < 0 or columna_actual >= len(matriz[0]) or matriz[fila_actual][columna_actual] == '#' or (fila_actual, columna_actual) in celdas_visitadas:
        return 0
    
    celdas_visitadas.add((fila_actual, columna_actual))
    total_celdas = 1
    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for cambio_fila, cambio_columna in direcciones:
        total_celdas += dfs(matriz, fila_actual + cambio_fila, columna_actual + cambio_columna, celdas_visitadas)
    
    return total_celdas

while True:
    num_filas, num_columnas = map(int, input().strip().split())
    if num_filas == 0 and num_columnas == 0:
        break
    
    matriz = [input().strip() for _ in range(num_filas)]
    
    inicio_fila, inicio_columna = None, None
    for i in range(num_filas):
        for j in range(num_columnas):
            if matriz[i][j] == '@':
                inicio_fila, inicio_columna = i, j
                break
        if inicio_fila is not None:
            break
    
    celdas_visitadas = set()
    total_visibles = dfs(matriz, inicio_fila, inicio_columna, celdas_visitadas)
    
    print(total_visibles)
