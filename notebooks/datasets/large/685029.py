def calcular_desproporcion_diagonal(matriz):
    n = len(matriz)
    suma_diagonal_principal = 0
    suma_diagonal_secundaria = 0
    
    for i in range(n):
        suma_diagonal_principal += matriz[i][i]
        suma_diagonal_secundaria += matriz[i][n - 1 - i]
    
    desproporcion = suma_diagonal_principal - suma_diagonal_secundaria
    return desproporcion

# Lectura de entrada y procesamiento
num_casos = int(input().strip())

resultados = []
for _ in range(num_casos):
    n = int(input().strip())
    matriz = []
    for _ in range(n):
        fila = list(map(int, input().strip()))
        matriz.append(fila)
    
    resultado = calcular_desproporcion_diagonal(matriz)
    resultados.append(resultado)

# Imprimir resultados
for resultado in resultados:
    print(resultado)
