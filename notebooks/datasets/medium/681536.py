import heapq

def calcular_costo_minimo(nums):
    heapq.heapify(nums)
    costo_total = 0
    
    while len(nums) > 1:
        # Extraer los dos elementos más pequeños
        primero = heapq.heappop(nums)
        segundo = heapq.heappop(nums)
        
        # Sumar los elementos y actualizar el costo total
        suma = primero + segundo
        costo_total += suma
        
        # Insertar la suma de nuevo en el heap
        heapq.heappush(nums, suma)
    
    return costo_total

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    while True:
        N = int(data[index])
        index += 1
        if N == 0:
            break
        
        nums = list(map(int, data[index:index + N]))
        index += N
        
        print(calcular_costo_minimo(nums))

if __name__ == "__main__":
    main()
