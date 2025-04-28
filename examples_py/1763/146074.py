n=int(input())
for i in range ( n):
    x=int(input())
    sw=True
    for a in range (10000):
        A=x*2**a+1
        if(A==2 or 2**(A-1)%A==1):
            sw=False
            break
    if(sw):
       print(-1)
    else:
        print(A)