from math import ceil

def puede(plazo, tiempo):
    dias_op = 0
    while dias_op < plazo:
        tiempo_optimizado = ceil(tiempo / (dias_op + 1))
        if tiempo_optimizado <= plazo - dias_op:
            return "si"
        dias_op += 1
    return "no"

n = int(input())
resultados = []

for _ in range(n):
    plazo, tiempo_const = map(int, input().split())
    resultados.append(puede(plazo, tiempo_const))

for resultado in resultados:
    print(resultado)
