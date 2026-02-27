from sys import stdin
from math import isqrt

def input():
    return stdin.readline().strip()


def esprimo(n:int)->bool:
    if n<2:return False
    for i in range(2,isqrt(n)+1):
        if n%i==0:return False
    return True


def f(n,k):
    return n*n -n +k

t=int(input())

for _ in range(t):
    k=int(input())
    ans=0
    actual=0
    for n in range(1,501):
        if esprimo(f(n,k)):
            actual+=1
        else:
            actual=0
        ans=max(ans,actual)
    print(f"{k}: {ans}")


