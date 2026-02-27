import heapq

while True:
    n = int(input())
    if n == 0:
        break
    arr = list(map(int, input().split()))
    heapq.heapify(arr)  
    total_cost = 0
    while len(arr) > 1:  
        cost = heapq.heappop(arr) + heapq.heappop(arr)  
        total_cost += cost  
        heapq.heappush(arr, cost)  
    print(total_cost)