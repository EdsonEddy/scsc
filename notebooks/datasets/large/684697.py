def calcular_diferencia_diagonales(matriz):
    suma_diagonal_principal = 0
    suma_diagonal_secundaria = 0
    n = len(matriz)
    for i in range(n):
        suma_diagonal_principal += matriz[i][i]
        suma_diagonal_secundaria += matriz[i][n - 1 - i]
    return suma_diagonal_principal - suma_diagonal_secundaria

# Lectura de la entrada
casos_prueba = int(input())
for _ in range(casos_prueba):
    n = int(input())  # Número de filas y columnas de la matriz
    matriz = []
    for _ in range(n):
        fila = list(map(int, input().strip()))
        matriz.append(fila)
    
    # Calcular y mostrar la diferencia de diagonales
    print(calcular_diferencia_diagonales(matriz))