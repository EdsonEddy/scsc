import heapq

def minimo_costo_suma(nums):
    # Creamos el heap a partir de la lista de números
    heapq.heapify(nums)
    total_costo = 0

    # Mientras haya más de un número en el heap
    while len(nums) > 1:
        # Extraemos los dos números más pequeños
        primero = heapq.heappop(nums)
        segundo = heapq.heappop(nums)

        # El costo de sumarlos
        costo_actual = primero + segundo
        total_costo += costo_actual

        # Insertamos el resultado de la suma de nuevo en el heap
        heapq.heappush(nums, costo_actual)

    return total_costo

# Lectura de los casos de prueba
while True:
    N = int(input())
    if N == 0:
        break
    
    nums = list(map(int, input().split()))
    print(minimo_costo_suma(nums))
