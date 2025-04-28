n=int(input())
for i in range (n):
    q=int(input())
    p=True
    for y in range (10000):
        m=q*2**y+1
        if(m==2 or 2**(m-1)%m==1):
            p=False
            break
    if (p):
        print(-1)
    else:
        print(m)