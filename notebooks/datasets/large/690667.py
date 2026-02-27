def diferencia_diagonales(matriz, n):
    diagonal_principal = sum(matriz[i][i] for i in range(n))
    diagonal_secundaria = sum(matriz[i][n-i-1] for i in range(n))
    return diagonal_principal - diagonal_secundaria

# Leer el número de casos de prueba
t = int(input().strip())

for _ in range(t):
    # Leer el número de filas de la matriz
    n = int(input().strip())
    matriz = []
    
    # Leer cada fila de la matriz
    for _ in range(n):
        fila = list(map(int, list(input().strip())))
        matriz.append(fila)
    
    # Calcular y mostrar la diferencia de las diagonales
    print(diferencia_diagonales(matriz, n))