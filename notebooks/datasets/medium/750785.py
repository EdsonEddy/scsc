import heapq
def minima_suma(n):
    if len(n) < 2:
        return 0
    heapq.heapify(n)
    t = 0
    while len(n) > 1:
        f = heapq.heappop(n)
        s = heapq.heappop(n)
        d = f + s
        t += d
        heapq.heappush(n, d)
    return t
while True:
    n=int(input())
    if(n==0):
        break
    else:
        x=list(map(int,input().split()))
        c = minima_suma(x)
        print(c)