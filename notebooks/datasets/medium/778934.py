import sys
f=[1,2]
while f[-1]<=10**12: f+=[f[-1]+f[-2]]
for l in sys.stdin:
    n=int(l); i=len(f)-1
    while f[i]>n: i-=1
    r=""
    for j in range(i,-1,-1):
        if f[j]<=n: r+="1"; n-=f[j]
        else: r+="0"
    print(r)    