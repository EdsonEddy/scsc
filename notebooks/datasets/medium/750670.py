def costo_minimo_suma(lista_numeros):
    """
    Calcula el costo mínimo de sumar una lista de números donde cada suma parcial
    cuenta para el costo total.
    """
    # Si la lista tiene menos de 2 elementos, no hay costo
    if len(lista_numeros) < 2:
        return 0
    
    # Convertimos la lista en una cola de prioridad (min heap)
    import heapq
    cola_prioridad = lista_numeros.copy()
    heapq.heapify(cola_prioridad)
    
    costo_acumulado = 0
    
    # Mientras haya más de un elemento en el heap
    while len(cola_prioridad) > 1:
        # Tomamos los dos números más pequeños
        menor1 = heapq.heappop(cola_prioridad)
        menor2 = heapq.heappop(cola_prioridad)
        
        # Calculamos la suma parcial
        suma_parcial = menor1 + menor2
        
        # Añadimos el costo de esta suma al total acumulado
        costo_acumulado += suma_parcial
        
        # Añadimos la suma parcial de vuelta a la cola de prioridad
        heapq.heappush(cola_prioridad, suma_parcial)
    
    return costo_acumulado

def ejecutar():
    # Leer casos de prueba hasta encontrar un 0
    while True:
        cantidad = int(input())
        if cantidad == 0:
            break
            
        # Leer la lista de números
        lista_numeros = list(map(int, input().split()))
        
        # Calcular y mostrar el resultado
        resultado = costo_minimo_suma(lista_numeros)
        print(resultado)

if __name__ == "__main__":
    ejecutar()
