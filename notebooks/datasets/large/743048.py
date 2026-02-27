import math

def puede_cumplir_plazo(plazo, tiempo_construccion):
    dias_optimizacion = 0
    while plazo > 0:

        tiempo_reducido = math.ceil(tiempo_construccion / (dias_optimizacion + 1))
        
        if tiempo_reducido <= plazo:
            return "si"
        
        plazo -= 1
        dias_optimizacion += 1
    
    return "no"

n = int(input().strip())
resultados = []

for _ in range(n):
    plazo, tiempo_construccion = map(int, input().strip().split())
    resultados.append(puede_cumplir_plazo(plazo, tiempo_construccion))

for resultado in resultados:
    print(resultado)