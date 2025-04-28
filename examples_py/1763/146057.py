y=int(input())
for i in range ( y):
    w=int(input())
    a=True
    for j in range (10000):
        B=w*2**j+1
        if(B==2 or 2**(B-1)%B==1):
            a=False
            break
    if(a):
       print(-1)
    else:
        print(B)