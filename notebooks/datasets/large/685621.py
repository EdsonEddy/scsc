def calcular_desproporcion_diagonal(matriz, n):
    suma_diagonal_principal = 0
    suma_diagonal_secundaria = 0

    for i in range(n):
        suma_diagonal_principal += int(matriz[i][i])
        suma_diagonal_secundaria += int(matriz[i][n-1-i])
    
    return suma_diagonal_principal - suma_diagonal_secundaria

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    indice = 0
    num_casos = int(data[indice])
    indice += 1
    resultados = []

    for _ in range(num_casos):
        n = int(data[indice])
        indice += 1
        matriz = []
        for _ in range(n):
            matriz.append(data[indice])
            indice += 1
        
        resultado = calcular_desproporcion_diagonal(matriz, n)
        resultados.append(resultado)
    
    for resultado in resultados:
        print(resultado)
main()
