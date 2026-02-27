a,b=map(int,input().split())
v=input().split()
res=0
for i in range(len(v)):
    if int(v[i])>=a and int(v[i])<=b:
            res+=int(v[i])
print(res)   