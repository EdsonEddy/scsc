import heapq
import sys

def costo_minimo_suma(numeros):
    heapq.heapify(numeros)
    
    total_costo = 0
    
    while len(numeros) > 1:
        primero = heapq.heappop(numeros)
        segundo = heapq.heappop(numeros)
        costo_actual = primero + segundo
        total_costo += costo_actual
        heapq.heappush(numeros, costo_actual)
    
    return total_costo

def main():
    input = sys.stdin.read
    data = input().strip().splitlines()
    
    resultados = []
    i = 0
    
    while i < len(data):
        n = int(data[i])
        if n == 0:
            break
        i += 1
        numeros = list(map(int, data[i].split()))
        costo = costo_minimo_suma(numeros)
        resultados.append(costo)
        i += 1
    
    for resultado in resultados:
        print(resultado)

if __name__ == "__main__":
    main()