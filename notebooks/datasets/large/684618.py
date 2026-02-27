def calcular_desproporcion(matriz):
    n = len(matriz)
    suma_diagonal_principal = 0
    suma_diagonal_secundaria = 0
    for i in range(n):
        suma_diagonal_principal += matriz[i][i]
        suma_diagonal_secundaria += matriz[i][n - 1 - i]
    return suma_diagonal_principal - suma_diagonal_secundaria
casos = int(input())
for _ in range(casos):
    n = int(input())
    matriz = [list(map(int, input().strip())) for _ in range(n)]
    resultado = calcular_desproporcion(matriz)
    print(resultado)
