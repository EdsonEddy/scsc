import sys
f=[1,2]
while f[-1]<=10**12:
    f.append(f[-1]+f[-2])
for l in sys.stdin:
    n=int(l)
    r=""
    i=len(f)-1
    while f[i]>n:
        i-=1
    while i>=0:
        if f[i]<=n:
            r+="1"
            n-=f[i]
        elif r:
            r+="0"
        i-=1
    print(r)
