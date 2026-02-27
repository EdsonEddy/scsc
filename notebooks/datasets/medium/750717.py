import heapq

def calcular_costo_minimo(numeros):
    # Transformamos la lista de números en un heap (cola de prioridad)
    heapq.heapify(numeros)
    costo_total = 0
    
    # Mientras haya al menos dos elementos en el heap
    while len(numeros) > 1:
        # Extraer los dos elementos más pequeños
        x = heapq.heappop(numeros)
        y = heapq.heappop(numeros)
        
        # Calcular el costo actual de sumar x e y
        costo_actual = x + y
        costo_total += costo_actual
        
        # Insertar el resultado de la suma de nuevo en el heap
        heapq.heappush(numeros, costo_actual)
    
    return costo_total


while True:
    
    n = int(input().strip())
    if n == 0:
        break
    
    
    numeros = list(map(int, input().strip().split()))
    
    
    resultado = calcular_costo_minimo(numeros)
    print(resultado)
