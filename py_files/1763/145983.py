m=int(input())
for i in range(1,m+1):
    y=int(input())
    while y<=0 or y>1000:
        y=int(input())
    for t in range(0,y):
        z=y*2**t+1

        o=0
        w=0
        inp=0
        for f in range(1,z+1):
            if (z%f)==0:
                o=o+1
        if o==2:
            w=w+1
            print(z)
            break
        if w !=0:
            print("-1")