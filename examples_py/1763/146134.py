m=int(input())
for i in range(m):
    y=int(input())
    sw=True
    for j in range(10000):
        J=y*2**j+1
        if(J==2 or 2**(J-1)%J==1):
            sw=False
            break
    if(sw):
        print(-1)
    else:
        print(J)
           