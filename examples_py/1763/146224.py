l=int(input())
for i in range (l):
    x=int(input())
    sw=True
    for y in range (10000):
        p=x*2**y+1
        if(p==2 or 2**(p-1)%p==1):
            sw=False
            break
    if (sw):
        print(-1)
    else:
        print(p)
