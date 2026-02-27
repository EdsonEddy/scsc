import heapq
n=-1
while n!=0:
    n=int(input())
    if n==0:
        break
    a=[int(e) for e in input().split()]
    heapq.heapify(a)
    cos=0
    while len(a)>1:
        x=heapq.heappop(a)
        y=heapq.heappop(a)
        costo=x+y
        cos+=costo
        heapq.heappush(a,costo)
    print(cos)
