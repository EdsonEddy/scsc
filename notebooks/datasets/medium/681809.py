import heapq

def min_cost(nums):
    heapq.heapify(nums)
    total_cost = 0
    while len(nums) > 1:
        cost = heapq.heappop(nums) + heapq.heappop(nums)
        total_cost += cost
        heapq.heappush(nums, cost)
    return total_cost

# Lectura de los datos de entrada
while True:
    n = int(input())
    if n == 0:
        break
    nums = list(map(int, input().split()))
    print(min_cost(nums))
