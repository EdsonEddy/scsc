#BRYAN ADRIAN AGUILAR ROBLES
#INF 111

def diferencia_diagonales(matriz):
    diagonal_principal = 0
    diagonal_secundaria = 0
    n = len(matriz)
    for i in range(n):
        diagonal_principal += int(matriz[i][i])
        diagonal_secundaria += int(matriz[i][n - i - 1])
    return diagonal_principal - diagonal_secundaria

num_casos = int(input())

for _ in range(num_casos):
    num_filas = int(input())
    matriz = [input() for _ in range(num_filas)]
    diferencia = diferencia_diagonales(matriz)
    print(diferencia)