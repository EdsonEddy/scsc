def calcular_desproporcion_diagonal(matriz, n):
    suma_diagonal_principal = 0
    suma_diagonal_secundaria = 0
    
    for i in range(n):
        suma_diagonal_principal += int(matriz[i][i])
        suma_diagonal_secundaria += int(matriz[i][n-i-1])
    
    return suma_diagonal_principal - suma_diagonal_secundaria

# Leer el número de casos de prueba
casos_de_prueba = int(input())

resultados = []

for _ in range(casos_de_prueba):
    n = int(input())
    matriz = []
    
    for _ in range(n):
        linea = input().strip()
        matriz.append(linea)
    
    resultado = calcular_desproporcion_diagonal(matriz, n)
    resultados.append(resultado)

for resultado in resultados:
    print(resultado)
