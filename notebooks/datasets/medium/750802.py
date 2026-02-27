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
    n = int(input().strip())
    if n == 0:
        break
    
    numeros = list(map(int, input().strip().split()))
    

    resultado = costo_minimo_suma(numeros)
    

    print(resultado)
