n=int(input())
for i in range(1,n+1,1):
    a=int(input())
    f=True
    for j in range (10000):
        j=a*2**j+1
        if(j==2 or 2**(j-1)%j==1):
            f=False
            break
    if (f):
        print(-1)
    else:
        print(j)