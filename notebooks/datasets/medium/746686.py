import heapq
def costo_suma(nums):
    heapq.heapify(nums) 
    costo_total = 0
    while len(nums) > 1:
        primero = heapq.heappop(nums)
        segundo = heapq.heappop(nums)
        costo_actual = primero + segundo
        costo_total += costo_actual
        heapq.heappush(nums, costo_actual)
    
    return costo_total
while True:
    n = int(input())
    if n == 0:
        break
    nums = list(map(int, input().split()))
    print(costo_suma(nums))