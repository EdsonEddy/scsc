import math

def es_posible(plazo, demora):
    for dias_optimizados in range(plazo):
        tiempo_requerido = math.ceil(demora / (dias_optimizados + 1))
        if tiempo_requerido <= (plazo - dias_optimizados):
            return "si"
    return "no"

# Leer datos de entrada
import sys
input = sys.stdin.read
datos = input().strip().split()
n = int(datos[0])
casos = [(int(datos[i*2 + 1]), int(datos[i*2 + 2])) for i in range(n)]

# Procesar cada caso de prueba
resultados = []
for plazo, demora in casos:
    resultados.append(es_posible(plazo, demora))

# Imprimir resultados
print("\n".join(resultados))
