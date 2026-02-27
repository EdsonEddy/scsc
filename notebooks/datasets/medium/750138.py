import heapq

def calcular_costo_minimo(lista_numeros):
    heapq.heapify(lista_numeros) 
    costo_acumulado = 0

    while len(lista_numeros) > 1:
        num1 = heapq.heappop(lista_numeros)
        num2 = heapq.heappop(lista_numeros)
        suma_actual = num1 + num2
        costo_acumulado += suma_actual

        heapq.heappush(lista_numeros, suma_actual)

    return costo_acumulado

while True:
    cantidad_numeros = int(input().strip())
    if cantidad_numeros == 0:
        break

    valores = list(map(int, input().strip().split()))
    print(calcular_costo_minimo(valores))
