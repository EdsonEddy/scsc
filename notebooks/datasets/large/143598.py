a,b=map(int,input().split())
cad=input()
v=list(map(int,cad.split()))
ans=0
for i in range(len(v)):
    if v[i]>=a and v[i]<=b:
        ans+=v[i]
print(ans)
                     