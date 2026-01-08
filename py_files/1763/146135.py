k=int(input())
for i in range(1,k+1):
    x=int(input())
    z=0
    while x>1000 or x<=0:
        x=int(input())
    for t in range(0,x):
        z=x*2**t+1
        q=0
        a=0
        for f in range(1,z+1):
            if (z%f)==0:
                q=q+1
        if q==2:
            a=a+1
            print(z)
            break
        if a !=0:
            print("-1")