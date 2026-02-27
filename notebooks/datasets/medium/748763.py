import heapq

def costo_minimo_suma(nums):
    heapq.heapify(nums) 
    costo_total = 0

    while len(nums) > 1:
        a = heapq.heappop(nums)
        b = heapq.heappop(nums)
        costo_actual = a + b
        costo_total += costo_actual

        heapq.heappush(nums, costo_actual)

    return costo_total

while True:
    n = int(input().strip())
    if n == 0:
        break

    nums = list(map(int, input().strip().split()))
    print(costo_minimo_suma(nums))
