import heapq
 
def costo_min(num):
    heapq.heapify(num)
    
    costo = 0
    
    while len(num) > 1:
        min_primero = heapq.heappop(num)
        min_segundo = heapq.heappop(num)
        
        n = min_primero + min_segundo
        costo += n
 
        heapq.heappush(num, n)
    
    return costo
 
def main():
    while True:
        n = int(input().strip())
        if n == 0:
            break
        
        num = list(map(int, input().strip().split()))
        
        print(costo_min(num))
 
if __name__ == "__main__":
    main()
