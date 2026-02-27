import heapq

def costo_minimo_suma(nums):
    heapq.heapify(nums)  # Convertir la lista en una cola de prioridad (heap)
    costo_total = 0

    while len(nums) > 1:
        # Extraer los dos números más pequeños
        primero = heapq.heappop(nums)
        segundo = heapq.heappop(nums)
        
        # Calcular el costo actual y agregarlo al costo total
        costo_actual = primero + segundo
        costo_total += costo_actual
        
        # Insertar el resultado de la suma de vuelta en el heap
        heapq.heappush(nums, costo_actual)
    
    return costo_total

# Leer la entrada
while True:
    n = int(input())
    if n == 0:
        break
    nums = list(map(int, input().split()))
    print(costo_minimo_suma(nums))


