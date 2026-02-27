def calcular_desproporcion(matriz):
    n = len(matriz)
    suma_diagonal_principal = 0
    suma_diagonal_secundaria = 0
    for i in range(n):
        suma_diagonal_principal += matriz[i][i]
        suma_diagonal_secundaria += matriz[i][n - i - 1]
    return suma_diagonal_principal - suma_diagonal_secundaria

num_casos = int(input())
for _ in range(num_casos):
    n = int(input())
    matriz = [list(map(int, input().strip())) for _ in range(n)]
    print(calcular_desproporcion(matriz))
