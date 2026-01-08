casos=int(input())
for i in range(1,casos+1):
    numero=int(input())
    while numero<=0 or numero>1000:
        numero=int(input())
    for j in range(0,numero):
        g=numero*2**j+1
        h=0
        f=0
        for k in range(1,g+1):
            if (g%k)==0:
                h=h+1
        if h==2:
            f=f+1
            print(g)
            break
        if f!=0:
            print("-1")