import math

n = int(input())
resultados = []

for _ in range(n):
    plazo, demora = map(int, input().split())

    posible = False
    for días_optimizados in range(plazo):
        tiempo_requerido = math.ceil(demora / (días_optimizados + 1))
        if tiempo_requerido <= plazo - días_optimizados:
            posible = True
            break

    if posible:
        resultados.append("si")
    else:
        resultados.append("no")

for resultado in resultados:
    print(resultado)
