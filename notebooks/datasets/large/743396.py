for _ in range (int(input())):
    x,y=map(int,input().split())
    a=0
    while True:
        x=x-1
        a=a+1
        b=y/(a+1)
        if round(b,0)-b<0:
            b=round(b,0)+1
        if x>=b or x==0:
            break
    if x==0:
        print ("no")
    else:
        print ("si")