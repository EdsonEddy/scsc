import heapq

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        nums = list(map(int, input().split()))
        heapq.heapify(nums)
        total_cost = 0
        for i in range(n - 1):
            min1 = heapq.heappop(nums)
            min2 = heapq.heappop(nums)
            cost = min1 + min2
            total_cost += cost
            heapq.heappush(nums, cost)
        print(total_cost)

main()
