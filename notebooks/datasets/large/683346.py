def calcular_desproporcion_diagonal(matriz):
    diagonal_principal = sum(matriz[i][i] for i in range(len(matriz)))
    diagonal_secundaria = sum(matriz[i][len(matriz) - 1 - i] for i in range(len(matriz)))
    return diagonal_principal - diagonal_secundaria
num_casos = int(input())
for _ in range(num_casos):
    n = int(input())
    matriz = []
    for _ in range(n):
        fila = list(map(int, input().strip()))
        matriz.append(fila)
    desproporcion = calcular_desproporcion_diagonal(matriz)
    print(desproporcion)
