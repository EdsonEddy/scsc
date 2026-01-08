n=int(input())
for i in range (n):
    a=int(input())
    sw=True
    for k in range (10000):
        N=a*2**k+1
        if(N==2 or 2**(N-1)%N==1):
            sw=False
            break
    if(sw):
       print(-1)
    else:
        print(N)