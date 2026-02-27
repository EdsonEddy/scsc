import heapq

def costo_minimo_suma(numeros):
    heapq.heapify(numeros) 
    costo_total = 0
    
    while len(numeros) > 1:
        num1 = heapq.heappop(numeros)
        num2 = heapq.heappop(numeros)
        suma_actual = num1 + num2
        costo_total += suma_actual
        heapq.heappush(numeros, suma_actual)
    
    return costo_total


while True:

    N = int(input().strip())
    if N == 0:
        break 
    numeros = list(map(int, input().strip().split()))
    
    print(costo_minimo_suma(numeros))
