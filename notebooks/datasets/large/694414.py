def leer_matriz(f):
    m = []
    for _ in range(f):
        fi = input()
        m.append([int(num) for num in fi]) 
    return m

def calcular(m):
    suma1 = sum(m[i][i] for i in range(len(m)))
    suma2 = sum(m[i][len(m)-i-1] for i in range(len(m)))
    de = suma1 - suma2
    return de


c = int(input())
for _ in range(c):
    f = int(input())
    m = leer_matriz(f)
    re = calcular(m)
    print(re)