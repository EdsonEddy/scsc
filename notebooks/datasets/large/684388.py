def calcular_desproporcion_diagonal(matriz):
    n = len(matriz)
    diagonal_principal = 0
    diagonal_secundaria = 0
    for i in range(n):
        diagonal_principal += matriz[i][i]
        diagonal_secundaria += matriz[i][n - i - 1]
    return diagonal_principal - diagonal_secundaria
num_casos = int(input().strip())
for _ in range(num_casos):
    n = int(input().strip())
    matriz = []
    for _ in range(n):
        fila = input().strip()
        matriz.append([int(char) for char in fila])
    desproporcion = calcular_desproporcion_diagonal(matriz)
    print(desproporcion)
