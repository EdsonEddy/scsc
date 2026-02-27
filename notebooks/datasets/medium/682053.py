import heapq

def calcular_costo_minimo(numeros):
    heapq.heapify(numeros)
    costo_total = 0
    
    while len(numeros) > 1:
        primero = heapq.heappop(numeros)
        segundo = heapq.heappop(numeros)
        costo_actual = primero + segundo
        costo_total += costo_actual
        heapq.heappush(numeros, costo_actual)
    
    return costo_total

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    index = 0
    resultados = []
    
    while index < len(data):
        N = int(data[index])
        if N == 0:
            break
        
        numeros = list(map(int, data[index + 1 : index + 1 + N]))
        index += 1 + N
        
        resultado = calcular_costo_minimo(numeros)
        resultados.append(resultado)
    
    for resultado in resultados:
        print(resultado)

if __name__ == "__main__":
    main()
