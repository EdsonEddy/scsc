import heapq

def min_addition_cost(numeros):
    heapq.heapify(numeros)
    
    total_c = 0
    
    while len(numeros) > 1:
        primero = heapq.heappop(numeros)
        segundo = heapq.heappop(numeros)
        
        cur_c = primero + segundo
        total_c += cur_c
        
        heapq.heappush(numeros, cur_c)
    
    return total_c

def main():
    while True:
        n = int(input().strip())
        if n == 0:
            break
        
        numeros = list(map(int, input().strip().split()))
        
        resultado = min_addition_cost(numeros)
        print(resultado)

if __name__ == "__main__":
    main()
