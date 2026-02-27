import heapq
def minima_suma(n):
    if len(n) < 2:
        return 0
    heapq.heapify(n)
    t = 0
    while len(n) > 1:
        f = heapq.heappop(n)
        s = heapq.heappop(n)
        cost = f + s
        t += cost
        heapq.heappush(n, cost)
    return t
while True:
    n=int(input())
    if(n==0):
        break
    else:
        x=list(map(int,input().split()))
        cost = minima_suma(x)
        print(cost)