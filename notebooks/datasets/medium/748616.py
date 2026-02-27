import heapq
def costo_min(numeros):
    heapq.heapify(numeros)
    costo_total = 0
    while len(numeros) > 1:
        first = heapq.heappop(numeros) 
        second = heapq.heappop(numeros)

        costo_actual=first+second
        costo_total+=costo_actual

        heapq.heappush(numeros, costo_actual)
    return costo_total
#Main
while True:
    n = int(input())
    if n == 0:
        break
    numeros = list(map(int, input().strip().split()))
    print(costo_min(numeros))