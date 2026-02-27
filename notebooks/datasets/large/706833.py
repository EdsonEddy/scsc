m=int(input())
for i in range(m):
    lista=[]
    n=int(input())
    e=0
    for i in range (1,n+1):
        a=-1
        c=1
        d=0
        for j in range(i):
            a=a+2
            if a==1:
                b=0
            else:
                b=a-2
            c=c+b
        for k in range (a):
            d=d+c
            c=c+1
        e=d-e
        lista.append(e)
    if n==1:
        print(lista[0])
    else:
        print(f"{lista[-2]}+{lista[-1]}")