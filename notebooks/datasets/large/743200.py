import math
n=int(input())
for i in range(n):
    a,b=map(int, input().split())
    v=1 
    co=0
    for j in range(1,a+1):
        a-=1 
        c=math.ceil(b/(j+1))
        if c<=a:
            print("si")
            co+=1
            break
    if co==0:
        print("no")