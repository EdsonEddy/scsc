import math

def puede_cumplir_plazo(plazo, demora):
    dias_optimizados = 0
    while dias_optimizados < plazo:
        # Tiempo de construcción optimizado y redondeado
        tiempo_optimizado = math.ceil(demora / (dias_optimizados + 1))
        
        # Comprobamos si el tiempo optimizado es menor o igual al tiempo restante
        if tiempo_optimizado <= plazo - dias_optimizados:
            return "si"
        
        # Incrementamos el número de días de optimización
        dias_optimizados += 1

    return "no"

# Leer el número de casos de prueba
n = int(input())
resultados = []
for _ in range(n):
    plazo, demora = map(int, input().split())
    resultados.append(puede_cumplir_plazo(plazo, demora))

# Imprimir los resultados
for resultado in resultados:
    print(resultado)

