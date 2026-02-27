def desproporcion_diagonal(matriz):
    diagonal_principal = 0
    diagonal_secundaria = 0
    n = len(matriz)
    
    for i in range(n):
        diagonal_principal += matriz[i][i]
        diagonal_secundaria += matriz[i][n - 1 - i]
    
    return diagonal_principal - diagonal_secundaria
n= int(input())

for _ in range(n):
    N = int(input())
    matriz = [list(map(int, input().strip())) for _ in range(N)]
    
    # Salida
    print(desproporcion_diagonal(matriz))
