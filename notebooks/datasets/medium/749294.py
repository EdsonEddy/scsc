import heapq

def costo_minimo_adicion(numeros):
  
    heapq.heapify(numeros)
    costo_total = 0

    
    while len(numeros) > 1:
        
        costo1 = heapq.heappop(numeros)
        costo2 = heapq.heappop(numeros)
        
        
        suma_actual = costo1 + costo2
        costo_total += suma_actual
        
        
        heapq.heappush(numeros, suma_actual)

    return costo_total


while True:
   
    n = int(input())
    if n == 0:
        break

   
    numeros = list(map(int, input().split()))

   
    resultado = costo_minimo_adicion(numeros)
    print(resultado)
