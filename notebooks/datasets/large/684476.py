num_casos = int(input().strip())

# Procesar cada caso de prueba
for _ in range(num_casos):
    # Leer el tamaño de la matriz
    n = int(input().strip())
    
    # Inicializar sumas de las diagonales
    suma_principal = 0
    suma_secundaria = 0
    
    # Leer la matriz y calcular las sumas de las diagonales
    for i in range(n):
        fila = input().strip()
        suma_principal += int(fila[i])
        suma_secundaria += int(fila[n - 1 - i])
    
    # Calcular la desproporción diagonal
    desproporcion = suma_principal - suma_secundaria
    
    # Imprimir el resultado para el caso actual
    print(desproporcion)