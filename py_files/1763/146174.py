v=int(input())
for i in range (v):
    u=int(input())
    sw=True
    for y in range (10000):
        Y=u*2**y+1
        if(Y==2 or 2**(Y-1)%Y==1):
            sw=False
            break
    if (sw):
        print(-1)
    else:
        print(Y)

