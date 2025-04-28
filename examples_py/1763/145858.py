x=int(input())
for i in range (x):
    p=int(input())
    sw=True
    for l in range (10000):
        M=p*2**l+1
        if(M==2 or 2**(M-1)%M==1):
            sw=False
            break
    if(sw):
       print(-1)
    else:
        print(M)