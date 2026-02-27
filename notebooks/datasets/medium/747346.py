import heapq

def costo_minimo_suma(numeros):
    heapq.heapify(numeros)
    costo_total = 0
    while len(numeros) > 1:
        suma = heapq.heappop(numeros) + heapq.heappop(numeros)
        costo_total += suma
        heapq.heappush(numeros, suma)
    return costo_total

while True:
    n = int(input().strip())
    if n == 0:
        break
    numeros = list(map(int, input().strip().split()))
    print(costo_minimo_suma(numeros))