def calculate_diagonal_disproportion(matrix):
    n = len(matrix)
    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0
    
    # Calcular la suma de la diagonal principal y la diagonal secundaria
    for i in range(n):
        primary_diagonal_sum += int(matrix[i][i])
        secondary_diagonal_sum += int(matrix[i][n - i - 1])
    
    # Calcular la desproporción diagonal
    disproportion = primary_diagonal_sum - secondary_diagonal_sum
    return disproportion

def main():
    # Leer el número de casos de prueba
    test_cases = int(input().strip())
    
    # Procesar cada caso de prueba
    for _ in range(test_cases):
        # Leer la dimensión de la matriz (número de filas)
        n = int(input().strip())
        
        # Leer la matriz y convertir cada línea en una lista de enteros
        matrix = [list(map(int, input().strip())) for _ in range(n)]
        
        # Calcular la desproporción diagonal y mostrarla
        disproportion = calculate_diagonal_disproportion(matrix)
        print(disproportion)

if __name__ == "__main__":
    main()
