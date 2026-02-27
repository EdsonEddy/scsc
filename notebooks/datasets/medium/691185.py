import heapq
def costoMin(nums):
    heapq.heapify(nums)
    total_cost = 0
    while len(nums) > 1:
        min1 = heapq.heappop(nums)
        min2 = heapq.heappop(nums)
        cost = min1 + min2
        total_cost += cost
        heapq.heappush(nums, cost)
    return total_cost

while True:
    N = int(input())
    if N == 0:
        break
    numeros = list(map(int, input().split()))
    print(costoMin(numeros))
