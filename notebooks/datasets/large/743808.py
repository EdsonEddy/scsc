import math

def es_posible_cumplir_plazo(plazo, demora):
    for tiempo_opt in range(plazo):
        tiempo_reducido = math.ceil(demora / (tiempo_opt + 1))
        if tiempo_reducido <= plazo - tiempo_opt:
            return "si"
    return "no"

n = int(input())
for _ in range(n):
    plazo, demora = map(int, input().split())
    print(es_posible_cumplir_plazo(plazo, demora))
