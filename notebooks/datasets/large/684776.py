def diferencia_diagonales(arreglo, x):
    diagonal_principal = sum(arreglo[i][i] for i in range(x))
    diagonal_secundaria = sum(arreglo[i][x-i-1] for i in range(x))
    return diagonal_principal - diagonal_secundaria

t = int(input().strip())

for _ in range(t):
    x = int(input().strip())
    arreglo = []
    
    for _ in range(x):
        fila = list(map(int, list(input().strip())))
        arreglo.append(fila)
    
    print(diferencia_diagonales(arreglo, x))