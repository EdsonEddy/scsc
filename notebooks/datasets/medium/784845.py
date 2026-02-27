from sys import stdin
from math import isqrt
from queue import LifoQueue,PriorityQueue

def input():
    return stdin.readline().strip()

n=int(input())

while n!=0:

    vec=list(map(int,input().split()))
    pq=PriorityQueue()
    for num in vec:pq.put(num)

    ans=0
    while pq.qsize()>=2:
        sum=(pq.get())+(pq.get())
        ans+=sum
        pq.put(sum)
    print(ans)

    n=int(input())


    

