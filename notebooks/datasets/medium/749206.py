import heapq

def costo_minimo_suma(numeros):
    # Crear un min-heap a partir de la lista de números
    heapq.heapify(numeros)
    
    costo_total = 0
    
    # Mientras haya más de un número en el heap
    while len(numeros) > 1:
        # Sacar los dos números más pequeños
        primero = heapq.heappop(numeros)
        segundo = heapq.heappop(numeros)
        
        # Sumar los dos números
        suma = primero + segundo
        
        # Acumular el costo total
        costo_total += suma
        
        # Insertar la suma de vuelta en el heap
        heapq.heappush(numeros, suma)
    
    return costo_total

# Leer la entrada
while True:
    n = int(input())
    if n == 0:
        break
    numeros = list(map(int, input().split()))
    
    resultado = costo_minimo_suma(numeros)
    print(resultado)