def calcular_desproporcion_diagonal(matriz):
    n = len(matriz)
    diagonal_principal = 0
    diagonal_secundaria = 0
    
    for i in range(n):
        diagonal_principal += matriz[i][i]
        diagonal_secundaria += matriz[i][n - i - 1]
    
    return diagonal_principal - diagonal_secundaria

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    casos_prueba = int(data[0])
    index = 1
    resultados = []
    
    for _ in range(casos_prueba):
        n = int(data[index])
        matriz = []
        for j in range(n):
            fila = list(map(int, data[index + 1 + j]))
            matriz.append(fila)
        index += n + 1
        
        resultado = calcular_desproporcion_diagonal(matriz)
        resultados.append(resultado)
    
    for resultado in resultados:
        print(resultado)

if __name__ == "__main__":
    main()
