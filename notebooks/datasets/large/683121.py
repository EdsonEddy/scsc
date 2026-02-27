def leeMatriz(n):
    matriz = []
    for i in range(n):
        linea = input()
        linea2 = list(map(int, linea))
        matriz.append(linea2)
    return matriz

k=int(input())
for j in range(k):
    n = int(input())
    matriz = leeMatriz(n)
    cont = 0
    cont2=0
    for i in range(n):
        cont += matriz[i][n - 1 - i]
        cont2 += matriz[i][i]
    print(cont2-cont)