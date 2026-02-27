a,b=map(int,input().split(" "))
cad=input()
v=list(map(int,cad.split()))#convierte a lsiata de enteros
ans=0
for i in range(len(v)):
    if int(v[i])>=a and int(v[i]<=b):
        ans+=int(v[i])
print(ans)
