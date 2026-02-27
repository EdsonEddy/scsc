import heapq
import sys

def minimum_sum_cost(numbers):
    # Crear un min-heap inicializando con todos los números
    heapq.heapify(numbers)
    total_cost = 0
    
    # Mientras haya más de un elemento en el heap
    while len(numbers) > 1:
        # Sacar los dos elementos más pequeños
        first = heapq.heappop(numbers)
        second = heapq.heappop(numbers)
        
        # Calcular el costo actual de la suma
        current_cost = first + second
        
        # Sumar al costo total
        total_cost += current_cost
        
        # Agregar el resultado de la suma al heap
        heapq.heappush(numbers, current_cost)
    
    return total_cost

def main():
    input = sys.stdin.read().strip().split('\n')
    index = 0
    
    while index < len(input):
        line = input[index].strip().split()
        N = int(line[0])
        
        if N == 0:
            break
        
        numbers = list(map(int, input[index + 1].strip().split()))
        index += 2
        
        if len(numbers) != N:
            continue
        
        # Calcular el costo mínimo de suma para este conjunto de números
        min_cost = minimum_sum_cost(numbers)
        print(min_cost)

if __name__ == "__main__":
    main()
