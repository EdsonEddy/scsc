n=int(input())
for i in range (n):
    m=int(input())
    sw=False
    for j in range (99999):
        p=m*2**j+1
        if(p==2 or 2**(p-1)%p==1):
            sw=True
            break
    if not (sw):
        print(-1)
    else:
        print(p)
