def calcular_desproporcion_diagonal(matriz):
    n = len(matriz)
    diagonal = 0
    diagonal_secundaria = 0
    
    for i in range(n):
        diagonal += matriz[i][i]
        diagonal_secundaria += matriz[i][n - i - 1]
    
    return diagonal - diagonal_secundaria

def main():
    c = int(input())
    
    for _ in range(c):
        n = int(input())
        matriz = []
        for _ in range(n):
            fila = list(map(int, input().strip()))
            matriz.append(fila)
        
        resultado = calcular_desproporcion_diagonal(matriz)
        print(resultado)

if __name__ == "__main__":
    main()