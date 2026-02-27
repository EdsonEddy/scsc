def desproporcion_diagonal(matriz):
    diagonal_principal = sum(matriz[i][i] for i in range(len(matriz)))
    diagonal_secundaria = sum(matriz[i][len(matriz)-1-i] for i in range(len(matriz)))
    return diagonal_principal - diagonal_secundaria

# Función para leer una matriz desde la entrada del teclado
def leer_matriz(n):
    matriz = []
    for _ in range(n):
        # Asumiendo que cada línea de la matriz es ingresada como una secuencia de números sin espacios
        fila = list(map(int, list(input())))
        matriz.append(fila)
    return matriz

# Leer el número de casos
num_casos = int(input())

# Procesar cada caso de prueba
for _ in range(num_casos):
    n = int(input())
    matriz = leer_matriz(n)
    print(desproporcion_diagonal(matriz))

