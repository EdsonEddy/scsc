a,b=map(int,input().split())
v=input().split()
ans=0
for i in range(len(v)):
    if int(v[i])>=a and int(v[i])<=b:
        ans+=int(v[i])
print(ans)