def desproporcion_diagonal(matriz):
    n = len(matriz)
    suma_diagonal_principal = sum(matriz[i][i] for i in range(n))
    suma_diagonal_secundaria = sum(matriz[i][n - i - 1] for i in range(n))
    return suma_diagonal_principal - suma_diagonal_secundaria
casos_prueba = int(input())
for _ in range(casos_prueba):
    filas = int(input())
    matriz = [list(map(int, input())) for _ in range(filas)]
    print(desproporcion_diagonal(matriz))