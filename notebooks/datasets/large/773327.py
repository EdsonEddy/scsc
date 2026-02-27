m=int(input())
f=[]
for z in range(m):
    n=int(input())
    b=-1
    a=0
    res=[]
    y=0
    suma =0
    for i in range(n):
        b=b+2
        re=[]
        for j in range(b):
            a+=1
            if a==1:
                x=a
                re.append(str(a))
                res.append(re)
            else:
                suma=suma+a
        if a>1:
            y=x
            x=suma-x
            re.append(str(y)+"+"+str(x))
            res.append(re)
        suma = 0
    f.append(res[n-1])
for r in f:
    print("".join(r))