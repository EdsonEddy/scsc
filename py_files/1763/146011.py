k=int(input())
k1=1
while k1<=k:
    x=int(input())
    a=True
    for i in range (10000):
        n=x*2**i+1
        if(n==2 or 2**(n-1)%n==1):
            a=False
            break
    if(a):
        print(-1)
        k1=k1+1
    else:
        print(n)
        k1=k1+1