def diferencia_diagonales(matriz, n):
    suma_diagonal_principal = 0
    suma_diagonal_secundaria = 0
    
    for i in range(n):
        suma_diagonal_principal += int(matriz[i][i])
        suma_diagonal_secundaria += int(matriz[i][n-i-1])
    
    return suma_diagonal_principal - suma_diagonal_secundaria

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    resultados = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        matriz = []
        
        for _ in range(n):
            matriz.append(data[index])
            index += 1
        
        diferencia = diferencia_diagonales(matriz, n)
        resultados.append(diferencia)
    
    for resultado in resultados:
        print(resultado)

if __name__ == "__main__":
    main()
