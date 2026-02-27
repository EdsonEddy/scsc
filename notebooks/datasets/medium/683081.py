import heapq

def costo_minimo(nums):
    heapq.heapify(nums)  
    costo = 0
    while len(nums) > 1:
        suma = heapq.heappop(nums) + heapq.heappop(nums)  
        costo += suma
        heapq.heappush(nums, suma)  
    return costo

while True:
    N = int(input().strip())
    if N == 0:
        break
    nums = list(map(int, input().strip().split()))
    print(costo_minimo(nums))
