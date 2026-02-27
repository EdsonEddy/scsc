import heapq
import sys

def MinCost(n):
    heapq.heapify(n) 
    costo = 0
    while len(n) > 1:
        suma = heapq.heappop(n) + heapq.heappop(n)
        costo += suma
        heapq.heappush(n, suma)
    return costo

for i in sys.stdin:
    N = int(i)
    if N == 0:
        break
    nums = list(map(int, input().split()))    
    print(MinCost(nums))
