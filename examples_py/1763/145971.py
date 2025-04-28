n=int(input())
for i in range(1,n+1):
    x=int(input())
    while x<=0 or x>1000:
        x=int(input())
    for j in range(0,x):
        r=x*2**j+1

        c=0
        v=0
        inp=0
        for e in range(1,r+1):
            if (r%e)==0:
                c=c+1
        if c==2:
            v=v+1
            print(r)
            break
        if v !=0:
            print("-1")