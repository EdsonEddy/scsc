import heapq

def solve():
    while True:
        try:
            n = int(input())
            if n == 0:
                break
                
            numbers = list(map(int, input().split()))
            
            # Si solo hay un número, no hay operaciones
            if n == 1:
                print(0)
                continue
            
            # Convertir la lista en un heap (cola de prioridad)
            heapq.heapify(numbers)
            
            total_cost = 0
            while len(numbers) > 1:
                # Extraer los dos elementos más pequeños
                a = heapq.heappop(numbers)
                b = heapq.heappop(numbers)
                
                # Calcular el costo y la suma
                current_sum = a + b
                total_cost += current_sum
                
                # Insertar la suma de nuevo en el heap
                heapq.heappush(numbers, current_sum)
            
            print(total_cost)
            
        except EOFError:
            break

# Ejecutar la solución
solve()