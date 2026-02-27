import heapq
while True:
    n = int(input())
    if n == 0:
        break
    x = list(map(int, input().split()))
    heapq.heapify(x)  
    v = 0
    while len(x) > 1:  
        c = heapq.heappop(x) + heapq.heappop(x)  
        v += c  
        heapq.heappush(x, c)  
    print(v)