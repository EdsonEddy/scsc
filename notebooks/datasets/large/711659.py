def dig(n):
    if n==0:
        return 0
    else:
        return 1+(n-1)%9

def alg(n):
    return int("".join([str(dig(n))]+list(str(n))[:len(list(str(n)))-1:]))

def f(n,k):

    for i in range(k):
        n=alg(n)
    return n

x=int(input())
L=[]
for i in range(x):
    n,k=map(int,input().split())
    L=L+[f(n,k)]
print(*L, sep="\n")