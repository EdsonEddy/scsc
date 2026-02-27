def suma_costo_minimo(numeros):
    """
    Calcula el costo mínimo de sumar una lista de números donde cada suma parcial
    cuenta para el costo total.
    """
    # Si la lista tiene menos de 2 números, no hay costo
    if len(numeros) < 2:
        return 0
    
    # Convertimos la lista en una cola de prioridad (min heap)
    # para siempre tener acceso a los números más pequeños
    import heapq
    heap = numeros.copy()
    heapq.heapify(heap)
    
    costo_total = 0
    
    # Mientras haya más de un número en el heap
    while len(heap) > 1:
        # Tomamos los dos números más pequeños
        num1 = heapq.heappop(heap)
        num2 = heapq.heappop(heap)
        
        # Calculamos la suma parcial
        suma_parcial = num1 + num2
        
        # Añadimos el costo de esta suma al total
        costo_total += suma_parcial
        
        # Añadimos la suma parcial de vuelta al heap
        heapq.heappush(heap, suma_parcial)
    
    return costo_total

def main():
    # Leer casos de prueba hasta encontrar un 0
    while True:
        n = int(input())
        if n == 0:
            break
            
        # Leer la lista de números
        numeros = list(map(int, input().split()))
        
        # Calcular y mostrar el resultado
        resultado = suma_costo_minimo(numeros)
        print(resultado)

if __name__ == "__main__":
    main()