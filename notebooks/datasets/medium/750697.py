import heapq
import sys

def calcular_costo_minimo(nums):
    heapq.heapify(nums)
    costo_total = 0
    
    while len(nums) > 1:
        num1 = heapq.heappop(nums)
        num2 = heapq.heappop(nums)
        
        costo_actual = num1 + num2
        costo_total += costo_actual
        
        heapq.heappush(nums, costo_actual)
    
    return costo_total

# Leer entrada infinita del usuario
try:
    while True:
        # Leer el valor de n
        n = int(input().strip())
        
        # Si n es 0, se termina el programa
        if n == 0:
            break
        
        # Leer la siguiente línea de números
        numeros = list(map(int, input().strip().split()))
        
        # Calcular y mostrar el costo mínimo para estos números
        resultado = calcular_costo_minimo(numeros)
        print(resultado)

except EOFError:
    pass
