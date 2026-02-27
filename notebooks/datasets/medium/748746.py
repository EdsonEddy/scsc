import heapq

def costo_minimo_suma(numeros):
    heapq.heapify(numeros)
    costo_total = 0

    while len(numeros) > 1:
        primero = heapq.heappop(numeros)
        segundo = heapq.heappop(numeros)

        suma = primero + segundo
        costo_total += suma

        heapq.heappush(numeros, suma)

    return costo_total

while True:
    N = int(input())
    if N == 0:
        break
    entrada = input().strip().split()

    numeros = list(map(int, entrada))

    print(costo_minimo_suma(numeros))