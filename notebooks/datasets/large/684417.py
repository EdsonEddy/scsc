def c_desproporcion_diagonal(matriz):
    n = len(matriz)
    d_principal_suma = sum(matriz[i][i] for i in range(n))
    d_secundaria_suma = sum(matriz[i][n - 1 - i] for i in range(n))
    return d_principal_suma - d_secundaria_suma
casos = int(input())
for _ in range(casos):
    n = int(input())
    matriz = []
    for _ in range(n):
        fila = list(map(int, input().strip()))
        matriz.append(fila)
    resultado = c_desproporcion_diagonal(matriz)
    print(resultado)
