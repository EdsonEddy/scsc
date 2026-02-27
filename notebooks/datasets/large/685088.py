def diferencia_diagonales(matriz):
    n = len(matriz)
    diagonal_principal = sum(matriz[i][i] for i in range(n))
    diagonal_secundaria = sum(matriz[i][n - i - 1] for i in range(n))
    return diagonal_principal - diagonal_secundaria

casos = int(input())
for _ in range(casos):
    n = int(input())
    matriz = [list(map(int, input().strip())) for _ in range(n)]
    print(diferencia_diagonales(matriz))