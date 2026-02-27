import heapq

def calcular_costo_minimo(nums):
    heapq.heapify(nums)
    
    costo_total = 0

    while len(nums) > 1:
        num1 = heapq.heappop(nums)
        num2 = heapq.heappop(nums)
        
        suma = num1 + num2
        costo_total += suma
        
        heapq.heappush(nums, suma)
    
    return costo_total

def main():
    while True:
        entrada = input().strip()
        N = int(entrada)
        
        if N == 0:
            break
        
        numeros = list(map(int, input().split()))
        
        resultado = calcular_costo_minimo(numeros)
        print(resultado)

if __name__ == "__main__":
    main()
