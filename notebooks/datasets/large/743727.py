import math
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    if a>=b:
        print("si")
    else:
        aux=1
        x=b
        while b>a:
            b=math.ceil(x/(aux+1))
            aux+=1
            a-=1
            if a==0:
                break
        if a>=b:
            print("si")
        else:
            print("no")