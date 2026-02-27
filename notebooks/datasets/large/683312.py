def difdiag(matriz):
    n = len(matriz)
    sumdiagpri = sum(matriz[i][i] for i in range(n))
    sumdiagsecu = sum(matriz[i][n - 1 - i] for i in range(n))
    return sumdiagpri - sumdiagsecu


T = int(input())
for _ in range(T):
    N = int(input())

    matriz = [list(map(int, input().strip())) for _ in range(N)]

    print(difdiag(matriz))
