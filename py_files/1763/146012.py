num=int(input())
for i in range(1,num+1):
    k=int(input())
    while k<=0 or k>1000:
        k=int(input())
    for j in range(0,k):
        resp=k*2**j+1
        p=0
        tt=0
        inp=0
        for e in range(1,resp+1):
            if (resp%e)==0:
                p=p+1
        if p==2:
            tt=tt+1
            print(resp)
            break
        if tt!=0:
            print("-1")