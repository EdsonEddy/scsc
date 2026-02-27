def calcular_desproporcion_diagonal(matriz, n):
    suma_diagonal_principal = 0
    suma_diagonal_secundaria = 0
    
    for i in range(n):
        suma_diagonal_principal += int(matriz[i][i])
        suma_diagonal_secundaria += int(matriz[i][n - 1 - i])
    
    return suma_diagonal_principal - suma_diagonal_secundaria

# Leer número de casos de prueba
num_casos = int(input())

# Procesar cada caso de prueba
resultados = []
for _ in range(num_casos):
    # Leer tamaño de la matriz
    n = int(input().strip())
    
    # Leer la matriz
    matriz = []
    for _ in range(n):
        fila = input().strip()
        matriz.append(fila)
    
    # Calcular la desproporción diagonal para la matriz actual
    desproporcion = calcular_desproporcion_diagonal(matriz, n)
    
    # Guardar el resultado
    resultados.append(desproporcion)

# Imprimir los resultados
for resultado in resultados:
    print(resultado)
