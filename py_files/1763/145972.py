x=int(input())
for i in range(x):
    y=int(input())
    sw=True
    for j in range (1000):
        r=y*2**j+1
        if(r==2 or 2**(r-1)%r==1):
            sw=False
            break
    if(sw):
        print("-1")
    else:
        print(r)
