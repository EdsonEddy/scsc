def calcular_desproporcion_diagonal(matrices):
    resultados = []
    for matriz in matrices:
        n = len(matriz)
        diagonal_principal = sum(matriz[i][i] for i in range(n))
        diagonal_secundaria = sum(matriz[i][n-i-1] for i in range(n))
        desproporcion = diagonal_principal - diagonal_secundaria
        resultados.append(desproporcion)
    return resultados
num_casos = int(input())
matrices = []
for _ in range(num_casos):
    n = int(input())
    matriz = []
    for _ in range(n):
        fila = list(map(int, input().strip()))
        matriz.append(fila)
    matrices.append(matriz)

# Calcular y mostrar los resultados
resultados = calcular_desproporcion_diagonal(matrices)
for resultado in resultados:
    print(resultado)
