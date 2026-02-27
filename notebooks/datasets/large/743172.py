import math

def es_posible_cumplir_plazo(plazo, tiempo):
    # Iteramos por el número máximo de días que se pueden optimizar (hasta que plazo sea 0)
    for dias in range(plazo):
        # Calculamos el tiempo reducido redondeando al siguiente número entero más cercano
        tiempo_reducido = math.ceil(tiempo / (dias + 1))
        # Verificamos si el tiempo reducido se puede cumplir con el plazo restante
        if tiempo_reducido <= (plazo - dias):
            return "si"
    return "no"

# Entrada de datos
n = int(input())
for _ in range(n):
    plazo, tiempo = map(int, input().split())
    print(es_posible_cumplir_plazo(plazo, tiempo))
