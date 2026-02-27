a,b=map(int,input().split(" "))
cad=input()
c=list(map(int,cad.split()))
z=0
for i in  range(len(c)):
    if int(c[i])>=a and int(c[i])<=b:
        z+=c[i]
print(z)
