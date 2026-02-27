def calcular_desproporcion_diagonal(tamano_matriz, matriz):
    suma_diagonal_principal = 0
    suma_diagonal_secundaria = 0
    
    for i in range(tamano_matriz):
        suma_diagonal_principal += int(matriz[i][i])
        suma_diagonal_secundaria += int(matriz[i][tamano_matriz - 1 - i])
    
    return suma_diagonal_principal - suma_diagonal_secundaria

numero_de_casos = int(input())

for _ in range(numero_de_casos):
    n = int(input())
    matriz = []
    for _ in range(n):
        fila = input()
        matriz.append(fila)
    
    resultado = calcular_desproporcion_diagonal(n, matriz)
    print(resultado)
