a,b=map(int,input().split())
 
c=list(map(int,input().split()))
 
s=0
 
for i in c:
 
    if(a<=i and i<=b):
 
        s=s+i
 
print(s)