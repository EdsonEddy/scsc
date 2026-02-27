import heapq

while True:
    n = int(input())
    if n <= 0:
        break
    
    lista = list(map(int, input().split()))
    heapq.heapify(lista)
    
    total = 0
    while len(lista) > 1:
        costo_actual = heapq.heappop(lista)
        costo_actual += heapq.heappop(lista)
        total += costo_actual
        heapq.heappush(lista, costo_actual)
    
    print(total)