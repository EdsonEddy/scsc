import heapq

def costo_minimo_suma(numeros):
    # Usamos un min-heap para almacenar los números
    heapq.heapify(numeros)
    costo_total = 0
    
    # Mientras haya más de un número en la lista
    while len(numeros) > 1:
        # Sacamos los dos números más pequeños
        primero = heapq.heappop(numeros)
        segundo = heapq.heappop(numeros)
        
        # Sumar los dos números
        suma = primero + segundo
        
        # Agregar el costo de esta suma al costo total
        costo_total += suma
        
        # Insertar la suma de vuelta en el heap
        heapq.heappush(numeros, suma)
    
    return costo_total

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        numeros = list(map(int, input().split()))
        resultado = costo_minimo_suma(numeros)
        print(resultado)

if __name__ == "__main__":
    main()