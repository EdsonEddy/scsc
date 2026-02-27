# Función para calcular la diferencia entre las diagonales de una matriz cuadrada
def calcular_desproporcion_diagonal(matriz):
    tamano = len(matriz)
    suma_diagonal_principal = 0
    suma_diagonal_secundaria = 0
    for i in range(tamano):
        suma_diagonal_principal += matriz[i][i]
        suma_diagonal_secundaria += matriz[i][tamano - 1 - i]
    return suma_diagonal_principal - suma_diagonal_secundaria

# Lectura de la entrada
num_casos = int(input())

# Procesamiento de cada caso de prueba
for _ in range(num_casos):
    N = int(input())
    matriz = []
    for _ in range(N):
        fila = list(map(int, input().strip()))
        matriz.append(fila)
    
    # Calcular la diferencia entre las diagonales
    diferencia = calcular_desproporcion_diagonal(matriz)
    print(diferencia)
