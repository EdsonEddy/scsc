n=int(input())
for i in range ( n):
    x=int(input())
    sw=True
    for j in range (10000):
        N=x*2**j+1
        if(N==2 or 2**(N-1)%N==1):
            sw=False
            break
    if(sw):
       print(-1)
    else:
        print(N)