import math

def es_posible_cumplir(plazo, demora):
    tiempo_optimizar = 0
    
    while tiempo_optimizar <= plazo:
        nuevo_tiempo = math.ceil(demora / (tiempo_optimizar + 1))
        if nuevo_tiempo <= plazo - tiempo_optimizar:
            return "si"
        tiempo_optimizar += 1
    
    return "no"

# Leer la entrada
num_casos = int(input())
for _ in range(num_casos):
    a, b = map(int, input().split())
    resultado = es_posible_cumplir(a, b)
    print(resultado)