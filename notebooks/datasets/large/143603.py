a,b=map(int,input().split())
v=input().split()
c=0
for i in range(len(v)):
    if int(v[i])>=a and int(v[i])<=b:
        c+=int(v[i])
print(c)