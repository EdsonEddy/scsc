def encontrar_costo_minimo(numeros):
    if len(numeros) == 2:
        return numeros[0] + numeros[1]
    import heapq
    heap = numeros.copy()
    heapq.heapify(heap)
    
    costo_total = 0
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        suma = a + b
        costo_total += suma
        heapq.heappush(heap, suma)
    
    return costo_total

def procesar_entrada():
    while True:
        n = int(input())
        if n == 0:
            break
            
        numeros = list(map(int, input().split()))
        resultado = encontrar_costo_minimo(numeros)
        print(resultado)
if __name__ == "__main__":
    procesar_entrada()
