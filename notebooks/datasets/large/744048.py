import math

def puede_cumplir_con_plazo(plazo, demora):
    dias_optimizados = 0
    while plazo > 0:
        tiempo_actual = math.ceil(demora / (dias_optimizados + 1))
        if tiempo_actual <= plazo:
            return "si"
        dias_optimizados += 1
        plazo -= 1
    return "no"


casos = int(input())
for _ in range(casos):
    plazo, demora = map(int, input().split())
    print(puede_cumplir_con_plazo(plazo, demora))