def resta (matriz, n):
    diag_prin = sum(matriz[i][i] for i in range(n))
    diag_sec = sum(matriz[i][n-i-1] for i in range(n))
    return diag_prin - diag_sec

casos = int(input().strip())

for j in range(casos):
    num = int(input().strip())
    matriz = []
    
    for k in range(num):
        fila = list(map(int, list(input().strip())))
        matriz.append(fila)
    print(resta(matriz, num))