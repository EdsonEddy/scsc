from sys import stdin

f=[1,2]

for i in range(62):
    f.append(f[-1]+f[-2])

for linea in stdin:
    n=int(linea.strip())
    ans=["0"]*62
    for i in range(len(f)-1,-1,-1):
        
        if n>=f[i]:
            ans[i]="1"
            n-=f[i]
            
            
    ans=ans[::-1]
    for i in range(len(ans)):
        if ans[i]=="1":
            ans=ans[i:]
            break
    print(*ans,sep="")