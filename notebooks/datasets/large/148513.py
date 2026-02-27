a,b=map(int,input().split(" "))
c=input()
v=list(map(int,c.split()))
g=0
for i in range(len(v)):
    if int(v[i])>=a and int(v[i])<=b:
        g+=v[i]
print(g)
