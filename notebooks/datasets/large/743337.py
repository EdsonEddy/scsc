import math

def es_posible_cumplir_plazo(plazo, tiempo):
    dias_optimizados = 0
    while plazo > 0:
        tiempo_reducido = math.ceil(tiempo / (dias_optimizados + 1))
        if tiempo_reducido <= plazo:
            return "si"
        dias_optimizados += 1
        plazo -= 1
    return "no"

# Leer número de casos de prueba
n = int(input())
resultados = []

for _ in range(n):
    a, b = map(int, input().split())
    resultado = es_posible_cumplir_plazo(a, b)
    resultados.append(resultado)

# Imprimir los resultados
for resultado in resultados:
    print(resultado)
