def calcular_desproporcion_diagonal(matriz):
    n = len(matriz)
    diagonal_principal = 0
    diagonal_secundaria = 0
    
    for i in range(n):
        diagonal_principal += matriz[i][i]
        diagonal_secundaria += matriz[i][n - i - 1]
    
    return diagonal_principal - diagonal_secundaria
 
def main():
    casos_prueba = int(input())
    
    for _ in range(casos_prueba):
        n = int(input())
        matriz = []
        for _ in range(n):
            fila = list(map(int, input().strip()))
            matriz.append(fila)
        
        resultado = calcular_desproporcion_diagonal(matriz)
        print(resultado)
 
if __name__ == "__main__":
    main()