def desproporcion_diagonal(matriz):
    n = len(matriz)
    diagonal_principal = 0
    diagonal_secundaria = 0
    for i in range(n):
        diagonal_principal += matriz[i][i]
        diagonal_secundaria += matriz[i][n - 1 - i]
    return diagonal_principal - diagonal_secundaria

casos = int(input())

for _ in range(casos):
    n = int(input())
    matriz = [list(map(int, input().strip())) for _ in range(n)]
    print(desproporcion_diagonal(matriz))
