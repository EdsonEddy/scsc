def diferencia_diagonales(matriz, n):
    diagonal_principal = sum(matriz[i][i] for i in range(n))
    diagonal_secundaria = sum(matriz[i][n-i-1] for i in range(n))
    return diagonal_principal - diagonal_secundaria
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    matriz = []
    for _ in range(n):
        fila = list(map(int, list(input().strip())))
        matriz.append(fila)
    print(diferencia_diagonales(matriz, n))
