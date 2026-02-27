import heapq
import sys

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0

    while True:
        n = int(data[idx])
        idx += 1
        if n == 0:
            break
        
        pq = []
        for i in range(n):
            heapq.heappush(pq, int(data[idx]))
            idx += 1
        
        costo_total = 0
        while len(pq) > 1:
            primero = heapq.heappop(pq)
            segundo = heapq.heappop(pq)
            suma = primero + segundo
            costo_total += suma
            heapq.heappush(pq, suma)
        
        print(costo_total)

if __name__ == "__main__":
    main()
