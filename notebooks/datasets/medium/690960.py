import heapq

def costo_minimo(numeros):
    heapq.heapify(numeros)
    costo_total = 0
    while len(numeros) > 1:
        a = heapq.heappop(numeros)
        b = heapq.heappop(numeros)
        suma = a + b
        costo_total += suma
        heapq.heappush(numeros, suma)
    return costo_total

while True:
    n = int(input())
    if n == 0:
        break
    numeros = list(map(int, input().split()))
    print(costo_minimo(numeros))