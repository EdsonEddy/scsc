import math

def puede_cumplir_plazo(plazo_entrega, tiempo_demora):
    for dias_optimizados in range(plazo_entrega + 1):
        tiempo_reducido = math.ceil(tiempo_demora / (dias_optimizados + 1))
        
        if tiempo_reducido <= (plazo_entrega - dias_optimizados):
            return "si"

    return "no"

n = int(input())
resultados = []

for _ in range(n):
    plazo, demora = map(int, input().split())
    resultados.append(puede_cumplir_plazo(plazo, demora))

for resultado in resultados:
    print(resultado)