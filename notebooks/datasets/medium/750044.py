def suma_costo_minimo(numeros):
    if len(numeros) < 2:
        return 0
    
    import heapq
    heap = numeros.copy()
    heapq.heapify(heap)
    
    costo_total = 0
    
    while len(heap) > 1:
        num1 = heapq.heappop(heap)
        num2 = heapq.heappop(heap)

        suma_parcial = num1 + num2
        
        costo_total += suma_parcial
        
        heapq.heappush(heap, suma_parcial)
    
    return costo_total

def main():
    while True:
        n = int(input())
        if n == 0:
            break

        numeros = list(map(int, input().split()))
        
        resultado = suma_costo_minimo(numeros)
        print(resultado)

if __name__ == "__main__": 
    main()